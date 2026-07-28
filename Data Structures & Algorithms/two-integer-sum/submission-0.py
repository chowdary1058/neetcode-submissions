class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
'''        found = False

        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]

                if s == target:
                    print("Sub :", nums[i:j+1])
                    print(i, "to", j)
                    found = True

        if not found:
            print("No subarray found.")'''