# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：
第１回と比較してより欲しい回答をdocstringsに記載されている内容に沿って得ることができた。

- `--trace` で見えたツール呼び出し（ツール名と引数）：
[tool return] make_quiz -> {"question": "「量子化」の意味は？", "answer": "モデルの重みを少ないビット数（例：16ビットから4ビット）で表し、メモリ使用量や計算量を減らす技術。精度は少し下がることがある。"}…
[usage] RunUsage(cost=Decimal('0.0004018'), details={'text_prompt_tokens': 906}, input_text_tokens=906, input_tokens=906, output_tokens=52, requests=2, tool_calls=1)

- 1つの質問での LLM 呼び出し回数（`requests`）：
mainからmake_quizも呼び出されているので2回
requests=2
- 追加したツールと、docstring に書いた説明：
make_quiz
"""指定した回の用語から 1つを選び、
確認問題と答えを返す。
「第2回の確認問題を出して」のように、
復習用の問題を求められたときに使う。
"""


## 宿題

- 取り組んだレベル：基礎 / 実装 / 発展
- やったこと：
- 結果：
- 気づき・疑問：
