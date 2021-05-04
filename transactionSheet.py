import gspread 
import pandas as pd
from transaction import Transaction
from oauth2client.service_account import ServiceAccountCredentials

class TransactionSheet:
    def __init__(self):
      scope = ['https://www.googleapis.com/auth/drive']
      creds = ServiceAccountCredentials.from_json_keyfile_name('pymoney_client.json', scope)
      client = gspread.authorize(creds)
      sheet = client.open("pymoney")
      
      self.sheet = sheet.get_worksheet(0)
      
    def getAll(self) -> list:
        return self.sheet.get_all_records()
    def getTotal(self):
        df = pd.DataFrame(self.sheet.get_all_records())
        _total = df['value'].sum()
        _total_types = df.groupby(['type']).sum()
        return { 'total': str(_total), 'types': _total_types.to_json() }
    def add(self,transaction):
        value = '-' + str(transaction.value) if transaction.type == 'S' else transaction.value
        self.sheet.append_row([transaction.title, value, transaction.type, transaction.category])