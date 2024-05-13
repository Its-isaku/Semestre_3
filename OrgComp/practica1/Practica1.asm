.data 
    V: .word 10, 20, 25, 500, 3

    i: .word 1

.text
.globl main
main:

    lw $s0, V($zero)
    li $s5, 4
    lw $s1, V($s5)
    li $s6, 8
    lw $s2, V($s6)
    li $s7, 12
    lw $s3, V($s7)
    li $s8, 16
    lw $s4, V($s8)


    #salir del prgrama
    li $v0, 10
    syscall