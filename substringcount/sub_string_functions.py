def is_vowel(c):
    
    if c == 'a' or c == 'i' or c == 'e' or c == 'o' or c == 'u':
        
        return True
    
    else:
        return False


def findSubstring(s, k):
    
    longest_substring = ''
    len_ls = 0
    
    for i in range(len(s) - k+1):

        temp_string = s[i: i + k]
        print(temp_string)
        count = 0
        
        for j in temp_string:

            if is_vowel(j):
                count += 1
        
        if count > len_ls:

            len_ls, longest_substring = count, temp_string

            

        
    
    return longest_substring







            
    
