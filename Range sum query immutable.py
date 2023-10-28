class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = []
        total = 0
        for i in nums:
            total += i
            self.prefixSum.append(total)

    def sumRange(self, left: int, right: int) -> int:
        m = self.prefixSum

        if left == 0:
            return m[right]
        return m[right]-m[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
