import ast
import astunparse
with open('max.py') as f:
    code = f.read()
print(code)
tree = ast.parse(code)
print(tree)
print(astunparse.dump(tree))
