from collections import defaultdict
# WRITE GROUP_ANAGRAMS FUNCTION HERE #
def group_anagrams(my_list):
    words_dict = defaultdict(list)
    for word in my_list:
        cur_word = ''.join(sorted(word))
        words_dict[cur_word].append(word)
    return list(words_dict.values())
        
print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )