.data
t1: .word 0x55555555  # Definir el valor inicial de $t1
t2: .word 0x0AAAAAAA  # Definir el valor inicial de $t2
.space 4

.text
.globl main

main:
    lw $t1, t1($0)     # Cargar el valor de t1 en $t1
    lw $t2, t2($0)     # Cargar el valor de t2 en $t2
    
    or $t3, $t1, $t2   # Realizar operación OR y almacenar el resultado en $t3
    sw $t3, t1+4($0)   # Almacenar el resultado de $t3 en la memoria

    or $t4, $t1, $t2   # Realizar operación OR y almacenar el resultado en $t4
    sw $t4, t1+8($0)   # Almacenar el resultado de $t4 en la memoria

    xor $t5, $t1, $t2  # Realizar operación XOR y almacenar el resultado en $t5
    sw $t5, t1+12($0)  # Almacenar el resultado de $t5 en la memoria

    li $v0, 10         # Syscall para salir del programa
    syscall
