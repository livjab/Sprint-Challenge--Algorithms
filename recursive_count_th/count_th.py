'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # base case if string is empty
    if not word:
        return 0

    # check if word starts with "th", and increment count
    # progress through word by passing it recursively through funcction.
    elif word[0:2] == "th":
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])
