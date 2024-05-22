import requests
import mimetypes
import pathlib
import os
import re

class Post:
    #
    # Initialize Post
    #
    def __init__(self, url: str, key: str):
        self.init(url, key)

    #
    # Sets the API call
    #
    def init(self, url: str = None, key: str = None):
        self.url = self.url if url is None else url
        self.key = self.key if key is None else key
        self.json = {
            'status' : '',
            'visibility' : 'public',
            'attachment' : [],
            'media_ids' : [],
        }
        self.call = 'statuses'
        self.files = None
        self.data = None
        self.type = 'post'

    #
    # Get x number of posted posts
    #
    def statuses(self, limit=1):
        account = self.send('accounts/verify_credentials', '', '', '', 'get')
        if account.status_code != 200:
            return None

        response = self.send('accounts/' + account.json()['id'] + '/statuses', {'limit': limit}, '', '', 'get')
        if response.status_code == 200:
            return response.json()

        return None

    #
    # Delete a post
    #
    def delete(self, id):
        return self.send('statuses/' + id, '', '', '', 'delete')

    #
    # Sets the API call
    #
    def call(self, call):
        self.call = call

    #
    # Sets a status text
    #
    def status(self, status):
        self.json['status'] = status

    #
    # visibility
    # private public
    #
    def visibility(self, visibility):
        self.json['visibility'] = visibility

    #
    # Sets the Data
    #
    def data(self, data):
        self.data = data

    #
    # Sets the Type
    #
    def type(self, type):
        self.type = type

    #
    # Adds an attachment
    #
    def media(self, file_path: str, description = None, type = None):
        if (not type):
            filename = file_path.split("#")[0].split("?")[0]
            type = mimetypes.guess_type(filename)
            if (not type[0]):
                return
            type = type[0]

        if file_path.startswith("https://") or file_path.startswith("http://"):
            file_path = self.download(file_path, os.path.dirname(__file__) + '/../data/temp/')

        if (not file_path):
            print('Could not upload file...')
            return None

        if (not os.path.exists(file_path)):
            print('File', file_path, 'does not exists...')
            return None

        response = self.send('media', '', {'description': description}, {'file': open(file_path, 'rb')})
        media_id = response.json().get('id')

        if (not media_id):
            print('No media id returned...')
            return None

        self.json['media_ids'].append(media_id)

    #
    # Make a post request
    #
    def send(self, call = None, json = None, data = None, files = None, type = None):
        if (call == None):
            call = self.call 

        if (json == None):
            json = self.json

        if (data == None):
            data = self.data

        if (files == None):
            files = self.files  

        if (type == None):
            type = self.type

        try:
            if (type == 'post'):
                response = requests.post(
                    url = self.url + '/api/v1/' + call,
                    headers = {
                        'Authorization': 'Bearer ' + self.key
                    },
                    json = json,
                    data = data,
                    files = files
                )
            elif (type == 'delete'):
                response = requests.delete(
                    url = self.url + '/api/v1/' + call,
                    headers = {
                        'Authorization': 'Bearer ' + self.key
                    }
                )
            else:
                response = requests.get(
                    url = self.url + '/api/v1/' + call,
                    headers = {
                        'Authorization': 'Bearer ' + self.key
                    },
                    params = json
                )

            return response

        except:
            return None



    #
    # Downloads an url to a temp dir
    #
    def download(self, url: str, dest_folder: str, filename: str = None):
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)  # create folder if it does not exist

        if not filename:
            match = re.search(r'/([^/?]+)(?:\?|$)', url)
            if match:
                filename = match.group(1)
            else:
                return None

        file_path = os.path.join(dest_folder, filename)

        r = requests.get(url, stream=True)
        if r.ok:
            print("Saving to", os.path.abspath(file_path), '...')
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 8):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        os.fsync(f.fileno())
            return file_path

        print("Download failed: status code {}\n{}".format(r.status_code, r.text))
        return None
