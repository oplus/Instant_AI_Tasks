###Question-1
numbers = []
for i in range(1500, 2701):
	if i % 7 == 0 and i % 5 == 0:
		numbers.append(i)



###Question-2
def c_to_f(c):
	f = ( c * 1.8 ) + 32 
	return round(f, 2)

def f_to_c(f):
	c = (f - 32)  / 1.8  
	return round(c, 2)



###Question-3
for i in range (0, 5):
    for j in range(0, i + 1):
        print("* ", end='')
    print("\r")
for i in range (5, 0, -1):
    for j in range(0, i -1):
        print("* ", end='')
    print("\r")



###Question-4
word = input("Enter the word you want to reverse: ")
print(''.join(list(word)[::-1]))



###Question-5
num_list = []
for i in range(3):
	num = input(F"Enter number {i+1}: ")
	num_list.append(num)
print(max(num_list))



###Question-6
def summition(numbers):   #list is passed to the function
	summ = 0 
	for n in numbers:
		summ += n
		return summ



###Question-7
for i in range(7):
	if i == 0 or i == 6:
		continue
	print(i)



###Question-8
def feb(number):
	return 1 if (number == 0 or number == 1) else number * feb(number -1)

print(feb(10))



###Question-9
def uni(lst):
	return list(set(lst))



###Question-10
add_15 = lambda a: a + 15
multiply = lambda a, b: a * b

