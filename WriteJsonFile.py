import json

accounts_dict = {'accounts':
                 [
                     {
                         'account' : 100,'name':'Jones','balance' :24.98
                     },
                     {
                       'account' : 200,'name':'Doe','balance':345.67
                     }
                ]
                }

with open('/Users/kishorebattula/Desktop/Kishore/accounts_jason.txt',mode='w') as accounts:
    json.dump(accounts_dict, accounts)

print("data succesfully dumped in to the Json file")
