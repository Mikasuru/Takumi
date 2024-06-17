import requests
from tempfile import gettempdir
import os
from urllib.parse import urlparse

def TakumiWaifu(url, start_index=1):
    while True:
        response = requests.get(url)

        if response.status_code == 200:
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            file_extension = os.path.splitext(filename)[1]
            temp_dir = gettempdir()

            index = start_index
            while True:
                unique_filename = f"Takumi{index}{file_extension}"
                file_path = os.path.join(temp_dir, unique_filename)
                if not os.path.exists(file_path):
                    break
                index += 1

            with open(file_path, "wb") as file:
                file.write(response.content)

            start_index = index + 1