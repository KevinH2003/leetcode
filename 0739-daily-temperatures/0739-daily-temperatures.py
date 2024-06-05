class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #list of tuples of the form (temp, index)
        out = [0 for i in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][0]:
                top, topindex = stack.pop()
                out[topindex] = i - topindex

            stack.append( (temp, i))

        return out