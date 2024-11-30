print(" ")
print("Alvaro Campechano 3W")
print(" ")
class Agenda:
    def __init__(self):
        # Inicializa una lista vacía para almacenar los contactos
        self.contactos = []
    
    def añadir_contacto(self, nombre, telefono, email):
        # Añade un nuevo contacto a la lista de contactos
        # :param nombre: Nombre del contacto (str)
        # :param telefono: Teléfono del contacto (str)
        # :param email: Correo electrónico del contacto (str)
        self.contactos.append({"Nombre": nombre, "Teléfono": telefono, "Email": email})
    
    def listar_contactos(self):
        # Imprime todos los contactos almacenados
        for contacto in self.contactos:
            # Muestra nombre, teléfono y email de cada contacto
            print(f"{contacto['Nombre']} - {contacto['Teléfono']} - {contacto['Email']}")
    
    def buscar_contacto(self, nombre):
        # Busca un contacto por nombre en la lista
        # :param nombre: Nombre del contacto a buscar (str)
        for contacto in self.contactos:
            if contacto['Nombre'] == nombre:
                # Si se encuentra, imprime los detalles del contacto
                print(f"Encontrado: {contacto}")
                return
        # Si no se encuentra el contacto, muestra un mensaje
        print("Contacto no encontrado.")
    
    def cerrar_agenda(self):
        # Muestra mensaje de cierre de la agenda
        print("Agenda cerrada.")

# Ejemplo de uso
agenda = Agenda()
agenda.añadir_contacto("Alvarito Estrada", "6561062807", "alvarito@gmail.com")  # Añade un contacto
agenda.listar_contactos()  # Lista todos los contactos
agenda.buscar_contacto("Alvarito Estrada")  # Busca un contacto específico
agenda.cerrar_agenda()  # Cierra la agenda
