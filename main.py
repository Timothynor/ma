from pynput.keyboard import Key, Controller
class coordinates():
    x = 0
    y = 0
    z = 0
    def xyz():
        x = 0
        y = 0
        z = 0
        xinput = input(x)
        yinput = input(y)
        zinput = input(z)
            
        xInTaken = False
        yInTaken = False
        zInTaken = False
        
        xNowTaken = False
        yNOwTaken = False
        zNOwTaken = False
        
        def ifxyz1():
            if (xInTaken == True):
                for x in range(0,1):
                    x = opening.xinput
                    xNowTaken = True
        def ifxyz2():
            if (yInTaken == True):
                for y in range(0,1):
                    y = opening.yinput
                    yNOwTaken = True
        def ifxyz3():
            if (zInTaken == True):
                for z in range(0,1):
                    z = opening.zinput
                    zNOwTaken = True
                    
    def drawcoordinategrid():
        
#controls sculpting
class mouseAndKeyboard():
    def __init__(self, height, width, length, x, y, z):
        self.volume = mouse(height, width, length)
        self.position = coordinates(x, y, z)
    def __init__(self, click, playB, dragB, pressB, maskB, InvertB):
        self.click = False
        self.playB = False
        self.dragB = False
        self.pressB = False
        self.maskB = False
        self.InvertB = False
    def controls():
        if(keyboard.press('d')):
            self.dragB = True
        elif(keyboard.release('d')):
            self.dragB = False
        
        elif(keyboard.press('m')):
            self.maskB = True
        elif(keyboard.release('m')):
            self.maskB = False
        
        elif(keyboard.press('i' + 'm')):
            self.InvertB = True
        elif(keyboard.release('i')):
            self.maskB = False
        
        
        


class mesh():
    def __init__(self, quad, triangle, quadTrue, triangleTrue, Ntriangle, Nquad):
        self.quadTrue = False
        self.triangleTrue = False
        #number of quads or triangles
        self.Ntriangle = range(0, 100000000)
        self.Nquad = range(0, 100000000)
    def createQuad(quadApperance = "----\n|\n|\n----", triangleApperance = [chr(47),chr(92)]):
        #acsessing vertex on quad
        point1 = [1, 0]
        point2 = [2, 1]
        point3 = [1, 0]
        point4 = [0, 0]
        # creating points on quad
        quadApperance[0] = point1
        quadApperance[3] = point2
        quadApperance[8] = point3
        quadApperance[11] = point4
        # max number of quads
        if(self.quadTrue == True):
            for self.quadTrue in range(self.Nquad):
                print(quadApperance)
        elif(self.quadTrue == True and self.Nquad > 100000000):
            print("limit reached")
            self.quadTrue = False
        elif(self.triangleTrue == True):
            for self.triangleTrue in range(self.Ntriangle):
                print(triangleApperance)
        elif(self.triangleTrue == True and self.Ntriangle > 100000000):
            print("limit reached")
            self.triangleTrue = False
    def swaptriangle():
        
    def swapquad():
        #allows me to add new values to the arrays
        point1.append(x)
        point1.append(y)
        #write an if statement that can change values x and y then swap them
        if(point1[2] == 0):
            coordinates.ifxyz1()
        if(point1[3] == 0):
            coordinates.ifxyz2()
        
        point2.append(x)
        point2.append(y)
        if(point2[2] == 0):
            coordinates.ifxyz1()
        if(point2[3] == 0):
            coordinates.ifxyz2()
        
        
        point3.append(x)
        point3.append(y)
        if(point3[2] == 0):
            coordinates.ifxyz1()
        if(point3[3] == 0):
            coordinates.ifxyz2()
        
        point4.append(x)
        point4.append(y)
        if(point4[2] == 0):
            coordinates.ifxyz1()
        if(point4[3] == 0):
            coordinates.ifxyz2()
            
class meshtypes():
    def __init__(cone, sphere, cube):
        cone = False
        sphere = False
        cube = False
    
    
    







