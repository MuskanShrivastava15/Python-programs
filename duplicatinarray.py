#duplicate in an array
# count=0
#
# def duplicate():
#     for i in range(n):
#         j==i
#         count=+1
#         if(count>=2):
#             print(j)
#         else:
#
#
# a=[1,2,3,6,3,6,1]
# n=len(a)
# duplicate()
# print("the no of functions are",duplicate())
# Python3 code to find duplicates in O(n) time
numRay = [7, 4, 3, 2, 7, 8, 2, 3, 7]
arr_size = len(numRay)
for i in range(arr_size):

	x = numRay[i] % arr_size
	numRay[x] = numRay[x] + arr_size

print("The repeating elements are : ")
for i in range(arr_size):
	if (numRay[i] >= arr_size*2):
		print(i, " ")

# This code is contributed by 29AjayKumar
