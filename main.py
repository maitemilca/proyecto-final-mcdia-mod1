import os
from time import sleep
from utils import Colors, clear_screen, get_option
from controllers import ImageController
from metadata import MetadataManager
from files import excel_merge as excmerge
from files import excel_reader as excreader


image_controller = ImageController()
metadata_manager = MetadataManager()

def menu():
    while True:
        clear_screen()
        print(Colors.BLUE + "="*50 + Colors.RESET)
        print(Colors.BOLD + Colors.CYAN + "SISTEMA DE GESTIÓN DE IMÁGENES".center(50) + Colors.RESET)
        print(Colors.BLUE + "="*50 + Colors.RESET)
        print()
        print(Colors.YELLOW + "MENÚ PRINCIPAL" + Colors.RESET)
        print("1. Registrar nueva imagen")
        print("2. Modificar imagen")
        print("3. Eliminar imagen")
        print("4. Listar imágenes")
        print(Colors.RED + "0. " + Colors.RESET + "Salir")
        print(Colors.BLUE + "-"*50 + Colors.RESET)

        option = get_option()
        
        if option == 1:
            print()
            name = input("Nombre de la imagen: ").strip()
            route = image_controller.add_image(name)
           
            # metadata_manager.insert('Sheet1', {
            #'FILE NAME': 'COVID-XYZ', 
            #'FORMAT': 'JPG', 
            #'SIZE': '128x128', 
            #'URL': 'https://example.org/covid-img'
            #})
            if route:
                print(Colors.GREEN + f"Imagen: '{name}' registrada correctamente!\nRuta1: {route[0]}\nRuta2: {route[1]}" + Colors.RESET)
            else:
                print(Colors.RED + "No se pudo registrar la imagen" + Colors.RESET)
            sleep(1)
            input("\nPresione Enter para volver al menú principal...")
        elif option == 2:
            print()
            id_image = int(input("Ingrese el 'ID' de la imagen a modificar: "))
            name = input("Nuevo nombre de la imagen: ")
            
            if image_controller.modify_image(id_image, name):
              #metadata_manager.modify('Metadata', 0, 'FORMAT', 'PNG')
               print(Colors.GREEN + f"Imagen renombrada a '{name}' correctamente!" + Colors.RESET)
            else:
                print(Colors.RED + "Error: Imagen no encontrada." + Colors.RESET)
            sleep(1)
            input("\nPresione Enter para volver al menú principal...")
        elif option == 3:
            print()
            id_imagen = int(input("Ingrese el 'ID' de la imagen a eliminar: "))

            if image_controller.delete_image(id_imagen):
                #metadata_manager.delete('Metadata', 2)
                print(Colors.GREEN + f"Imagen con ID '{id_imagen}' eliminada correctamente!" + Colors.RESET)
            else:
                print(Colors.RED + "Error: Imagen no encontrada." + Colors.RESET)
            sleep(1)
            input("\nPresione Enter para volver al menú principal...")
        elif option == 4:
            print("Lista de imágenes:")
            image_controller.list_images()
            #for r in metadata_manager.listar('Metadata')[:5]:
            #print(r)
            sleep(1)
            input("\nPresione Enter para volver al menú principal...")
        elif option == 0:
            print(Colors.YELLOW + "\nSaliendo del sistema..." + Colors.RESET)
            sleep(1)
            print(Colors.GREEN + "¡Hasta pronto!" + Colors.RESET)
            sleep(1)
            clear_screen()
            break
        else:
            print(Colors.RED +"Opción no válida, por favor intente nuevamente"+ Colors.RESET)


if __name__ == "__main__":

    directory = "dataset"
    print (os.path.join(directory, "COVID.metadata"))

    files = [
    os.path.join(directory, "COVID.metadata"),
    os.path.join(directory, "Lung_Opacity.metadata"),
    os.path.join(directory, "Normal.metadata"),
    os.path.join(directory, "Viral_Pneumonia.metadata")
    ]
    
    #excmerge.merge_excels(files, os.path.join(directory, "metadata.xlsx") )
    #excreader.load_file_to_dict( os.path.join(directory, "COVID.metadata") )
    menu()
