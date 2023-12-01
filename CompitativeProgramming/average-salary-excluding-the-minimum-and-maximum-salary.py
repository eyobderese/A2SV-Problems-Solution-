class Solution:
    def average(self, salary: List[int]) -> float:
        return round(((sum(sorted(salary)[1:len(salary)-1]))/(len(salary)-2)),5)