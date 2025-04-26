import random




def main():


 secret_number = random.randint(1,99)


 print('thinking i am ')
 guess=  int(input("enter yor number"))
 while guess != secret_number:
        if guess < secret_number: 
            print("Your guess is too low")
        else:
            print("Your guess is too high")
            
        print() 
        guess = int(input("Enter a new guess: "))  
        


        print("Congrats! The number was: " + str(guess))

 


    
if __name__ == '__main__':
    main()
    