

class Report:
    def __init__(self):
        self.m_output = False
        self.m_fileread = False
    def set_output(self):
        self.m_output = True
    def set_fileread(self, status):
        self.m_fileread = status
        
    def log(self, *message):
        if (self.m_output):
            final_message =""
            for msg in message:
                final_message += msg
            print(final_message)
    