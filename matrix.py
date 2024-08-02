
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from time import sleep
from random import randint
 # Define the SPI interface and the number of cascaded MAX7219 devices
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1, block_orientation=-90)
device2 = max7219(serial, cascaded=1, block_orientation=-90)
def inislise(device):
    with canvas(device) as draw :
        for i in range (8):
            for j in range (8):
                draw.point((i,j),"black")

def look_dowen_0(device):
        with canvas(device) as draw:
            x=0
            y=7
            xd1=2
            xd2=3
            yd1=4
            yd2=5
        #el 5tot
            for i in range (2,6):
                draw.point((i,x), fill="white")
                draw.point((x,i), fill="white")
                draw.point((i,y), fill="white")
                draw.point((y,i), fill="white")
        #etraken
            draw.point((1,1), fill="white")
            draw.point((6,6), fill="white")
            draw.point((6,1), fill="white")
            draw.point((1,6), fill="white")
        
            draw.point((xd1,yd1), fill="white")
            draw.point((xd1,yd2), fill="white")
            draw.point((xd2,yd1), fill="white")
            draw.point((xd2,yd2), fill="white")

def close_frame_look_down_0_1 (device):
    
    xd1=2
    xd2=3
    yd1=4
    yd2=5
    
    fill_color="white"
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

def close_frame_look_down_0_2 (device):
    ###
    xd1=2
    xd2=3
    yd1=4
    yd2=5
    
    fill_color="white"
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
            draw.point((2,0), fill="black")
            draw.point((5,0), fill="black")

def blink_look_down_0(device,time):
	close_frame_look_down_0_1(device)
	sleep(time)
	inislise(device)
	close_frame_look_down_0_2(device)
	sleep(time)
	inislise(device)
	close_frame_look_down_0_3(device)
	sleep(time)
	inislise(device)
	close_frame_look_down_0_2(device)
	sleep(time)
	inislise(device)
	look_dowen_0(device)
	sleep(time)
	inislise(device)

def look_dowen_1(device):
    with canvas(device) as draw:
        x=0
        y=7
        xd1=3
        xd2=4
        yd1=4
        yd2=5
        #el 5tot
        for i in range (2,6):
            draw.point((i,x), fill="white")
            draw.point((x,i), fill="white")
            draw.point((i,y), fill="white")
            draw.point((y,i), fill="white")
        #etraken
        draw.point((1,1), fill="white")
        draw.point((6,6), fill="white")
        draw.point((6,1), fill="white")
        draw.point((1,6), fill="white")
        
        draw.point((xd1,yd1), fill="white")
        draw.point((xd1,yd2), fill="white")
        draw.point((xd2,yd1), fill="white")
        draw.point((xd2,yd2), fill="white")

def close_frame_look_down_1_1 (device):
    
    xd1=4
    xd2=3
    yd1=4
    yd2=5
    
    fill_color="white"
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

def close_frame_look_down_1_2 (device):
    
    xd1=4
    xd2=3
    yd1=4
    yd2=5
    
    fill_color="white"
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

def close_frame_look_down_1_3(device):
    with canvas(device) as draw:
            x1=3
            x2=4
            for i in range (8):
                draw.point((x1,i), fill="white")
                draw.point((x2,i), fill="white")

def blink_look_down_1(device,time):
	close_frame_look_down_1_1(device)
	sleep(time)
	close_frame_look_down_1_2(device)
	sleep(time)
	close_frame_look_down_1_3(device)
	sleep(time)
	close_frame_look_down_1_2(device)
	sleep(time)
	look_dowen_1(device)
	sleep(time)

def look_dowen_2(device):
    with canvas(device) as draw:
        x=0
        y=7
        xd1=5
        xd2=4
        yd1=4
        yd2=5
        #el 5tot
        for i in range (2,6):
            draw.point((i,x), fill="white")
            draw.point((x,i), fill="white")
            draw.point((i,y), fill="white")
            draw.point((y,i), fill="white")
        #etraken
        draw.point((1,1), fill="white")
        draw.point((6,6), fill="white")
        draw.point((6,1), fill="white")
        draw.point((1,6), fill="white")
        
        draw.point((xd1,yd1), fill="white")
        draw.point((xd1,yd2), fill="white")
        draw.point((xd2,yd1), fill="white")
        draw.point((xd2,yd2), fill="white")

