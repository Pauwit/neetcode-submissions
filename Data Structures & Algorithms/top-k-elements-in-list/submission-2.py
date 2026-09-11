class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()

        for num in nums:
            if not num in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        ret = []
        l = 0
        for (number, frequency) in freq.items():
            if l < k:
                i = 0
                while i < l and ret[i][1] < frequency:
                    i += 1
                
                ret.insert(i, (number, frequency))
                l += 1
            elif ret[0][1] < frequency:
                i = 1
                while i < l and ret[i][1] < frequency:
                    i += 1

                ret.insert(i, (number, frequency))
                ret.pop(0)
        

        return [cur[0] for cur in ret]
        