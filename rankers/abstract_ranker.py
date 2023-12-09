from abc import ABC, abstractclassmethod

class AbstractRanker(ABC):
    def __init__(self, list_of_investors_record, dict_mesurement_criteria):
        self.ranked_list = []
        self.list_of_investors_record = list_of_investors_record
        self.dict_mesurement_cirteria = dict_mesurement_criteria
    
    @abstractclassmethod
    def get_ranked_list(self):
        raise NotImplementedError("get_ranked_list is an abstract method; Needs to be implemented.")

