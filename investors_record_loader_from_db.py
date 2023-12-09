from database.pool import ref_guru_focus_data
from tickers import *

class InvestorsRecordLoaderFromDB:
    def __init__(self, date_of_record):
        self._already_loaded = False
        self.data_of_record = date_of_record
        self.list_of_investors_record = []
    
    def _load_list_of_investors_record_from_db(self):
        route = f'{self.data_of_record}'
        dict_serialized_investors_record = ref_guru_focus_data.get(route)
        for investors_name in dict_serialized_investors_record.keys():
            curr_inv_record = InvestorsRecord(investors_name)
            tickers_data_serialized = dict_serialized_investors_record[investors_name]
            curr_inv_record.load_data(tickers_data_serialized)
            self.list_of_investors_record.append(curr_inv_record)

    def get_loaded_list_of_investors_record_from_db(self):
        if self._already_loaded == False:
            self._load_list_of_investors_record_from_db()
            self._already_loaded = True
        return self.list_of_investors_record
            

