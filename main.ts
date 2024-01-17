datalogger.onLogFull(function on_log_full() {
    
    log = false
    basic.showIcon(IconNames.Chessboard)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    log = true
    basic.showIcon(IconNames.Yes)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    log = false
    basic.showIcon(IconNames.Skull)
    datalogger.deleteLog()
    datalogger.setColumnTitles("Temp", "Light", "Sound")
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    log = false
    basic.showIcon(IconNames.No)
})
let log = false
serial.redirectToUSB()
log = false
basic.showIcon(IconNames.No)
datalogger.setColumnTitles("Temp", "Light", "Sound")
loops.everyInterval(1000, function on_every_interval() {
    if (log) {
        basic.showIcon(IconNames.Heart)
        basic.clearScreen()
        datalogger.log(datalogger.createCV("Temp", input.temperature()), datalogger.createCV("Light", input.lightLevel()), datalogger.createCV("Sound", input.soundLevel()))
        serial.writeValue("light", input.lightLevel())
    }
    
})
