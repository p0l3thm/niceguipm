from nicegui import ui

# Funciones
def sumar():
        n1 = float(num1.value)
        n2 = float(num2.value)
        res = n1 + n2
        resultado.set_text(f'Resultado: {res}')

def restar():
        n1 = float(num1.value)
        n2 = float(num2.value)
        res = n1 - n2
        resultado.set_text(f'Resultado: {res}')

def multiplicar():
        n1 = float(num1.value)
        n2 = float(num2.value)
        res = n1 * n2
        resultado.set_text(f'Resultado: {res}')

def dividir():
        n1 = float(num1.value)
        n2 = float(num2.value)
        if n2 != 0:
                res = n1 / n2
                resultado.set_text(f'Resultado: {res}')
        else:
                resultado.set_text('Error: División por cero')  

# Estructuras de la interfaz de usuario
with ui.card().classes('w-60 m-auto p-4'):
        ui.label('Calculadora').classes("font-sans w-full text-center")
        with ui.row().classes('w-full items-center'):
                num1 = ui.input('Número 1').classes('w-full')
                num2 = ui.input('Número 2').classes('w-full')
        with ui.row().classes('w-full mt-2 gap-2'):
                bt_sumar = ui.button('Sumar').classes('w-full bg-blue-500 text-white flex-1').on('click', sumar)
                bt_restar = ui.button('Restar').classes('w-full bg-blue-500 text-white flex-1').on('click', restar)
        with ui.row().classes('w-full gap-2 mt-2'):
                bt_multiplicar = ui.button('Multiplicar').classes('w-full bg-blue-500 text-white flex-1').on('click', multiplicar)
                bt_dividir = ui.button('Dividir').classes('w-full bg-blue-500 text-white flex-1').on('click', dividir)
                resultado = ui.label('Resultado: ').classes('w-full text-center mt-4')


ui.run()