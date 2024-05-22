from libs.Dali import Dali
import re
import os

def init(self):
    self.random_words = 3
    self.Dali = Dali('dali', self.Config)

def run(self):
    words = self.Dali.get_random_words(self.random_words)
    prompt = 'Photo containing: ' + (', '.join(words))
    images = self.Dali.get(prompt)
    message = images[0]['revised_prompt'] + '\n\n#aYearForArt #Generated #AI #' + (' #'.join(words))
    image = images[0]['url']

    if (message and image):
        self.Post.init()
        self.Post.media(image, prompt)
        self.Post.status(message)
        print(self.Post.send())