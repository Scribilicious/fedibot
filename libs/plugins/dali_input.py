from libs.Dali import Dali
from libs.Gpt import Gpt
import re
import os

def init(self):
    self.Dali = Dali('dali_input', self.Config)
    self.Gpt = Gpt('dali_input', self.Config)

def run(self):
    prompt = input("What do you want to draw? ")

    if (not prompt):
        print('No input given...')
        return

    prompt = self.Gpt.get('Return only the corrected text of following input: ' + prompt)
    print('Corrected prompt:', prompt)

    hashtags = self.Gpt.get('Return only the hashtags of following input: ' + prompt)
    print('Prompt hashtags:', hashtags)

    images = self.Dali.get(prompt)

    message = images[0]['revised_prompt'] + '\n\n#aYearForArt #Generated #AI ' + hashtags
    image = images[0]['url']

    if (message and image):
        self.Post.init()
        self.Post.media(image, prompt)
        self.Post.status(message)
        print(self.Post.send())