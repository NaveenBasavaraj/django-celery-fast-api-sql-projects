def is_valid_anagram(s1, s2):
    if len(s1) != len(s2):
        # if not length is same, then not a valid anagram
        return False
    
    countS1 = {}
    countS2 = {}
    for i in range(len(s1)):
        # counting each character
        countS1[s1[i]] = 1 + countS1.get(s1, 0)
        countS2[s1[i]] = 1 + countS2.get(s2, 0)
    
    for s in s1:
        # verify count
        if countS1[s] != countS2[s]:
            return False
        
    return True


def group_anagrams(words):
    from collections import defaultdict
    ans = defaultdict(list)
    {"[0,1,3,1...26]": ["word1","word2"]}
    for word in words:
        count = [0] * 26
        for each_char in word:
            count[ord(each_char) - ord("a")] += 1
        ans[tuple(count)].append(word)
    return ans.values()