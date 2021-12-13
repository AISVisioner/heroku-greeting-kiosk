import os
from datetime import datetime, timezone
import uuid
import requests
from glob import glob
import cv2 as cv
import face_recognition
from dotenv import load_dotenv
load_dotenv()

def get_token():
    """
    a function to fetch a token to access REST API

    parameter: no
    return: token(str)
    
    """
    # device id - db 참조
    data = {
        'username': os.getenv('USERNAME'),
        'password': os.getenv('PASSWORD')
    }
    print(data)
    response=''
    try:
        response = requests.post(f'{os.getenv("BASEURL")}/auth/token/login/', data=data)
    except:
        print('error')
    my_token = response.json()['auth_token']
    print(my_token)

    return my_token

MY_TOKEN = get_token()

glob_files = glob('face_upload/images/*jpeg')
print(len(glob_files))

import random
randomlist = []
for i in range(0,20):
    n = random.randint(0,41)
    randomlist.append(n)
print(randomlist)

cnt = 0
for i in randomlist:
    # current_time = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d_%H:%M:%S")
    # guest_name = f"guest_{current_time}_{str(uuid.uuid4())[:10]}"
    frame = cv.imread(glob_files[i])
    image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(image)
    for box in boxes:
        encoding = face_recognition.face_encodings(image, [box])[0]
    print(encoding)
    files = {
        'photo': open(glob_files[i], 'rb')
    }
    data = {
        "id" : str(uuid.uuid4()),
        "encoding" : encoding,
        "name" : os.path.basename(glob_files[i])
    }
    response = requests.post(f'https://greetingkiosk.herokuapp.com/api/v1/lookup/', \
        files=files, data=data, headers={'Authorization': f'Token {MY_TOKEN}'})
    response.raise_for_status()
    cnt += 1
    print(cnt)