class Solution:
    def moveElements(self, arr):
        
        nextNonDuplicate, next = 0, 0
        while (next < len(arr)):
            if arr[nextNonDuplicate] != arr[next]:
                arr[nextNonDuplicate+1] = arr[next]
                nextNonDuplicate += 1

            next += 1

        return nextNonDuplicate+1


def main():
    sol = Solution()
    print(sol.moveElements([2])) #Expect 1
    print(sol.moveElements([2, 3])) #Expect 2
    print(sol.moveElements([2, 2])) #Expect 1
    print(sol.moveElements([2, 3, 3, 3, 6, 9, 9])) #Expect 4
    print(sol.moveElements([2, 2, 2, 11])) #Expect 2

main()