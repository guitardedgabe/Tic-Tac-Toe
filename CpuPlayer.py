import random

class cpuplayer:

	def __init__(self, name = "Sir Charles"):
		self.name = name
		self.wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
	
	def choice(self, board):
		if self.impendingWin(board):
			return self.endTheGame(board)
		elif self.impendingLoss(board):
			return self.block(board)
		else:
			return self.randomMove(board)
	
	def impendingWin(self, board):
		for win in self.wins:
			x_count = 0
			o_count = 0
			for i in win:
				if board[i] == 'x':
					x_count += 1
				elif board[i] == 'o':
					o_count += 1

			if o_count == 2 and x_count == 0:
				self.winningThree = win
				return True

		return False
	
	def endTheGame(self, board):
		for i in self.winningThree:
			if board[i] == '-':
				return str(i)
	
	def impendingLoss(self, board):
		for win in self.wins:
			x_count = 0
			o_count = 0
			for i in win:
				if board[i] == 'x':
					x_count += 1
				elif board[i] == 'o':
					o_count += 1

			if x_count == 2 and o_count == 0:
				self.losingThree = win
				return True

		return False
	
	def block(self, board):
		for i in self.losingThree:
			if board[i] == '-':
				return str(i)

	def randomMove(self, board):
		while True:
			position = random.randint(0, 8)
			if board[position] == '-':
				return str(position)
