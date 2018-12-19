#define the gen_primes function here
 

def main():
    number = 2
    while True:
        for i in range(2, number):
            if (number % i) == 0:
                break
            else:
                yield number
        number += 1
    
if __name__== "__main__":
    gen = main()
    print(next(gen))
    print(next(gen))
