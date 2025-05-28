from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from .crush import crush
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # אפשר לשים ['http://localhost:63343'] אם את רוצה להגביל
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class BoardInput(BaseModel):
    board: List[List[int]]

@app.post("/api/crush")
def crush_board(data: BoardInput):
    if not data.board or not data.board[0]:
        raise HTTPException(status_code=400, detail="Invalid board format")
    return crush(data.board)
