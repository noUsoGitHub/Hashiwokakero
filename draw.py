import dearpygui.dearpygui as dpg

dpg.create_context()


with dpg.window(label="Tutorial"):

    with dpg.drawlist(width=300, height=300):
            with dpg.draw_layer():
                dpg.draw_line((10, 10), (100, 100), color=(255, 0, 0, 255), thickness=1)
                dpg.draw_text((0, 0), "Origin", color=(250, 250, 250, 255), size=15)
                dpg.draw_arrow((50, 70), (100, 65), color=(0, 200, 255), thickness=1, size=10)

    b1= dpg.add_button(label="Button on the left")
    b2= dpg.add_button(label="Button on the right")
    slider_int = dpg.add_slider_int(label="Slide to the left!", width=100)
    slider_float = dpg.add_slider_float(label="Slide to the right!", width=100)



dpg.create_viewport(title='Hashiwokakero', width=800, height=800)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()