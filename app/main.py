from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from .crush import crush

app = FastAPI()

class BoardInput(BaseModel):
    board: List[List[int]]

@app.post("/api/crush")
def crush_board(data: BoardInput):
    if not data.board or not data.board[0]:
        raise HTTPException(status_code=400, detail="Invalid board format")
    return crush(data.board)
