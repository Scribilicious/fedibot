import requests
import random
import os
from libs.Sql import Sql

class Gpt:
    #
    # Initialize Gpt
    #
    def __init__(self, name, Config, words_list = 'nouns', words_count = 1524):
        self.words_file_name = os.path.dirname(__file__) + '/data/' + words_list + '.txt'
        self.words_count = words_count
        self.Config = Config
        self.name = name

    def get_random_words(self, word_count):
        _Sql = Sql(self.name)
        _Sql.createTable('words', 'word TEXT')

        words = []
        count = 0
        while count < word_count:
            number = random.randint(1, self.words_count)
            word = self.get_line_number(number)
            result = _Sql.execute('SELECT word FROM words WHERE word = (?)', [word], True)

            if (not result):
                _Sql.execute('INSERT INTO words VALUES (?)', [word])
                result = _Sql.execute("SELECT COUNT(*) FROM words", [], True)
                if (result[0][0] >= self.words_count):
                    _Sql.execute("DELETE FROM words")
                words.append(word)
                count += 1

        return words

    def get_line_number(self, line_number):
        with open(self.words_file_name, 'r') as file:
            lines = file.readlines()
            return lines[line_number - 1].strip()

    #
    # Makes the API call
    #
    def get(self, content):
        res = requests.post("https://api.openai.com/v1/chat/completions",
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.Config['CHATGPT']['key']
        },
        json={
            "model": self.Config['CHATGPT']['model'],
            "messages": [{"role": "user", "content": content}],
            "temperature": float(self.Config['CHATGPT']['temperature']),
            "max_tokens": int(self.Config['CHATGPT']['max_tokens'])
        }).json()

        return res['choices'][0]['message']['content']
