import pandas

def main():
    with open('/Users/kishorebattula/Desktop/Kishore/accounts.txt', mode='r') as accounts:
        print(json.dumps(json.load(accounts),indent=4))
main()