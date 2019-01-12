import random
print('Zadaj pytanie:')
input()
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'To pewne'
    elif answerNumber == 2:
        return 'Zdecydowanie tak'
    elif answerNumber == 3:
        return 'Tak'
    elif answerNumber == 4:
        return 'Niejasna odpowiedź'
    elif answerNumber == 5:
        return 'Zapytaj później'
    elif answerNumber == 6:
        return 'Nie'
    elif answerNumber == 7:
        return 'Być może'
    elif answerNumber == 8:
        return 'Nie licz na to'

r = random.randint(1,8)
fortune = getAnswer(r)
print(fortune)
