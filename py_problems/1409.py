import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1409. Queries on a Permutation With Key


def processQueries(queries, m):
    P = list(range(1, m + 1))
    result = []
    
    for i in queries:
        pos = P.index(i)
        result.append(pos)
        P.insert(0, P.pop(pos))
    
    return result

# END
queries = [3,1,2,1]
m = 5

result = processQueries(queries, m)
display(result)
