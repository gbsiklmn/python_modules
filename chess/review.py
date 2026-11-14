import tkinter as tk
import chess 
import chess.engine
import chess.pgn

ENGINE = "/home/gbs/Stockfish/src/stockfish"
PGN = "game.pgn"
LIMIT = chess.engine.Limit(depth=18)
SQ = 70

GLYPHS = {
    "P": "♙", "N": "♘", "B": "♗", "R": "♖", "Q": "♕", "K": "♔",
    "p": "♟", "n": "♞", "b": "♝", "r": "♜", "q": "♛", "k": "♚",
}

def analyse_game(path):
    with open(path) as f:
        game = chess.pgn.read_game(f)

    engine = chess.engine.SimpleEngine.popen_uci(ENGINE)
    board = game.board()
    positions = [{
        "board": board.copy(stack=False),
        "move": None,
        "label": "Start position",
        "info": engine.analyse(board, LIMIT)
    }]

    for move in game.mainline_moves():
        dots = "." if board.turn == chess.WHITE else "..."
        