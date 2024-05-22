import sys
import random

def init(self):
    pass

def run(self):
    statuses = self.Post.statuses(100)
    if (statuses):
        for status in statuses:
            if "#<span>ServerStatus</span>" in status['content']:
                print('Deleting ID:', status['id'], self.Post.delete(status['id']))

