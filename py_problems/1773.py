import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1773. Count Items Matching a Rule


def countMatches(items, ruleKey, ruleValue):
    key = 0
    count = 0
    if ruleKey == "color":
        key = 1
    elif ruleKey == "name":
        key = 2

    for i in range(len(items)):
        if items[i][key] == ruleValue:
            count += 1

    return count


# END
items = [["phone", "blue", "pixel"], ["computer",
                                      "silver", "phone"], ["phone", "gold", "iphone"]]
ruleKey = "type"
ruleValue = "phone"

result = countMatches(items, ruleKey, ruleValue)
display(result)
