class Solution:
    def calPoints(self, operations: List[str]) -> int:
        output = []

        for i in operations:
            if i == "+":
                output.append(output[-1] + output[-2])
            elif i == "C":
                output.pop()
            elif i == "D":
                output.append(2 * output[-1])
            else:
                output.append(int(i))
        
        return sum(output)