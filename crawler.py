import requests
import os
from aux import createRemoteFolder
from aux import upload_photo
from dotenv import load_dotenv
load_dotenv()

def main():
    url = os.environ.get('URL')
    max = int(os.environ.get('MAX'))
    name = split_name(url)
    
    download_images(name,get_image_list(url, max)) 

    remote_folder_id = createRemoteFolder(name)   
    for img in get_image_list(url, max): upload_photo(name, split_name(img),remote_folder_id)

def process_url(number, url):    
    sanitized_number = lambda x: f"_000{x}" if x < 10 else f"_00{x}" if x < 99 else f"_0{x}" if x < 998 else ""
    return f"{url}{sanitized_number(number)}.jpg"

def get_image_list(url,max):
    return list(map(lambda x: process_url(x,url), range(1,max+1)))

def download_images(path,url_list):
    full_path = f"img/{path}/" 
    try: 
        os.mkdir(full_path)
    except OSError as error: 
        print(error)
    for url in url_list: open(full_path+split_name(url), 'wb').write(requests.get(url).content)

def split_name(url):
    return  url.split('/')[-1]

if __name__ == "__main__":
    main()