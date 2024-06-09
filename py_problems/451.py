import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 451. Sort Characters By Frequency


def frequencySort(s):
    fre = {}

    for i in s:
        if i in fre:
            fre[i] += 1
        else:
            fre[i] = 1 
    
    return ''.join([char * freq for char, freq in sorted(fre.items(), key=lambda x: (-x[1], x[0]))])


# END
s = "tree"

result = frequencySort(s)
display(result)