def close_frame_look_down_2_1 (device):
    ###
    xd1=4
    xd2=5
    yd1=4
    yd2=5
    
    fill_color="white"
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

def close_frame_look_down_2_2 (device):
    ###
    xd1=4
    xd2=5
    yd1=4
    yd2=5
    
    fill_color="white"
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

def close_frame_look_down_2_3(device):
    with canvas(device) as draw:
            x1=3
            x2=4
            for i in range (8):
                draw.point((x1,i), fill="white")
                draw.point((x2,i), fill="white")

def blink_look_down_2(device,time):
	close_frame_look_down_2_1(device)
	sleep(time)
	close_frame_look_down_2_2(device)
	sleep(time)
	close_frame_look_down_2_3(device)
	sleep(time)
	close_frame_look_down_2_2(device)
	sleep(time)
	look_dowen_2(device)
	sleep(time)
	
def look_mid_0(device):
    with canvas(device) as draw:
        x=0
        y=7
        xd1=2
        xd2=3
        yd1=4
        yd2=3
        #el 5tot
        for i in range (2,6):
            draw.point((i,x), fill="white")
            draw.point((x,i), fill="white")
            draw.point((i,y), fill="white")
            draw.point((y,i), fill="white")
        #etraken
        draw.point((1,1), fill="white")
        draw.point((6,6), fill="white")
        draw.point((6,1), fill="white")
        draw.point((1,6), fill="white")
        
        draw.point((xd1,yd1), fill="white")
        draw.point((xd1,yd2), fill="white")
        draw.point((xd2,yd1), fill="white")
        draw.point((xd2,yd2), fill="white")

def close_frame_look_mid_0_1 (device):
    ###
    xd1=2
    xd2=3
    yd1=4
    yd2=3
    
    fill_color="white"
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

def close_frame_look_mid_0_2 (device):
    ###
    xd1=2
    xd2=3
    yd1=4
    yd2=3
    
    fill_color="white"
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

def close_frame_look_mid_0_3(device):
    with canvas(device) as draw:
            x1=3
            x2=4
            for i in range (8):
                draw.point((x1,i), fill="white")
                draw.point((x2,i), fill="white")

def blink_look_mid_0(device,time):
	close_frame_look_mid_0_1(device)
	sleep(time)
	close_frame_look_mid_0_2(device)
	sleep(time)
	close_frame_look_mid_0_3(device)
	sleep(time)
	close_frame_look_mid_0_2(device)
	sleep(time)
	look_dowen_2(device)
	sleep(time)

def look_mid_1(device):
    with canvas(device) as draw:
        x=0
        y=7
        xd1=3
        xd2=4
        yd1=4
        yd2=3
        #el 5tot
        for i in range (2,6):
            draw.point((i,x), fill="white")
            draw.point((x,i), fill="white")
            draw.point((i,y), fill="white")
            draw.point((y,i), fill="white")
        #etraken
        draw.point((1,1), fill="white")
        draw.point((6,6), fill="white")
        draw.point((6,1), fill="white")
        draw.point((1,6), fill="white")
        
        draw.point((xd1,yd1), fill="white")
        draw.point((xd1,yd2), fill="white")
        draw.point((xd2,yd1), fill="white")
        draw.point((xd2,yd2), fill="white")

def close_frame_look_mid_1_1 (device):
    ###
    xd1=4
    xd2=3
    yd1=4
    yd2=3
    
    fill_color="white"
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

def close_frame_look_mid_1_2 (device):
    ##
    xd1=4
    xd2=3
    yd1=4
    yd2=3
    
    fill_color="white"
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

def close_frame_look_mid_1_3(device):
    with canvas(device) as draw:
            x1=3
            x2=4
            for i in range (8):
                draw.point((x1,i), fill="white")
                draw.point((x2,i), fill="white")

def blink_look_mid_1(device,time):
	close_frame_look_mid_1_1(device)
	sleep(time)
	close_frame_look_mid_1_2(device)
	sleep(time)
	close_frame_look_mid_1_3(device)
	sleep(time)
	close_frame_look_mid_1_2(device)
	sleep(time)
	look_mid_1(device)
	sleep(time)
	
