from firebase_admin import credentials, db
import firebase_admin
firebase_url = "https://stock-ranker-a2862-default-rtdb.firebaseio.com/"

cred = credentials.Certificate("database/credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': firebase_url
})

class InvestorsRecordListDBInterface:
    def __init__(self, db):
        self.db = db
        self.min_number_of_slashes = 1

    def _is_valid_route(self, route):
        total = 0
        if '//' in route:
            return False
        route_length = len(route)
        for i in range(route_length):
            if route[i] == '/':
                if i==0 or i==route_length-1:
                    return False
                total += 1
        return total>=self.min_number_of_slashes

    def get(self, route=''):
        ref = self.db.reference('investors_record_list/' + route)
        return ref.get()
    
    def set(self, data, route):
        if(self._is_valid_route(route) == False):
            raise Exception('Invalid route')
        ref = self.db.reference('investors_record_list/' + route)
        ref.set(data)

ref_guru_focus_data = InvestorsRecordListDBInterface(db)