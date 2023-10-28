
def Fruite(listofFruit, prceTag):
    distFruit = len(set(listofFruit))
    noFruite = len(listofFruit)

    prceTag.sort()

    minn = sum(prceTag[:distFruit])+(noFruite-distFruit)*prceTag[0]
    maxx = sum(prceTag[len(prceTag)-distFruit:]) + \
        (noFruite-distFruit)*prceTag[-1]

    print(minn, maxx)


m = list(map(int, input().split()))

t = list(map(int, input().split()))

listOfFruit = []

for i in range(m[1]):
    fruit = input()
    listOfFruit.append(fruit)

Fruite(listOfFruit, t)