def look_mid_2(device):
    with canvas(device) as draw:
        x=0
        y=7
        xd1=5
        xd2=4
        yd1=4
        yd2=3
        #el 5tot
        for i in range (2,6):
            draw.point((i,x), fill="white")
            draw.point((x,i), fill="white")
            draw.point((i,y), fill="white")
            draw.point((y,i), fill="white")
        #etraken
        draw.point((1,1), fill="white")
        draw.point((6,6), fill="white")
        draw.point((6,1), fill="white")
        draw.point((1,6), fill="white")
        
        draw.point((xd1,yd1), fill="white")
        draw.point((xd1,yd2), fill="white")
        draw.point((xd2,yd1), fill="white")
        draw.point((xd2,yd2), fill="white")

def close_frame_look_mid_2_1 (device):
    ##
    xd1=4
    xd2=5
    yd1=4
    yd2=3
    
    fill_color="white"
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

def close_frame_look_mid_2_2 (device):
    ##
    xd1=4
    xd2=5
    yd1=4
    yd2=3
    
    fill_color="white"
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

def close_frame_look_mid_2_3(device):
    with canvas(device) as draw:
            x1=3
            x2=4
            for i in range (8):
                draw.point((x1,i), fill="white")
                draw.point((x2,i), fill="white")

def blink_look_mid_2(device,time):
	close_frame_look_mid_2_1(device)
	sleep(time)
	close_frame_look_mid_2_2(device)
	sleep(time)
	close_frame_look_mid_2_3(device)
	sleep(time)
	close_frame_look_mid_2_2(device)
	sleep(time)
	look_mid_2(device)
	sleep(time)
	
def look_up_0(device):
    with canvas(device) as draw:
        x=0
        y=7
        xd1=2
        xd2=3
        yd1=2
        yd2=3
        #el 5tot
        for i in range (2,6):
            draw.point((i,x), fill="white")
            draw.point((x,i), fill="white")
            draw.point((i,y), fill="white")
            draw.point((y,i), fill="white")
        #etraken
        draw.point((1,1), fill="white")
        draw.point((6,6), fill="white")
        draw.point((6,1), fill="white")
        draw.point((1,6), fill="white")
        
        draw.point((xd1,yd1), fill="white")
        draw.point((xd1,yd2), fill="white")
        draw.point((xd2,yd1), fill="white")
        draw.point((xd2,yd2), fill="white")

def close_frame_look_up_0_1 (device):
    ##
    xd1=2
    xd2=3
    yd1=2
    yd2=3
    
    fill_color="white"
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

def close_frame_look_up_0_2 (device):
    ##
    xd1=2
    xd2=3
    yd1=2
    yd2=3
    
    fill_color="white"
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

def close_frame_look_up_0_3(device):
    with canvas(device) as draw:
            x1=3
            x2=4
            for i in range (8):
                draw.point((x1,i), fill="white")
                draw.point((x2,i), fill="white")

def blink_look_up_0(device,time):
	close_frame_look_up_0_1(device)
	sleep(time)
	close_frame_look_up_0_2(device)
	sleep(time)
	close_frame_look_up_0_3(device)
	sleep(time)
	close_frame_look_up_0_2(device)
	sleep(time)
	look_up_0(device)
	sleep(time)

def look_up_1(device):
    with canvas(device) as draw:
        x=0
        y=7
        xd1=3
        xd2=4
        yd1=2
        yd2=3
        #el 5tot
        for i in range (2,6):
            draw.point((i,x), fill="white")
            draw.point((x,i), fill="white")
            draw.point((i,y), fill="white")
            draw.point((y,i), fill="white")
        #etraken
        draw.point((1,1), fill="white")
        draw.point((6,6), fill="white")
        draw.point((6,1), fill="white")
        draw.point((1,6), fill="white")
        
        draw.point((xd1,yd1), fill="white")
        draw.point((xd1,yd2), fill="white")
        draw.point((xd2,yd1), fill="white")
        draw.point((xd2,yd2), fill="white")

def close_frame_look_up_1_1 (device):
    ##
    xd1=4
    xd2=3
    yd1=2
    yd2=3
    
    fill_color="white"
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

def close_frame_look_up_1_2 (device):
    ##
    xd1=4
    xd2=2
    yd1=4
    yd2=3
    
    fill_color="white"
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

