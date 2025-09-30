'''
Write a Python program to print the indexes of numbers in a given list that are below a given threshold.
'''
# n = int(input("How many numbers? "))
# b = []
# for x in range(n):
#     num = int(input("Enter a number : "))
#     b.append(num)

n = input("Enter the numbers with space ").split()
x=int(input("Enter the threshold : "))
for i in n:
    if int(i) < x:  
        print(n.index(i))

print("end")
