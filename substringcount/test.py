import turtle
window = turtle.Screen()  # Create an instance of the Screen class
window.bgcolor('black')   # Use the bgcolor method to set the background color
window.setup(width=1800, height=1200)



spider = turtle.Turtle() # Create spider instance
spider.color('white')    # Use color method for web colour
spider.speed(-50)
spider.width(1)
  


def draw_arc(radius,startingAngle,angle, pos):
   spider.forward(pos)
   spider.setheading(startingAngle+90)
   spider.circle(radius,angle) 


for i in range(8):
    spider.left(i * 22.5)     # rotate direction by 22.5 degrees
    spider.forward(500)
    spider.backward(1000)
    spider.setposition(0, 0)  # Move the turtle to (0, 0)
    spider.setheading(0)      # Set the turtle's heading to 0 degrees (facing east)
    spider.hideturtle()

def build_stucture(spider):       

      
    
    
    
    rad = 500                    # set radius and angle with constant Arc
    ang = 157.5
    ARC = 22.5
    
    for i in range(16):
        
        if spider.pos() == (0, 0): 
            spider.forward(500)
                
            draw_arc(rad, ang, ARC)  # Draw the arc
            
        else:
            
            draw_arc(rad, ang - (i * 22.5), ARC)  # Draw arcs with adjusted angles

window.mainloop()