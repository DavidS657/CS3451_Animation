# Object Modeling Example Code

from __future__ import division
import traceback

time = 0   # time is used to move objects from one frame to another
#Replicating the 2nd skateboard that collides with bart's skateboard using instancing

def setup():
    size (800, 800, P3D)
    
    try:
        frameRate(120)       # this seems to be needed to make sure the scene draws properly
        perspective (60 * PI / 180, 1, 0.1, 1000)  # 60-degree field of view
    except Exception:
        traceback.print_exc()

def draw():
    try:
        bg = loadImage("background.jpg")
        img = loadImage("bartLine.png")
        background(bg)
        global time
        time += .5
    
        if time > 270:
            exit()
        if time >= 0 and time < 100:
            camera (-90 + time , 140 , 0 + time*3 , 90, 140, -30, 0, 1, 0)
        elif time >= 100 and time < 150:
            camera (10 , 140 , 300 + ((time-100)*2) , 90, 140, -30, 0, 1, 0) 
        else: 
            camera (0 , -160 , 300 - time, 0 , 0, 0 , 0, 1, 0) 
            
        # set up the lights
        ambientLight(50, 50, 50);
        lightSpecular(100, 100, 100)
        directionalLight (100, 100, 100, -0.3, 0.5, -1)
        
        # set some of the surface properties
        noStroke()
        specular (180, 180, 180)
        shininess (15.0)
        
        #Animation for Bart and his Skateboard
        pushMatrix()
        if time <= 147:
            translate(150 - time , 125, 0)
        else:
            translate(150 - 147, 125, 0)
        
        #rotate bart's body post collision
        pushMatrix()
        if time > 147 and time < 178:
            translate(-time + 147, -time + 147, 0)
            rotateY((-time+147)/20)
            rotateX((-time+147)/40)
        elif time >= 178 and time < 200:
            translate(-31 + ((-time + 178)*1.5), -31, 0)
            rotateY(-31/20)
            rotateX((-time+147)/40)
        elif time >= 200 and time < 250:
            translate(-64 + ((-time + 200)), -31 + ((time - 200)*1.2), 0)
            rotateY(-31 /20)
            rotateX((-53 + ((-time + 200)*.2))/40)
        elif time >= 250:
            translate(-114, 29, 0)
            rotateY(-31/20)
            rotateX(-63/40)
        
        bartHead()
        
        # bart's neck
        fill (255, 255, 0)
        pushMatrix()
        translate(0, -10, -5)
        rotateX(PI/2)
        scale(5, 5, 5)
        cylinder()
        popMatrix()
        
        
        
        bartBody()
        
        
        bartRightArmWithHand()
        
        pushMatrix()
        
        translate(-6,-6.5,-15)
        rotateX(PI/2)
        rotateY(-PI/6)
        bartRightHandFingers()
        popMatrix()
        
        bartLeftArmWithHand()
        bartLeftHandFingers()
        
        popMatrix()
        
        #skateboard that bart is riding
        pushMatrix()
        translate(22,13,0)
        rotateZ(PI/2)
        if time > 147 and time < 156:
            translate(-time + 145, time - 147, 0)
            rotateZ((-time + 147)/20)
        elif time >= 156:
            translate(-11, 9, 0)
            rotateZ(-9/20)
        scale(1,1.2,1)
        skateboard()
        popMatrix()
        
        popMatrix()
        
        #animation for other skateboard that bart collides with
        pushMatrix()
        translate(0,1,0)
        if time <= 147:
            translate(-200 + time, 137, -10)
        else:
            translate(-200 + 147, 137, -10)
        rotateZ(PI/2)
        rotateX(PI)
        scale(1,1.2,1)
        skateboard()
        popMatrix()
        #road()
        
        #speech bubble pop up
        pushMatrix()
        if time >= 100 and time <= 140:
            image(img, 135 - time, 0)
        
        popMatrix()
        
        road()
        
        
    except Exception:
        traceback.print_exc()

# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 50):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # round main body
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2
def cone(sides = 64):
    # cone base
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex (x, y, 0)
    endShape(CLOSE)
    
    #sides
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta1 = i * 2 * PI / sides
        theta2 = (i + 1) * 2 * PI / sides
        x2 = cos(theta2)
        y2 = sin(theta2)
        x1 = cos(theta1)
        y1 = sin(theta1)
        beginShape(TRIANGLES)
        vertex(x1, y1, 0)
        vertex(x2, y2, 0)
        
        vertex(0, 0, 1)
        
        endShape(CLOSE)
        
def skateboard():
    #body of skateboard 
        fill(50,205,50)
        pushMatrix()
        translate(24,20, -5)
        rotateX(PI/2)
        rotateY(PI/2)
        scale(13,7,1)
        cylinder()
        popMatrix()
        
        fill(50,205,50)
        pushMatrix()
        translate(23.5,8, -5)
        rotateX(PI/2)
        rotateY(PI/2.4)
        scale(4,4,1)
        cylinder()
        popMatrix()
        
        # wheels of skateboard
        fill (128, 128, 128)
        pushMatrix()
        translate (26, 12, -5)
        box(2.5)
        popMatrix()
        
        fill (128, 128, 128)
        pushMatrix()
        translate (26, 26, -5)
        box(2.5)
        popMatrix()
        
        fill(128,128,128)
        pushMatrix()
        translate(28,12, -5)
        scale(1,1,4)
        cylinder()
        popMatrix()
        
        fill(128,128,128)
        pushMatrix()
        translate(28,26, -5)
        scale(1,1,4)
        cylinder()
        popMatrix()
        
        fill(160,32, 240)
        pushMatrix()
        translate(28,26, 0)
        scale(1.5,1.5,2)
        cylinder()
        popMatrix()
        
        fill(160,32, 240)
        pushMatrix()
        translate(28,26, -10)
        scale(1.5,1.5,2)
        cylinder()
        popMatrix()
        
        fill(160,32, 240)
        pushMatrix()
        translate(28,12, 0)
        scale(1.5,1.5,2)
        cylinder()
        popMatrix()
        
        fill(160,32, 240)
        pushMatrix()
        translate(28,12, -10)
        scale(1.5,1.5,2)
        cylinder()
        popMatrix()
        
def bartHead():
    # bart's head
        fill (255, 255, 0)
        pushMatrix()
        translate(0, -25, 0)
        rotateX(PI/2)
        #rotateX(-time)
        scale(10, 10, 10)
        cylinder()
        popMatrix()
        
        #bart's nose
        fill (255, 255, 0)
        pushMatrix()
        translate(0, -17, 10)
        sphereDetail(20)
        sphere(1.2)
        popMatrix()
        
        #bart's ears
        fill (255, 255, 0)
        pushMatrix()
        translate(9.5, -18, 0)
        sphereDetail(5)
        sphere(1.5)
        popMatrix()
        
        fill (255, 255, 0)
        pushMatrix()
        translate(-9.5, -18, 0)
        sphereDetail(5)
        sphere(1.5)
        popMatrix()
        
        #bart's mouth
        fill (0, 0, 0)
        pushMatrix()
        translate(0, -14.5, 0)
        rotateX(PI/2)
        #rotateX(-time)
        scale(8, 8, .5)
        cylinder()
        popMatrix()
        
        fill (255, 255, 0)
        pushMatrix()
        translate(0, -13.5, 0)
        rotateX(PI/2)
        #rotateX(-time)
        scale(8, 10, .5)
        cylinder()
        popMatrix()
        
        #bart's hair
        fill (255, 255, 0)
        pushMatrix()
        translate(-7, -32, 0)
        scale(3, 10, 3)
        rotateX(PI/2)
        #rotateX(-time)
        cone()
        popMatrix()
        
        fill (255, 255, 0)
        pushMatrix()
        translate(-2.5, -32, 0)
        scale(3, 10, 3)
        rotateX(PI/2)
        #rotateX(-time)
        cone()
        popMatrix()
        
        fill (255, 255, 0)
        pushMatrix()
        translate(2, -32, 0)
        scale(3, 10, 3)
        rotateX(PI/2)
        #rotateX(-time)
        cone()
        popMatrix()
        
        fill (255, 255, 0)
        pushMatrix()
        translate(6.5, -32, 0)
        scale(3, 10, 3)
        rotateX(PI/2)
        #rotateX(-time)
        cone()
        popMatrix()
        
        
        
        # bart's eyes
        fill (255, 255, 255)
        pushMatrix()
        translate(-5, -20, 10)
        sphereDetail(60)
        sphere(3.5)
        popMatrix()
        
        fill (255, 255, 255)
        pushMatrix()
        translate(5, -20, 10)
        sphereDetail(60)
        sphere(3.5)
        popMatrix()
        
        #bart's pupils
        fill (0, 0, 0)
        pushMatrix()
        translate(-5, -20, 13)
        sphereDetail(60)
        sphere(1)
        popMatrix()
        
        fill (0, 0, 0)
        pushMatrix()
        translate(5, -20, 13)
        sphereDetail(60)
        sphere(1)
        popMatrix()
        
