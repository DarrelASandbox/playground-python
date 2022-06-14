from ast import Try

from regex import P

try:
    pass

except:
    pass

else:
    pass

finally:
    pass


def ask():
    
    while True:
        try:
            n = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break
            
        
    print('Thank you, your number squared is: ',n**2)

ask()