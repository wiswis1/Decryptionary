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
    def getDiff(self):
        return self.diff
    def getGuessNum(self):
        return self.guess
    # get the list of ciphered words
    def getCipheredList(self):
        cipheredList = self.synonyms
        cipheredList.append(self.word)
        return cipheredList
    def getCipher(self):
        return self.cipherList

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
        listCipher = {}
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
                listDef[i] = cipheredWord
                listCipher.add(cipheredWord)
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
                    listDef[i] = cipheredWord
            # re add the periods and commas yeah
            if hasPeriod:
                listDef[i] += "."
            if hasComma:
                listDef[i] += ","

        # unsplit listDef yeah        
        output = " ".join(listDef)
        # print(output)
        return (output, listCipher)
        

    def __init__(self, word, level):
        self.word = word.lower()
        self.synonyms = self.setSynonyms(word)
        self.definition = self.setDefinition(word)
        self.shift = random.randint(1, 13)
        self.cipherDefinition = self.setCipherDefinition(self.definition, self.shift)[0]
        self.cipherList = self.setCipherDefinition(self.definition, self.shift)[1]
        self.guess = 0
        self.diff = self.setDiff(level)
        

