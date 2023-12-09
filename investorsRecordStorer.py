from tickers import *
from database.pool import ref_guru_focus_data
from datetime import datetime

class InvestorsRecordDBStorer():
    def __init__(self):
        pass

    def store_investors_record_in_db(self, new_investors_record):
        serialized_data = new_investors_record.get_self_serialized_data()
        investors_name = new_investors_record.investors_name
        current_date = datetime.now().date()
        route = f'{current_date}/{investors_name}'
        ref_guru_focus_data.set(serialized_data, route)

    # def _iter_investors_record_to_fill_ticker_summatories(self, investors_record):
    #     dict_ticker_info = investors_record.dict_ticker_info
    #     for ticker in list(dict_ticker_info.keys()):
    #         record = dict_ticker_info[ticker]
    #         self.all_tickers_summatory_of_maket_cap.add_ticker_info(ticker, record['main_attribute'])
    #         self.all_tickers_summatory_of_contribution.add_ticker_info(ticker, record['percentage'])

    # def _fill_ticker_summatories(self):
    #     map(self._iter_investors_record_to_fill_ticker_summatories, self.lst_of_investors_record)
    #     self.all_tickers_summatory_of_maket_cap.add_percentage_for_each_ticker_from_total()
    #     self.all_tickers_summatory_of_contribution.add_percentage_for_each_ticker_from_total()

    # def _fill_ranking_list(self):
    #     dict_ticker_of_marketcap = self.all_tickers_summatory_of_maket_cap.dict_ticker_info
    #     dict_ticker_of_contribution = self.all_tickers_summatory_of_contribution.dict_ticker_info
    #     for ticker in list(dict_ticker_of_marketcap.keys()):
    #         ponderated_marketcap = dict_ticker_of_marketcap[ticker]['percentage'] * self.ponderation_of_marketcap
    #         ponderated_contribution = dict_ticker_of_contribution[ticker]['percentage'] * self.ponderation_of_contribution  
    #         total_ponderation = ponderated_marketcap + ponderated_contribution  
    #         self.ranking_list.append([ticker, total_ponderation])

    # def get_ranked_list(self, ponderation_of_marketcap, ponteration_of_contribution):
    #     self.ponderation_of_marketcap = ponderation_of_marketcap
    #     self.ponderation_of_contribution = ponteration_of_contribution
    #     self._fill_ticker_summatories()
    #     self._fill_ranking_list()
    #     self.ranking_list.sort(key=lambda x: -x[1])
    #     return self.ranking_list