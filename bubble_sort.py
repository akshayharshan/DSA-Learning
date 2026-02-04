# The thing to remember is the inner loop will do the job and out loop 
# is decide how many time to run the loop to make the array completely sorted

class Solution:
    def bubble_sort(self,arr):
        n = len(arr)

        for i in range(n):
            for j in range(0,n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr


arr = [5,6,73,21,5,7,4,3,1]
sol = Solution()
print(sol.bubble_sort(arr))