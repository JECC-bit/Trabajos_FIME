#from json.tool import main
#import sumar as s
#import restar as r
#import multiplicar as m
#import dividir as d
#import cuadrado as c
#
#if __name__ == "__main__":
#    print(s.sumar(5,6))
#    print(r.restar(6,10))
#    print(m.multiplicar(5, 10))
#    print(d.dividr(4, 2))
#    print(c.cuadrado(5))

#from operaciones import *
#
#if __name__ == "__main__":
#    print(sumar(5,6))
#    print(restar(6,10))
#    print(multiplicar(5, 10))
#    print(dividr(4, 2))
#    print(cuadrado(5))

import ops.operaciones as op
import ops.sumar as s
from ops.operaciones import multiplicar

if __name__ == "__main__":
    print(op.cuadrado(5))
    print(s.sumar(5,5))
    print(multiplicar(5,5))