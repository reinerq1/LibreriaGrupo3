from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import *


def index(request):
    return render(request, 'web/index.html')

def libros(request):
    libros = [
        {
            'imagen': 'web/images/Cien Años de Soledad - Gabriel García Márquez.webp',
            'nombre': 'Cien Años de Soledad ',
            'autor': 'Gabriel García Márquez',
            'precio': '1.000'
        },
        {
            'imagen': 'web/images/Cincuenta Sombras de Grey - E. L. James.webp',
            'nombre': 'Cincuenta Sombras de Grey',
            'autor': 'E. L. James',
            'precio': '2.000'
        },
        {
            'imagen': 'web/images/Diario de Ana Frank - Ana Frank.webp',
            'nombre': 'Diario de Ana Frank',
            'autor': 'Ana Frank',
            'precio': '3.000'
        },
        {
            'imagen': 'web/images/Don Quijote de la Mancha - Miguel de Cervantes.webp',
            'nombre': 'Don Quijote de la Mancha',
            'autor': 'Miguel de Cervantes',
            'precio': '4.000'
        },
        {
            'imagen': 'web/images/El Código Da Vinci - Dan Brown.webp',
            'nombre': 'El Código Da Vinci',
            'autor': 'Dan Brown',
            'precio': '5.000'
        },
        {
            'imagen': 'web/images/El Principito - Antoine de Saint-Exupéry.webp',
            'nombre': 'El Principito',
            'autor': 'Antoine de Saint-Exupéry',
            'precio': '6.000'
        },
        {
            'imagen': 'web/images/El Psicoanalista - John Katzenbach.webp',
            'nombre': 'El Psicoanalista',
            'autor': 'John Katzenbach',
            'precio': '7.000'
        },
        {
            'imagen': 'web/images/Harry Potter y la Piedra Filosofal - J. K. Rowling.webp',
            'nombre': 'Harry Potter y la Piedra Filosofal',
            'autor': 'J. K. Rowling',
            'precio': '8.000'
        },
        {
            'imagen': 'web/images/Rayuela - Julio Cortázar.webp',
            'nombre': 'Rayuela',
            'autor': 'Julio Cortázar',
            'precio': '9.000'
        },
        {
            'imagen': 'web/images/Romeo y Julieta - William Shakespeare.webp',
            'nombre': 'Romeo y Julieta',
            'autor': 'William Shakespeare',
            'precio': '10.000'
        }
    ]
    books_sorted = sorted(libros, key=lambda x: x['nombre'])

    contexto = {
        'libros': books_sorted,
    }
    return render(request, 'web/libros.html', contexto)

def contacto(request):

    contexto = {}

    if request.method == "GET":
        contexto['contato_forms'] = contactoForm()
    else: #Se asume que es un POST
        form = contactoForm(request.POST)
        contexto['contato_forms'] = form

        if form.is_valid(): 
            messages.success(request, 'Tu Mensaje fue enviado con éxito')
            return redirect('index')

    return render(request, 'web/contacto.html', contexto)