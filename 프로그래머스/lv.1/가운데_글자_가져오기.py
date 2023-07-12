def solution(s):
    wordlist = list(s)
    if len(wordlist) % 2 == 1:
        return ''+ wordlist[len(wordlist)//2]
    else:
        return ''+ wordlist[len(wordlist)//2-1] + wordlist[len(wordlist)//2]
    
#str 활용
def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2 + 1]