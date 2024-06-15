import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2125. Number of Laser Beams in a Bank


def numberOfBeams(bank):
    result, prev = 0, 0
    
    for i in bank:
        count = i.count("1")

        if count:
            result += count * prev
            prev = count
    return result

# END
bank = ["011001","000000","010100","001000"]

result = numberOfBeams(bank)
display(result)
