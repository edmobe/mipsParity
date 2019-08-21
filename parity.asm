# MAIN
addi $t0, $zero, 18 			# Número ingresado por el usuario (18) -> 18
jal parity				# Se llama a parity

li $v0 10  				# Se termina el programa
syscall					# Se sale del programa

  parity:
  add $t2, $t0, $zero 			# Copia del número ingresado por el usuario, manipulable
  add $t1, $zero, $zero 		# Bit paridad inicia en 0
  add $t3, $zero, $zero 		# Bit actual leído
  j while				# Se inicia el loop
  syscall
  
  while:  
  beq $t2, 0, END			# Si el número el número manipulable es igual a 0 saltar a END
  andi $t3, $t2, 1			# Se obtiene el último bit del manipulable
  bne $t3, $zero, changeBitParity	# Si el último bit es 1 se cambia la paridad
  j endLoop				# Se llama al final del while
  syscall
  
  changeBitParity:
  sub $t1, $t3, $t1			# Se niega el valor de $t1, pues la paridad cambió
  j endLoop				# Se llama al final del while
  syscall
  
  endLoop:
  srl $t2, $t2, 1			# Se obtiene el siguiente bit de n
  j while				# Se reinicia el loop
  syscall

  END:
  jr $31				# Se vuelve a main
  syscall
