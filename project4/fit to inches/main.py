inches:int = 12
def main():
    try:
      while True:
               feet = float(input('enter your feet number'))
               inches_answer:float = feet * inches
               print("That is", inches_answer, "inches!")
               
    except (KeyboardInterrupt, EOFError):
      print("\nProgram exited. Thanks for using the converter! 👋")

if __name__ == '__main__':
    main()