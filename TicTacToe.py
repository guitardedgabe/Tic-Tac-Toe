from CpuPlayer import cpuplayer

class tictactoe:

	def __init__(self):
		self.printWelcome()
		self.board = self.newBoard()
		self.possibleInputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
		self.wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
		self.player1 = "player1"
		answer = raw_input("Play against a CPU? (y/n) ")
		if 'y' in answer:
			self.player2 = "cpu"
			self.cpu_player = cpuplayer()
		else:
			self.player2 = "player2"
		self.cur_player = self.player1
	
	def available(self, position):
		position = int(position)
		return self.board[position] == '-'
	
	def newBoard(self):
		board = []
		for i in range(0, 9):
			board.append('-')

		return board
	
	def printBoard(self):
		print self.board[0] + " " + self.board[1] + " " + self.board[2]
		print self.board[3] + " " + self.board[4] + " " + self.board[5]
		print self.board[6] + " " + self.board[7] + " " + self.board[8]

	def printWelcome(self):
		print """Welcome to Tic Tac Toe! The board is represented as follows at the beginning:\n\n- - -\n- - -\n- - -\n\nwith positions being:\n\n0 1 2\n3 4 5\n6 7 8\n\n"""
	
	def switchTurn(self):
		if self.cur_player == self.player1:
			self.cur_player = self.player2
		else:
			self.cur_player = self.player1

		self.play()
	
	def gameWon(self):
		count = 0
		for i in self.board:
			if i != '-':
				count += 1
		if count == 9:
			self.endGame("tie")
				
		for win in self.wins:
			x_count = 0
			o_count = 0
			for i in win:
				if self.board[i] == 'x':
					x_count += 1
				elif self.board[i] == 'o':
					o_count += 1
			if x_count == 3 or o_count == 3:
				return True

		return False
	
	def endGame(self, case):
		if case == "quit":
			print "Goodbye."
			exit(0)
		elif case == "gameover":
			if self.cur_player == self.player1:
				playerInput = raw_input("Player 1 wins! Want to play again? (y/n) ")
			elif self.cur_player == self.player2:
				playerInput = raw_input("Player 2 wins! Want to play again? (y/n) ")
		elif case == "tie":
			playerInput = raw_input("You guys tied! Want to play again? (y/n) ")

		if 'y' in playerInput:
			self.board = self.newBoard()
			self.play()
		elif 'n' in playerInput:
			print "Goodbye."
			exit(0)
	
	def makeMove(self, position):
		position = int(position)
		if self.cur_player == self.player1:
			self.board[position] = 'x'
		elif self.cur_player == self.player2:
			self.board[position] = 'o'

		self.printBoard()
	
	def play(self):
		playerInput = "0"
		while True:
			if self.cur_player == self.player1:
				playerInput = raw_input("What's your move player 1? ")
			elif self.cur_player == self.player2 and self.player2 == "player2":
				playerInput = raw_input("What's your move player 2? ")
			elif self.cur_player == self.player2 and self.player2 == "cpu":
				print "cpu's turn"
				playerInput = self.cpu_player.choice(self.board)

			print playerInput

			if playerInput != "quit":
				if playerInput in self.possibleInputs:
					if self.available(playerInput):
						self.makeMove(playerInput)
						if self.gameWon():
							self.endGame("gameover")
						self.switchTurn()
					else:
						print "That spot is already taken"
				else:
					print "Illegal move"
			elif playerInput == "quit":
				self.endGame("quit")
