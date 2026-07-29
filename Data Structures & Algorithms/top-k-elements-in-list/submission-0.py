class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        arr = sorted(d.items(), key=lambda x: x[1], reverse=True)

        ans = []

        for i in range(k):
            ans.append(arr[i][0])

        return ans
'''        while k>0:
            for key,value in d.items():
                if value == 1:
                    print(key)
                    del d[key]
                    k-=1
                    break'''