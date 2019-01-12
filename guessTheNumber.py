import random
secretNumber = random.randint(1,20)
print('Mam na myśli pewną liczbę z zakresu 1 do 20')

for guessesTaken in range (1,7):
    print('Spróbuj odgadnąć liczbę.')
    guess = int(input())

    if guess > secretNumber:
        print('Liczba jest za duża')
    elif guess < secretNumber:
        print('Liczba jest za mała')
    else:
        break

if guess == secretNumber:
    print('Brawo! Zgadłeś liczbę w ciągu ' + str(guessesTaken) + ' prob!')
else:
    print('Nie udało się. Liczba, o której myslałem to' + str(secretNumber) + '.')
    
