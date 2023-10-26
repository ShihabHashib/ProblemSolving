import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 383. Ransom Note


def canConstruct(ransomNote, magazine):
    note, mega = list(ransomNote), list(magazine)

    print(note, mega)

    for char in note:
        if char in mega:
            mega.remove(char)
        else:
            return False

    return True


# END
ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"

result = canConstruct(ransomNote, magazine)
display(result)
