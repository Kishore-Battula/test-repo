import json

def main():
    accounts_dict = {'accounts':[
        {'account':100,'name':'Kishore','balance':24.98},
        {'account':200,'name':'Kalyan','balance':345.67}]}

    with open('/Users/kishorebattula/Desktop/Kishore/accounts.txt',mode='w') as accounts:
      json.dump(accounts_dict,accounts)

main()




