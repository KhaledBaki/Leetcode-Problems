import re
class Solution(object):
    def calculate(self, s):
        # Result is zero initially
        result = 0

        # Empty Stack
        stack = []
        s = s.replace(" ", "")

        # segments the string
        splitUp = re.split(r'([+/*-])', s)

        # Default initial operator
        currentOperator = '+'

        for term in splitUp:
            
            # Finds appropriate operator 
            if (term == '+') or (term == '-') or (term == '/') or (term == '*'):
                currentOperator = term
            
            # The term is a number
            else:
                if currentOperator == '+':
                    stack.append(int(term))

                elif currentOperator == '-':
                    stack.append(-1 * int(term))

                # Pops previous element from the stack
                elif currentOperator == '*':
                    stack.append(stack.pop() * int(term))

                # Pops previous element from the stack
                elif currentOperator == '/':
                    stack.append(int(float(stack.pop()) / int(term))) 

        # pops all remaining elements in the stack and adds them
        while not len(stack) == 0:
            result += stack.pop()
        
        return result

        
