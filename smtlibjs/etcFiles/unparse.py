import ast
import astunparse
code = """
if 1 == 1 and 2 == 2 and 3 == 3:
    test = 1
"""

tree = ast.parse(code)
print(tree)
print(astunparse.dump(tree))
print(astunparse.unparse(tree))