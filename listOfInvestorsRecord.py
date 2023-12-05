from tickers import *

def map(fucn, lst):
    for ele in lst:
        fucn(ele)

class ListOfInvestorsRecord():
    def __init__(self):
        self.lst_of_investors_record = []
        self.all_tickers_summatory_of_maket_cap = Tickers()
        self.all_tickers_summatory_of_contribution = Tickers()
        self.ponderation_of_market_cap = 0
        self.ponderation_of_contribution = 0
        self.ranking_list = []

    def append_investors_record(self, new_investors_record):
        self.lst_of_investors_record.append(new_investors_record)

    def _iter_investors_record_to_fill_ticker_summatories(self, investors_record):
        dict_ticker_info = investors_record.dict_ticker_info
        for ticker in list(dict_ticker_info.keys()):
            record = dict_ticker_info[ticker]
            self.all_tickers_summatory_of_maket_cap.add_ticker_info(ticker, record['main_attribute'])
            self.all_tickers_summatory_of_contribution.add_ticker_info(ticker, record['percentage'])

    def _fill_ticker_summatories(self):
        map(self._iter_investors_record_to_fill_ticker_summatories, self.lst_of_investors_record)
        self.all_tickers_summatory_of_maket_cap.add_percentage_for_each_ticker_from_total()
        self.all_tickers_summatory_of_contribution.add_percentage_for_each_ticker_from_total()

    def _fill_ranking_list(self):
        dict_ticker_of_market_cap = self.all_tickers_summatory_of_maket_cap.dict_ticker_info
        dict_ticker_of_contribution = self.all_tickers_summatory_of_contribution.dict_ticker_info
        for ticker in list(dict_ticker_of_market_cap.keys()):
            ponderated_market_cap = dict_ticker_of_market_cap[ticker]['percentage'] * self.ponderation_of_market_cap
            ponderated_contribution = dict_ticker_of_contribution[ticker]['percentage'] * self.ponderation_of_contribution  
            total_ponderation = ponderated_market_cap + ponderated_contribution  
            self.ranking_list.append([ticker, total_ponderation])

    def get_ranked_list(self, ponderation_of_market_cap, ponteration_of_contribution):
        self.ponderation_of_market_cap = ponderation_of_market_cap
        self.ponderation_of_contribution = ponteration_of_contribution
        self._fill_ticker_summatories()
        self._fill_ranking_list()
        self.ranking_list.sort(key=lambda x: -x[1])
        return self.ranking_list