import shutil
import random

def init(self):
    pass

def run(self):
    disc = shutil.disk_usage('/')
    bleeps = ['Bleep' for _ in range(random.randint(1, 3))]
    message = ', '.join(bleeps) + '... Free server space is ' + format(((100 / disc.total) * disc.free), '.2f') + '%' + '\n\n#FreeSpace #ServerStatus'
    self.Post.status(message)
    print(self.Post.send())
