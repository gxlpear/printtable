def multtable(number, limit):
    for i in range(1, limit+1):
        print(i * number)



def powertable(power, limit):
	for n in range(1, limit + 1):
		result =  n **power
		print(result)

if __name__ == "__main__":
    multtable(7, 10)
    powertable(2, 4)


