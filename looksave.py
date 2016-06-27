# Look and say method
# Created/tested with Python 2.7.11

def look(seed, num):
	n = seed
	print "Seed is", seed, "and we will run this", num, "times."
	print n # printing the input that we start with
	for look in range(num):
		#print "Look and see #", look + 1
		s = str(n) # convert the seed to string
		#print s
		#l = len(s)
		a = list(s) # we get the length of the converted string
		#print a
		count = 0 # initialize counter
		#newstr = ""
		next = "" # this is what we will use to keep track of the new string
		for i in range(len(a)):
			if i == 0:
				# For the first digit we increment the counter and move to check the next
				count = count + 1
				continue
			if a[i] == a[i-1]:
				# if current digit is same as previous, we increment the counter
				count = count + 1
			else:
				# if the new digit is different from previous, we append the count and digit
				# and initialize the counter to 1 for the current digit
				next += str(count) + str(a[i-1])
				count = 1 
		next += str(count) + str(a[len(a)-1]) # This helps count the first time when there is only one digit
		print next
		n = int(next) # this is our new n that we check in the next iteration of the loop
	#return n

look(1,10)
look(5, 12)
look(123,5)