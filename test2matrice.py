from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from time import sleep
# Define the SPI interface and the number of cascaded MAX7219 devices
serial = spi(port=0, device=0, gpio=noop())
device1 = max7219(serial, cascaded=1, block_orientation=-90)
device2 = max7219(serial, cascaded=1, block_orientation=-90)
def inisilize(device):
    with canvas(device1) as draw:
        for i in range (8):
            for j in range (8):
                draw.point((i,j), fill="black")
    with canvas(device2) as draw:
        for i in range (8):
            for j in range (8):
                draw.point((i,j), fill="black")

def blink_look_down_0(device,time):
	close_frame_look_down_0_1(device)
	sleep(time)
	close_frame_look_down_0_2(device)
	sleep(time)
	close_frame_look_down_0_3(device)
	sleep(time)
	close_frame_look_down_0_2(device)
	sleep(time)
	look_dowen_0(device)
	sleep(time)

def close_frame_look_down_0_1 (devices):
    #inisilize(device)
    xd1=2
    xd2=3
    yd1=4
    yd2=5
    
    fill_color="white"
    for device in devices :
        with canvas(device) as draw:
            #el tol 
            for i in range (1,7):
                draw.point((1,i), fill="white")
                draw.point((6,i), fill="white")
        #el 3ordh
            for i in range (2,6):
                draw.point((i,0), fill="white")
                draw.point((i,7), fill="white")
                
            draw.point((xd1,yd1), fill=fill_color)
            draw.point((xd1,yd2), fill=fill_color)
            draw.point((xd2,yd1), fill=fill_color)
            draw.point((xd2,yd2), fill=fill_color)
        
    

def close_frame_look_down_0_2 (devices):
   # inisilize(device)
    xd1=2
    xd2=3
    yd1=4
    yd2=5
    
    fill_color="white"
    for device in devices :
        with canvas(device) as draw:
        #el tol 
            for i in range (1,7):
                draw.point((2,i), fill="white")
                draw.point((5,i), fill="white")
        #el 3ordh
            for i in range (2,6):
                draw.point((i,0), fill="white")
                draw.point((i,7), fill="white")
                
            draw.point((xd1,yd1), fill=fill_color)
            draw.point((xd1,yd2), fill=fill_color)
            draw.point((xd2,yd1), fill=fill_color)
            draw.point((xd2,yd2), fill=fill_color)

def close_frame_look_down_0_3(device):
    with canvas(device) as draw:
            x1=3
            x2=4
            for i in range (8):
                draw.point((x1,i), fill="white")
                draw.point((x2,i), fill="white")
while True :
    close_frame_look_down_0_2([device1,device2])
