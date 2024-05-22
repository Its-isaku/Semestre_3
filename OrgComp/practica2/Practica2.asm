.data
    a:   .word  6
    f:   .word  7
    c:   .word  6
    d:   .word  0

.text
.globl main

main:
    
    # cargar las variables en los registros 
    lw $t0, a
    lw $t1, f
    lw $t2, c
    li $t3, 2
    # calcular primer parentesis
    sub $t4, $t0, $t3  

    # calcular segundo parentesis
    mul $t5, $t1,  $t2
    sub $t6, $t0, $t5

    # Terminar operacion
    mul $t7, $t4, $t6

    # guardar resultados en d
    sw $t7, d

    #salir del prgrama
    li $v0, 10
    syscall