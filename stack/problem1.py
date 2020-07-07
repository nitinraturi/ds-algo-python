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

from .app import Stack

brackets_map = {
    '{': '}',
    '[': ']',
    '(': ')'
}

setA = "(({[]}))"  # Balanced
setB = "{{{)}]"  # Unbalanced


def isBalancedSet(bracket_set):
    s = Stack()
    for a in setA:
        pass


print(isBalancedSet(setA))
print(isBalancedSet(setB))
