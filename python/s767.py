import collections
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S:
            return S
        L = len(S)
        counter = collections.Counter(S)
        max_cnt = max(counter.values())
        if max_cnt > (L + 1) // 2:
            return ""
        heap = [(-v, k) for k, v in counter.items()]
        heapq.heapify(heap)
        ret = []
        # while len(ret) < L: # 错误示范
        while len(heap) > 1:  # 保证有两个元素出堆
            _, letter1 = heapq.heappop(heap)
            _, letter2 = heapq.heappop(heap)
            ret += [letter1, letter2]
            counter[letter1] -= 1
            counter[letter2] -= 1
            if counter[letter1] > 0:
                heapq.heappush(heap, (-counter[letter1], letter1))
            if counter[letter2] > 0:
                heapq.heappush(heap, (-counter[letter2], letter2))
        # 考虑只有1个元素的情况
        if heap:
            ret.append(heap[0][1])
        return "".join(ret)


print(Solution().reorganizeString("aab"))
