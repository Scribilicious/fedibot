from libs.Gpt import Gpt

def init(self):
    self.random_words = 3
    self.post_size = 1000
    self.Gpt = Gpt('gptpost', self.Config)

def run(self):
    words = self.Gpt.get_random_words(self.random_words)
    message = self.Gpt.get('Create a post of ' + str(self.post_size) + ' characters using following words: ' + (', '.join(words)))
    message += '\n\n#AI #' + (' #'.join(words))

    if (message):
        self.Post.status(message)
        print(self.Post.send())
