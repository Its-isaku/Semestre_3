.data
    original: .word 0x10203040  # La palabra original
    resultado: .word 0          # se almacenará el resultado invertido

.text
.globl main
main:
    # Cargar la palabra original en el registro $t0
    lw $t0, original($zero)

    # Invertir palabra bit a bit
    andi $t1, $t0, 0xFF         # Aislar el byte menos significativo
    sll  $t1, $t1, 24           # Mover el byte menos significativo a la posición más significativa

    andi $t2, $t0, 0xFF00       # Aislar el segundo byte menos significativo
    srl  $t2, $t2, 8            # Mover el segundo byte menos significativo a la segunda posición más significativa

    # en los dos bytes más significativos se dividen en partes
    lui  $t3, 0xFF00            # Cargar la parte alta del tercer byte menos significativo
    and  $t3, $t0, $t3          # Aislar el tercer byte menos significativo
    srl  $t3, $t3, 8            # Mover el tercer byte menos significativo a la segunda posición menos significativa

    lui  $t4, 0xFF              # Cargar la parte alta del byte más significativo
    and  $t4, $t0, $t4          # Aislar el byte más significativo
    srl  $t4, $t4, 24           # Mover el byte más significativo a la posición menos significativa

    # Combinar todos los bytes invertidos en un solo registro
    or   $t5, $t1, $t2          # Combinar los dos bytes más significativos
    or   $t5, $t5, $t3          # Agregar el tercer byte
    or   $t5, $t5, $t4          # Agregar el byte menos significativo

    # Guardar el resultado en la memoria
    sw $t5, resultado($zero)

    # Salir del programa
    li $v0, 10
    syscall
