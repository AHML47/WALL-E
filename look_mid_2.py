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

def close_frame_mid_2_1 (device):
    inisilize(device)
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

def close_frame_mid_2_2 (device):
    inisilize(device)
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

def blink_look_down(device,time):
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