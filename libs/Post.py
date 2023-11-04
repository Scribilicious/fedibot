import requests
import mimetypes
import pathlib
import os

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
            print('File', filepath, 'does not exists...')
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
    def send(self, call = None, json = None, data = None, files = None):
        if (call == None):
            call = self.call 

        if (json == None):
            json = self.json

        if (data == None):
            data = self.data

        if (files == None):
            files = self.files  

        try:
            response = requests.post(
                url = self.url + '/api/v1/' + call,
                headers = {
                    'Authorization': 'Bearer ' + self.key
                },
                json = json,
                data = data,
                files = files
            )

            return response

        except:
            return None

    #
    # Downloads an url to a temp dir
    #
    def download(self, url: str, dest_folder: str):
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)  # create folder if it does not exist

        filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
        filename = filename.split('?')[0]
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
