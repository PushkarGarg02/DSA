class Solution:
    def search(self, arr, target_sum):
        left, right = 0, len(arr)-1
        while (left < right):
            current_sum = arr[left] + arr[right]
            if current_sum == target_sum:
                return [left, right]
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1

        return [-1,-1]


def main():
    sol = Solution()
    print(sol.search([1,2,3,4,5,6],6))
    print(sol.search([2,5,9,11],11))

main()



          