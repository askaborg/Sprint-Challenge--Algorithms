'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC

    # base case
    if len(word) < 2:
        return 0
    # check for th
    elif word[-2] == 't' and word[-1] == 'h':
        return 1 + count_th(word[:-1])    # keep count and search the rest

    else:
        return count_th(word[:-1])    # search the rest
