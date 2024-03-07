word=input("adjalszot")
word=word.split()

word.sort()

def lists():
    newList=[]

    for i in word:
        word.append((i,len(i)))

    print(word)
    print(newList)

lists()
