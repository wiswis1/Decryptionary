# Import PyMultiDictionary
from PyMultiDictionary import MultiDictionary
import time

# set dictionary language and such
dictionary = MultiDictionary()
dictionary.set_words_lang('en')
definition = dictionary.meaning('en',"hello")
line = definition[1]

lineSplit = line.split()
print(''.join(lineSplit))


synonyms = dictionary.synonym('en', 'hello') 
print(synonyms)


for i in range(len(lineSplit)): 
    if lineSplit[i].lower() == "hello" :
        lineSplit[i] = "BLANK"
    # check synonyms
    for j in range(len(synonyms)):
        if lineSplit[i] == synonyms[j]:
            lineSplit[i] = "BLANK"
        
print(''.join(lineSplit))


def timer():
    my_time = 60
    for x in range(my_time, 0,-1):
        seconds = x % 60
        minutes = int(x / 60)  
        print(f"{minutes:02}:{seconds:02}")
        time.sleep(1)
    

def points():
    pass

timer()


