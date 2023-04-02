import ast
import astunparse
def parse_ast(filename):
    with open(filename) as f:
        code = f.read()
    tree = ast.parse(code)
    return astunparse.dump(tree)
