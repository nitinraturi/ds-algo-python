"""
Question:

Determine if Brackets are Balanced

Examples of Balanced Brackets #
- { }
- { } { }
- ( ( { [ ] } ) )

Examples of Unbalanced Brackets #
- ( ( )
- { { { ) } ]
- [ ] [ ] ] ]

"""

from app import Stack

opening_brackets = {
    '{': '}',
    '[': ']',
    '(': ')'
}

closing_brackets = {
    '}': '{',
    ']': '[',
    ')': '('
}

setA = "(({}))"  # Balanced
setB = "{{{)}]"  # Unbalanced


def isBalancedSet(bracket_set):
    s = Stack()
    for bracket in bracket_set:
        cb = opening_brackets.get(bracket)
        ob = closing_brackets.get(bracket)
        if cb is not None:
            s.push(bracket)
        elif ob is not None:
            pb = s.pop()
            if ob == pb:
                continue
            else:
                return -1
        else:
            return None

    return -1 if len(s.get_stack()) > 0 else 1


print(isBalancedSet(setA))
print(isBalancedSet(setB))
