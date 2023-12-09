import pickle
import base64

class Serializer:
    def __init__(self):
        pass

    def get_serialized_data(self, object):
        serialized_obj = pickle.dumps(object)
        return base64.b64encode(serialized_obj).decode('utf-8')
    
    def get_deserialized_object(self, serialized_data):
        return pickle.loads(base64.b64decode(serialized_data))