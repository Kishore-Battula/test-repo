
def main():
    with open('/Users/kishorebattula/Desktop/Kishore/accounts.txt', mode='r') as accounts:
        print(f'{"Account":<10}{"Name":<10}{"Pay":>10}')
        for record in accounts:
            account, name, pay=record.split()
            print(f'{account:<10}{name:<10} {pay:>10}')

main()

