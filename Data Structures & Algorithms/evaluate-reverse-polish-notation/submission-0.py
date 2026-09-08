class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        g = []

        for token in tokens:

            if token not in ["+", "-", "*", "/"]:
                g.append(int(token))

            else:
                a = g.pop()
                b = g.pop()

                if token == "+":
                    g.append(b + a)

                elif token == "-":
                    g.append(b - a)

                elif token == "*":
                    g.append(b * a)

                elif token == "/":
                    g.append(int(b / a))

        return g[-1]