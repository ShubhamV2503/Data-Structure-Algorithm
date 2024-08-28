
# https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card



#User function Template for python3
class Solution:

	def count(self,arr, n, x):
		# code here
		counter = 0
		for i in range(len(arr)):
		    if x == arr[i]:
		        counter = counter  +1 
		return counter



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1



