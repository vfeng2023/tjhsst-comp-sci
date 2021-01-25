# Torbert, 8.25.2005

from Tkinter import *
from math import sin, cos, radians
from time import sleep

east, north, west, south, infinity = 0, 90, 180, 270, -1

class Robot:
    COUNT = 1
    def __init__(self, world, x=1, y=1, direction=east, beepers=0):
        self.world, self.image = world, None
        self.x, self.y, self.d, self.beepers = x, y, direction%360, beepers
        self.alive = True
        self.world.register(x,y,self)
        self.draw()
        self.world.refresh()
        self.count = Robot.COUNT
        Robot.COUNT += 1
        self.debug()        

    def destroy(self):
        if not self.alive:
            raise Exception("Robot has been destroyed.")
        if self.world.debug is True:
            print "DESTROYING...",
            self.debug()
        self.world.erase(self.image)
        self.world.refresh()
        self.world.remove(self.x,self.y,self)
        self.alive = False

    def __str__(self):
        if not self.alive:
            raise Exception("Robot has been destroyed.")
        if self.beepers == infinity:
            s = "infinite"
        else:
            s = str(self.beepers)
        return "Robot %d at (%d,%d) facing %s carrying %s beeper(s)." % \
               (self.count, self.x, self.y, ["east", "north", "west", "south"][self.d/90], s)

    def lift(self):
        if not self.alive:
            raise Exception("Robot has been destroyed.")
        self.world.lift(self.image)

    def draw(self):
        if not self.alive:
            raise Exception("Robot has been destroyed.")
        self.image = self.world.draw(self.x, self.y, self.d, self.image)

    def debug(self):
        if not self.alive:
            raise Exception("Robot has been destroyed.")
        if self.world.debug is True:
            print self        
    
    def move(self):
        if not self.alive:
            raise Exception("Robot has been destroyed.")
        d = self.d/90
        dx, dy = (d+1)%2*(d-1)*-1, d%2*(d-2)*-1
        x, y = self.x, self.y
        self.x += dx
        self.y += dy
        if self.world.crash(x, y, self.x, self.y):
            raise Exception("Walked through wall.")
        self.world.recordMove(self.count, x, y, self.x, self.y)
        self.draw()
        self.world.refresh()
        self.debug()

    def turnLeft(self):
        if not self.alive:
            raise Exception("Robot has been destroyed.")
        self.d += 90
        if self.d == 360:
            self.d = 0
        self.draw()
        self.world.refresh()
        self.debug()        

    def putBeeper(self):
        if not self.alive:
            raise Exception("Robot has been destroyed.")
        if self.beepers == 0:
            raise Exception("No beepers to put.")
        if self.beepers is not infinity:
            self.beepers -= 1
        self.world.addBeeper(self.x, self.y)
        self.world.refresh()
        self.debug()        
        
    def pickBeeper(self):
        if not self.alive:
            raise Exception("Robot has been destroyed.")
        if not self.world.isBeeper(self.x, self.y):
            raise Exception("No beepers to pick.")
        if self.beepers is not infinity:
            self.beepers += 1
        self.world.removeBeeper(self.x, self.y)
        self.world.refresh()
        self.debug()        

    def hasBeepers(self):
        if not self.alive:
            raise Exception("Robot has been destroyed.")
        return not self.beepers == 0

    def frontIsClear(self):
        if not self.alive:
            raise Exception("Robot has been destroyed.")
        d = self.d/90
        dx, dy = (d+1)%2*(d-1)*-1, d%2*(d-2)*-1
        x1, y1 = self.x, self.y
        x2, y2 = x1+dx, y1+dy
        return not self.world.crash(x1, y1, x2, y2)
        
    def leftIsClear(self):
        if not self.alive:
            raise Exception("Robot has been destroyed.")
        d = self.d/90
        d = (d+1)%4
        dx, dy = (d+1)%2*(d-1)*-1, d%2*(d-2)*-1
        x1, y1 = self.x, self.y
        x2, y2 = x1+dx, y1+dy
        return not self.world.crash(x1, y1, x2, y2)
    
    def rightIsClear(self):
        if not self.alive:
            raise Exception("Robot has been destroyed.")
        d = self.d/90
        d = (d+3)%4
        dx, dy = (d+1)%2*(d-1)*-1, d%2*(d-2)*-1
        x1, y1 = self.x, self.y
        x2, y2 = x1+dx, y1+dy
        return not self.world.crash(x1, y1, x2, y2)
    
    def backIsClear(self):
        if not self.alive:
            raise Exception("Robot has been destroyed.")
        d = self.d/90
        d = (d+2)%4
        dx, dy = (d+1)%2*(d-1)*-1, d%2*(d-2)*-1
        x1, y1 = self.x, self.y
        x2, y2 = x1+dx, y1+dy
        return not self.world.crash(x1, y1, x2, y2)

    def facingNorth(self):
        if not self.alive:
            raise Exception("Robot has been destroyed.")
        return self.d == 90

    def facingSouth(self):
        if not self.alive:
            raise Exception("Robot has been destroyed.")
        return self.d == 270

    def facingEast(self):
        if not self.alive:
            raise Exception("Robot has been destroyed.")
        return self.d == 0

    def facingWest(self):
        if not self.alive:
            raise Exception("Robot has been destroyed.")
        return self.d == 180    

    def nextToABeeper(self):
        if not self.alive:
            raise Exception("Robot has been destroyed.")
        return self.world.isBeeper(self.x, self.y)

    def nextToARobot(self):
        if not self.alive:
            raise Exception("Robot has been destroyed.")
        return self.world.countRobots(self.x, self.y) > 1

