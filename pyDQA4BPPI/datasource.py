import pandas as pd

class DataSource:
    def __init__(self, _filename):
        self.filename = _filename
        self.dataset = pd.DataFrame()
        
    def open(self):
        try:
            self.dataset = pd.read_csv(self.filename)
            return True
        except Exception as e:
            return False