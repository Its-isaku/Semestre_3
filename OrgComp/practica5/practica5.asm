.data
V:      .word 0x00000001, 0x00000002, 0x7FFFFFFF, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007, 0x00000008, 0x00000009
suma:   .word 0x00000000

.text
.globl main

main:
    # Cargar los valores del vector en registros temporales
    lw $t0, V           # Cargar el primer elemento en $t0
    lw $t1, V+4         # Cargar el segundo elemento en $t1
    lw $t2, V+8         # Cargar el tercer elemento en $t2
    lw $t3, V+12        # Cargar el cuarto elemento en $t3
    lw $t4, V+16        # Cargar el quinto elemento en $t4
    lw $t5, V+20        # Cargar el sexto elemento en $t5
    lw $t6, V+24        # Cargar el séptimo elemento en $t6
    lw $t7, V+28        # Cargar el octavo elemento en $t7
    lw $t8, V+32        # Cargar el noveno elemento en $t8
    lw $t9, V+36        # Cargar el décimo elemento en $t9

    # Sumar los elementos del vector utilizando add para detectar desbordamiento
    add $t0, $t0, $t1  # $t0 = V[0] + V[1]
    add $t0, $t0, $t2  # $t0 = $t0 + V[2]
    add $t0, $t0, $t3  # $t0 = $t0 + V[3]
    add $t0, $t0, $t4  # $t0 = $t0 + V[4]
    add $t0, $t0, $t5  # $t0 = $t0 + V[5]
    add $t0, $t0, $t6  # $t0 = $t0 + V[6]
    add $t0, $t0, $t7  # $t0 = $t0 + V[7]
    add $t0, $t0, $t8  # $t0 = $t0 + V[8]
    add $t0, $t0, $t9  # $t0 = $t0 + V[9]

    # Almacenar el resultado en la variable suma
    la $t1, suma        # Cargar la dirección de suma en $t1
    sw $t0, 0($t1)      # Almacenar el resultado en suma

    # Terminar el programa
    li $v0, 10
    syscall
