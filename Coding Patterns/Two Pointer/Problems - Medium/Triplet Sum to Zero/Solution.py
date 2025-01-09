class Solution:
    def findTriplets(self, arr):
        triplets = []
        arr.sort()

        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            self.searchPair(arr, -arr[i], i, triplets)

        return triplets


    def searchPair(self, arr, targetSum, itemIndex, triplets):
        left = itemIndex + 1
        right = len(arr) - 1

        while(left < right):
            pairSum = arr[left] + arr[right]
            if pairSum == targetSum:
                triplets.append([-targetSum, arr[left], arr[right]])
                left += 1
                right -= 1
            elif pairSum < targetSum:
                left += 1
            else:
                right -= 1


def main():
    sol = Solution()
    print("Triplets are: "+ str(sol.findTriplets([-3, 0, 1, 2, -1, 1, -2])))
    #Expects [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]

    print("Triplets are: "+ str(sol.findTriplets([-5, 2, -1, -2, 3])))
    #Expects [[-5, 2, 3], [-2, -1, 3]]

    print("Triplets are: "+ str(sol.findTriplets([-5, -5, 2, -1, -2, 3])))
    #Expects [[-5, 2, 3], [-2, -1, 3]]

main()