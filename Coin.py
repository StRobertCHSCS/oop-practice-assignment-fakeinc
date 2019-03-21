import random


# Define your Coin class here
class Coin:
    def __init__(self):
        self.face = random.choice(["heads", "tails"])

    def get_face(self):
        return self.face

    def flip(self):
        self.face = random.choice(["heads", "tails"])


if __name__ == '__main__':
    # put your code that utilizes your Coin class here

    # get a coin
    coin_1 = Coin()

    # set the total of heads and tails both equal to zero
    coin_1_heads = 0
    coin_1_tails = 0

    # loop 1000 times
    for i in range(1000):

        # count total heads
        if coin_1.get_face() == "heads":
            coin_1_heads += 1

        # count total tails
        else:
            coin_1_tails += 1

        # flip it
        coin_1.flip()

    # output total heads and tails
    print("Total number of \"heads\" is {0}".format(coin_1_heads))
    print("Total number of \"tails\" is {0}".format(coin_1_tails))
