class Voyageur(object):
	def __init__(self, debut, dest, vision, pas):
		self.debut    = debut
		self.position = debut
		self.dest  	  = dest
		self.vision   = vision
		self.pas      = pas

	def observation(self):
		pass

	def deplacement(self):
		pass