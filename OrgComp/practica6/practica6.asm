.data
    arr: .word 12, 17

.text
.globl main

main:
    # EJEMPLO 1: Excepción por desbordamiento aritmético
    # li $t0, 0x7fffffff
    # li $t1, 1 # $t1 = 1
    # addu $t2, $t0, $t1 # Ignora el desbordamiento
    # add $t3, $t0, $t1 # Detecta el desbordamiento

    # EJEMPLO 2: Excepción de dirección de almacenamiento.
    # No es posible almacenar en la dirección elegida
    # li $t0, 4
    # li $a0, 5
    # sw $a0, ($t0)

    # EJEMPLO 3: Excepción en la dirección de carga
    la $t0, arr
    lw $t0, 1($t0)

    # Salir del programa
    li $v0, 10
    syscall
