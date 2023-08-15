import tkinter as tk
from random import shuffle

# define the deck
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

class Game:
    def __init__(self, master):
        self.master = master
        self.player_hand = []
        self.dealer_hand = []
        self.deck = cards.copy()
        shuffle(self.deck)

        # Create the labels for the hands
        self.player_label = tk.Label(master, text="")
        self.dealer_label = tk.Label(master, text="")
        self.player_label.pack()
        self.dealer_label.pack()

        # Create the buttons
        self.hit_button = tk.Button(master, text="Hit", command=self.hit)
        self.stand_button = tk.Button(master, text="Stand", command=self.stand)
        self.hit_button.pack()
        self.stand_button.pack()

        # Deal the initial hands
        self.player_hand.append(self.deal_card())
        self.player_hand.append(self.deal_card())
        self.dealer_hand.append(self.deal_card())
        self.dealer_hand.append(self.deal_card())
        self.update_labels()

    def deal_card(self):
        return self.deck.pop()

    def update_labels(self):
        self.player_label["text"] = "Your hand: " + ' '.join(map(str, self.player_hand)) + " total: " + str(sum(self.player_hand))
        self.dealer_label["text"] = "Dealer's hand: " + ' '.join(map(str, self.dealer_hand)) + " total: " + str(sum(self.dealer_hand))

    def hit(self):
        self.player_hand.append(self.deal_card())
        self.update_labels()
        if sum(self.player_hand) > 21:
            self.end_game("Player busts! Dealer wins.")

    def stand(self):
        while sum(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deal_card())
        self.update_labels()
        if sum(self.dealer_hand) > 21:
            self.end_game("Dealer busts! You win!")
        elif sum(self.dealer_hand) < sum(self.player_hand):
            self.end_game("You win!")
        else:
            self.end_game("Dealer wins.")

    def end_game(self, message):
        self.hit_button["state"] = "disabled"
        self.stand_button["state"] = "disabled"
        self.player_label["text"] = message

root = tk.Tk()
my_game = Game(root)
root.mainloop()
