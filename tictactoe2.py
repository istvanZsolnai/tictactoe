def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8 ), (0, 3, 6), (1, 4, 7), (2, 5, 8 ), (0, 4, 8 ), (2, 4, 6))
    player1 = input("Whats the name of player 1?: ")
    player2 = input("Whats the name of player 2?: ")
    #This draws out the board from the list. Its built for the num pad, so its comfortable
    def draw():
        k = "\033[1;32;40m|\033[0m"
        slash = "\033[1;32;40m-\033[0m"
        print(slash*13)
        print(k,board[6],k,board[7],k,board[8],k)
        print(slash*13)
        print(k,board[3],k,board[4],k,board[5],k)
        print(slash*13)
        print(k,board[0],k,board[1],k,board[2],k)
        print(slash*13)
        print()
    #Player one input checking
    def p1():
        n = choose_number()
        if board[n] == "\033[1;31;40mX\033[0m" or board[n] == "\033[1;34;40mO\033[0m":
            print("\nDont try to overwrite! Cheater")
            p1()
        else:
            board[n] = "\033[1;31;40mX\033[0m"
    # Player two input checking
    def p2():
        n = choose_number()
        if board[n] == "\033[1;31;40mX\033[0m" or board[n] == "\033[1;34;40mO\033[0m":
            print("\nDont try to overwrite! Cheater")    
            p2()
        else:
            board[n] = "\033[1;34;40mO\033[0m"
    #Asking for input with try - except
    def choose_number():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nnope")
                        continue
                except ValueError:
                   print("\nThats a letter.... Pick a proper number")
                   continue
    #checking the board for win or tie situations
    def check_board():
        count = 0
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "\033[1;31;40mX\033[0m":
                print(player1, " won!\n")
                print("Good Job!\n")
                return True
            if board[a[0]] == board[a[1]] == board[a[2]] == "\033[1;34;40mO\033[0m":
                print(player2," won!\n")
                print("Good Job!\n")
                return True
        for a in range(9):
            if board[a] == "\033[1;31;40mX\033[0m" or board[a] == "\033[1;34;40mO\033[0m":
                count += 1
            if count == 9:
                print("Its a Tie!\n")
                return True
    #While end is not true the program keeps on running, 
    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print(player1, " choose where to place an X")
        p1()
        print()
        draw()
        end = check_board()
        if end == True:
            break
        print(player2," choose where to place a O")
        p2()
        print()
    #play again feature
    if input("If you want to play again press R!\n") == "R":
        print("Good decision\n")
        tic_tac_toe()
    else:
        print("See you later!\n")

tic_tac_toe()