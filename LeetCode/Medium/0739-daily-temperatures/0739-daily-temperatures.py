class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                top = stack.pop()
                answer[top] = i - top
            stack.append(i)
    
        return answer