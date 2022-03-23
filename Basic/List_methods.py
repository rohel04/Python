# numbers=[1,2,3,5,6]
# numbers.append(9)
# print(numbers)
# numbers.insert(2,4)
# print(numbers.index(3))
# print(numbers.count(1))
# print(numbers.remove(6))
# print(numbers.pop())

# numbers2=numbers.copy();
# print(numbers2)
# print(numbers)

numbers=[1,1,2,2,6,8,9]
for x in numbers:
    if numbers.count(x)>1:
        numbers.remove(x)
print(numbers)
        
#Another method

numbers1=[1,1,2,2,6,8,9]
numbers1_0=[]
for number in numbers1:
    if number not in numbers1_0:
        numbers1_0.append(number)
print(numbers1_0)
    