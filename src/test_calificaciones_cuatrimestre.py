from calificaciones import *

def main(): 
    c1 = lee_real("Dame la nota del C1: ")
    c2 = lee_real("Dame la nota del C2: ")
    c3 = lee_real("Dame la nota del C3: ")
    pr1 = lee_real("Dame la nota del proyecto en Python: ")
    ex1 = lee_real("Dame la nota del examen práctico en Python: ")
    cuatrimestre1 = calcula_nota_cuatrimestre((c1, c2, c3), pr1, ex1)
    print("La nota del primer cuatrimestre es:", cuatrimestre1)
    '''c4 = lee_real("Dame la nota del C4: ")
    c5 = lee_real("Dame la nota del C5: ")
    c6 = lee_real("Dame la nota del C6: ")
    pr2 = lee_real("Dame la nota del proyecto en Java: ")
    ex2 = lee_real("Dame la nota del examen práctico en Java: ")
    cuatrimestre2 = calcula_nota_cuatrimestre(c4, c5, c6, pr2, ex2)
    print("Tu nota de evaluación continua es: ", (cuatrimestre1 + cuatrimestre2)/2)'''

if __name__ == "__main__":
    main()
  
