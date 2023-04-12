import dearpygui.dearpygui as dpg
from clases.speedCommons import utils

dpg.create_context()

global new_button1


matriz,n,m=utils.load_matrix("matriz.txt")
with dpg.window(label="Tutorial",height=n*45,width=n*45):
 for i in range(n):
        with dpg.group(horizontal=True):
            for j in range(n):
                dpg.add_button(tag=f"a{i}{j}",label=f"{matriz[i][j]}", width=30, height=30,show=True)


dpg.create_viewport(title='Hashiwokakero',height=n*45,width=n*45)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()