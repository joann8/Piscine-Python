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
    
    def transfer(self, origin, dest, amount):
        """
            @origin:  int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return         True if success, False if an error occured
        """
        sender = self.find_account(origin)
        receiver = self.find_account(dest)
        if sender is None or receiver is None:
            print("Sender or Receiver do not exist")
            return False
        if self.check_account(sender) is False or self.check_account(receiver) is False:
            print("Sender or Receiver : account corrupted")
            return False
        print("Sender value : %d | Receiver value : %d | amount = %d" %(sender.value, receiver.value, amount))
        if amount > sender.value:        
            print("Sender : not enought money " )
            return False
        sender.value -= amount
        receiver.value += amount
        print("Sender value : %d | Receiver value : %d" %(sender.value, receiver.value))
        return True

    def find_account(self, account):
        res = 0
        if isinstance(account, str):
            for client in self.account:
                if client.name == account:
                    res = 1
                    break
            if res == 0:
                print("This account NAME (%s) does not exists" %(account))
                return None
        elif isinstance(account, int):
            for client in self.account:
                if client.id == account:
                    res = 1
                    break
            if res == 0:
                print("This account ID (%d) does not exists" %(account))           
                return None
        else:
            print("This account is not and ID or a NAME")
            return None
        return client

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
        """
        #Does the account exist?
        res = 0
        client = self.find_account(account)
        if client is None:
            return False
        print("*********** Account to fix! *********")
        print(dir(client))
        print("*****************************************")
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

        for word in client.__dict__:
            if word[0] == 'b':
                setattr(client, '_' + word[1:], getattr(client, word))
                delattr(client, word)
       
        if len(client.__dict__) % 2 == 0: #== even
            client.other = 'odd'
        
        print("*********** Account Fixed! *********")
        print(dir(client))
        print("*****************************************")

    def check_account(self, client):

        if hasattr(client, 'name') == False:
            return False
        if hasattr(client, 'id') == False:
            return False
        if hasattr(client, 'value') == False:
            return False
               
        zip_list = [word for word in client.__dict__ if word[:3] == "zip"]
        if len(zip_list) == 0:
            return False

        addr_list = [word for word in client.__dict__ if word[:4] == "addr"]
        if len(addr_list) == 0:
            return False

        for word in client.__dict__:
            if word[0] == 'b':
                return False

        if len(client.__dict__) % 2 == 0: #== even
            return False              
