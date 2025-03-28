import os, json, time
from datetime import datetime
from django.conf import settings

DATA_DIR = os.path.join(settings.BASE_DIR, 'message','data')

os.makedirs(DATA_DIR, exist_ok=True)

def create(nom,objet,email,message,status):
    status = False
    timestamp = str(int(time.time()))
    file_path = os.path.join(DATA_DIR,f'{timestamp}.json')

    with open(file_path , 'w') as json_file:
        json.dump({
            "nom":nom,
            "objet":objet,
            "email":email,
            "message":message,
            "status":status
        },json_file)

def get_message():
    messages = []
    for filename in os.listdir(DATA_DIR):
        timestamp = filename.replace('.json','')
        date_string = datetime.fromtimestamp(int(timestamp))

        with open(os.path.join(DATA_DIR,filename),'r')as json_file:
            data = json.load(json_file)
            messages.append({
                "filename":filename,
                "date":date_string,
                **data
            })
    return messages