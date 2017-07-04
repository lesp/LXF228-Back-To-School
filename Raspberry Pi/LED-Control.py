from guizero import App, Picture, PushButton, Slider, Text
from gpiozero import PWMLED, Buzzer
from time import sleep

blue = PWMLED(17)
bz = Buzzer(27)

def led_brightness(x):
    blue.value = (brightness.get() / 10)
    
def buzzer_beep():
    bz.beep(0.1,0.1)
    sleep(1)
    bz.off()

app = App(title="GPIO Zero Control Panel", height=300, width=500)
picture = Picture(app, image="lxf.gif")
instructions = Text(app, text="Instructions:", size=20, font="Times New Roman", color="red")

led_text = Text(app, text="Use the slider to control the LED brightness")
brightness = Slider(app, command=led_brightness, start=0, end=10)

buzzer_text = Text(app, text="Press the button to beep")
button = PushButton(app, command=buzzer_beep, text="Buzzer")

app.display()
