import os
def main():
    account = open('/Users/kishorebattula/Desktop/Kishore/accounts.txt','r')
    temp_file = open('/Users/kishorebattula/Desktop/Kishore/temp_file.txt','w')

    with account, temp_file:
        for record in account:
            name,account,salary = record.split()
            if name != 'Nandeesh' :
                temp_file.write(record)
            else:
                new_record = ' '.join(['YukthaSree',account,salary])
                temp_file.write(new_record+'\n')
        os.remove('/Users/kishorebattula/Desktop/Kishore/accounts.txt')
        os.rename('/Users/kishorebattula/Desktop/Kishore/temp_file.txt','/Users/kishorebattula/Desktop/Kishore/accounts.txt')

main()
