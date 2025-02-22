from PyMultiDictionary import MultiDictionary, DICT_SYNONYMCOM
import random

# main game class !
class Game:

    global dictionary
    dictionary = MultiDictionary()
    dictionary.set_words_lang('en')

    

    # global return methods


    def getWord(self): 
        # print(f"This is the word: {self.word}\n")
        return self.word
    def getDefinition(self): 
        # print(f"This is the definition: {self.definition}\n")
        return self.definition
    def getSynonyms(self): 
        # print(f"synonyms: {self.synonyms}\n")
        return self.synonyms
    def getCipherDefinition(self): 
        # print(f"cipher definition: {self.cipherDefinition}\n")
        return self.cipherDefinition
    def getGuessNum(self):
        return self.guess
   
    # set the synonyms of a word
    def setSynonyms(self, word): 
        self.synonyms = dictionary.synonym('en', word , DICT_SYNONYMCOM) 
        return self.synonyms
    
 # set the definition of a word       
    def setDefinition(self, word):
        definition = dictionary.meaning('en', word)
        definition = definition[1]
        return definition
    
    def setDiff(self,level):
        if level == 'Easy':
            self.guess = 8
        elif level == "Medium":
            self.guess = 5
        else:
            self.guess = 3
        return level
    
# set the cipher of a definition
    def setCipherDefinition(self, definition, shift):

        definition = str(definition)
        listDef = definition.split()
        alpha = "abcdefghijklmnopqrstuvwxyz"

        for i in range(len(listDef)) :
            # checkin' for periods and commas
            hasPeriod = False
            hasComma = False
            if "." in listDef[i]:
                hasPeriod = True
                listDef[i] = listDef[i].replace(".", "")
            if "," in listDef[i]:
                hasComma = True                
                listDef[i] = listDef[i].replace(",", "")
            if listDef[i].lower() == self.word.lower() :
                cipheredWord = ""
                # for all letters in listDef[i]
                for k in range(len(listDef[i])):
                   # for all letters in the alphabet
                   for l in range(len(alpha)):
                       # if the current letter matches this letter of the alphabet   
                        if (alpha[l].lower() == listDef[i][k].lower()):
                           # shift the letter by the predefined shift 
                           cipheredWord += alpha[l - shift]
                listDef[i] = cipheredWord # TAG AS GREEN !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # check synonyms
            for j in range(len(self.synonyms)) :
                if listDef[i].lower() == self.synonyms[j].lower():
                    cipheredWord = ""
                # for all letters in listDef[i]
                    for k in range(len(listDef[i])):
                        # for all letters in the alphabet
                        for l in range(len(alpha)):
                                # if the current letter matches this letter of the alphabet   
                                if (alpha[l].lower() == listDef[i][k].lower()):
                                    # shift the letter by the predefined shift 
                                        cipheredWord += alpha[l - shift]
                    listDef[i] = cipheredWord # TAG AS GREEN !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # re add the periods and commas yeah
            if hasPeriod:
                listDef[i] += "."
            if hasComma:
                listDef[i] += ","

        print(listDef)
        # unsplit listDef yeah        
        output = " ".join(listDef)
        print(output)
        return output
        

    def __init__(self, word, level):
        self.word = word.lower()
        self.synonyms = self.setSynonyms(word)
        self.definition = self.setDefinition(word)
        self.shift = random.randint(1, 13)
        self.cipherDefinition = self.setCipherDefinition(self.definition, self.shift)
        self.guess = 0
        self.diff = self.setDiff(level)
        

    # def startGame(self):
    #     threading.Thread(target=self.gamePlay, daemon=True).start()
    #     self.gameTimer()
    #     self.done = False

    # def gameTimer(self):
    #     my_time = 60 
    #     for x in range(my_time, 0, -1):
    #         if self.done:
    #             break
    #         seconds = x % 60
    #         minutes = int (x / 60)% 60
    #         print(f"{minutes:02}:{seconds:02}")
    #         time.sleep(1)

    # def gamePlay(self):
    #     playing = True
    #     while(playing):
    #         self.guessNum
    #         print("Welcome to Decryptionary!")
    #         while (guesses < self.guessNum and not self.done):
    #             ans = str(input("Enter your guess: "))
    #             if (self.word.lower() == ans.lower()):
    #                     flag = True
    #                     break
    #             else:
    #                 flag = False
    #                 print("Wrong! Try again")
    #                 print()
    #                 guesses -= 1
    #         if (flag):
    #             print("Congrats for guessing the word")
    #             self.done = True
    #             return flag
    #         else :
    #             print("You lost! Try again!")
    #             return flag

    