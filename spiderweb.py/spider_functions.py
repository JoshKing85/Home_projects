import turtle


def create_window():
    #image = r'C:\Users\joshk\OneDrive\Documents\Progamming\At home projects\spiderweb.py'
    window = turtle.Screen()  # Create an instance of the Screen class
    window.setup(width=1800, height=1200)
    #window.bgpic(image)  # Set the background image
    window.bgcolor('black')
    return window

def create_spider():
    
    spider = turtle.Turtle() # Create spider instance
    spider.hideturtle()
    spider.color('white')    # Use color method for web colour
    spider.speed(6)
    spider.width(1)
    

    return spider
spider = create_spider()

def build_frame(spider):
    
    for i in range(8):
        spider.left(i * 22.5)     # rotate direction by 22.5 degrees
        spider.forward(500)
        spider.backward(1000)
        spider.setposition(0, 0)  # set pos to  (0, 0)
        spider.setheading(0)      # Set heading to 0 degrees (facing east)
        spider.hideturtle()

  

def build_stucture(spider):               
    rad = 500                    # set radius and angle with constant Arc
    ang = 157.5
    ARC = 22.5


    
    def draw_arc(radius,startingAngle,angle,):
        spider.setheading(startingAngle+90)
        spider.circle(radius,angle) 
        
    
    while rad > 25:


        if spider.pos() == (0, 0): 
            
            for i in range(16):
                if spider.pos() == (0, 0):
                    spider.forward(rad)
                
                    draw_arc(rad, ang, ARC)  # Draw the arc
            
                else:
            
                    draw_arc(rad, ang - (i * 22.5), ARC)  # Draw arcs with adjusted angles
    
        
        elif rad == 500:
            spider.setposition(0, 0)  
            spider.setheading(0)
            rad -= 100
            
            for i in range(16):
                if spider.pos() == (0, 0):
                    spider.forward(rad)
                    draw_arc(rad, ang, ARC)  
                
                else:
            
                    draw_arc(rad, ang - (i * 22.5), ARC)  # Draw arcs with adjusted angles
        
        elif rad == 400:
            spider.setposition(0, 0)  
            spider.setheading(0)
            rad -= 75
            
            for i in range(16):
                if spider.pos() == (0, 0):
                    spider.forward(rad)
                    draw_arc(rad, ang, ARC)  
                
                else:
            
                    draw_arc(rad, ang - (i * 22.5), ARC)  # Draw arcs with adjusted angles

        
        
        
        elif rad > 225:
            spider.setposition(0, 0)  # Move the turtle to (0, 0)
            spider.setheading(0)
            rad -= 50
            
            for i in range(16):
                if spider.pos() == (0, 0):
                    spider.forward(rad)
                    draw_arc(rad, ang, ARC)  #
                
                else:
            
                    draw_arc(rad, ang - (i * 22.5), ARC)  # Draw arcs with adjusted angles
        
        
        
        else:
            spider.setposition(0, 0)  
            spider.setheading(0)
            rad -= 25
            
            for i in range(16):
                if spider.pos() == (0, 0):
                    spider.forward(rad)
                    draw_arc(rad, ang, ARC)  
                
                else:
            
                    draw_arc(rad, ang - (i * 22.5), ARC)  # Draw arcs with adjusted angles
        
            
        


def draw_spider(spider):
    
    def draw_arc(radius,startingAngle,angle,):
        spider.setheading(startingAngle+90)
        spider.circle(radius,angle) 
    
    spider.setposition(0, 0)  
    spider.setheading(45)
    spider.forward(225)
    pos = spider.pos()
    print(pos)

    draw_arc(10, 0, 360)
    pos = spider.pos()
    hed = spider.heading()
    print(pos, hed)

    

            
  
    

    

    










