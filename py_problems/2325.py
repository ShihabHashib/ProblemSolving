import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2325. Decode the Message


def decodeMessage(key, message):
    table = {' ': ' '}
    i = 97
    for k in key:
        if k not in table and k is not ' ':
            table[k] = chr(i)
            i += 1
    return "".join(table[m] for m in message)


# END


key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
result = decodeMessage(key, message)
display(result)
