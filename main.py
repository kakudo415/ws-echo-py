from typing import List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

class WebSocketManager:
    def __init__(self) -> None:
        self.connections: List[WebSocket] = []

    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.connections.append(ws)

    async def disconnect(self, ws: WebSocket):
        self.connections.remove(ws)

    async def broadcast(self, data: str):
        for connection in self.connections:
            await connection.send_text(data)

manager = WebSocketManager()

@app.websocket("/")
async def handler(ws: WebSocket):
    await manager.connect(ws)
    try:
        while True:
            data = await ws.receive_text()
            await manager.broadcast(data)
    except WebSocketDisconnect:
        await manager.disconnect(ws)
