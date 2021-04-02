import random

board = ['  ', '  ' ,'  ' , '  ' , '  ' , '  ' , '  ' , '  ' ,'  ']

def printBoard(board):
	for i in range(9):
		if (i + 1) % 3 == 0:
			print(board[i] + '|')
			print("---------")
		else:
			print(board[i] + '|', end='')

def takeInput():
	pos = input('enter the position to put(1-9)')
	return pos

def isvalid(board , pos):
	if pos < 0 or pos > 9:
		return False

	# trying to check if the value is a integer
	if board[pos] != '  ':
		return False

	return True

def compmove(board):
	possibemoves = []		
	for i in range(9):
		if board[i] == '  ':
			possibemoves.append(i)

	for let in [' o' , ' x']:
		for i in range(9):
			if i in possibemoves:
				boardcopy = board[:]
				insertcompmove(boardcopy , i , let)
				if iswinner(boardcopy , let):
					return i
	notcorners = []
	for i in possibemoves:
		if i in [1,3,5,7]:
			notcorners.append(i)

	corners = []
	for i in possibemoves:
		if i in [0,6,2,8]:
			corners.append(i)

	if 4 in possibemoves:
		return 4

	if len(corners) != 0 and len(corners) != 2:
		random_corner = random.randint(0 , len(corners) - 1)
		return corners[random_corner]
	
	else:
		random_not_corner = random.randint(0 , len(notcorners) - 1)
		return notcorners[random_not_corner]
		
def insertmove(board , pos):
	board[pos] = ' x'

def insertcompmove(board , pos , sy):
	board[pos] = sy 
 
#the is sy is the symbol like ' x' for the human and ' o' for the computer
def iswinner(bo , sy):
	if bo[0] == sy and bo[1] == sy and bo[2] == sy:
		return True

	if bo[3] == sy and bo[4] == sy and bo[5] == sy:
		return True

	if bo[6] == sy and bo[7] == sy and bo[8] == sy:
		return True

	if bo[0] == sy and bo[3] == sy and bo[6] == sy:
		return True

	if bo[1] == sy and bo[4] == sy and bo[7] == sy:
		return True

	if bo[2] == sy and bo[5] == sy and bo[8] == sy:
		return True

	if bo[0] == sy and bo[4] == sy and bo[8] == sy:
		return True

	if bo[2] == sy and bo[4] == sy and bo[6] == sy:
		return True

	return False



def main():
	time_done = 0 
	while True: #gnt is game not tie 
		print(time_done)	
		

		printBoard(board)
		pos = int(takeInput()) - 1

		if not isvalid(board , pos):
			print("enter a valid value")	
			main()

		insertmove(board , pos)	
		time_done =  time_done + 1

		if time_done == 5:
			print("ITS A TIE GG!")
			break
			
		comppos = compmove(board)

		insertcompmove(board , comppos ,' o')

		if iswinner(board , ' x'):
			print("good job you win")
			printBoard(board)
			exit()

		elif iswinner(board , ' o'):
			print('lmao u cant even tie with this computer')
			printBoard(board)
			exit()
		
			
print('TICTACTOE')
main()
