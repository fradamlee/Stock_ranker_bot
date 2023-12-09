from investors_record_loader_from_db import *
from rankers.rankerA import RankerA

today = '2023-12-07'
inv_loader = InvestorsRecordLoaderFromDB(today)
lst = inv_loader.get_loaded_list_of_investors_record_from_db()
mesurement_criteria = {
    'marketcap_ponderation': 0,
    'contribution_ponderation': 100,
    'contribution_flatness': 1.2
}

rankerA = RankerA(lst, mesurement_criteria)
ranked_list1 = rankerA.get_ranked_list()
print(ranked_list1)

# total_perc = 0
# for perc in rankerA.get_ranked_list():
#     total_perc += perc[1]

# print(total_perc)