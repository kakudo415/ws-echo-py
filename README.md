# ws-echo-py

アクセスしてきたユーザーを部屋ごとに振り分け、WebSocketで部屋ごとにメッセージを中継するサーバーの例です。

## Installation

このexampleは[uv](https://docs.astral.sh/uv/)を使っています。
実行するには、まずuvをインストールしてください。

2024年11月現在、macOSとLinuxでは以下のコマンドでインストールできます。

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

インストールが完了したら、以下のコマンドでこのexampleを実行できます。

```sh
uv run main.py
```
