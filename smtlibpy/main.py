import sygParser as sp
import astToPython as ap
import sygSolver as ss
import astReader as ar

def main():
    sygFile = 'max2.sl'
    sygAnswer = ss.solveSyg(sygFile)
    print('\nSYGUS SOLUTION: \n' +sygAnswer)
    splitAnswer = (sygAnswer.split('\n'))[1]
    pAnswer = sp.norm_get(splitAnswer)
    pyFunc = ap.astToPython(pAnswer)
    print('\nSYNTHESIZED FUNCTION: \n' +pyFunc)

    pyFile = sygFile.split('.')[0] + '.py'
    f = open(pyFile, "w")
    f.write(pyFunc)
    f.close()

    print('\n CREATED FUNCTION AT ' + pyFile)

    print('\n FORMAL PYTHON AST OF CREATED PYTHON FILE: \n')
    astTree = ar.parse_ast(pyFile)
    print(astTree)
if __name__ == '__main__':
    main()
  