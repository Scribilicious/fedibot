import requests
import re
import urllib

class Crawler:
    #
    # Initialize Post
    #
    def __init__(self):
        self.url = None
        self.response = None

    def get(self, url):
        self.url = url
        try:
            self.response = requests.get(url).text
            return self.response
        except Exception as e:
            print(f"Error downloading {url}: {str(e)}")

        return None

    def getResponse(self):
        return self.response

    def findImages(self):
        return self.find('<img .*?src="(.*?)"')

    def find(self, regex, all = True):
        if (all):
            return re.findall(regex, self.response)
        else:
            return re.search(regex, self.response).group(1)
