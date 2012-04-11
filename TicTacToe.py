class TicTacToe:

	""" Create an instance of the board, set up legal positions for playing, and define the win scenarios """
	def __init__(self):
		self.board = self.newBoard()
		self.printWelcome()
		self.plausibleAnswers = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
		self.wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8]]
	
	""" Method to start the game """
	def play(self):
		answer = raw_input("To begin the game, type a number (0-8) representing the position you wish to mark. Type 'quit' now or any time to exit.\n")

		while (answer != "quit"):
			if answer in self.plausibleAnswers:
				""" Checks to see if the position is available """
				if self.available(answer):
					self.makeMove("human", answer)
					if self.winner():
						answer = raw_input("Winner! Want to play again? (y/n) ")
						if 'y' in answer:
							self.board = self.newBoard()
							self.play()
						else:
							print "Goodbye"
							exit(0)
				elif not self.available(answer):
					print "That spot is already taken."
			else:
				print "Illegal move."

			answer = raw_input("Next move? ")

		print "Goodbye"
	
	""" Method to create a new board """
	def newBoard(self):
		board = []
		for i in range(0, 9):
			board.append("-")

		return board

	""" Method for printing the current state of the board """
	def printBoard(self):
		print self.board[0] + " " + self.board[1] + " " + self.board[2]
		print self.board[3] + " " + self.board[4] + " " + self.board[5]
		print self.board[6] + " " + self.board[7] + " " + self.board[8]
	
	""" Method that handles the move-making """
	def makeMove(self, player, position):
		position = int(position)
		if player == "human":
			self.board[position] = 'x'
		elif player == 'cpu':
			self.board[position] = 'o'

		self.printBoard()
	
	""" Method for checking to see if a player has won. Uses the self.wins list """
	def winner(self):
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
	
	""" Check the availability of a position on the board """
	def available(self, position):
		position = int(position)
		return self.board[position] == '-'
	
	""" A courtesy welcome message to orient the player with the board and possible positions """
	def printWelcome(self):
		print """Welcome to Tic Tac Toe! The board is represented as follows at the beginning:\n\n- - -\n- - -\n- - -\n\nwith positions being:\n\n0 1 2\n3 4 5\n6 7 8\n\n"""
