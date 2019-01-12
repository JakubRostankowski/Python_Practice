def collatz(number):
    if number % 2 == 0:
        print(number //2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number +1)
        return 3 * number +1

number = int(input('Podaj liczbę: '))
while collatz(number) !=1:
    number = collatz(number)
