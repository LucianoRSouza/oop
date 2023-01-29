class GP2Clients:
    
    def __init__(self, company_name, ceo_first_name, ceo_last_name, budget):
        self.company_name = company_name
        self.ceo_first_name = ceo_first_name
        self.ceo_last_name = ceo_last_name
        self.budget = budget
        self.email = self.ceo_first_name + "."+ self.ceo_last_name + "@gmail.com" 

    def RaiseBudget(self, budget):
        self.budget = budget


class ServicePackage(GP2Clients):
    
    def __init__(self, company_name, ceo_first_name, ceo_last_name, budget, serv_pac):
        super().__init__(company_name, ceo_first_name, ceo_last_name, budget)
        self.serv_pac = serv_pac

    def AddPackageService (self, serv_pac):
        self.serv_pac += [serv_pac]


client = GP2Clients("Grace and beauty", "Grace", "Silva", 10000)

client.RaiseBudget(20000)

print(client.company_name, client.ceo_first_name, client.ceo_last_name, client.email, client.budget)

serv_pac1 = ServicePackage("Grace and Beauty", "Grace", "Silva" ,20000, ["Instagram", "Facebook"])
serv_pac1.AddPackageService("Market Place")

print(serv_pac1.company_name, serv_pac1.budget, serv_pac1.serv_pac)

