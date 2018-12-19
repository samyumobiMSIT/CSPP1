def guess(secret_num):
    print("Is your secret number "+ str(secret_num)+" ?") 
    print("Enter 'h' to indicate the guess is too high.")
    print("Enter 'l' to indicate the guess is too low.")
    print("Enter 'c' to indicate I guessed correctly.")
    input_val = input()
    return input_val

def main():
    '''This is main function'''
    print("Please think of a number between 0 and 100!")
    
    input_val = ""

    secret_num = 50
    l = 1
    h = 100

    input_val = guess(secret_num)
    
    while(input_val != 'c'):
        if input_val == 'h':
            l = secret_num
            secret_num = (l+h)//2            
            input_val = guess(secret_num)
        if input_val == 'l':
            h = secret_num
            secret_num = (h+l)//2            
            input_val = guess(secret_num)

    print("Game over! Your secret number is : "+ str(secret_num))    
    

if __name__ == "__main__":
    main()
