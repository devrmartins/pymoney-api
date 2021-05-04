class Transaction:
    def __init__(self,_title='',_value=0,_type='',_category=''):
        self.title = _title
        self.value = float(_value)
        self.type = _type
        self.category = _category