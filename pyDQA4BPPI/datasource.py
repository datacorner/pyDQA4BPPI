import pandas as pd

class DataSource:
    def __init__(self, _filename, _pfi, _sn, _t):
        self.m_filename = _filename
        self.m_dataset = pd.DataFrame()
        self.m_keyname_PFI = _pfi
        self.m_keyname_SN = _sn
        self.m_keyname_T = _t
    
    def isOpened(self):
        return not self.m_dataset.empty
    
    def open(self):
        try:
            self.m_dataset = pd.read_csv(self.m_filename)
            return True
        except Exception as e:
            return False
        
    # Check if the 3 fields really exists in the dataset
    def checkColumns(self):
        pfi_ok = False
        sn_ok = False
        t_ok = False
        pot_attr = []
        msg = ""
        try:
            for col in self.m_dataset.columns:
                if (col == self.m_keyname_PFI):
                    pfi_ok = True
                if (col == self.m_keyname_SN):
                    sn_ok = True
                if (col == self.m_keyname_T):
                    t_ok = True
                else:
                    pot_attr.append(col)
            if (not pfi_ok):
                msg = msg + "> ERROR: Timeline ID column has not been found.\n"
            if (not sn_ok):
                msg = msg + "> ERROR: Event ID column has not been found.\n"
            if (not t_ok):
                msg = msg + "> ERROR: Timestamp column has not been found."
            if (pfi_ok and sn_ok and t_ok):
                msg = msg + "INFO> Potential attributes: " + str(pot_attr)
            return (pfi_ok and sn_ok and t_ok), msg
        except Exception as e:
            msg = "ERROR> Error while opening the file, error ->" + e
            return False, msg
    
    def head(self, _first = 10):
        if (self.isOpened):
            return self.m_dataset.head(_first)
        else:
            return -1
        
    def colsCount(self):
        if (self.isOpened):
            return self.m_dataset.shape[1]
        else:
            return -1
        
    def rowsCount(self):
        if (self.isOpened):
            return self.m_dataset.shape[0]
        else:
            return -1

    def colFreqDistrib(self, _col):
        if (self.isOpened):
            counts = self.m_dataset[_col].value_counts()[:10]
            colName = counts.index
            colFreq = counts
            res = pd.DataFrame(columns=["Column", "Frequency"])
            res["Column"] = colName
            res["Frequency"] = colFreq.values
            return res
        else:
            return None
        
    def countDiffValues(self, _colName):
        return len(self.m_dataset[_colName].value_counts())
    
    