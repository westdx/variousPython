
def main():
    '''Co-prime: two integers a and b, if the only positive integer that 
divides both of them is 1 '''
    
    print ('coprimeTest()',coprimeTest.__doc__)
    print ('coprime(a,b)', coprime.__doc__)
    print ('\n')

def coprimeTest():
    '''User interface for coprime function.'''
    
    while True: #a while loop for user to check multiple set of coprime
        a_input = ''
        b_input = ''
        print ('Co-Prime Test')
        print('Reminder: Negative interger input will turn to positive.')
        print('Enter 0 to quit.') #an Exit loop reminder
        
        while type(a_input) is not int: #check for int only
            try: #if it is int, exit loop and continue
                a_input = abs(int(input('Please enter your first number:')))
                break
            except: #raise a reminder that it can only accept integer
                print('Please enter an integer only! ie. 1,2,3,4..')
                print('\n')
       
        if a_input == 0: # enter 0 to end the while loop and the function
            break
        
        else: #similar to a_input 
            while type(b_input) is not int: #check for int only
                try:
                    b_input = abs(int(input('Please enter your second number:')))
                    break
                except:
                    print('Please enter an integer only! ie. 1,2,3,4..')
                    print('\n')
            if b_input == 0: #if user want to quit on the second input
                break
            
            print (coprime(a_input,b_input)) #call coprime function
            print('\n')
            
        

def coprime(a,b):
    '''Return True/False if the set of number is or not Co-prime.'''
    highest_factor = ''
    
    while b != 0:
        a,b = b,a%b #Euclidean algorithm, flip the divisor until it reach 0, 
    #(a) will be the last remainder of previous loop and that is the highest factor
    
    highest_factor = a
    print('The highest common factor is',highest_factor) #for math checking
    if highest_factor == 1: #if ==1 meaning they don't share a common factor
        return True
    return False


if __name__ =='__main__':
    print(main.__doc__)
    main()
    coprimeTest()
