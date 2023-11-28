class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0

        i = 0
        while True:
            if tickets[i] == 0:
                i = (i+1) % len(tickets)

                continue
            tickets[i] -= 1
            count += 1
            if tickets[k] == 0:
                return count

            i = (i+1) % len(tickets)
