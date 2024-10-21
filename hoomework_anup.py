# Question1

lista=["M","y","name","is","Anil"]
i= 0
sum=" "
while i< len(lista):
  print(lista[i])
  sum=sum+lista[i]
  i=i+1

print(sum)
 

# Question2

lista=[1, 5, 10, 15]
i = 0
sum=0
while i < len(lista):
  sum=sum+lista[i]
  i = i + 1
print(sum)

# Question3

list_a=["My", "is"]
list_b=["Name", "Anil"]

for i in range(0,2):
    print(f"{list_a[i]}  {list_b[i]} ", end="")

# Question4

lista=[1,2,3,4,5,6,7,8,9,10]
odd_numbers = []
even_numbers = []
def odd_even(numbers):
    for number in numbers:
        if number % 2 == 0:
             even_numbers.append(number)
        else:
            odd_numbers.append(number)
    return even_numbers, odd_numbers
even_numbers, odd_numbers = odd_even(lista)

print("Odd numbers: ",  odd_numbers)    
print("Even numbers: ", even_numbers) 


# Question5

x=[1,2,3,4,5,6,7,8,9,10]
squares=[]
def square():

    for i in x: 

        squares.append(i**2)

    return squares  

result=square()
print(result)

# Question6

list_a=["My", 5,7,"Name","is",9,"Anil"]
sum=0 
for item in list_a:
    if type(item)==str:
        print(f"{item} ", end="")
    else:
     
        sum=sum+item
print(end="\n")
print(sum)
        
# Question 7

list_a=[1,5,2,{"data":"Hello"},10]

print(list_a[3]["data"])

# Question8

list_a=["Hello", "Anil"]
print(list_a[0]*2+" "+list_a[1]*2)

# Question9

lista=[{"data1":"Hello"},{"data2":"world"}]

print(lista[0]["data1"]+ " " + lista[1]["data2"])

# Question10

list_a=[1,2,{"data1":[3,4,5]}]

print(list_a[2]["data1"][2])

#Question11

data1={"Hello": "World"}
data2={"Name":  "Anil"}

print(f"{data1['Hello']} {data2['Name']}")


# Question12

data1={1:3,2:4,3:2}

print(data1[2])

# Question13

data1={1:1,2:2,3:3,4:4}

print(data1[3]**2)

      







