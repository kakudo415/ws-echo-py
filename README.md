# ws-echo-py

アクセスしてきたユーザーを部屋ごとに振り分け、それぞれの部屋でメッセージをブロードキャストするWebSocketサーバーのPython実装です。

[Ryosuke0425/Tanks_GroupE](https://github.com/Ryosuke0425/Tanks_GroupE)のためのプロトタイプとして作成しました。

## Implementation Status

- [x] 部屋の区別なくテキストメッセージをブロードキャストする
- [ ] 部屋の区別なくJSONメッセージをブロードキャストする
- [ ] ユーザーを部屋ごとに振り分ける
- [ ] 部屋ごとにJSONメッセージをブロードキャストする

## Usage

### Installation

このプロジェクトはパッケージ・プロジェクトマネージャーとして[astral-sh/uv](https://docs.astral.sh/uv/)を使っています。

2024年11月現在、macOSとLinuxでは以下のコマンドでインストールできます。

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

`uv`のインストールが完了したら、依存関係のインストールをします。

```sh
uv sync
```

### Running the Server

WebSocketサーバーの起動は以下を実行してください。

```sh
uv run fastapi dev
```

## Note

### Ruffがいい感じ

PythonのFormatter・Linterの[Ruff](https://docs.astral.sh/ruff/)がいい感じでした。

Installationの手順に従っていれば`uvx`が使えるはずなので、そのままプロジェクト全体を次のようにフォーマットできます。

```sh
uvx ruff format .
```
