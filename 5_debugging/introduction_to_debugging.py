#Run-time Error
def checkTemp(temp):
	if temp < 60:
		print("Bring a jacket")
checkTemp(59)

age = input("How old are you?")
#if age > 70: | should you but int() to make it work
if int(age) > 70:
    print ("wow, you're old")


#Logic Error

i=10
while i > 0:
	#i +=1 | The code will never stop
    i -= 1
    print(i)