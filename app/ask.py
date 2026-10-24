"""第1回: 素のLLMに1回だけ質問するスクリプト。

使い方:
    uv run python -m app.ask "LoRAとは何ですか？"
    uv run python -m app.ask            # 質問を省略すると、講座に固有の質問をする

ツールも会話履歴も持たない「素の」呼び出し。
講座に固有のことを聞くと、「分からない」と答えるか、一般論でもっともらしく答える
（講座の実際とは違う）ことを確かめよう。
（第3回で、用語集を検索できるエージェントにして改善する）
"""

import argparse

from google import genai
from google.genai import errors
from google.genai import types

from app.config import MODEL, api_error_message, get_api_key

# 講座に固有の質問。正しい答えは data/glossary.json の homework-levels にある
DEFAULT_QUESTION = "AIE2026の講座の宿題にある「3レベル」とは何ですか？"

# 現在利用可能と思われるモデルの一覧
# 安定版: gemini-2.5-flash、gemini-2.5-pro、gemini-2.5-flash-lite、gemini-3.1-flash-lite、gemini-3.6-flash、gemini-3.7-flash
# エイリアス: gemini-flash-latest、gemini-flash-lite-latest、gemini-pro-latest
# Preview: gemini-3-flash-preview、gemini-3.1-pro-preview、gemini-3.1-flash-lite-preview


def ask(model: str, question: str) -> str:
    client = genai.Client(api_key=get_api_key())

    results = []
    
    try:
        config = types.GenerateContentConfig(temperature=0.2)
        response = client.models.generate_content(model=model, contents=question, config=config)
        usage = response.usage_metadata
        log_message = ""
        if usage is not None:
            log_message = (
                f"[モデル] {model} / [Temperature] {config.temperature}, "
                f"[トークン数] 入力: {usage.prompt_token_count}, ¥n"
                f"出力: {usage.candidates_token_count}"

            )
        results.append(log_message + response.text)
    except errors.APIError as e:
        print(api_error_message(e.code, e.message))
    return results


def main() -> None:
    models = ["gemini-2.5-pro", "gemini-3.1-flash-lite", "gemini-3.5-flash", "gemini-3.6-flash", "gemini-3.8-flash"]
    parser = argparse.ArgumentParser(description="素のLLMに質問する")
    for model in models:
        parser.add_argument("model", nargs="?", default=MODEL, help=f"使用するモデル (デフォルト: {MODEL})")
        parser.add_argument("question", nargs="?", default=DEFAULT_QUESTION)

        args = parser.parse_args()
        print(f"[model] {model}")
        print(f"[質問] {args.question}\n")
        try:
            print('\n'.join(ask(model=model, question=args.question)))
        except errors.APIError as e:
            print(api_error_message(e.code, e.message))
            raise SystemExit(1)


if __name__ == "__main__":
    main()
