class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False #negative numbers are not palindromes

        #convert to string
        x_str = str(x)
        return x_str == x_str[::-1]
        




                    
        