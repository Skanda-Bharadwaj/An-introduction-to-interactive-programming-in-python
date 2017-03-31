# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

paddle1_pos = HEIGHT / 2.5 
paddle2_pos = HEIGHT / 2.5
paddle1_vel = 0
paddle2_vel = 0
paddle_vel = 5 


# initialize ball_pos and ball_vel for new bal in middle of table

ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0, 0]

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel[0] = -random.randrange(120, 240) / 100
    if direction == True:
        ball_vel[0] *= -1
    ball_vel[1] = -random.randrange(60, 80) / 100

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(0)
    paddle1_pos = HEIGHT / 2.5
    paddle2_pos = HEIGHT / 2.5

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 2, "white")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 2, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 2, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH) or ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS):        
        ball_vel[0] *= -1
        
        if (ball_pos[0] > WIDTH / 2):             
            if (ball_pos[1] < paddle2_pos or ball_pos[1] > paddle2_pos + PAD_HEIGHT):
                score1 += 1 
                spawn_ball(LEFT) 
            else: ball_vel[0] += 0.2 * ball_vel[0]
            
        if (ball_pos[0] < WIDTH / 2):
            if (ball_pos[1] < paddle1_pos or ball_pos[1] > paddle1_pos + PAD_HEIGHT):
                score2 += 1
                spawn_ball(RIGHT)
            else: ball_vel[0] += 0.2 * ball_vel[0]
        
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] *= -1
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "WHITE", "RED")
    
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos <= HEIGHT - PAD_HEIGHT and paddle1_vel > 0) or (paddle1_pos >= 0 and paddle1_vel < 0) :
        paddle1_pos += paddle1_vel    
    elif (paddle2_pos <= HEIGHT - PAD_HEIGHT and paddle2_vel > 0) or (paddle2_pos >= 0 and paddle2_vel < 0) :
        paddle2_pos += paddle2_vel  
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos], [PAD_WIDTH, paddle1_pos],[PAD_WIDTH, (paddle1_pos) + PAD_HEIGHT ],[0, (paddle1_pos) + PAD_HEIGHT]], 2, "white", "blue");
    canvas.draw_polygon([[WIDTH, paddle2_pos], [WIDTH - PAD_WIDTH, paddle2_pos],[WIDTH - PAD_WIDTH, (paddle2_pos) + PAD_HEIGHT ],[WIDTH, (paddle2_pos) + PAD_HEIGHT]], 2, "white", "blue");
    # determine whether paddle and ball collide    
    
    # draw scores
    canvas.draw_text(str(score1), [120, 100], 48, 'white')
    canvas.draw_text(str(score2), [450, 100], 48, 'white')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    #right side
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = +paddle_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -paddle_vel
    
    #left side
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -paddle_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = +paddle_vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel, paddel_vel
    
    #left side
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
        
    #right side
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background("green")
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New Game", new_game, 100)


# start frame
new_game()
frame.start()
