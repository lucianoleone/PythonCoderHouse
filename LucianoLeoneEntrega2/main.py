from cliente import Cliente

## Crear una clase Cliente:
#     - Minimo 4 atributosde los cuales 2 tienen que ser de instancia
#     - Metodo "__str__"
#     - Metodo "__init__"
#     - 2 metodos a eleccion
# - Esta clase va a estar en un modulo dentro de un paquete
# - Crear un archivo que haga uso de la clase Cliente

# - Crear el paquete redistribuible que se usa para el modelo de la clase.
# - Guardar este archivo y el .tar.gz creado en un archivo comprimido que tenga como nombre "LucianoLeoneEntrega2.zip"

import re

# Lista para almacenar los clientes creados
clientes = []

def validar_nombre(nombre):
    return nombre.isalpha()

def validar_email(email):
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(patron, email)

def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) >= 7

def crear_cliente():
    print("\n--- Crear nuevo cliente ---")
    while True:
        nombre = input("Nombre: ").strip()
        if validar_nombre(nombre):
            break
        print("Nombre inválido. Debe contener solo letras.")
    
    while True:
        apellido = input("Apellido: ").strip()
        if validar_nombre(apellido):
            break
        print("Apellido inválido. Debe contener solo letras.")
    
    while True:
        email = input("Email: ").strip()
        if validar_email(email):
            break
        print("Email inválido. Intente de nuevo.")
    
    while True:
        telefono = input("Teléfono: ").strip()
        if validar_telefono(telefono):
            break
        print("Teléfono inválido. Solo números y mínimo 7 dígitos.")
    
    nuevo_cliente = Cliente(nombre, apellido, email, telefono)
    clientes.append(nuevo_cliente)
    print("\n✅ Cliente creado exitosamente!\n")

def mostrar_clientes():
    print("\n--- Lista de clientes ---")
    if not clientes:
        print("No hay clientes registrados.")
    else:
        for i, cliente in enumerate(clientes, start=1):
            print(f"\nCliente #{i}")
            print(cliente)
    print(f"\nTotal de clientes: {Cliente.cantidad_clientes}\n")

def actualizar_cliente():
    print("\n--- Actualizar cliente ---")
    nombre = input("Ingrese el nombre del cliente: ").strip().lower()
    apellido = input("Ingrese el apellido del cliente: ").strip().lower()

    # Buscar cliente
    for cliente in clientes:
        if cliente.nombre.lower() == nombre and cliente.apellido.lower() == apellido:
            print("\nCliente encontrado:")
            print(cliente)
            print("\n¿Qué desea actualizar?")
            print("1. Email")
            print("2. Teléfono")
            opcion = input("Seleccione una opción: ").strip()

            if opcion == '1':
                nuevo_email = input("Nuevo email: ").strip()
                if validar_email(nuevo_email):
                    cliente.actualizar_email(nuevo_email)
                    print("✅ Email actualizado correctamente.")
                else:
                    print("❌ Email inválido.")
            elif opcion == '2':
                nuevo_tel = input("Nuevo teléfono: ").strip()
                if validar_telefono(nuevo_tel):
                    cliente.actualizar_telefono(nuevo_tel)
                    print("✅ Teléfono actualizado correctamente.")
                else:
                    print("❌ 0Teléfono inválido.")
            else:
                print("❌ Opción inválida.")
            return

    print("❌ Cliente no encontrado.")

def buscar_cliente():
    print("\n--- Buscar cliente por nombre ---")
    nombre_busqueda = input("Ingrese el nombre a buscar: ").strip().lower()
    encontrados = [c for c in clientes if c.nombre.lower() == nombre_busqueda]

    if encontrados:
        print(f"\n🔎 Se encontraron {len(encontrados)} cliente(s):")
        for c in encontrados:
            print("\n", c)
    else:
        print("❌ No se encontró ningún cliente con ese nombre.\n")

def menu():
    while True:
        print("=== MENÚ CLIENTES ===")
        print("1. Crear nuevo cliente")
        print("2. Mostrar todos los clientes")
        print("3. Buscar cliente por nombre")
        print("4. Actualizar email o teléfono de un cliente")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            crear_cliente()
        elif opcion == '2':
            mostrar_clientes()
        elif opcion == '3':
            buscar_cliente()
        elif opcion == '4':
            actualizar_cliente()
        elif opcion == '5':
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.\n")

if __name__ == "__main__":
    menu()
