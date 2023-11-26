import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1720. Decode XORed Array


def decode(encoded, first):
    target = [first]

    for i in range(len(encoded)):
        target.append(encoded[i] ^ target[i])

    return target


# END
encoded = [1, 2, 3]
first = 1

result = decode(encoded, first)
display(result)
