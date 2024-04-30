.data
    # Definir un array de cuatro palabras
    arreglo: .word 1 4 12 13

    # Definir los tres primeros bytes de la siguiente palabra
    .byte 0x1c, 0x0b,11

    # Alinear en una palabra el siguiente dato en memoria
    .align 2

    # Definir una cadena de caracteres
    .ascii " Hola "

    # Definir una cadena de caracteres terminada con el caracter nulo.
    .asciiz " , MIPS "

    .align 2

    # Definir un índice para el arreglo
    i: .word 1

.text
.globl main

main:
    lw $s0, arreglo($zero) # Carga en $se arreglo[0]
    lw $s4,i # Carga en $s4 el índice del array
    mul $s5,$s4,4 # Guarda en $s5 el resultado de $s4*4
    lw $s1, arreglo($s5) # Carga en $s1 arreglo[1]
    add $s4,$s4,1 # Se incrementa en uno el índice del array
    mul $s5,$s4,4 # Guarda en $s5 el resultado de $s4*4
    lw $s2,arreglo ($s5) # Carga en $s2 arreglo[2]
    add $s4,$s4,1 # Se incrementa en uno el índice del array
    mul $s5,$s4,4 # Guarda en $s5 el resultado de $s4*4
    lw $s3, arreglo($s5) # Carga en $s3 arreglo[3]
    
    #Salir del programa
    li $v0, 10
    syscall