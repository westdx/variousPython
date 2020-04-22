

def main():
    '''The game follow the classic Hangman rule. Player have 6 chances to guess
the word. If the player repeat the same letter or already guessed the letter will
not count as wrong. The game uses the book The Project Gutenberg EBook of The 
Devil's Dictionary, by Ambrose Bierce. It will randomly choose a word from the
book. The word length is between 5 to 12. If you think it is too hard or too 
easy, you can change the range at the end of if __name__=='__main__': playHangman
'''
    


class hangMan():
    '''Class contains all functions to make the hangman word gussing game works'''
    
    def __init__(self,word):
        self.word = word.upper()
        self.secret = self.word
        self.right = '' #Guess Right storage
        self.wrong = '' #Guess Wrong storage
        self.hint = '' #Hint and actual input storage

        #Generate mask '?' for the word
        i = 0 #to stop the while loop
        while i < len(self.word):
            self.hint += '?'
            i += 1

    def getSecret(self):
        '''Return the word of the game'''
        return self.secret
    
    def getHint(self):
        '''Return the length of the word, and word guessed right'''
        return self.hint
  
    def guess(self,letter):
        '''Game's main function to guess the letter '''
        start = 0
        letter = letter.upper()
        char = []
        if self.hint == self.word: #check if the game is won
            pass
        elif letter in self.wrong: #check for repeating letter entry
            pass
        elif len(self.wrong) == 6: #end loop if 6 wrong guesses
            pass
        elif letter not in self.word: #add letter to the Wrong list
            self.wrong += letter
        else: #actual guess loop
            self.right += letter #add letter to the Right list 
            for i in list(self.word):
                if letter == i:
                    char.append(self.word.find(letter,start))
                    start = self.word.find(letter, start)+1
                    templist = list(self.hint)
                    #modify self.hint
                    for l in char:
                        templist[l] = letter
                    self.hint =''.join(templist)

    def getRight(self):
        '''Return a list of guess right letters'''
        #Eliminate duplicates but remain the order
        self.right = ''.join(sorted(set(self.right),key=self.right.index))
        return self.right
    
    def getWrong(self):
        '''Return a list of guess wrong letters'''
        #Eliminate duplicates but remain the order
        self.wrong = ''.join(sorted(set(self.wrong),key=self.wrong.index))
        return self.wrong

    def getState(self):
        '''Return the status of the game, Won/Lost/Playing'''
        if len(self.wrong) == 6:
            return 'lost'
        elif self.hint == self.word:
            return 'won'
        else:
            return 'playing'


def clean(bad,phrase):
    '''Return phrase by replacing unwanted letter(s) with space'''
    for i in phrase:
        if i in bad:
            phrase = phrase.replace(i,' ')
    return phrase


def wordsByLength(phrase):
    '''Return a dictionary by split the input phrase'''
    dic = {}
    for word in phrase.split():
        words = len(word)
        if words in dic:
            dic[words].append(word)
        else:
            dic[words] = [word]
    return dic
 
       
def playHangman(word):
    '''User interactive function of the game.'''
    wg = hangMan(word)
    while True:
        print('What is this word?', wg.getHint())
        print('Right:',wg.getRight())
        print('Wrong:',wg.getWrong())
        wg.guess(input('Guess a letter: '))
        state = wg.getState()
        if state == 'won':
            print('Congratulations, you guessed it! The word is', wg.getSecret()+'.')
            break
        elif state == 'lost':
            print('Sorry, you lose! The secret word is', wg.getSecret()+'.')
            break
        
            

if __name__=='__main__':
    print(main().__doc__)
    main()
    import random
    bad = '="0€%:@)795]”,(#-!3/;81?2&\'$.4*[6â'
    biercetxt = clean(bad,open('Bierce.txt').read())
    wbl = wordsByLength(biercetxt)
    # random word with random length, change the number for different difficulty
    playHangman(random.choice(wbl[random.randrange(5,12)]))

