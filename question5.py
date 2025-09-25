master_list = [21,22,23,24,25,26,27,28,29]
present=[]
count = 0
with open("C:\\Users\\Himanshu\\Desktop\\Python\\Assignment_17_september\\present.txt") as f:
    for x in f:
        present.append(int(x.strip()))  # this is for comparison to present vs  master list
        if (int(x.strip())) in master_list:
            print('present', x.strip())
            count+=1

print("total present is:" , count)
# absent
a = []
for x in master_list:
   if x not in present:
       a.append(x)
       print("absent" , x)
       print(a)

with open(r"C:\\Users\\Himanshu\\Desktop\\Python\\Assignment_17_september\\absent.txt", 'w') as f:
    for c in a:
       f.write(str(c) + '\n')       

'''
list comprehension
absent = [str(x) for x in master_list if x not in present]
print(absent)
'''



