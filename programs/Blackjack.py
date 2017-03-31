# Mini-project #6 - Blackjack
import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
score = 0
to_player = "Hit or Stand?"
msg = ""

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, 
                          [pos[0] + CARD_CENTER[0], 
                           pos[1] + CARD_CENTER[1]], 
                          CARD_SIZE)
        
    def drawBack(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, 
                          [pos[0] + CARD_BACK_CENTER[0] + 1, 
                           pos[1] + CARD_BACK_CENTER[1] + 1], 
                          CARD_BACK_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        strRepforCard = ""
        for card in self.cards:
            strRepforCard = strRepforCard + str(card) + " "
        return "Hand" + strRepforCard.strip()

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        totalCardValue = 0
        bAce = False
        for card in self.cards:
            totalCardValue += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                bAce = True
        if bAce and totalCardValue < 12:
            totalCardValue += 10
        return totalCardValue
   
    def draw(self, canvas, pos):
        for card in self.cards:
            pos[0] = pos[0] + CARD_SIZE[0] + 20
            card.draw(canvas, pos)
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        strRepforCard = ""
        for card in self.cards:
            strRepforCard = strRepforCard + str(card) + " "
        return "Deck contains " + strRepforCard.strip()

#define event handlers for buttons
def deal():
    global in_play, myDeck, playerHand, dealerHand, to_player, score, show_player, show_dealer, msg
    if in_play:
        score -= 1
        in_play = False
        deal()
    else:    
        myDeck = Deck()
        playerHand = Hand()
        dealerHand = Hand()
        myDeck.shuffle()
        playerHand.add_card(myDeck.deal_card())
        playerHand.add_card(myDeck.deal_card())
        dealerHand.add_card(myDeck.deal_card())
        dealerHand.add_card(myDeck.deal_card())
        to_player = "Hit or Stand?"
        show_player = "Player"
        show_dealer = "Dealer"
        msg = ""
        in_play = True

def hit():
    global in_play, myDeck, playerHand, score, to_player, show_player, msg
    if in_play:
        if playerHand.get_value() < 22:
            playerHand.add_card(myDeck.deal_card())
            if playerHand.get_value() > 21:
                show_player = "Busted!"
                msg = "You've busted! You loose!"
                score -= 1
                to_player = "New deal?"
                in_play = False
       
def stand():
    global in_play, dealerHand, playerHand, score, to_player, show_dealer, msg
    if in_play:
        while (dealerHand.get_value() < 17):
            dealerHand.add_card(myDeck.deal_card())
        if dealerHand.get_value() > 21:
            show_dealer = "Busted!"
            msg = "Dealer busted! You win!"
            score += 1
            to_player = "New deal?"
            in_play = False
        elif playerHand.get_value() > dealerHand.get_value():
            msg = "Your hand's stronger! You win!"
            score += 1
            to_player = "New deal?"
            in_play = False
        else:
            msg = "Your hand's weaker! You loose!"
            score -= 1
            to_player = "New deal?"
            in_play = False

# draw handler    
def draw(canvas):
    canvas.draw_text("Blackjack", (60, 100), 40, "White")
    lDealer = canvas.draw_text(show_dealer, (60, 185), 33, "Black")
    lPlayer = canvas.draw_text(show_player, (60, 385), 33, "Black")
    lto_player = canvas.draw_text(to_player, (250, 385), 33, "Black")
    lMessage = canvas.draw_text(msg, (250, 185), 25, "White")
    lScore = canvas.draw_text("Score: " + str(score), (450, 100), 33, "White")
    dealerHand.draw(canvas, [-65, 200])
    playerHand.draw(canvas, [-65, 400])
    if in_play:
        dealerHand.cards[0].drawBack(canvas, [28, 200])
        

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
deal()
