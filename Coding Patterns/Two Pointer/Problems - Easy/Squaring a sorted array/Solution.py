class Solution:
    def squareSortedArray(self, arr):
        sortedSquaresArr = [0 for x in range(len(arr))]

        left, right, tempPointer = 0, len(arr)-1, len(arr)-1
        while(left <= right):
            leftSquare = arr[left] * arr[left]
            rightSquare = arr[right] * arr[right]

            if leftSquare <= rightSquare:
                sortedSquaresArr[tempPointer] = rightSquare
                right -= 1
            else:
                sortedSquaresArr[tempPointer] = leftSquare
                left += 1

            tempPointer -= 1

        return sortedSquaresArr
    

def main():
    sol = Solution()
    print("Sorted Sqaures: "+ str(sol.squareSortedArray([-2, -1, 0, 2, 3])))
    print("Sorted Sqaures: "+ str(sol.squareSortedArray([-3, -1, 0, 1, 2])))

main()