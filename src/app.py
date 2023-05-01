

x = 5
y = 6

def sum(x,y):
    return x + y

print( "La suma de "+ str(x) +" y "+ str(y) +" da como resultado " + str(sum(x,y)) )


shopping_car = [
    {
        "brand": "ACER",
        "item": "ACER ASPIRE 5 Ci3-10110U - 4GB - 256GB-SSD - 15.6 - W11",
        "type": "laptop",
        "year": 2022,
        "description": """  Sistema operativo  -   Windows 11
                            Procesador  -   Intel® Core™ i3-10110U  1,90 GHz  4 núcleos™
                            Gráficos  -   Gráficos UHD
                            Tipo de Pantalla  -   LCD
                            Memoria  -   4GB SDRAM DDR4
                            Almacenamiento  -   256GB PCI-Express
                            Tipo de Unidad Óptica  -   No
                            WiFi  -   AX201
                            Estándar Bluetooth  -   bluetooth 4.2
                            Micrófono  -   Si
                            Lector de huellas digitales  -   No
                            Número de Altavoces  -   2
                            Interfaces/Puertos  -   HDMIx1 / USB 2.0x1 / USB 3.1 Gen 1 Tipo-Ax2 / USB 3.1 Gen 1 Tipo-Cx1
                            Características Físicas  -   Altura 17,95 mm x Ancho 363,4 mm x Profundidad 250,5 mm
                            Peso (aproximado)  -   1,90 kg
                        """,
        "cost": 179000
    },
     {
        "brand": "Logitech",
        "item": "Mouse Pad Logitech Serie Studio - Lila",
        "type": "Mouse Pad",
        "year": 2023,
        "description": """  TU ESPACIO DE TRABAJO. BIEN DEFINIDO.
                            Mira cómo es el accesorio que mejora tu espacio de trabajo y complementa perfectamente tus herramientas Logitech. Consigue esa nota de color que agradece tanto tu entorno, el confort que necesitas y la protección de tu mesa de trabajo.
                            OPTIMIZA TU ESPACIO
                            Mejora tu espacio y protege tu escritorio. La alfombrilla de tela suave proporciona estilo y comodidad.
                            RESISTENTE A SALPICADURAS
                            La alfombrilla de escritorio Logitech posee un recubrimiento a prueba de salpicaduras que resiste posibles percances, limpiar fácilmente líquidos derramados.
                            Dimensiones
                            Alfombrilla de escritorio
                            Altura: 300 mm
                            Ancho: 700 mm
                            Grosor: 2 mm
                            pesos: 286 gramos
                        """,
        "cost": 11500
    },
]

def _sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i['cost']

    return(sum)

print("Total de productos en el carrito"+str(len(shopping_car))+" monto a pagar "+ str( _sum(shopping_car) ))