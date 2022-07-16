#while True:
# print("Running Infinite Loop")

a=1
while True:
    a += 1
    if(a == 5):
        print(f"Loop broken value a: {a}")
        break

    print("loop finished")

print("Loop finished2")


i = 1
while i<=3:
    print(f"\ni's value: {i}\n")
    j=0
    while j<5:
        print(f"value of j: {j}")
        j+=1
    print("--------------------------")
    i +=1


for i in range(0,5): starts from 0 to 5 thanks to #range 5 is not included
        print(i)

my list = ["Abdul","Samet","Lightning"] #we can print the list like this
for i in my list:
    print(i)

#search for elements inside lists nested for
mylist1 = ["Ahmet","Mehmet","Yilmaz"]
mylist2 = ["Ayşe","Fatma","Elif"]
mylist3 = ["Abdul","Samet","Lightning"]
my lists = [mylist1,mylist2,mylist3]

for i in range(0,3):
    for j in my lists[i]:
        if j == "Samet":
            print(f"{i+1} There is Samet in the list")

for i in range(0.6):
    if i ==2:
        continue #we skipped
    print(i)