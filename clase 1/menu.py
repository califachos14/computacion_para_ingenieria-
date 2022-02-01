# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:50:52 2022

@author: Diego Lima
"""
"""
Crear un programa que registre nuevos alumno, liste los actuales alumno
borre un alumno , el alumno tiene nombre y apellido

"""
# crear una list
list = []

salir = False
while salir !=True:
    print("---------------Menu--------------------")
    print("1.- Listar Alumnos")
    print("2.- Registrar Alumno")
    print("3.-quitar alumno")
    print("4.- Salir")
    print("-----------------------------------")
    
    
    
    option = int(input("Seleccione una Opcion [1-2-3]:"))
    
    ## opcion 1 list alumno
    if option == 1:
        # muestro los alumnos
        print ("La list de alumno es:")
        for alumno in list:
            print (alumno)
    # opcion 2 agregar alumno
    elif option == 2:
        new_alumno = input("Ingrese Nombre Completo de Alumno:")
        list.append(new_alumno)
    elif option == 3:
        quitar_alumno = input ("ingresar el nombre del alumno que se quitara:")
        list . remover(quitar_alumno)
        print ("se quito de la lista a:", quitar_alumno)
    elif option == 4:
        print ("bye!")
        salir = True
    else:
       print("Porfavor ingrese una opcion valida [1, 2 , 3]")
        
        
print (f'la opcion seleccionada es : {option}')
