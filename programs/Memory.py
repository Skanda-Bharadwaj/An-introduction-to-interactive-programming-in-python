# implementation of card game - Memory
import simplegui
import random

# helper function to initialize globals
def init():
    global cards, opened, state, first_open, second_open, score, moves
    
    state = 0  
    score = 0 
    moves = 0 
    first_open = -1 
    second_open = -1

    cards = []
    for x in range(8):
        cards.append(x)
    cards *= 2 
    random.shuffle(cards)
    opened = [False]*16

# define event handlers
def mouseclick(pos):
    global state, score, first_open, second_open, moves
    cardIndex = list(pos)[0]//50
    
    if not opened[cardIndex]:
        if state == 0: #just started
            first_open = cardIndex
            opened[cardIndex] = True
            state = 1
        elif state == 1: #one card flipped
            second_open = cardIndex
            opened[cardIndex] = True
            if cards[first_open] == cards[second_open]:
                score += 1
            state = 2
            moves += 1
            label.set_text("Moves = " + str(moves))
        else: #two cards flipped
            if cards[first_open] != cards[second_open]:
                opened[first_open], opened[second_open] = False, False
                first_open, second_open = -1, -1
            first_open = cardIndex
            opened[cardIndex] = True
            state = 1  
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        if opened[i]:
            canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 100], [i*50, 100]], 1, "Black", "White")
            canvas.draw_text(str(cards[i]), (i*50+11, 69), 55, "Black")
        else:
            canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 100], [i*50, 100]], 1, "Black", "Green")
    label.set_text("Moves = " + str(moves))

init()
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = " + str(moves))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
