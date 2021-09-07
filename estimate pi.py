import math


i = 3
piEstimate = 1.0
plus = False
counter = 1


while counter <= 100000000:
	if plus == True:
		piEstimate += (1/i)
		plus = False
	else:
		piEstimate -= (1/i)
		plus = True
	i += 2
	print(str(counter) + ".: ",end="")
	print(piEstimate*4)
	counter += 1


print("The Estimate of pi after" + str(counter) + "iterations is ", end="")
print(piEstimate * 4)

end = input()