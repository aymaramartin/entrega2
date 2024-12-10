import json

class Cliente:
    def __init__(self, nombre, gmail, direccion, productos=None):
        """
        Constructor para inicializar los atributos de la clase Cliente.
        
        nombre: Nombre completo del cliente.
        gmail: Correo electrónico del cliente.
        direccion: Dirección del cliente.
        productos: Lista de productos comprados (por defecto vacío).
        """
        if productos is None:
            productos = []
        self.nombre = nombre
        self.gmail = gmail
        self.direccion = direccion
        self.productos = productos

    def __str__(self):
        """
        Método para dar una representación en cadena del objeto Cliente.
        
        muestra la información del cliente.
        """
        return f"Cliente: {self.nombre}\ngmail: {self.gmail}\nDirección: {self.direccion}\nProductos comprados: {', '.join(self.productos) if self.productos else 'Ninguno'}"

    def agregar_producto(self, producto):
        """
        Método para agregar un producto al historial de compras del cliente.
        
        Nombre del producto comprado.
        """
        self.productos.append(producto)

    def mostrar_historial_compras(self):
        """
        Método para mostrar el historial de compras del cliente.
        
        muestra los productos comprados o un mensaje si no ha comprado nada.
        """
        if self.productos:
            return f"Historial de compras de {self.nombre}: " + ", ".join(self.productos)
        else:
            return f"{self.nombre} no ha realizado compras aún."

    def guardar_datos(self):
        """
        Guarda los datos del cliente en un archivo JSON.
        """
        cliente_data = {
            'nombre': self.nombre,
            'gmail': self.gmail,
            'direccion': self.direccion,
            'productos': self.productos
        }
        return cliente_data

class ClienteVIP(Cliente):
    def __init__(self, nombre, gmail, direccion, productos=None, descuento=0.0):
        """
        inicializar los atributos de la clase ClienteVIP.
        
        Descuento en compras (porcentaje).
        """
        super().__init__(nombre, gmail, direccion, productos)
        self.descuento = descuento

    def __str__(self):
        """
        Sobreescribimos el __str__ para agregar el descuento en la representación del cliente VIP.
        """
        return f"{super().__str__()}\nDescuento VIP: {self.descuento}%"

    def aplicar_descuento(self, precio):
        """
        Aplica el descuento en el precio de un producto o total de la compra.
        
        precio: el precio original.
        muestra el precio después de aplicar el descuento.
        """
        return precio - (precio * self.descuento / 100)

    def guardar_datos(self):
        """
        Guarda los datos del cliente VIP, incluyendo el descuento.
        """
        cliente_data = super().guardar_datos()
        cliente_data['descuento'] = self.descuento
        return cliente_data
