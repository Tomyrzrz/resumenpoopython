#Repaso de POO para la evaluacion del 3er parcial

class Hotel():
	"""docstring for Hotel"""
	def __init__(self, phabitaciones, pnombre, phospedados, pmenu):
		self._habitaciones = phabitaciones
		self._nombre = pnombre
		self.hospedados = phospedados
		self.menu = pmenu

	def hacerReservaciones(self, pcliente, phabitacion):
		print("Sr. ", pcliente, "\nUsted reservo la habitacion: ", phabitacion)

	def darHospedaje(self, pcliente):
		self._hacerLimpieza()
		return "Esta hospedado el cliente: ", pcliente

	def _hacerLimpieza(self):
		print("Estamos haciendo limpieza del hotel ", self._nombre, " y hoy el menu tiene ", self.menu)

class HabitacionHotel(Hotel):
	"""docstring for HabitacionHotel"""
	def __init__(self, ptipo, pcliente):
		self._tipo = ptipo
		self.cliente = pcliente

	def darHospedaje(self, pcliente):
		return "En esta habitacion esta el cliente ", self.cliente


def hospedaje(photelhabitacion, pcliente):
	print(photelhabitacion.darHospedaje(pcliente))

sanJuan = Hotel(20, "Hotal San Juan", 3, "Hoy hay buffet")
habitacion3 = HabitacionHotel("Doble", "Rodrigo Juarez Gatel")

hospedaje(habitacion3, "Rodrigo")
hospedaje(sanJuan, "Pedro Martinez")

print("Estas construyendo en el hotel")
sanJuan._habitaciones = 30
sanJuan.hospedados = 0

print("Las habitaciones disponibles ahora son: ", sanJuan._habitaciones)
sanJuan.hacerReservaciones("Timo Ruiz Ruiz",1)
print(sanJuan.darHospedaje("Juan Lopez Perez"))








