import os

def main():
    accounts = open('/Users/kishorebattula/Desktop/Kishore/accounts.txt', 'r')
    temp_file = open('/Users/kishorebattula/Desktop/Kishore/temp_file.txt','w')

    with accounts,temp_file:
        for record in accounts:
            account,name,balance = record.split()
            if account != '300':
                temp_file.write(record)
            else:
                new_record = ' '.join([account, 'Williams' , balance])
                temp_file.write(new_record +'\n')
    os.remove('/Users/kishorebattula/Desktop/Kishore/accounts.txt')
    os.rename('/Users/kishorebattula/Desktop/Kishore/temp_file.txt','/Users/kishorebattula/Desktop/Kishore/accounts.txt')

main()
