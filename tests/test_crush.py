from app.crush import crush

def test_crush_board():
    board = [
        [1, 1, 1, 1],
        [2, 2, 2, 0],
        [3, 3, 3, 0]
    ]
    result = crush(board)
    assert result["combo"] >= 1
