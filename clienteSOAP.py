#!/usr/bin/env python

from suds.client import Client
from os import system, name

def main():
    url = "http://localhost:7000/ws/AcademicoWebService?wsdl"
    client = Client(url)
    consultar(client)

def consultar(client):
    string = '\nConsulta con SOAP\n\n1 - Listar Estudiantes\n2 - Consultar Estudiante\n3 - Crear Estudiante\n4 - Borrar Estudiante\n5 - Salir \n'
    res = 0
    while res != 5: 

        print(string)
        res = int(input('Ingrese la opcion deseada: '))

        if res > 0 and res < 6:
            if res == 1:
                listar(client)
            if res == 2:
                buscar(client)
            if res == 3:
                agregar(client)
            if res == 4:
                borrar(client)
        else:
            print('\n\nOpcion invalida!! Intente de nuevo')

        

def listar(client):
    estudiantes = client.service.getListaEstudiante()
    print('\n\nListado de estudiantes: \n' + str(estudiantes))
    return

def buscar(client):
    mat = int(input('\nIngrese la matricula del estudiante que sea buscar: '))
    estudiante = client.service.getEstudiante(mat)

    print(estudiante)

def agregar(client):
    print('\n\n Ingrese los datos del estudiante\n')
    mat = int(input('Matricula: '))
    nombre = input('Nombre: ')
    carrera = input('Carrera: ')

    estudiante = client.factory.create('estudiante')
    estudiante.matricula = mat
    estudiante.nombre = nombre
    estudiante.carrera = carrera

    client.service.crearEstudiante(estudiante)
    print('\nSe registro al estudainte')

def borrar(client):
    mat = int(input('\nIngrese la matricula del estudiante que desea eliminar: '))
    client.service.borrarEstudiante(mat)

    print('Estudiante eliminado')




main()


