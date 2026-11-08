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

- 取り組んだレベル：基礎
- やったこと：
 docstringを「選ぶ個数」を以下のように変更
 （変更前）
    """指定した回の用語から 1つを選び、
    確認問題と答えを返す。
    「第2回の確認問題を出して」のように、
    復習用の問題を求められたときに使う。
    lecture は 1 始まりの回番号を指定する。
    """ 1 始まりの回番号を指定する。

（変更後）
    """指定した回の用語から 2つを選び、
    確認問題と答えを返す。
    「第2回の確認問題を出して」のように、
    復習用の問題を求められたときに使う。
    lecture は 1 始まりの回番号を指定する。
    """ 1 始まりの回番号を指定する。

- 結果：
------
uv run python -m app.agent --trace " 第2回の内容から確認問題を 1問出して"
の結果
[model] gemini-3.5-flash-lite
第2回からの確認問題です。ぜひチャレンジしてみてください！

**【確認問題】**
「ファインチューニング」の意味や目的について説明してください。

---
関係する回：第2回

--- trace ---
[tool call]   make_quiz({'lecture': 2})
[tool return] make_quiz -> {"question": "「ファインチューニング」の意味は？", "answer": "事前学習済みモデルを、特定のタスクや形式に合ったデータで追加学習させること。出力の形式や口調、特定ドメインの振る舞いを身につけさせるのに向く。最新の事…
[usage] RunUsage(cost=Decimal('0.0004233'), details={'text_prompt_tokens': 936}, input_text_tokens=936, input_tokens=936, output_tokens=57, requests=2, tool_calls=1)
------

次に質問文で「２問出して」としたところ、２問得ることができた。
uv run python -m app.agent --trace " 第2回の内容から確認問題を 2問出して"
------
[model] gemini-3.5-flash-lite
第2回から確認問題を2問出題します！

**第1問**
> 機械学習において、学習データ全体を1周学習することを何と呼びますか？また、その回数を増やしすぎるとどのような問題が起きやすいですか？

**第2問**
> （追加問題）
> 過学習（オーバーフィッティング）を防ぐための代表的なアプローチや、その対策として講じられる工夫にはどのようなものがありますか？（ヒント：データ、モデル、正則化など）

---
答えが気になったり、解説が必要になったりしたら、いつでも声をかけてくださいね！

（第2回）

--- trace ---
[tool call]   make_quiz({'lecture': 2})
[tool return] make_quiz -> {"question": "「エポック」の意味は？", "answer": "学習データ全体を1周学習することを1エポックと数える。回数を増やしすぎると過学習しやすい。"}…
[usage] RunUsage(cost=Decimal('0.0006460'), details={'text_prompt_tokens': 895}, input_text_tokens=895, input_tokens=895, output_tokens=151, requests=2, tool_calls=1)
(aie2026-exercises) @kosukem ➜ /workspaces/lecture-ai-engineering-2026 (lec03) $ 
------

- 気づき・疑問：
docstringに２個選んでという指示は、実際の質問文と矛盾している場合は、質問が優先されているように見えた。