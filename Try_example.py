def main():
    """ Simple exception handling example."""

    while True:
        # attempt to convert and divide values

        try:
            number1 = int(input('Enter numerator:  '))
            number2 = int(input('Enter Denominator: '))
            result = number1 / number2
        except ValueError:
            print('You must enter two integeres\n')
        except ZeroDivisionError:
            print('Attempted to divide by zero.\n')
        else:
            print(f'{number1:.3f}/{number2:.3f} = {result:.3f}')
            break


main()