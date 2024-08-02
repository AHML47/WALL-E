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

def close_frame_up_0_1 (device):
    inisilize(device)
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

def close_frame_up_0_2 (device):
    inisilize(device)
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

def blink_look_up(device,time):
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