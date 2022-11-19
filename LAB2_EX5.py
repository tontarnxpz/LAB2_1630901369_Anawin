array = [['Number ID','Name','Count','Status'],[],[],[],[]]

print("Length of array =",len(array))
print("\n")
array[1].append('1')
array[2].append('Rubber')
array[3].append(0)
array[4].append('Out of stock')

array[1].append('2')
array[2].append('Ruler')
array[3].append(5)
array[4].append('In stock')

array[1].append('3')
array[2].append('Pencil')
array[3].append(1)
array[4].append('In stock')

array[1].append('4')
array[2].append('Pen')
array[3].append(10)
array[4].append('In stock')

array[1].append('5')
array[2].append('Colour pencil')
array[3].append(5)
array[4].append('In stock')

array[1].append('6')
array[2].append('A4 Paper')
array[3].append(0)
array[4].append('Out of stock')


for i in range(0,len(array[1])):
    print('|',array[0][0],":",array[1][i],'|',array[0][1],":",array[2][i],'|',array[0][2],":",array[3][i],'|',array[0][3],":",array[4][i])
print("\n")
for i in range(0,len(array[1])):
    if array[4][i] == "In stock" :
        print(array[2][i],'= In stock')

print("\n")
for i in range(0,len(array[1])):
    if array[4][i] == "Out of stock" :
        print(array[2][i],'= Out of stock')

array[3][1] = array[3][1]-1
array[3][2] = array[3][2]-1
array[4][2] = "Out of stock"
array[3][3] = array[3][3]-2
array[3][4] = array[3][4]-1
print("\n")

for i in range(0,len(array[1])):
    print('|',array[0][0],":",array[1][i],'|',array[0][1],":",array[2][i],'|',array[0][2],":",array[3][i],'|',array[0][3],":",array[4][i])