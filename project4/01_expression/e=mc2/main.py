C =299792458

def main():
    try:
       while True:
           mass = float(input('type your kilogram mass'))
           energy=  float(mass*(C**2)) 
           print("e = m * C^2...")
           print("m = " + str(mass) + " kg")
           print("C = " + str(C) + " m/s")
           print(str(energy)+"joules of energy")

    except (KeyboardInterrupt, EOFError):
        print("\nProgram exited. Thank you for using the energy calculator! 🚀")


if __name__ ==  "__main__":
      main()