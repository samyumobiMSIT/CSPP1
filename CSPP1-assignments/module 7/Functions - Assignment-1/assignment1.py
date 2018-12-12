'''Functions | Assignment-1 - Paying Debt off in a Year

program to calculate the credit card balance after one year'''



def paying_debt_off_inayear(balance_unpaid, annual_interest_rate, monthly_payment_rate):
    '''to calculate remaining balance'''
    balance_copy = balance_unpaid

    iterator_i = 1
    while iterator_i <= 12:
        montly_interest_rate = annual_interest_rate / 12.0
        minimum_monthly_payment = monthly_payment_rate*balance_copy
        monthly_unpaid_balance = balance_copy - minimum_monthly_payment
        balance_copy = monthly_unpaid_balance + (montly_interest_rate * monthly_unpaid_balance)
        iterator_i += 1
    return "Remaining balance: "+str(round(balance_copy, 2))
def main():
    '''main function'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(paying_debt_off_inayear(data[0], data[1], data[2]))

if __name__ == "__main__":
    main()

