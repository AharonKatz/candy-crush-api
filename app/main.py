from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from .crush import crush

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (including GitHub Pages)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root check for Render
@app.get("/")
def health_check():
    return {"status": "ok"}

class BoardInput(BaseModel):
    board: List[List[int]]

@app.post("/api/crush")
def crush_board(data: BoardInput):
    if not data.board or not data.board[0]:
        raise HTTPException(status_code=400, detail="Invalid board format")
    return crush(data.board)
