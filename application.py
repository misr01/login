from flask import Flask, render_template, session
from flask_session import Session
from tempfile import mkdtemp #this is where data is stored

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem" #stores data in files
Session(app)

def board(height,width): #generates board
    boardheight = []
    for x in range(height): #creates columns
        boardheight.append([])
        for i in range(width): #creates arrays with  blank spaces, each array is 1 row
            boardheight[x].append("-")
    return boardheight #returns created array(board)
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registration")
def registration():
    return render_template("registration.html")
    
@app.route("/login")
def login():
    return render_template("login.html")

    
@app.route("/game")
def OpenGame():
    if "board" not in session:
        turn = "x"
        height = 4
        width = 4
        boardreal = board(height,width)
        session["turn"] = turn
        session["height"] = height
        session["width"] = width
        session["board"] = boardreal
        
        
    return render_template("game.html", game=session["board"], height=session["height"], width=session["width"], turn=session["turn"])
    
@app.route("/play/<int:row>/<int:col>")
def play(row,col):
    session["board"][row][col] = session["turn"]
    if session["turn"] == "x":
        session["turn"] = "o"
    else:
        session["turn"] = "x"
    return redirect(url_for("game"))
