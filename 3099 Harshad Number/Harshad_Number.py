class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        sumOfDigits = 0
        original = x

        # Convert to singluar digits
        x = list(str(x))
        for num in x:
            sumOfDigits += int(num)

        # Harshad Number check
        if original % sumOfDigits == 0:
            return sumOfDigits

        return -1
