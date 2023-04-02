ast = [['define', '-', 'fun', 'max2', [['x', 'Int'], ['y', 'Int']], 'Int', ['ite', ['<', '=', 'x', 'y'], 'y', 'x']]]
ast2 = [['define', '-', 'fun', 'max2', [['x', 'Int'], ['y', 'Int']], 'Int', ['-', ['+', ['+', 500, 'y'], 'x'], 0]]]
aOperators = ['+','-','*','/']
eOperators = ['=', '<','>']
def astToPython(ast):
    funcAst = ast[0]
    funcName = funcAst[3]
    params = astParamsToPython(funcAst[4])
    returnType = funcAst[5]
    body = funcAst[6]
    pyFunc = 'def ' +funcName + params + '->' + returnType.lower() + ':'+ astBodyToPython(body, 1)
    return pyFunc

def astParamsToPython(params):
    paramString = '('
    for p in params:
        paramString += str(p[0]) + ': '  +str(p[1].lower()) + ','
    paramString += ')'
    return paramString

def astBodyToPython(body,depth):
    if type(body) is not list:
        return str(body)
    if(body[0] == 'ite'):
        conditional = astBodyToPython(body[1], depth+1)
        ifResult = astBodyToPython(body[2], depth+1)
        elseResult = astBodyToPython(body[3], depth+1)
        conditStr = '\n\tif ' + conditional + ':'+'\n\t\t' + 'return' + ifResult + '\n\telse:'  + '\n\t\t'+ 'return' +elseResult
        return conditStr
    elif(body[0] in aOperators):
        lOperator = astBodyToPython(body[1], depth+1)
        rOperator = astBodyToPython(body[2], depth+1)
        if depth ==1:
            conditStr = '\n\treturn ' +str(lOperator) + str(body[0]) + str(rOperator)
        else:
            conditStr = str(lOperator) + str(body[0]) + str(rOperator)
        return conditStr
    elif(body[0] in eOperators):
        
        if(body[1] == '='):
            lOperator = astBodyToPython(body[2], depth+1)
            rOperator = astBodyToPython(body[3], depth+1)
            conditStr = lOperator + body[0] + body[1] + rOperator
        else:
            lOperator = astBodyToPython(body[1], depth+1)
            rOperator = astBodyToPython(body[2], depth+1)
            conditStr = lOperator + body[0] + rOperator
        return conditStr



    
    
pyFunc = astToPython(ast2)
print(pyFunc)
f = open("pyFunc.py", "w")
f.write(pyFunc)
f.close()