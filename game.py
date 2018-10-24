class Game(object):
	def __init__ (self):
		self.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
					  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
					  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
					  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
					  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
					  [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

	def show_board(self):
		#
		# Prints the board with numbers above it
		#
		print('\n  1    2    3    4    5    6    7\n')
		for line in self.board:
			print('%s \n' %(line))		
		return self.board

	def clear_board(self):
		#
		# Clears the board for a new game
		# 
		self.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
					  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
					  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
					  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
					  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
					  [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
		return self.board

	def game_start(self):
		#
		# Initialize the game, and if done allows user to replay
		#
		global player_1
		global player_2
		global current_game
		global count
		global winner
		winner = False
		count = 0

		current_game.clear_board()
		current_game.show_board()

		player_1 = Player(0,0)
		player_2 = Player(0,0)

		player_1.name = input('Player 1 name: ')
		print('Hello %s' %(player_1.show_name()))

		player_1.set_symbol()
		if player_1.get_symbol() == 'X':
			player_2.set_symbol_fast('O')
		else:
			player_2.set_symbol_fast('X')

		player_2.name = input('Player 2 name: ')
		print('Hello %s' %(player_2.show_name()))

		while winner == False:
			current_game.get_move()
			current_game.show_board()
			continue
		else:
			game_over = input('Game over!\nWant to play again? ').lower()
			if game_over == 'yes' or game_over == 'y':
				current_game.game_start()
			else:
				print('Okay, thanks for playing!')

	def get_move(self):
		#
		# Takes user move, check if it is valid, and puts it on the board
		#
		global play
		global count
		global current_line
		global current_player
		global current_symbol
		play = 0
		
		current_game.current_player()

		while True:
			try:
				play = int(input('%s, pick your play: ' %(current_player))) - 1
				while play not in range(0,7):
					print('Pick a number between 1 and 7')
					play = int(input('%s, pick your play: ' %(current_player))) - 1
				else:
					current_game.board_gravity()
					current_game.check_full()
					while current_game.check_full() == True:
						print('This column is full, pick another one')
						play = int(input('%s, pick your play: ' %(current_player))) - 1
					else:
						current_game.board_gravity()
						self.board[current_line][play] = current_symbol
						current_game.check_winner()
						count += 1
						break
			except ValueError:
				print('Pick a valid number')

	def current_player(self):
		#
		# Determines which player is making a move
		#
		global current_player
		global current_symbol
		global count

		if count % 2 == 0:
			current_player = player_1.show_name()
			current_symbol = player_1.get_symbol()
		else:
			current_player = player_2.show_name()
			current_symbol = player_2.get_symbol()

	def board_gravity(self):
		#
		# Makes symbols stack over each other
		#
		global play
		global current_line
		current_line = 5

		while current_line > 0:
			if self.board[current_line][play] != ' ':
				current_line -= 1
				continue
			else:
				self.board[current_line][play]
				break

	def check_full(self):
		#
		# Checks if the column chosen by the player is full
		#
		global play
		global current_line

		if (current_line == 0 
			and self.board[current_line][play] != ' '):
			return True
		else:
			return False

	def check_winner(self):
		#
		# Checks if a winning combination is present in the board
		#
		global winner
		winner = False
		check_h = 6
		check_v = 5

		while check_v >= 0 and winner == False:

			while check_h >= 0 and winner == False:
				
				# Horizontal check:
				if (self.board[check_v][check_h] != ' '
				and check_h >= 3
				and self.board[check_v][check_h] == self.board[check_v][check_h-1]
				and self.board[check_v][check_h] == self.board[check_v][check_h-2]
				and self.board[check_v][check_h] == self.board[check_v][check_h-3]):
					current_game.print_winner()
					print('Horizontal win')
					winner = True
					break
				
				# Vertical check:
				elif (self.board[check_v][check_h] != ' '
				and check_v <= 2
				and self.board[check_v][check_h] == self.board[check_v+1][check_h]
				and self.board[check_v][check_h] == self.board[check_v+2][check_h]
				and self.board[check_v][check_h] == self.board[check_v+3][check_h]):
					current_game.print_winner()
					print('Vertical win')
					winner = True
					break

				# Diagonal right check:
				elif (self.board[check_v][check_h] != ' '
				and check_h <= 3
				and check_v >= 3
				and self.board[check_v][check_h] == self.board[check_v-1][check_h+1]
				and self.board[check_v][check_h] == self.board[check_v-2][check_h+2]
				and self.board[check_v][check_h] == self.board[check_v-3][check_h+3]):
					current_game.print_winner()
					print('Diagonal right win')
					winner = True
					break

				# Diagonal left check:
				elif (self.board[check_v][check_h] != ' '
				and check_h >= 3
				and check_v >= 3
				and self.board[check_v][check_h] == self.board[check_v-1][check_h-1]
				and self.board[check_v][check_h] == self.board[check_v-2][check_h-2]
				and self.board[check_v][check_h] == self.board[check_v-3][check_h-3]):
					current_game.print_winner()
					print('Diagonal left win')
					winner = True
					break
				
				else:
					check_h -= 1
					continue

			else:
				check_v -= 1
				check_h = 6
				continue

	def print_winner(self):
		#
		# Prints the winner based on current player
		#
		global count

		if count % 2 == 0:
			print('\n%s won the game!' %(player_1.show_name()))
		else:
			print('\n%s won the game!' %(player_2.show_name()))


class Player(object):

	def __init__(self, name, symbol):
		Game.__init__(self)
		self.symbol = symbol

	def show_name(self):
		return self.name

	def set_symbol(self):
		symbol = ''
		self.symbol = symbol
		symbol = input("Choose 'X' or 'O' as your symbol: ").lower()
		while symbol != 'x' and symbol != 'o':
			print("Pick a valid symbol")
			symbol = input("Choose 'X' or 'O' as your symbol: ").lower()
		else:
			if symbol == 'x':
				print("You pick 'X', so player 2 will use 'O'")
				self.symbol = 'X'
			else:
				print("You pick 'O', so player 2 will use 'X'")
				self.symbol = 'O'
			return self.symbol

	def set_symbol_fast(self, symbol):
		self.symbol = symbol
		return self.symbol

	def get_symbol(self):
		return self.symbol

current_game = Game()
current_game.game_start()
