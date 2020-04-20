#Repaso de POO para la evaluacion del 3er parcial

class Hotel(object):
	"""docstring for Hotel"""

	__permisoComercio = True

	def __init__(self, phabitaciones, pnombre, pdireccion, phospedados):
		self._habitaciones = phabitaciones
		self._nombre = pnombre
		self._direccion = pdireccion
		self.hospedados = phospedados

	def hacerReservaciones(self, pnombreCliente, pNoHabitacion):
		self.__hacerLimpieza()
		print("En el hotel ", self._nombre, "\nEl cliente ", pnombreCliente, "\nReservo la habitacion ", pNoHabitacion)

	def darHospedaje(self, pnombreCliente):
		self.__hacerLimpieza()
		return "El hotel esta dando hospedaje al cliente ", pnombreCliente

	def __hacerLimpieza(self):
		print("Haciendo limpieza en el hotel ", self._nombre, " en las ", self._habitaciones, " habitaciones")


class Habitacion(Hotel):
	"""docstring for Habitacion"""
	def __init__(self, ptipo, pnumero):
		self._tipo = ptipo
		self._numero = pnumero

	def darHospedaje(self, pnombreCliente):
		return "La habitacion de numero ", self._numero, " hospeda al cliente ", pnombreCliente

def hospedar(pHabitacionHotel, pCliente):
	print(pHabitacionHotel.darHospedaje(pCliente))

hotelHernandez = Hotel(30, "Hotel Hernandez", "Libramiento Sur #267", 7)
habitacion22 = Habitacion("Doble", 22)

hospedar(hotelHernandez, "Laura Merlos Hinojosa")
hospedar(habitacion22, "Juan Luis Perez Gonzalez")

hotelHernandez.hacerReservaciones("Juan Pedro Gracia Luna", 8)
print(hotelHernandez.darHospedaje("Pablo Hernandez Garcia"))


