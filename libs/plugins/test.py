import sys
import random

def init(self):
    pass

def run(self):
    statuses = self.Post.statuses(100)
    if (statuses):
        for status in statuses:
            if "#<span>AI</span>" in status['content']:
                print('Skipped ID:', status['id'])
            else:
                print('Deleting ID:', status['id'], self.Post.delete(status['id']))
            #print('Deleting post id:', status['id'], self.Post.delete(status['id']))

