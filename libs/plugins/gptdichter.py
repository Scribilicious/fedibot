import locale, datetime
from libs.Gpt import Gpt

def init(self):
    self.random_words = 3
    self.Gpt = Gpt('gptdichter', self.Config, 'nomen', 786)

def run(self):
    locale.setlocale(locale.LC_TIME, locale.normalize("de_DE.utf8"))
    today = datetime.datetime.today()
    words = self.Gpt.get_random_words(self.random_words)
    message = self.Gpt.get(
        'Schreibe eine Gedicht mit die folgende Wörtern: ' + (', '.join(words)) + '. ' +
        'Bitte beachte den Wochentag und Monat beim schreiben vom Gedicht. Der Wochentag ist ' + today.strftime("%A") + ' und der Monat ist ' + today.strftime("%B") + '.')
    message += '\n\n#Gedicht ' + today.strftime("#%A #%B") + ' #' + (' #'.join(words))

    if (message):
        self.Post.status(message)
        print(self.Post.send())
