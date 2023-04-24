import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")


db = client["diccionario"]


palabras = db["palabras"]


def menu():
    print("=== Diciconario Paname;o===")
    print("1. Insertar una palabra")
    print("2. Editar una palabra")
    print("3. Eliminar una palabra")
    print("4. Mostrar todas las palabras")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion


def insertar_palabra():
    palabra = input("Ingrese la palabra a insertar: ")
    significado = input("Ingrese el significado de la palabra: ")
    palabras.insert_one({"palabra": palabra, "significado": significado})
    print("La palabra se ha insertado correctamente.")


def editar_palabra():
    palabra = input("Ingrese la palabra a editar: ")
    significado = input("Ingrese el nuevo significado de la palabra: ")
    palabras.update_one({"palabra": palabra}, {"$set": {"significado": significado}})
    print("La palabra se ha editado correctamente.")


def eliminar_palabra():
    palabra = input("Ingrese la palabra a eliminar: ")
    palabras.delete_one({"palabra": palabra})
    print("La palabra se ha eliminado correctamente.")


def mostrar_palabras():
    # Obtener todas las palabras en la colección
    palabras = db.palabras.find()

    # Contar el número de documentos en la colección
    count = db.palabras.count_documents({})

    if count > 0:
        print(f"\nHay {count} palabras en el diccionario:")
        for palabra in palabras:
            print(f"{palabra['palabra']} - {palabra['significado']}")
    else:
        print("\nNo hay palabras en el diccionario.")

while True:
    opcion = menu()

    if opcion == "1":
        insertar_palabra()
    elif opcion == "2":
        editar_palabra()
    elif opcion == "3":
        eliminar_palabra()
    elif opcion == "4":
        mostrar_palabras()
    elif opcion == "5":
        print("Hasta luego.")
        break
    else:
        print("Opción inválida.")
