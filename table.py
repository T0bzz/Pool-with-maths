import pygame
import pymunk
import math
from math import cos, sin, tan, radians
from config import *
from pocket import Pocket
from cushion import Cushion
from ball import Cueball, Red_Ball, Yellow_Ball, Black_Ball
from ball import Cueball
from inputbox import Inputbox



class Table:
    def __init__(self, engine, display_surface, x, y):
        self.x = x
        self.y = y
        self.force = FORCE 
        self.max_force = MAX_FORCE
        self.direction = DIRECTION
        self.cushions = [Cushion(CUSHION1), Cushion(CUSHION2), Cushion(
            CUSHION3), Cushion(CUSHION4), Cushion(CUSHION5), Cushion(CUSHION6)]
        self.space = pymunk.Space()
        self.static_body = self.space.static_body
        self.engine = engine
        self.display_surface = display_surface
        self.image = pygame.image.load(
            path.join(TABLE_FOLDER, "Table.png")).convert_alpha()
        self.cueball = Cueball(260 - BALL_RADIUS * 2, 209 - BALL_RADIUS * 2, 5, self.static_body)
        self.redball = [Red_Ball(RED1, 5, self.static_body), Red_Ball(RED2, 5, self.static_body), Red_Ball(RED3, 5, self.static_body), Red_Ball(RED4, 5, self.static_body), Red_Ball(RED5, 5, self.static_body), Red_Ball(RED6, 5, self.static_body), Red_Ball(RED7, 5, self.static_body)]
        self.yellowball = [Yellow_Ball(Yellow1, 5, self.static_body), Yellow_Ball(Yellow2, 5, self.static_body), Yellow_Ball(Yellow3, 5, self.static_body), Yellow_Ball(Yellow4, 5, self.static_body), Yellow_Ball(Yellow5, 5, self.static_body), Yellow_Ball(Yellow6, 5, self.static_body), Yellow_Ball(Yellow7, 5, self.static_body)]
        self.blackball = Black_Ball(Black1, 1, self.static_body)
        self.pockets = [Pocket(CP_TL), Pocket(CP_TR), Pocket(CP_BL), Pocket(CP_BR), Pocket(MP_T), Pocket(MP_B)]
        self.cue_image_original = pygame.image.load(path.join(CUESTICK_FOLDER, "cue.png"))
        self.cue_image_scaled = pygame.transform.rotozoom(self.cue_image_original, 0, 0.09)

        self.space.add(self.cueball.body, self.cueball.shape, self.cueball.pivot)
        self.space.add(self.blackball.body, self.blackball.shape, self.blackball.pivot)
        for cushion in self.cushions:
            self.space.add(cushion.body, cushion.shape)
        for redball in self.redball:
            self.space.add(redball.body, redball.shape, redball.pivot)
        for yellowball in self.yellowball:
            self.space.add(yellowball.body, yellowball.shape, yellowball.pivot)
        for pockets in self.pockets:
            self.space.add(pockets.body, pockets.shape)
        

        self.input_box = Inputbox()


    def input_handler(self, event):
        self.input_box.input_handler(event)



    def draw(self):
        self.display_surface.blit(self.image, (self.x, self.y))
        self.display_surface.blit(
            self.cueball.image, ((self.cueball.body.position.x), (self.cueball.body.position.y)))
        self.display_surface.blit(
            self.blackball.image, ((self.blackball.body.position.x), (self.blackball.body.position.y)))
        for redball in self.redball:
            self.display_surface.blit(redball.image, ((redball.body.position.x), (redball.body.position.y)))
        for yellowball in self.yellowball:
            self.display_surface.blit(yellowball.image, ((yellowball.body.position.x), (yellowball.body.position.y)))
        text = INPUT_FONT.render(
           self.input_box.angle_input, True, pygame.Color("turquoise"))
        self.display_surface.blit(text, text.get_rect())
        self.display_surface.blit(self.cue_image_scaled, (self.cueball.body.position.x-200, self.cueball.body.position.y-5))

    def pocket(self):
        #Red and yellow balls
        for pocket in pocket_coords:
            for ball in self.redball:
                #print(pocket_coords)
                #print(ball.body.position.x)
                red_x_dist = abs((ball.body.position.x) - (pocket[0]))
                red_y_dist = abs((ball.body.position.y) - (pocket[1]))
                red_dist = math.sqrt((red_x_dist**2) + (red_y_dist**2))
                if red_dist < POCKET_RADIUS:
                    self.display_surface.blit(ball.image, (0, 0))
                    self.space.remove(ball.body, ball.shape)
                    self.redball.remove(ball)
        for pocket in pocket_coords:
            for ball in self.yellowball:
                yellow_x_dist = abs((ball.body.position.x) - (pocket[0]))
                yellow_y_dist = abs((ball.body.position.y) - (pocket[1]))
                yellow_dist = math.sqrt((yellow_x_dist**2) + (yellow_y_dist**2))
                if yellow_dist < POCKET_RADIUS:
                    self.space.remove(ball.body, ball.shape)
                    self.yellowball.remove(ball)
                    self.display_surface.blit(ball.image, (0, 0))
        for pocket in pocket_coords:
            cue_x_dist = abs((self.cueball.body.position.x) - (pocket[0]))
            cue_y_dist = abs((self.cueball.body.position.y) - (pocket[1]))
            cue_dist = math.sqrt((cue_x_dist**2) + (cue_y_dist**2))
            if cue_dist < POCKET_RADIUS:
                print("self.cueball.image")
                self.display_surface.blit(self.cueball.image, (260 - BALL_RADIUS * 2, 209 - BALL_RADIUS * 2))
                self.cueball.body.velocity = (0, 0)


    def ball_velocity(self):
        stopped = False
        if self.cueball.body.velocity == (0, 0) and self.blackball.body.velocity == (0, 0) and self.redball[0].body.velocity == (0, 0) and self.redball[1].body.velocity == (0, 0) and self.redball[2].body.velocity == (0, 0) and self.redball[3].body.velocity == (0, 0) and self.redball[4].body.velocity == (0, 0) and self.redball[5].body.velocity == (0, 0) and self.redball[6].body.velocity == (0, 0) and self.yellowball[0].body.velocity == (0, 0) and self.yellowball[1].body.velocity == (0, 0) and self.yellowball[2].body.velocity == (0, 0) and self.yellowball[3].body.velocity == (0, 0) and self.yellowball[4].body.velocity == (0, 0) and self.yellowball[5].body.velocity == (0, 0) and self.yellowball[6].body.velocity == (0, 0):
            stopped = True
        return stopped
        


    def update(self):
        print("----------------------------------------------------------------------------------------------------")
        self.pocket()
        print("Redball:", self.redball[1].body.velocity)
        print("Cueball:", self.cueball.body.velocity)
        print("Cueball position y:", self.cueball.body.position.y)
        self.space.step(1/480)
        if self.input_box.play and self.ball_velocity() == True:
            print("Hello")
            self.cueball.move((self.cueball.body.position), self.input_box.angle_input)
        else:
            pass
        if self.input_box.play:
            self.input_box.play = False

