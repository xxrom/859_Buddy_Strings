# 0123

# 01
# 02
# 03
# 12
# 13
# 23


class Solution(object):
    def changeInWord(self, word, i, j):
        print(word)
        print(i)
        print(j)
        wordList = list(word)
        print(wordList)

        temp = wordList[i]
        wordList[i] = wordList[j]
        wordList[j] = temp

        return ''.join(wordList)

    # Generate all possible variants for swapping caracters
    def generateAllVariants(self, word):
        word

    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """

        for i in A:
            print('%s ' % i, end='')

        print()
        for i in B:
            print('%s ' % i, end='')

        newA = self.changeInWord(A, 0, 1)
        print('newA %s' % newA)


word = Solution()

A1 = 'ab'
B1 = 'ba'
word.buddyStrings(A1, B1)
