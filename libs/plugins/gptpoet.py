import datetime
from libs.Gpt import Gpt

def init(self):
    self.random_words = 3
    self.Gpt = Gpt('gptpoet', self.Config)

def run(self):
    today = datetime.datetime.today()

    words = self.Gpt.get_random_words(self.random_words)
    # words.append(today.strftime("%A"))
    # words.append(today.strftime("%B"))

    #message = self.Plugin.gpt(self, 'Create a poem that contains following words: ' + (', '.join(words)) + '. Keep in mind that the season of the poem is set in the month ' + today.strftime("%B") + '.')
    message = self.Gpt.get(
        'Create a poem that contains following words: ' + (', '.join(words)) + '. ' +
        'The day and season of the poem is on a ' + today.strftime("%A") + ' in ' + today.strftime("%B") + '.')
    message += '\n\n#Poems #AI ' + today.strftime("#%A #%B") + ' #' + (' #'.join(words))

    if (message):
        self.Post.status(message)
        print(self.Post.send())
