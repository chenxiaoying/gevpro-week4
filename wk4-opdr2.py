#Opdracht2 week4.py

import json
from collections import namedtuple

def main():
    # Open het bestand blood-die.json
    infile = json.load(open('blood-die.json','r'))
    lis =[]
    
    # definieer een namedtuple
    lijst = namedtuple('lijst', 'taal, classificaties, bloed, sterven')
    
    for i in infile:
        # element in lijst wordt named tuple
        li = lijst(*i)
        
        # als concept voor bloed gelijk is aan concept voor sterven, dan kopieer in nieuwe lijst
        l = [i for i in li for b in li.bloed.split() for a in li.sterven.split() if a == b]
        if l != []:
            lis.append(l)
    print(lis)
            
if __name__ == '__main__':
    main()
