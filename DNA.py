import sys

def checklt(input:str):
    valid_letters = ['A', 'C', 'G', 'T']
    for letter in input:
        if letter not in valid_letters:
            print(input + " Not Ok") 
            quit()
    print(input + " Ok")
    

if __name__ == "__main__":
    checklt(sys.argv[1])
