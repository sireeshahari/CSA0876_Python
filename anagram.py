from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("Output for Test Case 1:", groupAnagrams(strs))