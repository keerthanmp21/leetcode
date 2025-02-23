class Solution:
    def checkInclusion1(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
            
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
            
        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index]+1 == s2Count[index]:
                matches -= 1
                
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index]-1 == s2Count[index]:
                matches -= 1
                
            l += 1
        return matches == 26

    def checkInclusion2(self, s1: str, s2: str) -> bool:
        s1N = len(s1)
        s2N = len(s2)
        if s1N > s2N:
            return False

        s1Count = {}
        s2Count = {}

        for i in range(s1N):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
            s2Count[s2[i]] = s2Count.get(s2[i], 0) + 1

        if s1Count == s2Count:
            return True

        l = 0
        for r in range(s1N, s2N):
            s2Count[s2[r]] = s2Count.get(s2[r], 0) + 1

            s2Count[s2[l]] -= 1
            if s2Count[s2[l]] == 0:
                del s2Count[s2[l]]
            l += 1

            if s1Count == s2Count:
                return True

        return False

    