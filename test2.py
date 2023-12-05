import firebase_admin
from firebase_admin import credentials, db
import json
import time
from test import lst_of_invest
import pickle
import base64



class ExampleClass:
    def __init__(self):
        self.lst = []
    
if __name__ == '__main__':
    ex1 = ExampleClass()
    ex1.lst.append(6)
    ex1.lst.append(7)

    firebase_url = "https://stock-ranker-a2862-default-rtdb.firebaseio.com/"

    # Replace "path/to/your/credentials.json" with the path to your downloaded service account JSON file
    cred = credentials.Certificate("credentials.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': firebase_url
    })

    # # serialized_obj = json.dumps(lst_of_invest.__dict__)
    # serialized_obj = pickle.dumps(lst_of_invest)
    # encoded_data = base64.b64encode(serialized_obj).decode('utf-8')

    ref = db.reference('/test')
    # ref.child('costum_key').set(encoded_data)
    # time.sleep(1)
    retrieved_obj_str = ref.get()
    # Deserialize the object
    # retrieved_obj_dict = json.loads(retrieved_obj_str['costum_key'])
    # reconstructed_obj = ExampleClass(**retrieved_obj_dict)
    decoded_data = pickle.loads(base64.b64decode(retrieved_obj_str['costum_key']))
    # print(retrieved_obj_dict)
    decoded_data.get_ranked_list(100, 0)


