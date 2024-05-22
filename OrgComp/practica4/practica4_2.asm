.data
numero: .word 0x3ff41
.space 4

.text
main:
    lw $t0, numero($0)  # Cargar el valor de 'numero' en $t0
    andi $t1, $t0, 0xfffe  # Aplicar AND bit a bit con 0xfffe y almacenar en $t1
    sw $t1, numero+4($0)  # Almacenar el valor de $t1 en la siguiente palabra de memoria

    li $v0, 10
    syscall