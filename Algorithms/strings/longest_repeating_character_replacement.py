def charReplacement(s, k):
    '''
    given a string like 'aabab', replace any string k times
    to get the longest string with repeating characters
    1. get the count of max repeating character
    2. get window length
    3. if windowLen - count[most freqChar] <= k, that means we are within
        the limit of allowed replacements
    4. Use sliding window --> if above condition fails, move window
    '''
    count = {} # to count the occurences of each character character
    left = 0 # left pointer
    mostFreq = 0 # length of most freq charcter
    windowLen = 0
    for right in range(len(s)): # this is my right pointer
        count[s[right]] = 1 + count.get(s[right], 0)
        mostFreq = max(mostFreq, count[s[right]])
        
        windowLen = right - left + 1 
        print(f"windowLen = {right} - {left} + 1")
        # subract the len of most freq from window to 
        # to check if replacements are within range
        if windowLen - mostFreq > k: 
            # remove the count of left most character
            # move left pointer by one
            count[s[left]] -= 1
            left += 1
    
    print(f"{right} - {left} + 1")
    return right - left + 1


s = "AABABBA"
k = 1

result = charReplacement(s, k)

print(result) # expected output 4

            
    