class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for element in operations: 
            if element == "C":
                score.pop()
            elif element == "D":
                score.append(score[-1]*2)
            elif element == "+":
                score.append(score[-1] + score[-2])
            else: 
                score.append(int(element))
        return sum(score)
