array = [['Number ID','Name','Count','Status'],[],[],[],[]]

print("Length of array =",len(array))
array[1].append('1')
array[2].append('Rubber')
array[3].append(0)
array[4].append('Out of stock')

array[1].append('2')
array[2].append('Rule')
array[3].append(5)
array[4].append('In stock')

array[1].append('3')
array[2].append('Pencil')
array[3].append(1)
array[4].append('In stock')

for i in range(0,len(array[1])):
    print('|',array[0][0],":",array[1][i],'|',array[0][1],":",array[2][i],'|',array[0][2],":",array[3][i],'|',array[0][3],":",array[4][i])