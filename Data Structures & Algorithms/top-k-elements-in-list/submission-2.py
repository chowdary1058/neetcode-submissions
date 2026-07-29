'''class Solution:
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

        return ans'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        d = {}

        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        print(d)
        a=[]
        while k>0:
            for key,value in d.items():
                if value == max(d.values()):
                    a.append(key)
                    del d[key]
                    k-=1
                    break
        return a
'''
        ans = []

        while k > 0:
            maxi = 0
            key1 = None

            for key, value in d.items():
                if value > maxi:
                    maxi = value
                    key1 = key

            ans.append(key1)
            del d[key1]
            k -= 1

        return ans'''
'''        while k>0:
            for key,value in d.items():
                if value == 1:
                    print(key)
                    del d[key]
                    k-=1
                    break'''