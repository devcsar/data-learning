# def compareTriplets(a, b):
#     # Write your code here
#     total_a = 0
#     total_b = 0
    
    
#     for element_a, element_b in zip(a, b):
#         print(element_a,element_b, sep=" - ")
        
        
#         if element_a > element_b:
#             total_a + 1
#         elif element_a < element_b:
#             total_b + 1
#     print(total_a,total_b)        
#     return [total_a, total_b]
    
        
# ar1 = [1,2,3]
# ar2 = [3,2,1]

# result =  compareTriplets(ar1,ar2)
# print(result)

# matriz = [[0 for _ in range(3)] for _ in range(3)]
# arr = [1,2,3,4,5]
# print(type(len(arr)))


# data = (23,13)
# print( type(data), data[0], sep=" - ")

# data = [[i + 1 +j for j in range(2)] for i in range(2)]

# print(data)
nums = [23, 12, 21, 4, 23 , 56, 12]

target = 100


array_target = []
result = []

for index, element in enumerate(nums):

    array_target.append(element)
    if sum(array_target) <= target:
        result.append(index)

print(result)    