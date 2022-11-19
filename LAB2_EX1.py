value = [5,7,9,11,13]
len_value = len(value)
result = 0

for i in range(0,len_value):
   result = value[i] + result

print("length of integer array =",len_value)
print("Summation of array =",result)