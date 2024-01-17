def on_log_full():
    global log
    log = False
    basic.show_icon(IconNames.CHESSBOARD)
datalogger.on_log_full(on_log_full)

def on_button_pressed_a():
    global log
    log = True
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global log
    log = False
    basic.show_icon(IconNames.SKULL)
    datalogger.delete_log()
    datalogger.set_column_titles("Temp", "Light", "Sound")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global log
    log = False
    basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.B, on_button_pressed_b)

log = False
serial.redirect_to_usb()
log = False
basic.show_icon(IconNames.NO)
datalogger.set_column_titles("Temp", "Light", "Sound")

def on_every_interval():
    if log:
        basic.show_icon(IconNames.HEART)
        basic.clear_screen()
        datalogger.log(datalogger.create_cv("Temp", input.temperature()),
            datalogger.create_cv("Light", input.light_level()),
            datalogger.create_cv("Sound", input.sound_level()))
        serial.write_value("light",input.light_level())
loops.every_interval(1000, on_every_interval)
