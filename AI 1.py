"""def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("Select Operation.")
print("1.Add")
print("2.Subtract")
print("3.Divide")
choice=input("Enter the choice(1/2/3/4):")
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
if choice=='1':
    print(num1,"+",num2,"=",add(num1.num2))
elif choice=='2':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=='3':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='4':
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("Invalid input")"""
"""Matrix1=[[1,2,3],
         [4,5,6],
         [7,8,9]]
Matrix2=[[10,11,12],
         [13,14,15],
         [16,17,18]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(Matrix1)):
    for j in range(len(Matrix1[0])):
        result[i][j]=Matrix1[i][j]+Matrix2[i][j]
for row in result:
            print (row)"""
"""matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rows = len(matrix)
cols = len(matrix[0])

transpose_matrix = [[0 for x in range(rows)] for y in range(cols)]

for i in range(rows):
    for j in range(cols):
        transpose_matrix[j][i] = matrix[i][j]

print("Original Matrix:")
for row in matrix:
    print(row)

print("Transposed Matrix:")
for row in transpose_matrix:
    print(row)"""
"""sentence=input("Enter a sentence:")
words=sorted(sentence.split())
sorted_sentence=" ".join(words)
print("Sorted sentence:",sorted_sentence)"""
"""nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested List:", nested_list)

my_list = [1, 2, 3, 4, 5]
print("Length of List:", len(my_list))

list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("Concatenated List:", concatenated_list)

my_list = [1, 2, 3, 4, 5]

if 3 in my_list:
    print("3 is in the list")
else:
    print("3 is not in the list")"""
my_list = []

my_list.append(1)
print("List after adding an item using append method:", my_list)

my_list.append(2)
print("List after appending an item using append method:", my_list)

my_list.extend([3, 4, 5])
print("List after extending using extend method:", my_list)

my_list.remove(3)
print("List after removing an item using remove method:", my_list)

