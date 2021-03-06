from typing import List
from math import inf


class Solution:
    # https://leetcode-cn.com/problems/gas-station/solution/shi-yong-tu-de-si-xiang-fen-xi-gai-wen-ti-by-cyayc/
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        reward = 0
        min_i = 0
        min_reward = inf
        for i in range(N):
            reward += gas[i] - cost[i]
            if reward < min_reward:
                min_reward = reward
                min_i = i
        return (min_i + 1) % N if reward >= 0 else -1


res=Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
print(res)
