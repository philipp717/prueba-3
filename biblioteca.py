import json

def base_de_datos():
    {
    "Autor": [
        {
            "AutorID": 1,
            "Nombre": "Gabriel Garc\u00eda M\u00e1rquez",
            "Nacionalidad": "Ecuador"
        },
        {
            "AutorID": 2,
            "Nombre": "Isabel Allende",
            "Nacionalidad": "Austria"
        },
        {
            "AutorID": 3,
            "Nombre": "Julio Cort\u00e1zar",
            "Nacionalidad": "Kuwait"
        },
        {
            "AutorID": 4,
            "Nombre": "Mario Vargas Llosa",
            "Nacionalidad": "Micronesia"
        },
        {
            "AutorID": 5,
            "Nombre": "Carlos Ruiz Zaf\u00f3n",
            "Nacionalidad": "Equatorial Guinea"
        },
        {
            "AutorID": 6,
            "Nombre": "Jorge Luis Borges",
            "Nacionalidad": "China"
        },
        {
            "AutorID": 7,
            "Nombre": "Miguel de Cervantes",
            "Nacionalidad": "Brazil"
        },
        {
            "AutorID": 8,
            "Nombre": "Pablo Neruda",
            "Nacionalidad": "Guinea"
        },
        {
            "AutorID": 9,
            "Nombre": "Federico Garc\u00eda Lorca",
            "Nacionalidad": "Micronesia"
        },
        {
            "AutorID": 10,
            "Nombre": "Octavio Paz",
            "Nacionalidad": "Belize"
        },
        {
            "AutorID": 11,
            "Nombre": "Gabriel Garc\u00eda M\u00e1rquez",
            "Nacionalidad": "Iceland"
        },
        {
            "AutorID": 12,
            "Nombre": "Isabel Allende",
            "Nacionalidad": "Ukraine"
        },
        {
            "AutorID": 13,
            "Nombre": "Julio Cort\u00e1zar",
            "Nacionalidad": "Western Sahara"
        },
        {
            "AutorID": 14,
            "Nombre": "Mario Vargas Llosa",
            "Nacionalidad": "Indonesia"
        },
        {
            "AutorID": 15,
            "Nombre": "Carlos Ruiz Zaf\u00f3n",
            "Nacionalidad": "Croatia"
        },
        {
            "AutorID": 16,
            "Nombre": "Jorge Luis Borges",
            "Nacionalidad": "Moldova"
        },
        {
            "AutorID": 17,
            "Nombre": "Miguel de Cervantes",
            "Nacionalidad": "Bahrain"
        },
        {
            "AutorID": 18,
            "Nombre": "Pablo Neruda",
            "Nacionalidad": "Iraq"
        },
        {
            "AutorID": 19,
            "Nombre": "Federico Garc\u00eda Lorca",
            "Nacionalidad": "Cayman Islands"
        },
        {
            "AutorID": 20,
            "Nombre": "Octavio Paz",
            "Nacionalidad": "Cocos (Keeling) Islands"
        }
    ],
    "Categoria": [
        {
            "CategoriaID": 1,
            "Nombre": "Ficci\u00f3n"
        },
        {
            "CategoriaID": 2,
            "Nombre": "Realismo M\u00e1gico"
        },
        {
            "CategoriaID": 3,
            "Nombre": "Novela"
        },
        {
            "CategoriaID": 4,
            "Nombre": "Poes\u00eda"
        },
        {
            "CategoriaID": 5,
            "Nombre": "Teatro"
        },
        {
            "CategoriaID": 6,
            "Nombre": "Ensayo"
        },
        {
            "CategoriaID": 7,
            "Nombre": "Historia"
        },
        {
            "CategoriaID": 8,
            "Nombre": "Biograf\u00eda"
        },
        {
            "CategoriaID": 9,
            "Nombre": "Ciencia Ficci\u00f3n"
        },
        {
            "CategoriaID": 10,
            "Nombre": "Fantas\u00eda"
        },
        {
            "CategoriaID": 11,
            "Nombre": "Literatura Cl\u00e1sica"
        },
        {
            "CategoriaID": 12,
            "Nombre": "Cuento"
        }
    ],
    "Libro": [
        {
            "LibroID": 1,
            "Titulo": "Cien A\u00f1os de Soledad",
            "AutorID": 1,
            "CategoriaID": 6,
            "AnoPublicacion": 1937,
            "ISBN": "978-0-388-65180-3"
        },
        {
            "LibroID": 2,
            "Titulo": "La Casa de los Esp\u00edritus",
            "AutorID": 2,
            "CategoriaID": 6,
            "AnoPublicacion": 1919,
            "ISBN": "978-1-950410-01-9"
        },
        {
            "LibroID": 3,
            "Titulo": "Rayuela",
            "AutorID": 3,
            "CategoriaID": 9,
            "AnoPublicacion": 1986,
            "ISBN": "978-1-5347-6367-8"
        },
        {
            "LibroID": 4,
            "Titulo": "La Ciudad y los Perros",
            "AutorID": 4,
            "CategoriaID": 11,
            "AnoPublicacion": 1931,
            "ISBN": "978-1-5467-2222-9"
        },
        {
            "LibroID": 5,
            "Titulo": "La Sombra del Viento",
            "AutorID": 5,
            "CategoriaID": 1,
            "AnoPublicacion": 1941,
            "ISBN": "978-1-919794-21-1"
        },
        {
            "LibroID": 6,
            "Titulo": "Ficciones",
            "AutorID": 6,
            "CategoriaID": 1,
            "AnoPublicacion": 1979,
            "ISBN": "978-0-8493-3305-7"
        },
        {
            "LibroID": 7,
            "Titulo": "Don Quijote de la Mancha",
            "AutorID": 7,
            "CategoriaID": 3,
            "AnoPublicacion": 2019,
            "ISBN": "978-1-155-07917-2"
        },
        {
            "LibroID": 8,
            "Titulo": "Veinte Poemas de Amor y una Canci\u00f3n Desesperada",
            "AutorID": 8,
            "CategoriaID": 9,
            "AnoPublicacion": 1953,
            "ISBN": "978-1-317-82715-3"
        },
        {
            "LibroID": 9,
            "Titulo": "Bodas de Sangre",
            "AutorID": 9,
            "CategoriaID": 10,
            "AnoPublicacion": 1991,
            "ISBN": "978-0-427-52918-6"
        },
        {
            "LibroID": 10,
            "Titulo": "El Laberinto de la Soledad",
            "AutorID": 10,
            "CategoriaID": 8,
            "AnoPublicacion": 1997,
            "ISBN": "978-0-8341-7859-5"
        },
        {
            "LibroID": 11,
            "Titulo": "El Amor en los Tiempos del C\u00f3lera",
            "AutorID": 11,
            "CategoriaID": 9,
            "AnoPublicacion": 1999,
            "ISBN": "978-1-61878-398-1"
        },
        {
            "LibroID": 12,
            "Titulo": "Eva Luna",
            "AutorID": 12,
            "CategoriaID": 7,
            "AnoPublicacion": 2013,
            "ISBN": "978-1-70770-142-1"
        },
        {
            "LibroID": 13,
            "Titulo": "Bestiario",
            "AutorID": 13,
            "CategoriaID": 7,
            "AnoPublicacion": 1943,
            "ISBN": "978-1-4471-5171-5"
        },
        {
            "LibroID": 14,
            "Titulo": "La Fiesta del Chivo",
            "AutorID": 14,
            "CategoriaID": 5,
            "AnoPublicacion": 2015,
            "ISBN": "978-1-881360-19-3"
        },
        {
            "LibroID": 15,
            "Titulo": "El Juego del \u00c1ngel",
            "AutorID": 15,
            "CategoriaID": 5,
            "AnoPublicacion": 1940,
            "ISBN": "978-1-361-67728-5"
        },
        {
            "LibroID": 16,
            "Titulo": "El Aleph",
            "AutorID": 16,
            "CategoriaID": 10,
            "AnoPublicacion": 1927,
            "ISBN": "978-1-56793-349-9"
        },
        {
            "LibroID": 17,
            "Titulo": "Novelas Ejemplares",
            "AutorID": 17,
            "CategoriaID": 12,
            "AnoPublicacion": 1926,
            "ISBN": "978-0-05-625482-4"
        },
        {
            "LibroID": 18,
            "Titulo": "Residencia en la Tierra",
            "AutorID": 18,
            "CategoriaID": 1,
            "AnoPublicacion": 1978,
            "ISBN": "978-0-689-88688-1"
        },
        {
            "LibroID": 19,
            "Titulo": "La Casa de Bernarda Alba",
            "AutorID": 19,
            "CategoriaID": 6,
            "AnoPublicacion": 2015,
            "ISBN": "978-1-998513-16-1"
        },
        {
            "LibroID": 20,
            "Titulo": "Piedra de Sol",
            "AutorID": 20,
            "CategoriaID": 10,
            "AnoPublicacion": 1920,
            "ISBN": "978-0-8485-3333-5"
        }
    ],
    "Usuario": [
        {
            "UsuarioID": 1,
            "Nombre": "Derek George",
            "Email": "potterrebecca@yahoo.com",
            "FechaRegistro": "2022-12-11"
        },
        {
            "UsuarioID": 2,
            "Nombre": "Phillip Kirby",
            "Email": "jeffrey45@yahoo.com",
            "FechaRegistro": "2022-07-10"
        },
        {
            "UsuarioID": 3,
            "Nombre": "Dustin Snyder",
            "Email": "millerwilliam@gmail.com",
            "FechaRegistro": "2024-01-23"
        },
        {
            "UsuarioID": 4,
            "Nombre": "Thomas Livingston",
            "Email": "theresabray@webb-hicks.net",
            "FechaRegistro": "2023-04-26"
        },
        {
            "UsuarioID": 5,
            "Nombre": "Mark King",
            "Email": "ryanthomas@peck-schwartz.org",
            "FechaRegistro": "2024-02-12"
        },
        {
            "UsuarioID": 6,
            "Nombre": "Joshua Shannon",
            "Email": "bbarber@hotmail.com",
            "FechaRegistro": "2023-12-25"
        },
        {
            "UsuarioID": 7,
            "Nombre": "Kelly Bradley",
            "Email": "stonemichael@kim.info",
            "FechaRegistro": "2023-07-09"
        }
    ],
    "Prestamo": [
        {
            "PrestamoID": 1,
            "LibroID": 8,
            "UsuarioID": 7,
            "FechaPrestamo": "2023-11-21",
            "FechaDevolucion": "2023-12-18"
        },
        {
            "PrestamoID": 2,
            "LibroID": 20,
            "UsuarioID": 6,
            "FechaPrestamo": "2023-12-23",
            "FechaDevolucion": "2024-01-12"
        },
        {
            "PrestamoID": 3,
            "LibroID": 19,
            "UsuarioID": 2,
            "FechaPrestamo": "2024-01-24",
            "FechaDevolucion": "2024-02-08"
        },
        {
            "PrestamoID": 4,
            "LibroID": 5,
            "UsuarioID": 3,
            "FechaPrestamo": "2024-05-04",
            "FechaDevolucion": "2024-05-17"
        },
        {
            "PrestamoID": 5,
            "LibroID": 20,
            "UsuarioID": 7,
            "FechaPrestamo": "2023-09-22",
            "FechaDevolucion": "2023-10-19"
        },
        {
            "PrestamoID": 6,
            "LibroID": 8,
            "UsuarioID": 7,
            "FechaPrestamo": "2024-05-23",
            "FechaDevolucion": "2024-06-18"
        },
        {
            "PrestamoID": 7,
            "LibroID": 5,
            "UsuarioID": 2,
            "FechaPrestamo": "2023-06-18",
            "FechaDevolucion": "2023-07-09"
        },
        {
            "PrestamoID": 8,
            "LibroID": 8,
            "UsuarioID": 5,
            "FechaPrestamo": "2024-02-27",
            "FechaDevolucion": "2024-03-08"
        },
        {
            "PrestamoID": 9,
            "LibroID": 7,
            "UsuarioID": 4,
            "FechaPrestamo": "2024-06-09",
            "FechaDevolucion": "2024-06-21"
        },
        {
            "PrestamoID": 10,
            "LibroID": 16,
            "UsuarioID": 1,
            "FechaPrestamo": "2024-04-02",
            "FechaDevolucion": "2024-04-26"
        },
        {
            "PrestamoID": 11,
            "LibroID": 16,
            "UsuarioID": 1,
            "FechaPrestamo": "2024-05-22",
            "FechaDevolucion": "2024-06-19"
        },
        {
            "PrestamoID": 12,
            "LibroID": 8,
            "UsuarioID": 7,
            "FechaPrestamo": "2024-02-11",
            "FechaDevolucion": "2024-03-05"
        },
        {
            "PrestamoID": 13,
            "LibroID": 17,
            "UsuarioID": 6,
            "FechaPrestamo": "2023-08-30",
            "FechaDevolucion": "2023-09-15"
        },
        {
            "PrestamoID": 14,
            "LibroID": 8,
            "UsuarioID": 4,
            "FechaPrestamo": "2024-04-17",
            "FechaDevolucion": "2024-05-02"
        },
        {
            "PrestamoID": 15,
            "LibroID": 10,
            "UsuarioID": 4,
            "FechaPrestamo": "2023-09-23",
            "FechaDevolucion": "2023-10-07"
        },
        {
            "PrestamoID": 16,
            "LibroID": 12,
            "UsuarioID": 3,
            "FechaPrestamo": "2024-04-09",
            "FechaDevolucion": "2024-05-06"
        },
        {
            "PrestamoID": 17,
            "LibroID": 9,
            "UsuarioID": 4,
            "FechaPrestamo": "2023-08-23",
            "FechaDevolucion": "2023-09-08"
        },
        {
            "PrestamoID": 18,
            "LibroID": 14,
            "UsuarioID": 5,
            "FechaPrestamo": "2023-12-15",
            "FechaDevolucion": "2024-01-06"
        },
        {
            "PrestamoID": 19,
            "LibroID": 19,
            "UsuarioID": 3,
            "FechaPrestamo": "2024-04-15",
            "FechaDevolucion": "2024-04-28"
        },
        {
            "PrestamoID": 20,
            "LibroID": 5,
            "UsuarioID": 2,
            "FechaPrestamo": "2023-07-01",
            "FechaDevolucion": "2023-07-29"
        },
        {
            "PrestamoID": 21,
            "LibroID": 13,
            "UsuarioID": 2,
            "FechaPrestamo": "2024-01-24",
            "FechaDevolucion": "2024-02-17"
        },
        {
            "PrestamoID": 22,
            "LibroID": 11,
            "UsuarioID": 4,
            "FechaPrestamo": "2023-09-28",
            "FechaDevolucion": "2023-10-05"
        },
        {
            "PrestamoID": 23,
            "LibroID": 8,
            "UsuarioID": 4,
            "FechaPrestamo": "2023-07-11",
            "FechaDevolucion": "2023-08-02"
        },
        {
            "PrestamoID": 24,
            "LibroID": 20,
            "UsuarioID": 4,
            "FechaPrestamo": "2024-04-24",
            "FechaDevolucion": "2024-05-01"
        },
        {
            "PrestamoID": 25,
            "LibroID": 10,
            "UsuarioID": 2,
            "FechaPrestamo": "2023-08-01",
            "FechaDevolucion": "2023-08-27"
        },
        {
            "PrestamoID": 26,
            "LibroID": 5,
            "UsuarioID": 6,
            "FechaPrestamo": "2024-01-16",
            "FechaDevolucion": "2024-01-29"
        },
        {
            "PrestamoID": 27,
            "LibroID": 18,
            "UsuarioID": 3,
            "FechaPrestamo": "2023-09-19",
            "FechaDevolucion": "2023-10-02"
        },
        {
            "PrestamoID": 28,
            "LibroID": 5,
            "UsuarioID": 4,
            "FechaPrestamo": "2023-10-27",
            "FechaDevolucion": "2023-11-14"
        },
        {
            "PrestamoID": 29,
            "LibroID": 6,
            "UsuarioID": 5,
            "FechaPrestamo": "2023-08-31",
            "FechaDevolucion": "2023-09-21"
        },
        {
            "PrestamoID": 30,
            "LibroID": 6,
            "UsuarioID": 2,
            "FechaPrestamo": "2023-06-21",
            "FechaDevolucion": "2023-07-05"
        },
        {
            "PrestamoID": 31,
            "LibroID": 15,
            "UsuarioID": 6,
            "FechaPrestamo": "2023-08-15",
            "FechaDevolucion": "2023-09-03"
        },
        {
            "PrestamoID": 32,
            "LibroID": 8,
            "UsuarioID": 3,
            "FechaPrestamo": "2023-08-14",
            "FechaDevolucion": "2023-09-10"
        }
    ]
}

with open("base_de_datos.json" , "r") as archivo:
    escritura = json.load(base_de_datos, archivo)
