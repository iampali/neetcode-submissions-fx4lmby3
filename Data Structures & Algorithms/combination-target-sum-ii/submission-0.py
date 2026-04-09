class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()
        def helper(curr, idx, curr_sum):
            if curr_sum == target:
                output.append(curr[:])
                return
            
            if curr_sum > target:
                return
            
            for i in range(idx, len(candidates)):
               # 🔑 Skip duplicates at the same recursion level
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                
                helper(curr + [candidates[i]], i+1, curr_sum + candidates[i])
        

        helper([],0,0)

        return output