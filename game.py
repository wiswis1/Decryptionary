# Import PyMultiDictionary
from PyMultiDictionary import MultiDictionary
import random
import threading
import time

# main game class !
class game:

    global dictionary
    dictionary = MultiDictionary()
    dictionary.set_words_lang('en')

   
# get the synonyms of a word
    def getSynonyms(self, word): 
        synonyms = dictionary.synonym('en', word) 
        return synonyms
        
        
    def getCipherDefinition(self, definition):
        definition = definition.replace(".|\\,", " ")
        print(definition)
        listDef = definition.split()
        shift = random.randint(1, 13)
        alpha = "abcdefghijklmnopqrstuvwxyz"

        for i in range(len(listDef)) :
            if listDef[i].lower() == self.word.lower() :
                cipheredWord = ""
                # for all letters in listDef[i]
                for k in range(len(listDef[i])):
                   # for all letters in the alphabet
                   for l in range(len(alpha)):
                       # if the current letter matches this letter of the alphabet   
                        if (alpha[l] == listDef[i][k]):
                           # shift the letter by the predefined shift 
                           cipheredWord += alpha[l - shift]
                print(listDef[i])
                listDef[i] = cipheredWord
                print(listDef[i])
            # check synonyms
            for j in range(len(self.synonyms)) :
                if listDef[i].lower == self.synonyms[j].lower():
                    cipheredWord = ""
                # for all letters in listDef[i]
                for k in range(len(listDef[i])):
                   # for all letters in the alphabet
                   for l in range(len(alpha)):
                       # if the current letter matches this letter of the alphabet   
                        if (alpha[l].lower() == listDef[i][k].lower()):
                           # shift the letter by the predefined shift 
                           cipheredWord += alpha[l - shift]
                print(listDef[i])
                listDef[i] = cipheredWord
                print(listDef[i])

        # unsplit listDef yeah        
        output = " ".join(listDef)
        print(output)
        return output
        
        
    def getDefinition(self, word):
        definition = dictionary.meaning('en', word)
        definition = definition[1]
        print(definition)
        return definition


    def __init__(self,word):
        self.word = word
        self.synonyms = self.getSynonyms(word)
        self.definition = self.getDefinition(word)
        self.cipherDefinition = self.getCipherDefinition(self.definition)

    def startGame(self):
        guesses = 10
        print("Welcome to Decryptionary!")
        while (guess < 10 ):
            ans = str(input("Enter your guess: "))
            if (self.word.lower() == ans.lower()):
                    flag = true
                    break
                    guess -= 1
            else:
                flag = false
                print("Wrong! Try again")
                print()
                guess -= 1


    