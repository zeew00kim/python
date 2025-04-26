num = int(input("enter the size of list : "))

fruit = []

for i in range(num) :
    temp = input("enter the value : ") 
    fruit.append(temp)

fruit.append("귤")

print(fruit)