class World(Tk):
    def __init__(self,filename=None,block=50,debug=True,delay=0.25,image=True,width=10,height=10):
        Tk.__init__(self)
        self.title("")
        arg, self.width, self.height = block, width, height
        self.photos = [PhotoImage(file=(k+".gif")) for k in ["east","north","west","south"]]
        self.beepers, self.ovals, self.numbers, self.robots, self.walls = {},{},{},{},{}
        self.m, self.n, self.t, self.delay = arg*(width+3), arg*(height+3), arg, delay
        self.debug, self.useImage = debug, image
        a, b, c = self.t+self.t/2, self.m-self.t-self.t/2, self.n-self.t-self.t/2
        self.canvas = Canvas(self, bg="white", width=self.m, height=self.n)
        self.canvas.pack()
        count = 1
        for k in range(2*self.t, max(self.m,self.n)-self.t, self.t):
            if k < b: 
                self.canvas.create_line(k, c, k, a, fill="red")
                self.canvas.create_text(k, c+self.t/2, text=str(count), font=("Times",max(-self.t*2/3,-15),""))
            if k < c: 
                self.canvas.create_line(b, k, a, k, fill="red")
                self.canvas.create_text(a-self.t/2, self.n-k, text=str(count), font=("Times",max(-self.t*2/3,-15),""))
            count += 1
        self.canvas.create_line(a, c, b, c, fill="black", width=3)
        self.canvas.create_line(a, a, a, c, fill="black", width=3)
        if filename is not None:
            self.readWorld(filename)
        self.refresh()

    def readWorld(self,filename):
        try:
            infile = open("worlds\\%s.wld" % filename, "r")
        except IOError:
           try:
               infile = open("worlds/%s.wld" % filename, "r")
           except IOError:
               infile = open(filename, "r")            
        text = infile.read().split("\n")
        infile.close()
        for t in text:
            if t.startswith("eastwestwalls"):
                s = t.split(" ")
                y, x = int(s[1]), int(s[2])     #  row, col 
                self.addWall(x, y, -1, y)
            if t.startswith("northsouthwalls"):
                s = t.split(" ")
                x, y = int(s[1]), int(s[2])
                self.addWall(x, y, x, -1)
            if t.startswith("beepers"):
                s = t.split(" ")
                y, x, n = int(s[1]), int(s[2]), int(s[3])  # row, col for beepers!
                if n is infinity:
                    self.addInfiniteBeepers(x, y)
                else:
                    for k in range(n):
                        self.addBeeper(x, y)

    def pause(self):
        sleep(self.delay)

    def isBeeper(self,x,y):
        return (x,y) in self.beepers.keys() and not self.beepers[(x,y)] == 0

    def countRobots(self,x,y):
        if (x,y) not in self.robots.keys():
            return 0
        return len(self.robots[(x,y)])

    def crash(self,x1,y1,x2,y2):
        if 0 in (x1,y1,x2,y2):
            return True
        if (x2,y2) in self.walls.keys() and (x1,y1) in self.walls[(x2,y2)]:
            return True
        if (x1,y1) in self.walls.keys() and (x2,y2) in self.walls[(x1,y1)]:
            return True        
        return False

    def addInfiniteBeepers(self,x,y):
        flag = (x,y) not in self.beepers.keys() or self.beepers[(x,y)] is 0        
        self.beepers[(x,y)] = infinity
        text = "oo"
        a, b = self.t+x*self.t, self.n-(self.t+y*self.t)
        t = self.t/3
        if flag:
            self.ovals[(x,y)] = self.canvas.create_oval(a-t, b-t, a+t, b+t, fill="black")
            self.numbers[(x,y)] = self.canvas.create_text(a, b, text=text, fill="white", font=("Times",max(-self.t/2,-20),""))
        else:
            self.canvas.itemconfig(self.numbers[(x,y)], text=text)
        if (x,y) in self.robots.keys():
            for robot in self.robots[(x,y)]:
                robot.lift()

    def addBeeper(self,x,y):
        if (x,y) in self.beepers.keys() and self.beepers[(x,y)] is infinity:
            return
        flag = (x,y) not in self.beepers.keys() or self.beepers[(x,y)] is 0
        if flag:
            self.beepers[(x,y)] = 1
        else:
            self.beepers[(x,y)] += 1
        text = str(self.beepers[(x,y)])
        a, b = self.t+x*self.t, self.n-(self.t+y*self.t)
        t = self.t/3
        if flag:
            self.ovals[(x,y)] = self.canvas.create_oval(a-t, b-t, a+t, b+t, fill="black")
            self.numbers[(x,y)] = self.canvas.create_text(a, b, text=text, fill="white", font=("Times",max(-self.t/2,-20),""))
        else:
            self.canvas.itemconfig(self.numbers[(x,y)], text=text)
        if (x,y) in self.robots.keys():
            for robot in self.robots[(x,y)]:
                robot.lift()            

    def removeBeeper(self,x,y):
        if self.beepers[(x,y)] is infinity:
            return        
        self.beepers[(x,y)] -= 1
        flag = self.beepers[(x,y)] is 0        
        text = str(self.beepers[(x,y)])
        if flag:
            self.canvas.delete(self.ovals[(x,y)])
            self.canvas.delete(self.numbers[(x,y)])            
        else:
            self.canvas.itemconfig(self.numbers[(x,y)], text=text)
        if (x,y) in self.robots.keys():
            for robot in self.robots[(x,y)]:
                robot.lift()            

    def addWall(self,x1,y1,x2,y2):
        if not x1 == x2 and not y1 == y2:
            return
        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            if y1 == -1:
                y1 = y2
            for k in range(y1, y2+1):
                self.walls.setdefault((x1,k), []).append((x1+1,k))
                a, b = self.t+x1*self.t+self.t/2, self.n-(self.t+k*self.t)+self.t/2
                c, d = self.t+x1*self.t+self.t/2, self.n-(self.t+k*self.t)-self.t/2
                self.canvas.create_line(a, b+1, c, d-1, fill="black", width=3)                
        else:
            x1, x2 = min(x1, x2), max(x1, x2)
            if x1 == -1:
                x1 = x2
            for k in range(x1, x2+1):
                self.walls.setdefault((k,y1), []).append((k,y1+1))
                a, b = self.t+k*self.t-self.t/2, self.n-(self.t+y1*self.t)-self.t/2
                c, d = self.t+k*self.t+self.t/2, self.n-(self.t+y1*self.t)-self.t/2
                self.canvas.create_line(a-1, b, c+1, d, fill="black", width=3)

    def draw(self,x,y,d,img):
        if self.useImage:
            if img is not None:
                self.canvas.delete(img)
            x, y = self.t+x*self.t, self.n-(self.t+y*self.t)
            photo = self.photos[d/90]
            img = self.canvas.create_image(x, y, image=photo)            
            return img
        else:
            t, angle = self.t/2, 120
            x, y = self.t+x*self.t, self.n-(self.t+y*self.t)
            x1, y1 = x+3**0.5*t/2*cos(radians(d)), y-3**0.5*t/2*sin(radians(d))
            x2, y2 = x+t*cos(radians(d+angle)), y-t*sin(radians(d+angle))
            x3, y3 = x+t/4*cos(radians(d+180)), y-t/4*sin(radians(d+180))
            x4, y4 = x+t*cos(radians(d-angle)), y-t*sin(radians(d-angle))
            if img is not None:
                self.canvas.delete(img)
            img = self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, fill="blue")
            return img

    def erase(self,img):
        self.canvas.delete(img)

    def recordMove(self,count,x1,y1,x2,y2):
        for robot in self.robots[(x1,y1)]:
            if robot.count == count:
                self.robots[(x1,y1)].remove(robot)
                self.robots.setdefault((x2,y2), []).append(robot)                
                break

    def lift(self,img):
        self.canvas.lift(img)

    def refresh(self):
        self.canvas.update()
        self.pause()

    def register(self,x,y,robot):
        self.robots.setdefault((x,y), []).append(robot)

    def remove(self,x,y,robot):
        self.robots[(x,y)].remove(robot)


