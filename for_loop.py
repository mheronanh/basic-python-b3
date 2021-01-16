fruits = ['apple', 'banana', 'cherry']

#Printing
print('Non-indexing')
for fruit in fruits:
    print(fruit)

print('\nWith indexing')

for i in range(len(fruits)):
    print(fruits[i])

print('\n')

my_fav_fruits = [fruit for fruit in fruits if fruit == 'apple']
print(my_fav_fruits)
