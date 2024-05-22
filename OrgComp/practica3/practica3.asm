.data

    a: .float 5.0
    f: .float 15.0
    c: .float 0.0

.text
.globl main 

main:
    
    # cargar los valores
    l.s $f1, a
    l.s $f2, f

    # Operaciones para sacar hipotenusa
    mul.s $f3, $f1, $f1
    mul.s $f4, $f2, $f2
    add.s $f5, $f3, $f4
    sqrt.s $f6, $f5

    s.s $f6, c

    #salir del prgrama
    li $v0, 10
    syscall
