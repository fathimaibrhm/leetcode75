class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str :

        if str1 +str2 != str2 + str1:
            return ""

        def gcd(a, b):
            while b > 0 :
                reminder = a % b
                a = b
                b = reminder
            return a

        return str1[:gcd(len(str1), len(str2))]


if __name__ == "__main__":
    solution = Solution()

    str1 = "ABCABC"
    str2 = "ABC"
    print("GCD of strings is :", solution.gcdOfStrings(str1, str2))

    str1 = "ABABAB"
    str2 = "ABAB"
    print("GCD of strings is :", solution.gcdOfStrings(str1, str2))

    str1 = "LEET"
    str2 = "CODE"
    print("GCD of strings is :", solution.gcdOfStrings(str1, str2))

