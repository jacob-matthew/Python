from scene import *

class Game(Scene):
	def setup(self):
		self.background_color = '#030704'
		ground = Node(parent=self)
		x = 0
		while x <= self.size.w +64:
			tile = SpriteNode('plf:Ground_Dirt', position=(x,25))
			ground.add_child(tile)
			x += 64
		#Create Player Sprite
		self.player = SpriteNode('plf:AlienPink_front')
	
		#self.player.anchor_point = (0.5, 0)
						
		#Position
		self.player.position = (self.size.w / 2, 120)
		ground.add_child(self.player)								

run(Game())	
