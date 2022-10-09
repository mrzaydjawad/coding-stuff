nolist = ("n","N")
yeslist = ("y","Y")
def tictactoe():
        print("work in progress")
def snakegame():
    print("work in progress")
def tetris():
    print("work in progress")
def gamemenu():
    print("[1]tic tac toe")
    print("[2]snake game")
    print("[3]tetris")
    uc = int(input("pls chose a game(1,2,3)"))
    if uc == 1:
        tictactoe()
    elif uc == 2:
        snakegame()
    elif uc == 3:
        tetris()
    else:
        print()
        print("please enter either 1,2 or 3")
        gamemenu()
def greeting():
    print("are you bored cause i am very bored")
    print("sooo. . . .")
    gamegreeting()
def gamegreeting():
    Q = str(input("do you wanna play a game?(y/n)"))
    if Q in yeslist:
        gamemenu()
    elif Q in nolist:
        print("ok byeeeeee")
    else:
        print("pls enter either (y or n)")
        gamegreeting()
greeting()