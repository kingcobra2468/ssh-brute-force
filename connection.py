import threading
import paramiko

class connection:
    __passfound = False
  
    def __init__(self, address, username):
        self.address = address
        self.username = username
    
    @staticmethod
    def passFound(self):
        return True if self.__passfound == True else False

    def attemptConnection(self, password):
        self.password = password
        try:
            attempt = paramiko.SSHClient()
            attempt.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            attempt.connect(
                self.address, 
                port = 22,
                username = self.username, 
                password = self.password, 
                timeout = 0.2, 
                banner_timeout = 0, 
                auth_timeout = 0)
            
        except:
            print("Failed")
            

x=connection('10.0.1.32', 'leo', 'accss');
x.attemptConnection()