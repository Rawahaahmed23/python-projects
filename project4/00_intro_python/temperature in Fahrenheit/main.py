def main():
    while True:
       temprature = float(input("enter your tempreature convert into celsius"))
       degrees_celsius = (temprature - 32) * 5.0/9.0

       print(degrees_celsius)

       choice = input('Do you want to convert another temperature? (yes/no):')
       if choice == 'no':
           print('thank you so much for coming')
           break



main()