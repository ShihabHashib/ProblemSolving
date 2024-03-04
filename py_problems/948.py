import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 948. Bag of Tokens


def bagOfTokensScore(tokens, power):
    tokens.sort()
    score = 0
    maxScore = 0
    left, right = 0, len(tokens) - 1

    while left <= right:
        if power >= tokens[left]:
            power -= tokens[left]
            score += 1
            left += 1
            maxScore = max(score, maxScore)
        elif score > 0:
            power += tokens[right]
            score -= 1
            right -= 1
        else:
            return maxScore

    return maxScore


# END
tokens = [100]
power = 50

result = bagOfTokensScore(tokens, power)
display(result)
