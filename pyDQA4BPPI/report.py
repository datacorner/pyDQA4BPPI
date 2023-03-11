
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
        if (self.m_output):
            final_message =""
            for msg in message:
                final_message += msg
            if (self.m_info):
                print(final_message)
    