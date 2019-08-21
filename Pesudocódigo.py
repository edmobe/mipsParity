# ================================================================
# IMPORTANTE: ESTE NO ES UN CÓDIGO FUNCIONAL, SOLO UN PSEUDOCÓDIGO
# ================================================================

global t0                           # Valor n
global t1                           # Paridad
global t2                           # Copia de n para manipular
global t3                           # Bit actual leído


def main():                         # (1) # MAIN
    t0 = 3                          # (2) addi $t0, $zero, 3
    parity()                        # (3) jal parity


def parity():                       # (8) Parity:
    t2 = t0                         # (9) add $t2, $t0, $zero
    t1 = 0                          # (10) add $t1, $zero, $zero
    t3 = 0                          # (11) add $t3, $zero, $zero
    whileFunction()                 # (12) j while


def whileFunction():                # (15) while:
    if (t2 == 0):                   # (16) beq $t2, 0, END
        return                      # (33) jr $31
    t3 = getLastBitOf($t2)          # (17) andi $t3, $t2, 1
    if (t3 != 0):                   # (18) bne $t3, $zero, changeBitParity
        changeBitParity()           # (18) bne $t3, $zero, changeBitParity
    endLoop()                       # (19) j endloop


def changeBitParity():              # (22) changeBitParity:
    t1 = t3 - t1                    # (23) sub $t1, $t3, $t1
    endLoop()                       # (24) j endLoop


def endLoop():                      # (27) endLoop
    swipeRightLogic(t2, t2, t1)     # (28) srl $t2, $t2, 1
    whileFunction()                 # (29) j while
