import ahorcado
# Juego de ahorcado

# Introduzca aqu� las instrucciones para el juego

# Despliegue de la entrada
ahorcado.printIntro('intro.txt')

# Variables globales
letrasIntentadas=''
numeroIntentos = 8
intentos_fallidos = 0
otraVez = 'y'

while otraVez == 'y':
	''' Inicio ciclo de nuevo juego '''
	# Selecci�n del modo de juego (1: palabra secreta, 2: archivo)
	# C�digo ...
	juego = input("Seleccione del modo de juego (1: palabra secreta, 2: archivo):\n")
	if juego == "1":
		palabraSecreta = ahorcado.inputSecret()
	else:
		palabraSecreta = ahorcado.pickWord(ahorcado.loadWords("superHeroes.txt"), ",")
	# ...
	ban = 1 # Bandera que indica la culminaci�n de una tanda de turnos
			# ya sea por que el usuario acierta o por que pierde
			
	# Impresi�n de las estad�sticas (Numero de intentos, letras disponibles, palabra secreta (rayas))
	# C�digo ...
	print("Número de intentos = ",numeroIntentos,"\nLetras disponibles = ",ahorcado.obtenerLetrasDisponibles(letrasIntentadas),"\n",ahorcado.obtenerParteAdivinada(palabraSecreta, letrasIntentadas))
	
	# ...
	while ban <= numeroIntentos:
		''' Inicio ciclo para adivinar la palabra oculta '''
		# Solicitud interactiva de palabras
		# C�digo ...
		letra = input("Introduce una letra: ")
		# ...
		
		# Verificaci�n de la letra e impresi�n de lo que va de la palabra
		# C�digo ...
		verifi = ahorcado.verificarLetraIngresada(letra, letrasIntentadas)
		letrasIntentadas += letra
		if verifi == True:
			print("La letra ingresada ya está en uso, intenta con otra letra.")
			continue
		else:
			pa = ahorcado.obtenerParteAdivinada(palabraSecreta, letrasIntentadas)
			if letra in pa:
				print("Letra acertada")
				ahorcado.dibujar_ahorcado(intentos_fallidos)
			else:
				print("Letra no acertada, pierdes una vida")
				intentos_fallidos += 1
				numeroIntentos -= 1			
				ahorcado.dibujar_ahorcado(intentos_fallidos)
				
		# ...
		
		# Verificaci�n de la condici�n de finalizaci�n del juego
		# C�digo ...
		condi = ahorcado.palabraAdivinada(palabraSecreta, letrasIntentadas)
		if condi == True:
			print("Palabra adivinada!")
			break
		# ...
		
		# Impresi�n del estado del juego (N�mero de intentos, letras disponibles)
		# C�digo ...
		# ...
		print("Número de intentos = ",numeroIntentos,"\nLetras disponibles = ",ahorcado.obtenerLetrasDisponibles(letrasIntentadas),"\n",ahorcado.obtenerParteAdivinada(palabraSecreta, letrasIntentadas))

		# Verificaci�n de la condici�n de finalizaci�n del juego
		# C�digo ...
		if numeroIntentos == 0:
			print("No pudo adivinar la palabra, paila. Vuelva a jugar.\nLa palabra secreta era: ",palabraSecreta)

			break
		# ...
		''' Fin ciclo para adivinar la palabra oculta '''
	# Inicializar nuevamente las variables que crea necesario...
	letrasIntentadas = ""
	numeroIntentos = 8
	# Solicitud de nuevo juego
	otraVez = input('Desea jugar otra vez (y/n): ')  
	otraVez = otraVez.lower()
	''' Fin ciclo de nuevo juego '''