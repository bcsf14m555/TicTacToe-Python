import os    
import time    
        
board = [' ','1','2','3','4','5','6','7','8','9']    
player = 1    
Win = 1    
Draw = -1    
Running = 0    
Stop = 1    
Game = Running    
Mark = 'X'    
n=1
#Function for Game Board    
def DrawBoard():    
	print(" %c | %c | %c " % (board[1],board[2],board[3]))    
	print("___|___|___")    
	print(" %c | %c | %c " % (board[4],board[5],board[6]))    
	print("___|___|___")    
	print(" %c | %c | %c " % (board[7],board[8],board[9]))    
	print("   |   |   ")    

#Checks board position is empty or not    
def CheckPosition(x):    
	if(board[x] != 'X' and board[x] != 'O'):    
	    return True    
	else:    
	    return False    

#Checks the winning conditions for player
def CheckWin():    
	global Game    

	if(board[1] == board[2] and board[2] == board[3]):    
	    Game = Win    
	elif(board[4] == board[5] and board[5] == board[6]):    
	    Game = Win    
	elif(board[7] == board[8] and board[8] == board[9]):    
	    Game = Win    

	elif(board[1] == board[4] and board[4] == board[7]):    
	    Game = Win    
	elif(board[2] == board[5] and board[5] == board[8]):    
	    Game = Win    
	elif(board[3] == board[6] and board[6] == board[9]):    
	    Game=Win    

	elif(board[1] == board[5] and board[5] == board[9]):    
	    Game = Win    
	elif(board[3] == board[5] and board[5] == board[7]):    
	    Game=Win    

	elif(board[1]!='1' and board[2]!='2' and board[3]!='3' and board[4]!='4' and board[5]!='5' and board[6]!='6' and board[7]!='7' and board[8]!='8' and board[9]!='9'):    
	    Game=Draw    
	else:            
	    Game=Running    
  
print("\n\nPlayer 1 == [X] AND Player 2 == [O]\n")        

while(Game == Running):       
	if(n==1):
		DrawBoard()
		n=n+1    
	if(player % 2 != 0):    
	    print("Player 1's turn")    
	    Mark = 'X'    
	else:    
	    print("Player 2's turn")    
	    Mark = 'O'    
	choice = int(input("\nFor Mark , Enter the number between 1 to 9 : "))    
	if(CheckPosition(choice)):    
	    board[choice] = Mark    
	    player+=1    
	    CheckWin()    

	os.system('clear')    
	DrawBoard()    
	if(Game==Draw):    
		print("Game Draw")    
	elif(Game==Win):    
		player-=1    
		if(player%2!=0):    
			print("Player 1 Won")    
		else:    
			print("Player 2 Won")    
