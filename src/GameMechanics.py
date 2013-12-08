#!/usr/bin/env python

class GameMechanics(object):
	def __init__(self, turn_counter):
		self.turn_counter = turn_counter

	def turn_picker(self, turn_counter):
		if (turn_counter % 2 == 0):
			turn = "White's"
		else:
			turn = "Black's"
		return turn

