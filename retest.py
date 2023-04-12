import dearpygui.dearpygui as dpg

from clases.speedCommons import *
from clases.structures import *
import traceback


dpg.create_context()

dpg.set_global_font_scale(1.2)
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvWindowAppItem):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (200, 200, 200), category=dpg.mvThemeCat_Core)
with dpg.theme() as disabled_theme:
    with dpg.theme_component(dpg.mvButton, enabled_state=False):
        dpg.add_theme_color(dpg.mvThemeCol_Button, [37, 37, 38])
dpg.bind_theme(disabled_theme)

#Fotos
with dpg.texture_registry():
    w, h, c, data = dpg.load_image("resources/Logo.png") # 0: width, 1: height, 2: channels, 3: data
    dpg.add_static_texture(w, h, data, tag="Logo")
    w, h, c, data = dpg.load_image("resources/Victoria.png") # 0: width, 1: height, 2: channels, 3: data
    dpg.add_static_texture(w, h, data, tag="Victoria")
    
# Creamos una instancia de la clase Hashiwokakero y cargamos la matriz de nodos
hashi = Hashiwokakero()
solicitud = Solicitud()
returnValue = ""
#Pop Ups
with dpg.window(no_title_bar=True,modal=True,show=False,tag="modal_id"):
                 dpg.add_text("Error de Carga")
                 dpg.add_separator()
                 dpg.add_spacer(height=10)
                 dpg.add_text("Se ha producido un error al intentar cargar el archivo, porfavor revise e intente de nuevo.")
                 dpg.add_spacer(height=10)
                 dpg.add_button(label="Close", callback=lambda: dpg.configure_item("modal_id", show=False))
#Pop Ups
def end():
     exit()
with dpg.window(no_title_bar=True,modal=True,show=False,tag="Ganaste"):
                 dpg.add_separator()
                 dpg.add_spacer(height=10)
                 with dpg.drawlist(width=400, height=200):
                    dpg.draw_image("Victoria",(0, 0), (700, 200), uv_min=(0, 0), uv_max=(1, 1))
                 dpg.add_spacer(height=10)
                 dpg.add_separator()
                 dpg.add_button(label="Close", callback=lambda: end())
# definimos una función que crea una ventana emergente para cada mensaje de error
def create_popup(name, message):
    def popup():
        dpg.add_window(no_title_bar=True,modal=True,show=True,tag=name)
        dpg.add_text(message,parent=name)
        dpg.add_button(label="Aceptar", callback=lambda:dpg.delete_item(name),parent=name)
    return popup

# definimos el diccionario
DICPOPUPS = {
    -1: create_popup("PuntosNoEstanEnMismaFilaOColuma", "Los puntos no están en la misma fila o columna."),
    -2: create_popup("CaminoBloqueado", "Camino bloqueado."),
    -3: create_popup("MaximoPuentesPuntoOrigen", "Máximo de puentes en el punto de origen."),
    -4: create_popup("MaximoPuentesPuntoDestino", "Máximo de puentes en el punto de destino."),
    -5: create_popup("SeleccionaIslaObjetivoValida", "Selecciona una isla objetivo válida."),
    -6: create_popup("NoSeleccionasteIslaInicialValida", "No seleccionaste una isla inicial válida."),
    1: create_popup("Exito", "Islas Conectadas con exito.")
}
#Funciones
def cargarMatriz():
        inputValue = dpg.get_value("Input")
        try:
            if hashi.created:
                n=len(hashi.Matriz)
                for i in range(n):
                        for j in range(n):
                            dpg.delete_item(f"{i}{j}")
            hashi.convertir(inputValue)
            n=len(hashi.Matriz)
            for i in range(n):
                    with dpg.group(horizontal=True,parent="VHashiGroup"):
                        for j in range(n):
                            enable=True
                            if not isinstance(hashi.Matriz[i][j].Dato,int):
                                 enable=False
                            id=f"{i}{j}"
                            dpg.add_button(tag=id,label=f"{hashi.Matriz[i][j].Dato}", width=30, height=30,track_offset=0.5,enabled=enable,callback=lambda sender: procesarIsla(sender))
                            with dpg.tooltip(id):
                                dpg.add_text(id)
            hashi.created=True
        except:
            traceback.print_exc()
            dpg.configure_item("modal_id", show=True)
def procesarIsla(sender):
    x=int(sender[0])
    y=int(sender[1])
    print("presionaste ",x,y)
    if solicitud.x1==-1 and solicitud.y1==-1:
            solicitud.x1=x
            solicitud.y1=y
    elif solicitud.x2==-1 and solicitud.y2==-1:
            solicitud.x2=x
            solicitud.y2=y
    print("Solicitud vale ahora mismo: ",solicitud.x1,solicitud.y1,solicitud.x2,solicitud.y2)
    if solicitud.validate():
       print("Procesando ",solicitud.x1,solicitud.y1,solicitud.x2,solicitud.y2)
       returnValue= hashi.Matriz[solicitud.x1][solicitud.y1].conectar(hashi,hashi.Matriz[solicitud.x2][solicitud.y2],maths.calcular_direccion(solicitud.x1,solicitud.x2,solicitud.y1,solicitud.y2))
       solicitud.empty()
       print(returnValue)
       if returnValue != 1:
            DICPOPUPS.get(returnValue)()
       else:
            DICPOPUPS.get(returnValue)()
            actualizarBotones()
def actualizarBotones():
    n=len(hashi.Matriz)
    for i in range(n):
        for j in range(n):
            dpg.set_item_label(f"{i}{j}", hashi.Matriz[i][j].Dato)
    if hashi.verificar_victoria():
        dpg.configure_item("Ganaste", show=True)
        
        
        
#"Main"
with dpg.window(tag="Hashiwokakero",label="Hashiwokakero",height=1080,width=1920, no_title_bar=True):
        with dpg.group(horizontal=True):
            dpg.add_spacer(width=20)
            with dpg.group(tag="VHashiGroup"):
                dpg.add_spacer(height=12)
                with dpg.drawlist(width=700, height=200):
                    dpg.draw_image("Logo",(0, 0), (700, 200), uv_min=(0, 0), uv_max=(1, 1))
                dpg.add_spacer(height=12)
                dpg.add_text("Ingrese el nombre del archivo")
                dpg.add_input_text(tag="Input",hint="matriz.txt")
                dpg.add_button(tag="cargarMatriz",label="Cargar Matriz",callback=cargarMatriz)
                dpg.add_separator()
                dpg.add_spacer(height=32)
#Inicializar
dpg.create_viewport(title='Hashiwokakero',height=1080,width=1920)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()