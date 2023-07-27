import sys
import random

def init(self):
    pass

def run(self):
    self.Post.status('Just a bot test :)')
    self.Post.media('https://www.kitchenrecords.nl/data/releases/electro_maniac/cover.jpg', 'Kitchen Records World Wide :)')
    print(self.Post.send())
