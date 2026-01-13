class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        # Segment tree for range max query
        max_val = max(nums)
        tree = [0] * (2 * max_val + 2)
        
        def update(idx, val):
            idx += max_val + 1
            tree[idx] = val
            while idx > 1:
                idx //= 2
                tree[idx] = max(tree[2 * idx], tree[2 * idx + 1])
        
        def query(l, r):
            # Query max in range [l, r]
            res = 0
            l += max_val + 1
            r += max_val + 1
            while l <= r:
                if l % 2 == 1:
                    res = max(res, tree[l])
                    l += 1
                if r % 2 == 0:
                    res = max(res, tree[r])
                    r -= 1
                l //= 2
                r //= 2
            return res
        
        ans = 0
        for num in nums:
            # Find max LIS length ending at values in range [num - k, num - 1]
            left = max(0, num - k)
            right = num - 1
            if left <= right:
                best = query(left, right)
            else:
                best = 0
            current = best + 1
            ans = max(ans, current)
            update(num, current)
        
        return ans