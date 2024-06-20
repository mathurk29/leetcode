from asyncio import QueueEmpty


def QuestionsMarks(s):
    qnum = 0
    l_val = 0
    has_10 = False
    for ch in s:
        if ch.isdigit():
            if int(ch) + l_val == 10:
                if qnum != 3:
                    return "false"
                has_10 = True
            l_val = int(ch)
            qnum = 0
        elif ch == "?":
            qnum += 1
    return "true" if has_10 else "false"


QuestionsMarks("arrb6???4xxbl5???eee5")

QuestionsMarks("acc?7??sss?3rr1??????5")

QuestionsMarks("5??aaaaaaaaaaaaaaaaaaa?5?5")

QuestionsMarks("9???1???9???1???9")

QuestionsMarks("aa6?9")
