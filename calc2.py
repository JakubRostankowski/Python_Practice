loop = 1
while loop == 1:
	n1 = int(raw_input("Show numbers from: "))
	n2 = int(raw_input("to: "))
	y = int(raw_input("divisible by: "))
	for x in range(n1, (n2+1)):
    		if x % y == 0:
        		print x,
        q = raw_input("\nDo you want to check for new numbers (yes/no)?")
        if len(q) <=2:
          	break