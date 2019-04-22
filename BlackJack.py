import random

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing = True

# Class definitions

class Card():
	def __init__(self,suit,rank,value):
		self.suit = suit
		self.rank = rank
		self.value = value

	def __str__(self):
		print(f'{self.rank} of {self.suit}')

class Deck():
	def __init__(self):
		deck = []
		for suit in suits:
			for rank in ranks:
				deck.append({'suit':'rank'})

	def __str__(self):
		for item in deck:
			print(item)

	def shuffle_deck(self):
		random.shuffle(deck)

	def deal(self):
		#player_hand = []
		first_card = random.choice(deck)
		#player_hand.append(first_card)
		deck.remove(first_card)

class Hand():
	def __init__(self):
		self.player_hand = []
		self.value = 0
		self.aces = 0

	def __str__(self):
		for item in player_hand:
			print(item)

	def sum_hand(self):
		
		if item in self.player_hand == 'Ace':
			self.aces += 1

		try:
			for item in self.player_hand:
				self.value += values[player_hand.values()]
		except:
			if self.value > 21 and self.aces !=0:
				self.value += 1
				continue
		finally:
			print(self.value)

class Chips():
	def __init__(self):
		bankroll = 100
		bet = 0

	def take_bet(self):
		try:
			print(f"Your bankroll is {bankroll}")
			bet = int(input('What amount would you like to bet? '))

		except:
			print('Please input an amount for your bet.')

	def win_bet(self):
		bankroll += bet*2
		print(f"Congratulations! You won {bet*2}. Your new bankroll is {bankroll}")

	def lose_bet(self):
		bankroll -= bet
		print(f"Sorry, you lost your bet. Your new bankroll is {bankroll}")


# Function definitions




		