def bartRightArmWithHand():
    #bart's right arm
        fill (255, 255, 0)
        pushMatrix()
        translate(-18, 3, -5)
        rotateX(PI/2)
        rotateY(PI/4)
        #rotateX(-time)
        scale(3, 3, 7)
        cylinder()
        popMatrix()
    #bart's right hand
        fill(255, 255, 0)
        pushMatrix()
        translate(-24, 9, -5)
        sphereDetail(20)
        sphere(4)
        popMatrix()
        
def bartRightHandFingers():
        #bart's right hand fingers
        fill (255, 255, 0)
        pushMatrix()
        translate(-24, 13.5, -5)
        rotateX(PI/2)
        #rotateY(-PI/2.5)
        scale(1, 1, 2)
        cylinder()
        popMatrix()
        
        fill (255, 255, 0)
        pushMatrix()
        translate(-28, 10, -5)
        rotateX(PI/2)
        rotateY(PI/3)
        scale(.8, .8, 1.5)
        cylinder()
        popMatrix()
        
        fill (255, 255, 0)
        pushMatrix()
        translate(-27, 12, -5)
        rotateX(PI/2)
        rotateY(PI/4)
        scale(.8, .8, 1.5)
        cylinder()
        popMatrix()
        
        fill (255, 255, 0)
        pushMatrix()
        translate(-27, 7, -5)
        rotateX(PI/2)
        rotateY(PI/2)
        scale(.8, .8, 1.5)
        cylinder()
        popMatrix()

def bartLeftArmWithHand():
            #bart's left arm
        fill (255, 255, 0)
        pushMatrix()
        translate(15, 0, -5)
        rotateX(PI/2)
        rotateY(PI/2)
        #rotateX(-time)
        scale(3, 3, 7)
        cylinder()
        popMatrix()
        
        fill (255, 255, 0)
        pushMatrix()
        translate(22, 0, -5)
        sphereDetail(100)
        sphere(2.6)
        #rotateX(-time)
        popMatrix()
        
        fill (255, 255, 0)
        pushMatrix()
        translate(24.5, 3, -5)
        rotateX(PI/2)
        rotateY(-PI/4)
        scale(3, 3, 4)
        cylinder()
        popMatrix()
        

        #left hand
        fill (255, 255, 0)
        pushMatrix()
        translate(28, 7, -5)
        sphereDetail(100)
        sphere(3.5)
        popMatrix()
