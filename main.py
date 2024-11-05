from typing import List
from queue import Queue
from asyncio import sleep, create_task
from contextlib import asynccontextmanager

from fastapi import FastAPI, WebSocket, WebSocketDisconnect


class RoomManager:
    def __init__(self):
        self.connections: List[WebSocket] = []
        self.matching = Queue()

    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.connections.append(ws)

    async def join(self, ws: WebSocket):
        await ws.send_json({"status": "matching"})
        self.matching.put(ws)

    async def match(self):
        while True:
            if self.matching.qsize() >= 2:
                ws1 = self.matching.get()
                ws2 = self.matching.get()
                await ws1.send_json({"status": "matched"})
                await ws2.send_json({"status": "matched"})
            await sleep(1)

    async def disconnect(self, ws: WebSocket):
        self.connections.remove(ws)

    async def broadcast(self, data: dict):
        for connection in self.connections:
            await connection.send_json(data)


manager = RoomManager()


@asynccontextmanager
async def lifespan(_: FastAPI):
    create_task(manager.match())
    yield


app = FastAPI(lifespan=lifespan)


@app.websocket("/")
async def handler(ws: WebSocket):
    await manager.connect(ws)
    await manager.join(ws)
    try:
        while True:
            req = await ws.receive_json()
            await manager.broadcast(req)
    except WebSocketDisconnect:
        await manager.disconnect(ws)
