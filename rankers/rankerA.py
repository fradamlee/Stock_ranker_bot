from rankers.abstract_ranker import *
from tickers import *
from math import sqrt, pow

'''
This type of ranker is based on two criteria
1.  The marketcap sum gived by all guru investors portfolio per ticker
2.  The contribution that can be understand as the sum of the
    percentages after made it a square root (to make it more flat) 
    and raised to the power of some criteria called 'contribution_flatness',
    This number is typically between 1 and 2
    The idea of this criteria is to give importance to the 
    propotion that each investors have per ticker, (not just
    to the total money in a stock)
'''
class RankerA(AbstractRanker):
    def __init__(self, *args):
        super().__init__(*args)
        self.all_tickers_summatory_of_marketcap = Tickers()
        self.all_tickers_summatory_of_contribution = Tickers()
        self._already_ranked = False
        self.marketcap_ponderation = self.dict_mesurement_cirteria['marketcap_ponderation']
        self.contribution_ponderation = self.dict_mesurement_cirteria['contribution_ponderation']
        self.contribution_flatness = self.dict_mesurement_cirteria['contribution_flatness']
    
    def _get_the_contibution_per_ticker(self, percentage, number_of_tickers):
        brute_contribution = percentage * number_of_tickers / 10
        brute_contribution_sqrt = sqrt(brute_contribution)
        return pow(brute_contribution_sqrt, self.contribution_flatness)
    
    def _map_dict_ticker_info_to_fill_summatories(self, dict_ticker_info):
        tickers = dict_ticker_info.keys()
        number_of_tickers = len(tickers)
        for ticker in tickers:
            marketcap = dict_ticker_info[ticker]['main_attribute']
            percentage = dict_ticker_info[ticker]['percentage']
            contribution = self._get_the_contibution_per_ticker(percentage, number_of_tickers)
            self.all_tickers_summatory_of_marketcap.add_ticker_info(ticker, marketcap)
            self.all_tickers_summatory_of_contribution.add_ticker_info(ticker, contribution)
    
    def _map_list_of_investors_record_to_fill_summatories(self):
        for inv_rec in self.list_of_investors_record:
            dict_ticker_info = inv_rec.get_dict_ticker_info()
            self._map_dict_ticker_info_to_fill_summatories(dict_ticker_info)

    def _sort_ranked_list(self):
        self.ranked_list.sort(key=lambda x: -x[1])

    def _get_partial_rank_punctuation(self, percentage, ponderation):
        return percentage * ponderation / 100

    def _get_rank_punctuation_per_ticker(self, marketcap_percentage, contribution_percentage):
        marketcap_partial_rank_punctuation = self._get_partial_rank_punctuation(marketcap_percentage, self.marketcap_ponderation)
        contribution_partial_rank_punctuation = self._get_partial_rank_punctuation(contribution_percentage, self.contribution_ponderation)
        return marketcap_partial_rank_punctuation + contribution_partial_rank_punctuation

    def _map_percentages_of_summatories_to_fill_ranked_list(self):
        dict_of_all_tickers_summatory_of_marketcap = self.all_tickers_summatory_of_marketcap.get_dict_ticker_info()
        dict_of_all_tickers_summatory_of_contribution = self.all_tickers_summatory_of_contribution.get_dict_ticker_info()
        all_tickers = dict_of_all_tickers_summatory_of_marketcap.keys()
        for ticker in all_tickers:
            marketcap_percentage = dict_of_all_tickers_summatory_of_marketcap[ticker]['percentage']
            contribution_percentage = dict_of_all_tickers_summatory_of_contribution[ticker]['percentage']
            rank_punctuation = self._get_rank_punctuation_per_ticker(marketcap_percentage, contribution_percentage)
            self.ranked_list.append([ticker, rank_punctuation])
    
    def _prepare_ranked_list(self):
        self._map_list_of_investors_record_to_fill_summatories()
        self.all_tickers_summatory_of_marketcap.add_percentage_for_each_ticker_from_total()
        self.all_tickers_summatory_of_contribution.add_percentage_for_each_ticker_from_total()
        self._map_percentages_of_summatories_to_fill_ranked_list()
        self._sort_ranked_list()

    def get_ranked_list(self):
        if(self._already_ranked == False):
            self._prepare_ranked_list()
            self._already_ranked = True
        return self.ranked_list
        