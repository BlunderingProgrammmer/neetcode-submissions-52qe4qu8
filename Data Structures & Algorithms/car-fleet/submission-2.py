class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position,speed)] #list comp peroper values
        stack = []
        for p,s in sorted(pair)[::-1]:#go in reverse order
            time = (target - p)/s #calc time and append to stack
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: #compare if pop() if time on top is smaller or equal to the one below then we pop
                stack.pop()
        return len(stack)