def close_frame_look_up_1_3(device):
    with canvas(device) as draw:
            x1=3
            x2=4
            for i in range (8):
                draw.point((x1,i), fill="white")
                draw.point((x2,i), fill="white")

def blink_look_up_1(device,time):
	close_frame_look_up_1_1(device)
	sleep(time)
	close_frame_look_up_1_2(device)
	sleep(time)
	close_frame_look_up_1_3(device)
	sleep(time)
	close_frame_look_up_1_2(device)
	sleep(time)
	look_up_1(device)
	sleep(time)
	
def look_up_2(device):
    with canvas(device) as draw:
        x=0
        y=7
        xd1=5
        xd2=4
        yd1=2
        yd2=3
        #el 5tot
        for i in range (2,6):
            draw.point((i,x), fill="white")
            draw.point((x,i), fill="white")
            draw.point((i,y), fill="white")
            draw.point((y,i), fill="white")
        #etraken
        draw.point((1,1), fill="white")
        draw.point((6,6), fill="white")
        draw.point((6,1), fill="white")
        draw.point((1,6), fill="white")
        
        draw.point((xd1,yd1), fill="white")
        draw.point((xd1,yd2), fill="white")
        draw.point((xd2,yd1), fill="white")
        draw.point((xd2,yd2), fill="white")

def close_frame_look_up_2_1 (device):
    ##
    xd1=4
    xd2=5
    yd1=2
    yd2=3
    
    fill_color="white"
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

def close_frame_look_up_2_2 (device):
    ##
    xd1=4
    xd2=5
    yd1=2
    yd2=3
    
    fill_color="white"
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

def close_frame_look_up_2_3(device):
    with canvas(device) as draw:
            x1=3
            x2=4
            for i in range (8):
                draw.point((x1,i), fill="white")
                draw.point((x2,i), fill="white")

def blink_look_up_2(device,time):
	close_frame_look_up_2_1(device)
	sleep(time)
	close_frame_look_up_2_2(device)
	sleep(time)
	close_frame_look_up_2_3(device)
	sleep(time)
	close_frame_look_up_2_2(device)
	sleep(time)
	look_up_2(device)
	sleep(time)

def eye_margin(device):
    with canvas(device) as draw:
        fillcolor="white"
        x=0
        y=7
        #el 5tot
        for i in range (2,6):
            draw.point((i,x), fill="white")
            draw.point((x,i), fill="white")
            draw.point((i,y), fill="white")
            draw.point((y,i), fill="white")
        #etraken
        draw.point((1,1), fill="white")
        draw.point((6,6), fill="white")
        draw.point((6,1), fill="white")
        draw.point((1,6), fill="white")
        #el waset
        draw.point((3,3), fill="white")
        draw.point((4,4), fill="white")
        draw.point((4,3), fill="white")
        draw.point((3,4), fill="white")
# Call the function to display the pattern
def look_group_1(device,time,time2):
    look_dowen_0(device)
    sleep(time)
    look_dowen_1(device)
    sleep(time)
    look_dowen_2(device)
    sleep(time)
    look_mid_0(device)
    sleep(time)
    look_up_2(device)
    sleep(time)
    look_up_1(device)
    sleep(time)
    look_up_0(device)
    sleep(time)
    look_mid_0(device)
    sleep(time)
    look_dowen_0(device)
    sleep(time)
    look_mid_1(device)
    sleep(time)
    blink_look_mid_1(device,time2)
    sleep(time)
    
def look_group_2(device,time1,time2):
    look_mid_0(device)
    sleep(time1)
    blink_look_down_0(device,time2)
    sleep(time1)
    look_mid_0(device)
    sleep(time1)
    look_mid_1(device)
    sleep(time1)
    look_mid_2(device)
    sleep(time1)
    look_mid_1(device)
    sleep(time1)
    blink_look_mid_1(device,time2)
    
def look_group_3(device,time,time2):
    look_mid_1(device)
    sleep(time)
    look_up_0(device)
    sleep(time)
    look_mid_1(device)
    sleep(time)
    blink_look_mid_1(device,time2)
    
    
while True:
    ran=randint(1,3)
    print(ran)
    if (ran==1):
        look_group_1(device,1,1)
        
    elif (ran==2):
        look_group_2(device,1,1)
    elif (ran==3):
        look_group_3(device,1,1)

###
