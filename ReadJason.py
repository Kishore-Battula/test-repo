import json

with open('/Users/kishorebattula/Desktop/Kishore/accounts_jason.txt', mode='r') as accounts:
    print(json.dumps(json.load(accounts),indent=4))


