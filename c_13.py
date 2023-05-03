# If I need the self inside my method, this is an instace method

class Connection:
    def __init__(self, host='localhost') -> None:
        self.host = host
        self.user = None
        self.password = None


    def set_user(self, user):
        ''''
            This function is a setter.
        '''
        self.user = user


    def set_password(self, password):
        self.password = password
    
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.password = password
        connection.user = user

        return connection
    

    @staticmethod
    def do_sum(x, y):
        return x + y


c1 = Connection()
c1.set_user("Gus")
c1.set_password("123445")

print(c1.user)
print(c1.password)

c2 = Connection.create_with_auth("Joao", 12324)
print(vars(c2))

print(Connection.do_sum(2, 2))