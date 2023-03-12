
# Levels:
#    1 -> DEBUG
#    2 -> INFO
#    3 -> ERROR

class Report:
    def __init__(self, _debug = True, _info = True, _error = True):
        self.m_info = _info
        self.m_debug = _debug
        self.m_error = _error
        
    def info(self, *message):
        if (self.m_info):
            final_message =""
            for msg in message:
                final_message += msg
            if (self.m_info):
                print("INFO>" + final_message)

    def error(self, *message):
        if (self.m_error):
            final_message =""
            for msg in message:
                final_message += msg
            if (self.m_info):
                print("ERROR>" + final_message)
                
    def debug(self, *message):
        if (self.m_debug):
            final_message =""
            for msg in message:
                final_message += msg
            if (self.m_info):
                print("DEBUG>" + final_message)