from autocorrect import Speller

def correction(x): 
    spell = Speller(lang='en')
    cor=spell(x)
    print(cor)
    return cor


correction("locaton")