def main():
    with open('/Users/kishorebattula/Desktop/Kishore/accounts.txt', mode='r') as accounts:
        all_records = accounts.readlines()
        print(all_records)

main()