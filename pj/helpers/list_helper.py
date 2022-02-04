class ListHelper:
    @classmethod
    def compact(cls, default_list):
        # returns list without empty elements ([], {}, '', None)
        return list(filter(None, default_list))
