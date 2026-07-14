class PDASimulator:

    def __init__(self, grammar):

        self.grammar = grammar

        self.trace = []

    def _push(self, stack, text):

        for c in reversed(text):

            if c != "ε":
                stack.append(c)

    def simulate(self, string):

        stack = ["$", "S"]

        self.trace = []

        index = 0

        while stack:

            self.trace.append(
                {
                    "stack": "".join(reversed(stack)),
                    "input": string[index:]
                }
            )

            top = stack.pop()

            if top == "$":

                break

            if top.isupper():

                if top not in self.grammar:

                    return False

                applied = False

                for production in self.grammar[top]:

                    temp = stack.copy()

                    self._push(temp, production)

                    applied = True

                    stack = temp

                    break

                if not applied:

                    return False

            else:

                if index >= len(string):

                    return False

                if string[index] != top:

                    return False

                index += 1

        return index == len(string)

    def get_trace(self):

        return self.trace