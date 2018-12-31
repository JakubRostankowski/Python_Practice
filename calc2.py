while True:
    n1 = int(input("Show numbers from: "))
    n2 = int(input("to: "))
    y = int(input("divisible by: "))
    for x in range(n1, (n2+1)):
        if x % y == 0:
            print (x),
    q = input("\nDo you want to check for new numbers (yes/no)?")
    if len(q) <=2:
        break

