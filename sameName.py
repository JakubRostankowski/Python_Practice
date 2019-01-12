def spam():
    eggs = 'Zmienna lokalna funckji spam()'
    print(eggs)

def bacon():
    eggs = 'Zmienna lokalna funkcji bacon()'
    print(eggs)
    spam()
    print(eggs)

eggs = 'Zmienna globalna'
bacon()
print(eggs)

#expected output: Zmienna lokalna funkcji bacon(), Zmienna lokalna funkcji spam(), Zmienna lokalna funkcji bacon(), Zmienna globalna.
