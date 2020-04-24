def main():
    '''The function were designed in a top down structure and consisted of 5 level.
the first level is the intro and geeting the user. It is also the core of the function that execute all the other functions.
Second level is the read function that open and return the file. 
Third level is the cleaning and sorting stage
Forth level is the checking level that ensure the list is within a set range
The last level is the stem and leaf function. It is the core of the entire function.'''
    print ('\n')
    print ('stemLeaf():',stemLeaf.__doc__)
    print ('stemleafSample():', stemleafSample.__doc__)
    print ('openStem():',openStem.__doc__)
    print ('switchMode():',switchMode.__doc__)
    print ('readStem(file):',readStem.__doc__)
    print ('cleanStem(file):',cleanStem.__doc__)
    print ('sortStem(file):',sortStem.__doc__)
    print ('rangeStem(lst):',rangeStem.__doc__)
    print ('drawStem(lst):',drawStem.__doc__)
    print ('stemPlot(lst):',stemPlot.__doc__)
    print ('\n')
    print ('Please make sure to modify readStem for the file path if needed.')
    print ('\n')
    

def stemLeaf():
    '''Main operation function for stem and leaf.'''
    
    print ('Janky Stem and Leaf Plotter')
    print ('1: Display a sample stem and leaf plot')
    print ('2: Open and read file to make stem and leaf plot')
    choice = switchMode()
    
    #steamleaf sample
    if choice is True:
        stemleafSample()
    
    #open user file
    elif choice is False:
        openStem()
        
    elif choice in ['exit','Exit']:
        return
    

def stemleafSample():
    '''Accept user input to draw a stem and leaf graph from StemAndLeaf sample files'''
    
    while True:
        print ('If you wish to exit, please type "exit" in respond.')
        print ('If you wish to change mode, please type "change" in respond.')
        print ('\n')
        print ('There are total of 3 stem and leaf plot avilable for display.')
        print ('The input, will read the appropriate datafile and display a stem and leaf plot.')
        num = input('Please enter either 1, 2 or 3: ')
        
        if num in ['1','2','3']:
            #call helper function
            file = readStem('StemAndLeaf'+ num +'.txt')
            file = cleanStem(file) #call cleanStem function
            file = sortStem(file) #call sortStem function
            file = rangeStem(file) #call rangeStem function
            
            #if the file is out of range, stop the loop
            if file == True:
                return
            else:
                file = drawStem(file) #call drawStem function
        elif num in ['exit','Exit']:
            return
        elif num in ['change','Change']:
            stemLeaf()
            return
        else:
            print('the input is not valid.')

def openStem():
    '''Accept user file input to draw a stem and leaf graph'''
    
    while True:
        print ('Please enter the file name for the stem and leaf function')
        print ('If you wish to exit, please type "exit" in respond.')
        print ('If you wish to change mode, please type "change" in respond.')
        print ('\n')
        
        file = input('File name: ')
        
        if file in ['exit','Exit']:
            return
        elif file in ['change','Change']:
            stemLeaf()
            return
        else:
            file = readStem(file) #call readStem function
            file = cleanStem(file) #call cleanStem function
            file = sortStem(file) #call sortStem function
            file = rangeStem(file) #call rangeStem function
            if file == True:
                print ('\n')
                openStem()
                return
            else:
                file = drawStem(file) #call drawStem function
            

def switchMode():
    '''Return True/False to switch mode, or exit the function'''
    
    while True:
        choice = input('Please enter either 1 or 2: ')
        if choice in ['1']:
            return True
        elif choice in ['2']:
            return False
        elif choice in ['exit','Exit']:
            return choice
        #error message
        else:
            print ('Please enter 1 or 2 to continue. If you wish to exit, type "exit".')

def readStem(file):
    '''Open and return file '''
    
    #uncomment path and file if needed for file's path
    #path = "path/to/file/on/your/local/machine/"
    #file = path + file
    fileOpen = open(file).read()
    return fileOpen


def cleanStem(file):
    '''Return the argument with delimiter removed '''
    delimiter = ["'",'"','~','`','!','@','#','$','%','^','&','*','(',')',
                 '-','=','_','+',',','<','>','/','?',':',';','[',']','{',
                 '}','|','.','\n']
    
    #iterate the file and replace delimiter with space
    for i in file:
        if i in delimiter:
            file = file.replace(i,' ')
 
    return file


def sortStem(file):
    '''Return a list in integer and sorted'''
    sortFile = []
    #split the file and append the integer into a list
    for i in file.split():
        sortFile.append(int(i))
            
    #sort the list
    sortFile = sorted(sortFile)
    return sortFile


def rangeStem(lst):
    """Return the list if the list's difference is within an acceptable range"""
    counter = 0
    rangeLst = []
    #find the difference of two number in the list
    for i in range(len(lst)-1):
        rangeLst.append(lst[i+1] - lst[i])
    #to expand the acceptance range for plotting. Edit the number in the range
    for c in rangeLst:
        #Ensure that each number difference does not exceed 250
        if c in range(250):
            counter += 1
    #counter to make sure all number is within range
    if counter == len(lst)-1:
        return lst
    
    #return true to stop the next step
    else:
        print ('The File is out of range.')
        print ("Please make sure the file's data difference does not exceed 250.")
        #for checking to make sure it does work
        #print ('Only',counter,'/',len(lst)-1,'is in range.')
        return True


def drawStem(lst):
    '''Print result of the stem and leaf'''
    stem = stemPlot(lst) #call the stemPlot function
    smallest = min(stem.keys()) #plotting the smallest number
    largest = max(stem.keys()) #plotting the largest number
    spacing = len(str(largest)) #to make sure the spacing for higher number
 
    for i in range(smallest,largest+1): #+1 to include the highest stem
        stem[i].sort() #sort the value
        #join the stem (key) and leaf (value) from the dictionary
        print (str(i).ljust(spacing),'|',' '.join(map(str, stem[i])))
        

import collections
def stemPlot(lst):
    '''Return a dictionary of a list. key = first digit(s), value = last digit'''
    #collections required for .append function to work for dictionary
    stem = collections.defaultdict(list)
    
    for i in lst:
        #dictionary: key = stem, leaf = value. ie. 24 = 2 : 4, 123 = 12 : 3
        stem[i//10].append(i%10)
        # //  division for whole number key
        # % division for the remainder
    return stem

if __name__ =='__main__':
    print(main.__doc__)
    main()
    stemLeaf()