def bartLeftHandFingers():
    #left hand fingers
        fill (255, 255, 0)
        pushMatrix()
        translate(30, 10, -7)
        rotateX(PI/2)
        rotateY(-PI/6)
        scale(.8, .8, 1.5)
        cylinder()
        popMatrix()
        
        fill (255, 255, 0)
        pushMatrix()
        translate(30, 10, -5.5)
        rotateX(PI/2)
        rotateY(-PI/6)
        scale(.8, .8, 1.5)
        cylinder()
        popMatrix()
        
        fill (255, 255, 0)
        pushMatrix()
        translate(30, 10, -4)
        rotateX(PI/2)
        rotateY(-PI/6)
        scale(.8, .8, 1.5)
        cylinder()
        popMatrix()
        
        fill (255, 255, 0)
        pushMatrix()
        translate(28, 10, -2)
        rotateX(-PI/4)
        scale(1, 1, 1)
        cylinder()
        popMatrix()
        
def bartBody():
        #bart's torso/shirt
        fill (255, 153, 73)
        pushMatrix()
        translate(0,-5,-5)
        rotateX(PI/2)
        scale(10,10,10)
        cone()
        popMatrix()
    
        fill (255, 153, 73)
        pushMatrix()
        translate(0,5,-5)
        rotateX(PI/2)
        scale(13,12.2,10)
        cylinder()
        popMatrix()
        
        #bart's sleeves
        fill (255, 153, 73)
        pushMatrix()
        translate(-15,0,-5)
        rotateX(PI/2)
        rotateY(PI/4)
        scale(6,6,6)
        cone()
        popMatrix()
        
        fill (255, 153, 73)
        pushMatrix()
        translate(15,0,-5)
        rotateX(PI/2)
        rotateY(-PI/2)
        scale(6,6,6)
        cone()
        popMatrix()
        
        #bart's shorts
        fill (100, 200, 255)
        pushMatrix()
        translate(0, 10, -5)
        sphereDetail(50)
        sphere(12)
        popMatrix()
    
        fill (100, 200, 255)
        pushMatrix()
        translate(-5,20,-5)
        rotateX(PI/2)
        scale(4, 5, 5)
        cylinder()
        popMatrix()
        
        fill (100, 200, 255)
        pushMatrix()
        translate(5,20,-5)
        rotateX(PI/2)
        scale(4, 5, 5)
        cylinder()
        popMatrix()
        
        #bart's legs
        
        fill (255, 255, 0)
        pushMatrix()
        translate(5,25,-5)
        rotateX(PI/2)
        scale(3, 3, 6)
        cylinder()
        popMatrix()
        
        fill (255, 255, 0)
        pushMatrix()
        translate(-5,25,-5)
        rotateX(PI/2)
        scale(3, 3, 6)
        cylinder()
        popMatrix()
        
        #bart's kicks
        
        fill (255, 255, 255)
        pushMatrix()
        translate(-5,31,-5)
        rotateX(PI/2)
        scale(4, 5, 1)
        cylinder()
        popMatrix()
        
        fill (255, 255, 255)
        pushMatrix()
        translate(5,31,-5)
        rotateX(PI/2)
        scale(4, 5, 1)
        cylinder()
        popMatrix()
        
        fill (100, 200, 255)
        pushMatrix()
        translate(-5,34,-4)
        rotateX(PI/2)
        scale(4.5, 7, 2)
        cylinder()
        popMatrix()
        
        fill (100, 200, 255)
        pushMatrix()
        translate(5,34,-4)
        rotateX(PI/2)
        scale(4.5, 7, 2)
        cylinder()
        popMatrix()
        
        fill (255, 255, 255)
        pushMatrix()
        translate(-5,35.5,-4)
        rotateX(PI/2)
        scale(4.5, 7.1, .5)
        cylinder()
        popMatrix()
        
        fill (255, 255, 255)
        pushMatrix()
        translate(5,35.5,-4)
        rotateX(PI/2)
        scale(4.5, 7.1, .5)
        cylinder()
        popMatrix()
        
def road():
    fill(220,220,220)
    pushMatrix()
    translate(0,173,0)
    scale(20,.5,4)
    box(20)
    popMatrix()    
