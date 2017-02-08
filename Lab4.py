from bintreeFile import Bintree
from linkedQFile import *
import sys

def BintreeMaker(ordlista):
    svenska = Bintree()
    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip() 
            if ordet not in svenska:
                ordlista.append(ordet)
                svenska.put(ordet)
    return ordlista,svenska

def main():
    gamla = Bintree()
    q = LinkedQ()
    ordlista = []
    ordlista, svenska = BintreeMaker(ordlista)
    startordInput = input('Choose a start word')    
    slutordInput = input('Choose an end word')
    if startordInput in svenska and slutordInput in svenska:
        gamla.put(startordInput)
        q.enqueue(startordInput)
        while not q.isEmpty():
            node = q.dequeue()
            makechildren(node, ordlista, gamla, q)
            if slutordInput in gamla:
                print('Det finns en väg till ' + slutordInput)
                sys.exit()

            elif q.isEmpty():
                print('Det finns ingen väg till ' + slutordInput)
    else:
        print('The word is not in the dictionary')
        main()
        return 


def makechildren(ordet, ordlista, gamla, q):
    startord = bokstavsBytare(ordet)
    for ord in ordlista:
        a = bokstavsBytare(ord)
        for i in a:
            if i in startord and ord not in gamla:
                q.enqueue(ord)
                gamla.put(ord)
    return ordlista, gamla, q

def bokstavsBytare(ord):
    checklista = []
    for i in range(3):
        checklista.append(ord[:i] + '?' + ord[i+1:])
    #print(checklista)
    return checklista

            
main()
