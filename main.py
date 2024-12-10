import json
from clientes.cliente import Cliente, ClienteVIP


def cargar_clientes():
    try:
        with open("archivo_clientes.json", "r") as archivo:
            clientes_data = json.load(archivo)
            clientes = []
            for data in clientes_data:
                if "descuento" in data:
                    cliente = ClienteVIP(data["nombre"], data["gmail"], data["direccion"], data["productos"], data["descuento"])
                else:
                    cliente = Cliente(data["nombre"], data["gmail"], data["direccion"], data["productos"])
                clientes.append(cliente)
            return clientes
    except FileNotFoundError:
        return []


def guardar_clientes(clientes):
    with open("archivo_clientes.json", "w") as archivo:
        clientes_data = [cliente.guardar_datos() for cliente in clientes]
        json.dump(clientes_data, archivo, indent=4)

def main():
   
    clientes = cargar_clientes()

  
    cliente1 = ClienteVIP("Juan Lopez", "juanLopez@gmail.com", "Calle Falsa 123", descuento=10.0)
    cliente2 = Cliente("María Gómez", "maria@gmail.com", "Avenida Siempre Viva 456")
    
    cliente1.agregar_producto("Laptop")
    cliente1.agregar_producto("Auriculares")
    cliente1.agregar_producto("Teclado")
    cliente1.agregar_producto("Mouse")
    
    cliente2.agregar_producto("Smartphone")
    cliente2.agregar_producto("Auriculares")
    cliente2.agregar_producto("Cargador")
    cliente2.agregar_producto("Funda")

    print(cliente1)
    print(cliente2)

    
    precio_laptop = 850
    precio_descuento = cliente1.aplicar_descuento(precio_laptop)
    print(f"Precio de la laptop para {cliente1.nombre}: {precio_descuento} USD")
    

    clientes.append(cliente1)
    clientes.append(cliente2)
    guardar_clientes(clientes)

 
    print(cliente1.mostrar_historial_compras())
    print(cliente2.mostrar_historial_compras())

if __name__ == "__main__":
    main()
