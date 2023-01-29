# oop
An oriented object programming with some classes and subclasses really interesting I've created to my wife's business. 

First is the client's class where we have the variables as follows:

class GP2Clients:
    
    def __init__(self, company_name, ceo_first_name, ceo_last_name, budget):
        self.company_name = company_name
        self.ceo_first_name = ceo_first_name
        self.ceo_last_name = ceo_last_name
        self.budget = budget
        
Here below, we create a new class variable where we use the other classes variables to create an email:        
        
        self.email = self.ceo_first_name + "."+ self.ceo_last_name + "@gmail.com" 
        
Now we'll create a new class in order to raise the budget:        

    def RaiseBudget(self, budget):
        self.budget = budget


Now here we are creating a sub class of service packages which inharites the variables from the GP2clients'class:


class ServicePackage(GP2Clients):
    
    def __init__(self, company_name, ceo_first_name, ceo_last_name, budget, serv_pac):
        super().__init__(company_name, ceo_first_name, ceo_last_name, budget)
        self.serv_pac = serv_pac
        
Here we create a new class for this sub class to add a new service to the service packages list that already exists, in case the client decides to add a new service to his package:        

    def AddPackageService (self, serv_pac):
        self.serv_pac += [serv_pac]


Alright, so the OOP is created!

Let's test it with the following:

Here I create a client, who we will call client1:
client1 = GP2Clients("Grace and beauty", "Grace", "Silva", 10000)

Here we raise the budget in order to test the RaiseBudget class:
client1.RaiseBudget(20000)

Now let's print it all and check if it'll work properly:
print(client1.company_name, client1.ceo_first_name, client1.ceo_last_name, client1.email, client1.budget)

Now let's test the sub class and see if it's inhariting the class variables from the GP2Clients'class:
serv_pac1 = ServicePackage("Grace and Beauty", "Grace", "Silva" ,20000, ["Instagram", "Facebook"])

Now let us add a service to the existing list of services:
serv_pac1.AddPackageService("Market Place")

Now let's see if it's working:
print(serv_pac1.company_name, serv_pac1.budget, serv_pac1.serv_pac)

Hope you enjoy it!
