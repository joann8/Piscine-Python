class Account(object):
	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(kwargs)
		Account.ID_COUNT += 1

	def transfer(self, amount):
		self.value += amount
    
class Bank(object):
    """The bank"""
    
    def __init__(self):
        self.account = []
    
    def add(self, account):
        self.account.append(account)
        print(dir(account))
        self.fix_account(account.name)
        print(dir(account))

    
    def transfer(self, origin, dest, amount):
        """
            @origin:  int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return         True if success, False if an error occured
        """

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
        """
        #Does the account exist?
        res = 0
        if isinstance(account, str):
            for client in self.account:
                if client.name == account:
                    res = 1
                    break
            if res == 0:
                print("This account NAME (%s) does not exists" %(account))
                return False
        elif isinstance(account, int):
            for client in self.account:
                if client.id == account:
                    res = 1
                    break
            if res == 0:
                print("This account ID (%d) does not exists" %(account))           
                return False
        else:
            print("This account is not and ID or a NAME")
            return False

        if hasattr(client, 'name') == False:
            client.name = "default name"
        if hasattr(client, 'id') == False:
            client.id = client.Account.ID_COUNT
            client.Account.ID_COUNT += 1
        if hasattr(client, 'value') == False:
            client.value = 0
               
        zip_list = [word for word in client.__dict__ if word[:3] == "zip"]
        if len(zip_list) == 0:
            client.zip = "default zip"

        addr_list = [word for word in client.__dict__ if word[:4] == "addr"]
        if len(addr_list) == 0:
            client.addr = "default addr"

        
