






class agenda():

	def __init__(self):
	
		self.miscontactos=[]

	def menu(self):
		miagenda=["        ",
		"agenda personal" , 
		"1. añadir contacto",
		"2. lista de contactos",
		"3. buscas contactos",
		"4. editar contacto",
		"5. cerrar contacto "
		]
		
		

		for p in miagenda:
			print(p)

		opcion=int(input("intrdusca la opcion: "))

		if opcion==1:
			self.anadir()
		if opcion==2:
			self.lista_contactos()
		if opcion==3:
			self.buscar()
		if opcion==4:
			self.editar()
		if opcion==5:
			print("gracias por utilizar la agenda adios")
		

		self.menu()

	def anadir(self):
			
			nombre=input("instrodusca contacto: nombre: ")
			tel=int(input("instrodusca contacto: tel: "))
			email=input("instrodusca contacto: email: ")
			self.miscontactos.append(nombre)
			self.miscontactos.append(tel)
			self.miscontactos.append(email)
	

	def lista_contactos(self):
		print("Lista de contactos")


		print(self.miscontactos[:])

		if len(self.miscontactos) == 0:
			print("esta vacio marico")

		for p in range(0,len(self.miscontactos),3):
			print(self.miscontactos[p])

	def buscar(self):
		
		buscar_nombre=input("ponga el nombre cara chimva: ")
		valor= buscar_nombre in self.miscontactos
		
		if valor == True:
			ubicacion_name=self.miscontactos.index(buscar_nombre)
			
			ubicacion_tel=ubicacion_name+1
			ubicacion_email=ubicacion_name+2
			print(self.miscontactos[ubicacion_name])
			print(self.miscontactos[ubicacion_tel])
			print(self.miscontactos[ubicacion_email])

		else:
			print("no esta ")

	def editar(self):

		

		nombre_editar=input("escriba el nombre a editar: ")

		if nombre_editar in self.miscontactos:
			ubicacion_editar=self.miscontactos.index(nombre_editar)
			
		else:
			print("rata no esta el nombre")
			self.menu()

		lista_editar=["         ",
		"que quiere editar:" 
		,"1. editar nombre: "
		,"2. editar numero: "
		, "3. editar correo: ",
		"4. volver " ]

		for i in lista_editar:
			print(i)



		numerodevariable=int(input())


		

		if numerodevariable==1:
			

			nombreaeditar=input("escriba nuevo nombre: ")

			self.miscontactos.remove(nombre_editar)
			self.miscontactos.insert(ubicacion_editar,nombreaeditar)


			lista_editar=["         ",
			"que  otra casa queire editar quiere editar:" 
			,"1. editar nombre: "
			,"2. editar numero: "
			, "3. editar correo: ",
			"4. volver " ]

			for i in lista_editar:
				print(i)



			numerodevariable=int(input())

		if numerodevariable==2:

			ubicacion_teleditar=ubicacion_editar+1
			
			print(ubicacion_teleditar)

			numero_editar=input("escriba el numero a nuevo: ")
			n=self.miscontactos[ubicacion_teleditar]

			self.miscontactos.remove(n)
			self.miscontactos.insert(ubicacion_teleditar,numero_editar)
			lista_editar=["         ",
			"que otra cosa quiere editar:" 
			,"1. editar nombre: "
			,"2. editar numero: "
			, "3. editar correo: ",
			"4. volver " ]

			for i in lista_editar:
				print(i)



			numerodevariable=int(input())
		if numerodevariable==3:



			ubicacion_emaileditar=ubicacion_editar+2

			print(ubicacion_emaileditar)
			gmail_editar=input("escriba el correona nuevo: ")

		
			q=self.miscontactos[ubicacion_emaileditar]
			
			self.miscontactos.remove(q)
			

			self.miscontactos.insert(ubicacion_emaileditar,gmail_editar)
			lista_editar=["         ",
			"que otra cosa quiere editar:" 
			,"1. editar nombre: "
			,"2. editar numero: "
			, "3. editar correo: ",
			"4. volver " ]

			for i in lista_editar:
				print(i)



			numerodevariable=int(input())

		if numerodevariable==4:
			self.menu()

			




			




		







agenda_person=agenda()
agenda_person.menu()







