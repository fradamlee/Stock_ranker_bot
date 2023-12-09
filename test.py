from tickers import *
# from investorsRecordStorer import InvestorsRecordStorer

inv1 = InvestorsRecord('Bob')
inv1.add_ticker_info('AAPL', 0)
inv1.add_ticker_info('FB', 40) #
inv1.add_ticker_info('MST', 0)
inv1.add_ticker_info('V', 0)

inv2 = InvestorsRecord('Alice')
inv2.add_ticker_info('AAPL', 50800)
inv2.add_ticker_info('MU', 10200)
inv2.add_ticker_info('MST', 32950)
inv2.add_ticker_info('V', 18800)

inv3 = InvestorsRecord('Eve')
inv3.add_ticker_info('AAPL', 1030)
inv3.add_ticker_info('MU', 860)
inv3.add_ticker_info('MST', 3500)
inv3.add_ticker_info('V', 10950)

inv4 = InvestorsRecord('John')
inv4.add_ticker_info('AAPL', 590)
inv4.add_ticker_info('MU', 1020)
inv4.add_ticker_info('MST', 600)
inv4.add_ticker_info('V', 7000)

inv1.add_percentage_for_each_ticker_from_total()
inv2.add_percentage_for_each_ticker_from_total()
inv3.add_percentage_for_each_ticker_from_total()
inv4.add_percentage_for_each_ticker_from_total()

data = inv4.get_self_serialized_data()
inv1.load_data(data)
print(inv1.dict_ticker_info)

# lst_of_invest = InvestorsRecordStorer()
# lst_of_invest.store_investors_record_in_db(inv1)
# lst_of_invest.store_investors_record_in_db(inv2)
# lst_of_invest.store_investors_record_in_db(inv3)
# lst_of_invest.store_investors_record_in_db(inv4)

# lst_of_invest._fill_ticker_summatories()

# print(inv1.dict_ticker_info)

