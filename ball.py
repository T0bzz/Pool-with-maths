import pygame
from config import *
import pymunk


class Cueball:
    def __init__(self, x, y, mass, moment, speed):
        self.x = x
        self.y = y
        self.body = pymunk.Body(mass, moment)
        self.speed = speed
        self.shape = pymunk.Circle(self.body, CUEBALL_RADIUS)
        self.shape.friction = 10
        self.image = pygame.image.load(path.join(CUEBALL_FOLDER, "Cueball.png"))
        self.shape.elasticity = 1
        self.body.velocity = (10, 0)
        
        
    def slow_down(self):
        self.body.velocity = self.body.velocity.normalized() * self.speed


    def speed_down(self):
        if self.speed >= 0.01:
            if SLOW_BALL <= pygame.time.get_ticks() + 1 * 1000:
                self.speed -= 0.045
                if abs(self.body.velocity) < 0.036:
                    self.body.velocity = (0, 0)
                
        


    def move(self, eq):
        temp_pos = (self.x, self.y)
        self.x += 1
        try:
            self.y = eval(eq[3:])  # Skips 'y ='
            if type(self.y) not in (int, float):
                raise Exception("Unexpected eval() return")
        except:
            self.x, self.y = temp_pos  # Dont move if equation is invalid

class Ball(Cueball):
    def __init__(self, x, y, mass, moment, speed):
        self.body = pymunk.Body(mass, moment)
        self.speed = speed
        self.shape = pymunk.Circle(self.body, CUEBALL_RADIUS)
        self.shape.friction = 10
        self.image = pygame.image.load(path.join(CUEBALL_FOLDER, "Cueball.png"))
        self.shape.elasticity = 1
        self.body.velocity = (10, 0)
        self.body.position = (self.x, self.y)
        
        
    def slow_down(self):
        self.body.velocity = self.body.velocity.normalized() * self.speed


    def speed_down(self):
        if self.speed >= 0.01:
            if SLOW_BALL <= pygame.time.get_ticks() + 1 * 1000:
                self.speed -= 0.045
                if abs(self.body.velocity) < 0.036:
                    self.body.velocity = (0, 0)
                
    def move(self, eq):
        temp_pos = (self.x, self.y)
        self.x += 1
        try:
            self.y = eval(eq[3:])  # Skips 'y ='
            if type(self.y) not in (int, float):
                raise Exception("Unexpected eval() return")
        except:
           self.x, self.y = temp_pos  # Dont move if equation is invalid
    
class Red_Ball(Cueball):
    def __init__(self, position, mass, moment, speed):
        self.x, self.y = position
        self.speed = speed
        self.body = pymunk.Body(mass, moment)
        self.shape = pymunk.Circle(self.body, CUEBALL_RADIUS)
        self.image = pygame.image.load(path.join(BALL_FOLDER, "Redball.png"))
        self.shape.elasticity = 0.8
        self.body.velocity = (0, 0)
        self.body.position = (position)

    def slow_down(self):
        self.body.velocity = self.body.velocity.normalized() 

    def speed_down(self):
        if self.speed >= 0.01:
            if SLOW_BALL <= pygame.time.get_ticks() + 1 * 1000:
                self.speed -= 0.045
                if abs(self.body.velocity) < 0.036:
                    self.body.velocity = (0, 0)
            
    def move():
        pass
        self.image = pygame.image.load(path.join(BALL_FOLDER, "Redball.png"))
        self.shape.elasticity = 1
        self.body.velocity = (0, 0)
