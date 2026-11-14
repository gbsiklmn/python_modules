import chess
import chess.engine
import chess.pgn

def cp(info):
    return info["score"].white().score(mate_score=10000)


engine = chess.engine.SimpleEngine.popen_uci("/home/gbs/Stockfish/src/stockfish")
with open("game.pgn") as f:
    game = chess.pgn.read_game(f)

limit = chess.engine.Limit(depth=18)
board = game.board()
prev = engine.analyse(board, limit)

for move in game.mainline_moves():

    num = board.fullmove_number
    color = board.turn
    san = board.san(move)
    best = board.san(prev["pv"][0])
    board.push(move)
    cur = engine.analyse(board, limit)
    loss = cp(prev) - cp(cur) if color == chess.WHITE else cp(cur) - cp(prev)
    flag = " <-- mistake" if loss >= 100 else ""
    dots = "." if color == chess.WHITE else "..."
    print(f"{num}{dots} {san:8}  {cp(cur):+6} loss {loss:4} best: {best}{flag}")
    prev = cur
    
engine.quit()