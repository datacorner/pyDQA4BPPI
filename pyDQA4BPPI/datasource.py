import pandas as pd
from report import Report

class DataSource:
    def __init__(self, _filename, _pfi, _sn, _t):
        self.m_filename = _filename
        self.m_dataset = pd.DataFrame()
        self.m_keyname_PFI = _pfi
        self.m_keyname_SN = _sn
        self.m_keyname_T = _t
        self.m_report = Report()
    
    def set_Report(self, _report):
        self.m_report = _report
    
    def isOpened(self):
        return not self.m_dataset.empty
    
    def open(self):
        try:
            self.m_dataset = pd.read_csv(self.m_filename)
            return True
        except Exception as e:
            return False
        
    def check_columns(self):
        pfi_ok = False
        sn_ok = False
        t_ok = False
        pot_attr = []
        error_msg = ""
        for col in self.dataset.columns:
            if (col == self.m_keyname_PFI):
                pfi_ok = True
            if (col == self.m_keyname_SN):
                sn_ok = True
            if (col == self.m_keyname_T):
                t_ok = True
            else:
                pot_attr.append(col)
        if (not pfi_ok):
            error_msg = error_msg + "> ERROR: Timeline ID column has not been found.\n"
        if (not sn_ok):
            error_msg = error_msg + "> ERROR: Event ID column has not been found.\n"
        if (not t_ok):
            error_msg = error_msg + "> ERROR: Timestamp column has not been found."
        if (pfi_ok and sn_ok and t_ok):
            print("INFO> Potential attributes: ", pot_attr)
        return (pfi_ok and sn_ok and t_ok), error_msg

