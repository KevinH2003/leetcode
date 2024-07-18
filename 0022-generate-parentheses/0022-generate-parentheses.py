class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        ongoing = ""

        def rec(n, opened, closed, ongoing, ret):
            if opened == closed and opened == n:
                ret.append(ongoing)
            elif opened > closed and opened < n:
                rec(n, opened + 1, closed, ongoing + "(", ret)
                rec(n, opened, closed + 1, ongoing + ")", ret)
            elif opened == closed and opened < n:
                rec(n, opened + 1, closed, ongoing + "(", ret)
            else:
                rec(n, opened, closed + 1, ongoing + ")", ret)

        rec(n, 0, 0, ongoing, ret)

        return ret