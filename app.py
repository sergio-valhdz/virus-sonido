from utils.persitence.funtcions import run_at_startup_set,run_script_at_startup_set,run_at_startup_remove

opcion = input("Selecciones una opción \n1)Configurar la clave\n2)Correr scripts\n3)Eliminar el programa\n")

if opcion == '1':
    run_at_startup_set("antivirus",r"E:\Sergio\Documentos\Programacion\Python\Ejercicios\Virus\matrix.bat")

elif  opcion =='2':
    run_script_at_startup_set("Reproducir sonido",r"E:\Sergio\Documentos\Programacion\Python\Ejercicios\Virus\utils\sounds\nya.py")

elif  opcion=='3':
    run_at_startup_remove("antivirus")

else:
    print("No existe")