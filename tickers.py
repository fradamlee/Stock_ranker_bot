from serializer import Serializer
import math 

class Tickers():
    def __init__(self):
        self.dict_ticker_info = {}
        self.total = 0
        self.serializer = Serializer()

    def add_ticker_info(self, ticker, main_attibute_value):
        if (self.dict_ticker_info.get(ticker) != None):
            self.dict_ticker_info[ticker]['main_attribute'] += main_attibute_value
        else:
            self.dict_ticker_info[ticker] = {
                'main_attribute': main_attibute_value
            }
        self.total += main_attibute_value

    def add_percentage_for_each_ticker_from_total(self):
        for key in list(self.dict_ticker_info.keys()):
            record = self.dict_ticker_info[key]
            value = record['main_attribute']
            record['percentage'] = value * 100 / self.total

    def get_self_serialized_data(self):
        dic = {'tickers': self.dict_ticker_info}
        return self.serializer.get_serialized_data(dic)

    def load_data(self, serialized_data):
        obj = self.serializer.get_deserialized_object(serialized_data)
        self.dict_ticker_info = obj['tickers']

    def get_dict_ticker_info(self):
        return self.dict_ticker_info

class InvestorsRecord(Tickers):
    def __init__(self, investors_name):
        super().__init__()
        self.investors_name = investors_name
            
    # def _get_contribution(self, value):
    #     sqrt_val = math.sqrt(value)
    #     return math.pow(sqrt_val, 1.2)

    # def add_percentage_for_each_ticker_from_total(self):
    #     for key in list(self.dict_ticker_info.keys()):
    #         record = self.dict_ticker_info[key]
    #         value = record['main_attribute']
    #         percentage = value * 100 / self.total
    #         record['percentage'] = self._get_contribution(percentage)