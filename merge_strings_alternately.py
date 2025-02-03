class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        l1 = len(word1)
        l2 = len(word2)

        for i in range(min(l1, l2)):
            merged.append(word1[i])
            merged.append(word2[i])

        merged.append(word1[i+1:])
        merged.append(word2[i+1:])

        return "".join(merged)

if __name__ == "__main__":
    solution = Solution()

    word1 = "abc"
    word2 = "pqr"
    print("merged :", solution.mergeAlternately(word1, word2))


