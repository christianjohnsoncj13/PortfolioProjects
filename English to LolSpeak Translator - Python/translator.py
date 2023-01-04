import json

# Importing the english.txt file

text_file = open('english.txt', 'r')

tfr = text_file.readlines()

    
    
def clean(ogtext):
    ogtext = [string.strip() for string in ogtext]
    ogtext = [string.split() for string in ogtext]
    combo_ogtext = [t for string in ogtext for t in string]
    
    return combo_ogtext


# Importing the glossary (ranzlashun.json file)
# This dataset originally comes from the GitHub repository
# at https://github.com/irdumbs/Dumb-Cogs and is covered by an MIT license


with open('tranzlashun.json') as glossary:
    key = json.load(glossary)
trans = list(key)    
       

eng = clean(tfr)
    
    
# Translatint the English text into Lolspeak


for word in eng:
    if word in trans:
        translated_sentence = [key.get(word, word) for word in eng]
        break
    else:
        next
    
translated_sentence = ' '.join(translated_sentence)    
  

# Saving the translated text as the "lolcat.txt" file

with open('lolcat.txt', 'w') as glossary:
    glossary.writelines(translated_sentence)
    glossary.close()