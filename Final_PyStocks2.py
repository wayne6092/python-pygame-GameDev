import random
import sys
import pygame.sprite
from Stockmenu import StockMenu
# from pygame.locals import *
from button import Button
from sprite_sound import *

# container classes
# Groups used for collision and sprite removal
exchanges = pygame.sprite.Group(())
player = pygame.sprite.Group(())
score = pygame.sprite.Group(())
bouncer = pygame.sprite.Group(())
objects = pygame.sprite.Group(())
BG = pygame.sprite.Group(())
boss = pygame.sprite.Group(())
tv = pygame.sprite.Group(())


# This class will determine stock score based on all game play, then StockScore.stockScore will be used to write
# to highscore file through WinLooper Class
class StockScore:  # Unique random scoring depending on each choice made by player
    stockScore = random.randint(1000, 3000)

    def __init__(self, stockScore):
        StockScore.__init__(self, stockScore)
        self.stockScore = stockScore

    @staticmethod
    def update():
        v = random.randint(1, 5)
        # Uses attributes from class Points to determine stockScore
        # Uses values from stockPrice list of strings and ints
        # Uses the random number from computer score
        # Uses extra "Bonus random values" to add unique score
        # Use condition statement for each user choice to give unique score
        if userData["Type of trader"] == "Bull":
            if userData["Stock Chosen"] == "MSFT":
                if Points.count1 == 0 or Points.count2 == 0:
                    Points.count2 = 1
                    Points.count1 = 1

                if userData["Suit"] == "Blue":
                    Bonus = random.randint(1, 6)
                    Bonus2 = random.randint(100, 5000)
                    StockScore.stockScore = (stockPrice[0][1] + (Number.computer * v // 2)
                                             * Bonus // Points.count2) + Bonus2 // Points.count1
                    return StockScore.stockScore

                elif userData["Suit"] == "Red":
                    Bonus = random.randint(1, 2)
                    Bonus2 = random.randint(100, 8000)
                    StockScore.stockScore = (stockPrice[0][1] + (Number.computer * v // 2)
                                             * Bonus // Points.count2) + Bonus2 // Points.count1
                    return StockScore.stockScore

                elif userData["Suit"] == "Green":
                    Bonus = random.randint(1, 3)
                    Bonus2 = random.randint(100, 7000)
                    StockScore.stockScore = (stockPrice[0][1] + (Number.computer * v // 2)
                                             * Bonus // Points.count2) + Bonus2 // Points.count1
                    return StockScore.stockScore

                elif userData["Suit"] == "Purple":
                    Bonus = random.randint(1, 9)
                    Bonus2 = random.randint(100, 2000)
                    StockScore.stockScore = (stockPrice[0][1] + (Number.computer * v // 2)
                                             * Bonus // Points.count2) + Bonus2 // Points.count1
                    return StockScore.stockScore

            elif userData["Stock Chosen"] == "BBIG":
                if Points.count1 == 0 or Points.count2 == 0:
                    Points.count2 = 1
                    Points.count1 = 1

                if userData["Suit"] == "Blue":
                    Bonus = random.randint(1, 6)
                    Bonus2 = random.randint(100, 5000)
                    StockScore.stockScore = (stockPrice[1][1] + (Number.computer * v // 2)
                                             * Bonus // Points.count2) + Bonus2 // Points.count1
                    return StockScore.stockScore

                elif userData["Suit"] == "Red":
                    Bonus = random.randint(1, 2)
                    Bonus2 = random.randint(100, 8000)
                    StockScore.stockScore = (stockPrice[1][1] + (Number.computer * v // 2)
                                             * Bonus // Points.count2) + Bonus2 // Points.count1
                    return StockScore.stockScore

                elif userData["Suit"] == "Green":
                    Bonus = random.randint(1, 3)
                    Bonus2 = random.randint(100, 7000)
                    StockScore.stockScore = (stockPrice[1][1] + (Number.computer * v // 2)
                                             * Bonus // Points.count2) + Bonus2 // Points.count1
                    return StockScore.stockScore

                elif userData["Suit"] == "Purple":
                    Bonus = random.randint(1, 9)
                    Bonus2 = random.randint(100, 2000)
                    StockScore.stockScore = (stockPrice[1][1] + (Number.computer * v // 2)
                                             * Bonus // Points.count2) + Bonus2 // Points.count1
                    return StockScore.stockScore

            elif userData["Stock Chosen"] == "AMC":
                if Points.count1 == 0 or Points.count2 == 0:
                    Points.count2 = 1
                    Points.count1 = 1

                if userData["Suit"] == "Blue":
                    Bonus = random.randint(1, 6)
                    Bonus2 = random.randint(100, 5000)
                    StockScore.stockScore = (stockPrice[2][1] + (Number.computer * v // 2)
                                             * Bonus // Points.count2) + Bonus2 // Points.count1
                    return StockScore.stockScore

                elif userData["Suit"] == "Red":
                    Bonus = random.randint(1, 2)
                    Bonus2 = random.randint(100, 8000)
                    StockScore.stockScore = (stockPrice[2][1] + (Number.computer * v // 2)
                                             * Bonus // Points.count2) + Bonus2 // Points.count1
                    return StockScore.stockScore

                elif userData["Suit"] == "Green":
                    Bonus = random.randint(1, 3)
                    Bonus2 = random.randint(100, 7000)
                    StockScore.stockScore = (stockPrice[2][1] + (Number.computer * v // 2)
                                             * Bonus // Points.count2) + Bonus2 // Points.count1
                    return StockScore.stockScore

                elif userData["Suit"] == "Purple":
                    Bonus = random.randint(1, 9)
                    Bonus2 = random.randint(100, 2000)
                    StockScore.stockScore = (stockPrice[2][1] + (Number.computer * v // 2)
                                             * Bonus // Points.count2) + Bonus2 // Points.count1
                    return StockScore.stockScore

            elif userData["Stock Chosen"] == "GME":
                if Points.count1 == 0 or Points.count2 == 0:
                    Points.count2 = 1
                    Points.count1 = 1

                if userData["Suit"] == "Blue":
                    Bonus = random.randint(1, 6)
                    Bonus2 = random.randint(100, 5000)
                    StockScore.stockScore = (stockPrice[3][1] + (Number.computer * v // 2)
                                             * Bonus // Points.count2) + Bonus2 // Points.count1
                    return StockScore.stockScore

                elif userData["Suit"] == "Red":
                    Bonus = random.randint(1, 2)
                    Bonus2 = random.randint(100, 8000)
                    StockScore.stockScore = (stockPrice[3][1] + (Number.computer * v // 2)
                                             * Bonus // Points.count2) + Bonus2 // Points.count1
                    return StockScore.stockScore

                elif userData["Suit"] == "Green":
                    Bonus = random.randint(1, 3)
                    Bonus2 = random.randint(100, 7000)
                    StockScore.stockScore = (stockPrice[3][1] + (Number.computer * v // 2)
                                             * Bonus // Points.count2) + Bonus2 // Points.count1
                    return StockScore.stockScore

                elif userData["Suit"] == "Purple":
                    Bonus = random.randint(1, 9)
                    Bonus2 = random.randint(100, 2000)
                    StockScore.stockScore = (stockPrice[3][1] + (Number.computer * v // 2)
                                             * Bonus // Points.count2) + Bonus2 // Points.count1
                    return StockScore.stockScore

        elif userData["Type of trader"] == "Bear":
            if userData["Stock Chosen"] == "MSFT":
                if Points.count1 == 0 or Points.count2 == 0:
                    Points.count2 = 1
                    Points.count1 = 1

                if userData["Suit"] == "Blue":
                    Bonus = random.randint(1, 4)
                    Bonus2 = random.randint(1, 4000)
                    StockScore.stockScore = ((Bonus2 // Points.count1) + stockPrice[0][1] + (Number.computer * v // 2))\
                                            * (Bonus // Points.count2)
                    return StockScore.stockScore

                elif userData["Suit"] == "Red":
                    Bonus = random.randint(1, 4)
                    Bonus2 = random.randint(1, 4000)
                    StockScore.stockScore = ((Bonus2 // Points.count1) + stockPrice[0][1] + (Number.computer * v // 2))\
                                            * (Bonus // Points.count2)
                    return StockScore.stockScore

                elif userData["Suit"] == "Green":
                    Bonus = random.randint(1, 4)
                    Bonus2 = random.randint(1, 4000)
                    StockScore.stockScore = ((Bonus2 // Points.count1) + stockPrice[0][1] + (Number.computer * v // 2))\
                                            * (Bonus // Points.count2)
                    return StockScore.stockScore

                elif userData["Suit"] == "Purple":
                    Bonus = random.randint(1, 4)
                    Bonus2 = random.randint(1, 4000)
                    StockScore.stockScore = ((Bonus2 // Points.count1) + stockPrice[0][1] + (Number.computer * v // 2))\
                                            * (Bonus // Points.count2)
                    return StockScore.stockScore

            elif userData["Stock Chosen"] == "BBIG":
                if Points.count1 == 0 or Points.count2 == 0:
                    Points.count2 = 1
                    Points.count1 = 1

                if userData["Suit"] == "Blue":
                    Bonus = random.randint(1, 4)
                    Bonus2 = random.randint(1, 4000)
                    StockScore.stockScore = ((Bonus2 // Points.count1) + stockPrice[1][1] + (Number.computer * v // 2))\
                                            * (Bonus // Points.count2)
                    return StockScore.stockScore

                elif userData["Suit"] == "Red":
                    Bonus = random.randint(1, 5)
                    Bonus2 = random.randint(1, 2000)
                    StockScore.stockScore = ((Bonus2 // Points.count1) + stockPrice[1][1] + (Number.computer * v // 2))\
                                            * (Bonus // Points.count2)
                    return StockScore.stockScore

                elif userData["Suit"] == "Green":
                    Bonus = random.randint(1, 3)
                    Bonus2 = random.randint(1, 6000)
                    StockScore.stockScore = ((Bonus2 // Points.count1) + stockPrice[1][1] + (Number.computer * v // 2))\
                                            * (Bonus // Points.count2)
                    return StockScore.stockScore

                elif userData["Suit"] == "Purple":
                    Bonus = random.randint(1, 7)
                    Bonus2 = random.randint(1, 2000)
                    StockScore.stockScore = ((Bonus2 // Points.count1) + stockPrice[1][1] + (Number.computer * v // 2))\
                                            * (Bonus // Points.count2)
                    return StockScore.stockScore

            elif userData["Stock Chosen"] == "AMC":
                if Points.count1 == 0 or Points.count2 == 0:
                    Points.count2 = 1
                    Points.count1 = 1

                if userData["Suit"] == "Blue":
                    Bonus = random.randint(1, 8)
                    Bonus2 = random.randint(1, 3000)
                    StockScore.stockScore = ((Bonus2 // Points.count1) + stockPrice[2][1] + (Number.computer * v // 2))\
                                            * (Bonus // Points.count2)
                    return StockScore.stockScore

                elif userData["Suit"] == "Red":
                    Bonus = random.randint(1, 9)
                    Bonus2 = random.randint(1, 2500)
                    StockScore.stockScore = ((Bonus2 // Points.count1) + stockPrice[2][1] + (Number.computer * v // 2))\
                                            * (Bonus // Points.count2)
                    return StockScore.stockScore

                elif userData["Suit"] == "Green":
                    Bonus = random.randint(1, 10)
                    Bonus2 = random.randint(1, 5000)
                    StockScore.stockScore = ((Bonus2 // Points.count1) + stockPrice[2][1] + (Number.computer * v // 2))\
                                            * (Bonus // Points.count2)
                    return StockScore.stockScore

                elif userData["Suit"] == "Purple":
                    Bonus = random.randint(1, 4)
                    Bonus2 = random.randint(1, 12000)
                    StockScore.stockScore = ((Bonus2 // Points.count1) + stockPrice[2][1] + (Number.computer * v // 2))\
                                            * (Bonus // Points.count2)
                    return StockScore.stockScore

            elif userData["Stock Chosen"] == "GME":
                if Points.count1 == 0 or Points.count2 == 0:
                    Points.count2 = 1
                    Points.count1 = 1

                if userData["Suit"] == "Blue":
                    Bonus = random.randint(1, 7)
                    Bonus2 = random.randint(1, 4000)
                    StockScore.stockScore = ((Bonus2 // Points.count1) + stockPrice[3][1] + (Number.computer * v // 2))\
                                            * (Bonus // Points.count2)
                    return StockScore.stockScore

                elif userData["Suit"] == "Red":
                    Bonus = random.randint(1, 5)
                    Bonus2 = random.randint(1, 3444)
                    StockScore.stockScore = ((Bonus2 // Points.count1) + stockPrice[3][1] + (Number.computer * v // 2))\
                                            * (Bonus // Points.count2)
                    return StockScore.stockScore

                elif userData["Suit"] == "Green":
                    Bonus = random.randint(1, 6)
                    Bonus2 = random.randint(1, 7777)
                    StockScore.stockScore = ((Bonus2 // Points.count1) + stockPrice[3][1] + (Number.computer * v // 2))\
                                            * (Bonus // Points.count2)
                    return StockScore.stockScore

                elif userData["Suit"] == "Purple":
                    Bonus = random.randint(1, 3)
                    Bonus2 = random.randint(1, 8000)
                    StockScore.stockScore = ((Bonus2 // Points.count1) + stockPrice[3][1] + (Number.computer * v // 2))\
                                            * (Bonus // Points.count2)
                    return StockScore.stockScore

        elif userData["Type of trader"] == "Value":
            if userData["Stock Chosen"] == "MSFT":
                if userData["Suit"] == "Blue":
                    Bonus = random.randint(1, 9999)
                    StockScore.stockScore = (Points.count2 * 200) - stockPrice[0][1] + \
                                            (Number.computer * v // 2) + Bonus - (Points.count1 * 300)
                    return StockScore.stockScore

                elif userData["Suit"] == "Red":
                    Bonus = random.randint(1, 12000)
                    StockScore.stockScore = (Points.count2 * 200) - stockPrice[0][1] + \
                                            (Number.computer * v // 2) + Bonus - (Points.count1 * 300)
                    return StockScore.stockScore

                elif userData["Suit"] == "Green":
                    Bonus = random.randint(1, 15555)
                    StockScore.stockScore = (Points.count2 * 200) - stockPrice[0][1] + \
                                            (Number.computer * v // 2) + Bonus - (Points.count1 * 300)
                    return StockScore.stockScore

                elif userData["Suit"] == "Purple":
                    Bonus = random.randint(1, 7777)
                    StockScore.stockScore = (Points.count2 * 200) - stockPrice[0][1] + \
                                            (Number.computer * v // 2) + Bonus - (Points.count1 * 300)
                    return StockScore.stockScore

            elif userData["Stock Chosen"] == "BBIG":
                if userData["Suit"] == "Blue":
                    Bonus = random.randint(1, 9999)
                    StockScore.stockScore = (Points.count2 * 200) - stockPrice[1][1] + \
                                            (Number.computer * v // 2) + Bonus - (Points.count1 * 300)
                    return StockScore.stockScore

                elif userData["Suit"] == "Red":
                    Bonus = random.randint(1, 12000)
                    StockScore.stockScore = (Points.count2 * 200) - stockPrice[1][1] + \
                                            (Number.computer * v // 2) + Bonus - (Points.count1 * 300)
                    return StockScore.stockScore

                elif userData["Suit"] == "Green":
                    Bonus = random.randint(1, 15555)
                    StockScore.stockScore = (Points.count2 * 200) - stockPrice[1][1] + \
                                            (Number.computer * v // 2) + Bonus - (Points.count1 * 300)
                    return StockScore.stockScore

                elif userData["Suit"] == "Purple":
                    Bonus = random.randint(1, 7777)
                    StockScore.stockScore = (Points.count2 * 200) - stockPrice[1][1] + \
                                            (Number.computer * v // 2) + Bonus - (Points.count1 * 300)
                    return StockScore.stockScore

            elif userData["Stock Chosen"] == "AMC":
                if userData["Suit"] == "Blue":
                    Bonus = random.randint(1, 9999)
                    StockScore.stockScore = (Points.count2 * 200) - stockPrice[2][1] + \
                                            (Number.computer * v // 2) + Bonus - (Points.count1 * 300)
                    return StockScore.stockScore

                elif userData["Suit"] == "Red":
                    Bonus = random.randint(1, 12000)
                    StockScore.stockScore = (Points.count2 * 200) - stockPrice[2][1] + \
                                            (Number.computer * v // 2) + Bonus - (Points.count1 * 300)
                    return StockScore.stockScore

                elif userData["Suit"] == "Green":
                    Bonus = random.randint(1, 15555)
                    StockScore.stockScore = (Points.count2 * 200) - stockPrice[2][1] + \
                                            (Number.computer * v // 2) + Bonus - (Points.count1 * 300)
                    return StockScore.stockScore

                elif userData["Suit"] == "Purple":
                    Bonus = random.randint(1, 7777)
                    StockScore.stockScore = (Points.count2 * 200) - stockPrice[2][1] + \
                                            (Number.computer * v // 2) + Bonus - (Points.count1 * 300)
                    return StockScore.stockScore

            elif userData["Stock Chosen"] == "GME":
                if userData["Suit"] == "Blue":
                    Bonus = random.randint(1, 9999)
                    StockScore.stockScore = (Points.count2 * 200) - stockPrice[3][1] + \
                                            (Number.computer * v // 2) + Bonus - (Points.count1 * 300)
                    return StockScore.stockScore

                elif userData["Suit"] == "Red":
                    Bonus = random.randint(1, 12000)
                    StockScore.stockScore = (Points.count2 * 200) - stockPrice[3][1] + \
                                            (Number.computer * v // 2) + Bonus - (Points.count1 * 300)
                    return StockScore.stockScore

                elif userData["Suit"] == "Green":
                    Bonus = random.randint(1, 15555)
                    StockScore.stockScore = (Points.count2 * 200) - stockPrice[3][1] + \
                                            (Number.computer * v // 2) + Bonus - (Points.count1 * 300)
                    return StockScore.stockScore

                elif userData["Suit"] == "Purple":
                    Bonus = random.randint(1, 7777)
                    StockScore.stockScore = (Points.count2 * 200) - stockPrice[3][1] + \
                                            (Number.computer * v // 2) + Bonus - (Points.count1 * 300)
                    return StockScore.stockScore

        elif userData["Type of trader"] == "Swing":
            if userData["Stock Chosen"] == "MSFT":
                if userData["Suit"] == "Blue":
                    Bonus = random.randint(1, 15)
                    Bonus2 = random.randint(1, 10)
                    Bonus3 = random.randint(1, 9999)
                    StockScore.stockScore = ((stockPrice[0][1] + (Number.computer * v // 2) * (Bonus - Points.count1))
                                             // (Bonus2 + Points.count2)) + Bonus3
                    return StockScore.stockScore

                elif userData["Suit"] == "Red":
                    Bonus = random.randint(1, 20)
                    Bonus2 = random.randint(1, 13)
                    Bonus3 = random.randint(1, 7777)
                    StockScore.stockScore = ((stockPrice[0][1] + (Number.computer * v // 2) * (Bonus - Points.count1))
                                             // (Bonus2 + Points.count2)) + Bonus3
                    return StockScore.stockScore

                elif userData["Suit"] == "Green":
                    Bonus = random.randint(1, 14)
                    Bonus2 = random.randint(1, 5)
                    Bonus3 = random.randint(1, 11111)
                    StockScore.stockScore = ((stockPrice[0][1] + (Number.computer * v // 2) * (Bonus - Points.count1))
                                             // (Bonus2 + Points.count2)) + Bonus3
                    return StockScore.stockScore

                elif userData["Suit"] == "Purple":
                    Bonus = random.randint(1, 14)
                    Bonus2 = random.randint(1, 8)
                    Bonus3 = random.randint(1, 15555)
                    StockScore.stockScore = ((stockPrice[0][1] + (Number.computer * v // 2) * (Bonus - Points.count1))
                                             // (Bonus2 + Points.count2)) + Bonus3
                    return StockScore.stockScore

            elif userData["Stock Chosen"] == "BBIG":
                if userData["Suit"] == "Blue":
                    Bonus = random.randint(1, 15)
                    Bonus2 = random.randint(1, 10)
                    Bonus3 = random.randint(1, 9999)
                    StockScore.stockScore = ((stockPrice[1][1] + (Number.computer * v // 2) * (Bonus - Points.count1))
                                             // (Bonus2 + Points.count2)) + Bonus3
                    return StockScore.stockScore

                elif userData["Suit"] == "Red":
                    Bonus = random.randint(1, 20)
                    Bonus2 = random.randint(1, 13)
                    Bonus3 = random.randint(1, 7777)
                    StockScore.stockScore = ((stockPrice[1][1] + (Number.computer * v // 2) * (Bonus - Points.count1))
                                             // (Bonus2 + Points.count2)) + Bonus3
                    return StockScore.stockScore

                elif userData["Suit"] == "Green":
                    Bonus = random.randint(1, 14)
                    Bonus2 = random.randint(1, 5)
                    Bonus3 = random.randint(1, 11111)
                    StockScore.stockScore = ((stockPrice[1][1] + (Number.computer * v // 2) * (Bonus - Points.count1))
                                             // (Bonus2 + Points.count2)) + Bonus3
                    return StockScore.stockScore

                elif userData["Suit"] == "Purple":
                    Bonus = random.randint(1, 14)
                    Bonus2 = random.randint(1, 8)
                    Bonus3 = random.randint(1, 15555)
                    StockScore.stockScore = ((stockPrice[1][1] + (Number.computer * v // 2) * (Bonus - Points.count1))
                                             // (Bonus2 + Points.count2)) + Bonus3
                    return StockScore.stockScore

            elif userData["Stock Chosen"] == "AMC":
                if userData["Suit"] == "Blue":
                    Bonus = random.randint(1, 15)
                    Bonus2 = random.randint(1, 10)
                    Bonus3 = random.randint(1, 9999)
                    StockScore.stockScore = ((stockPrice[2][1] + (Number.computer * v // 2) * (Bonus - Points.count1))
                                             // (Bonus2 + Points.count2)) + Bonus3
                    return StockScore.stockScore

                elif userData["Suit"] == "Red":
                    Bonus = random.randint(1, 20)
                    Bonus2 = random.randint(1, 13)
                    Bonus3 = random.randint(1, 7777)
                    StockScore.stockScore = ((stockPrice[2][1] + (Number.computer * v // 2) * (Bonus - Points.count1))
                                             // (Bonus2 + Points.count2)) + Bonus3
                    return StockScore.stockScore

                elif userData["Suit"] == "Green":
                    Bonus = random.randint(1, 14)
                    Bonus2 = random.randint(1, 5)
                    Bonus3 = random.randint(1, 11111)
                    StockScore.stockScore = ((stockPrice[2][1] + (Number.computer * v // 2) * (Bonus - Points.count1))
                                             // (Bonus2 + Points.count2)) + Bonus3
                    return StockScore.stockScore

                elif userData["Suit"] == "Purple":
                    Bonus = random.randint(1, 14)
                    Bonus2 = random.randint(1, 8)
                    Bonus3 = random.randint(1, 15555)
                    StockScore.stockScore = ((stockPrice[2][1] + (Number.computer * v // 2) * (Bonus - Points.count1))
                                             // (Bonus2 + Points.count2)) + Bonus3
                    return StockScore.stockScore

            elif userData["Stock Chosen"] == "GME":
                # chance = list(range(1, 10))
                # results = random.choices(colors, weights=[18, 18, 2], k=10)
                if userData["Suit"] == "Blue":
                    Bonus = random.randint(1, 15)
                    Bonus2 = random.randint(1, 10)
                    Bonus3 = random.randint(1, 9999)
                    StockScore.stockScore = ((stockPrice[3][1] + (Number.computer * v // 2) * (Bonus - Points.count1))
                                             // (Bonus2 + Points.count2)) + Bonus3
                    return StockScore.stockScore

                elif userData["Suit"] == "Red":
                    Bonus = random.randint(1, 20)
                    Bonus2 = random.randint(1, 13)
                    Bonus3 = random.randint(1, 7777)
                    StockScore.stockScore = ((stockPrice[3][1] + (Number.computer * v // 2) * (Bonus - Points.count1))
                                             // (Bonus2 + Points.count2)) + Bonus3
                    return StockScore.stockScore

                elif userData["Suit"] == "Green":
                    Bonus = random.randint(1, 14)
                    Bonus2 = random.randint(1, 5)
                    Bonus3 = random.randint(1, 11111)
                    StockScore.stockScore = ((stockPrice[3][1] + (Number.computer * v // 2) * (Bonus - Points.count1))
                                             // (Bonus2 + Points.count2)) + Bonus3
                    return StockScore.stockScore

                elif userData["Suit"] == "Purple":
                    Bonus = random.randint(1, 14)
                    Bonus2 = random.randint(1, 8)
                    Bonus3 = random.randint(1, 15555)
                    StockScore.stockScore = ((stockPrice[3][1] + (Number.computer * v // 2) * (Bonus - Points.count1))
                                             // (Bonus2 + Points.count2)) + Bonus3
                    return StockScore.stockScore

        else:
            StockScore.stockScore = (stockPrice[0][1] + (Number.computer * v // 2))
            return StockScore.stockScore


# This class is called in the game loops to write and read from the high score file
# Uses StockScore.stockScore from StockScore class
class WinLooper:
    hScore = 0
    stockScore = StockScore.stockScore

    def __init__(self, hScore):
        WinLooper.__init__(self, hScore)
        self.hScore = hScore

    @staticmethod
    def update():

        try:
            text_file = open('highscores.txt', 'r')
        except FileNotFoundError:
            text_file = open('highscores.txt', 'w')
            text_file.close()
            text_file = open('highscores.txt', 'r')
        try:
            WinLooper.hScore = int(text_file.readline())
            line1 = text_file.readline()
            line2 = text_file.readline()
            line3 = text_file.readline()
            line4 = text_file.readline()
            line5 = text_file.readline()
            score2 = int(text_file.readline())
            line6 = text_file.readline()
            line7 = text_file.readline()
            line8 = text_file.readline()
            line9 = text_file.readline()
            line10 = text_file.readline()
            allScore = text_file.read()
        except ValueError:
            WinLooper.hScore = 3000
            line1 = "Type of Trader: Bull\n"
            line2 = "Suit Color: Blue\n"
            line3 = "Investor Name: Unknown\n"
            line4 = "Stock Chosen: Unknown\n"
            line5 = "*****************************\n"
            score2 = 2000
            line6 = "Type of Trader: allscore \n"
            line7 = "Suit Color: Blue\n"
            line8 = "Investor Name: Unknown\n"
            line9 = "Stock Chosen: Unknown\n"
            line10 = "*****************************\n"
            allScore = "-----End of Leaderboards-----"
        print(WinLooper.hScore)
        print(line1)
        print(line2)
        print(line3)
        print(line4)
        print(str(score2))

        text_file.close()

        if StockScore.stockScore > WinLooper.hScore:
            text_file = open('highscores.txt', 'w')

            oldHScore = WinLooper.hScore

            hScore = StockScore.stockScore

            print(hScore)
            text_file.write(str(StockScore.stockScore) +
                            "\nType of Trader: " + userData["Type of trader"] +
                            "\nSuit Color: " + userData["Suit"] +
                            "\nInvestor Name: " + userData["Name"] +
                            '\nStock Chosen: ' + userData["Stock Chosen"] +
                            '\n*****************************'
                            )
            text_file.write("\n" + str(oldHScore) + "\n")
            text_file.write(line1 + line2 + line3 + line4 + line5)

            text_file.write(str(score2) + "\n")
            text_file.write(line6 + line7 + line8 + line9 + line10)
            text_file.write(allScore)
            text_file.close()
            return WinLooper.hScore

        elif WinLooper.hScore > StockScore.stockScore > score2:
            text_file = open('highscores.txt', 'w')

            print(WinLooper.hScore)

            text_file.write(str(WinLooper.hScore) + "\n")
            text_file.write(line1 + line2 + line3 + line4 + line5)
            text_file.write(str(StockScore.stockScore) +
                            "\nType of Trader: " + userData["Type of trader"] +
                            "\nSuit Color: " + userData["Suit"] +
                            "\nInvestor Name: " + userData["Name"] +
                            '\nStock Chosen: ' + userData["Stock Chosen"] +
                            '\n*****************************\n'
                            )

            text_file.write(str(score2) + "\n")
            text_file.write(line6 + line7 + line8 + line9 + line10)
            text_file.write(str(allScore))
            text_file.close()

        else:
            text_file = open('highscores.txt', 'a')
            text_file.write("\n-------------------------------------")
            text_file.write("\nDid not make it on the leaderboards.")
            text_file.write("\nType of Trader: " + userData["Type of trader"] +
                            "\nSuit Color: " + userData["Suit"] +
                            "\nInvestor Name: " + userData["Name"] +
                            '\nStock Chosen: ' + userData["Stock Chosen"] +
                            '\n*****************************\n')
            text_file.close()


# Class is used to control, update and reuse counted variables from number games
class Points:
    # counter = 0
    counter = 0
    count1 = 0
    count2 = 0

    def __init__(self, counter, count1, count2):
        Points.__init__(self, counter, count1, count2)
        self.counter = counter
        self.count1 = count1
        self.count2 = count2
        # self.counter = 0

    @staticmethod
    def update():
        Points.counter += 1
        print("Counter: " + str(Points.counter))

    @staticmethod
    def reset():
        Points.counter = 0
        print("Counter: " + str(Points.counter))


# class Win:
#     wins = 0
#
#     def __init__(self, wins):
#         Number.__init__(self, wins)
#         self.wins = wins
#
#     @staticmethod
#     def update():
#         Win.wins += 1
#         return Win.wins
#
#     @staticmethod
#     def reset():
#         Win.wins = 0
#         return Win.wins

# Class is used to create and manipulate numbers used in number game
class Number:  # The game kept glitching and would assign 'number' the number 0, that is why we have classes now
    number = random.randint(1, 10)
    number2 = random.randint(1, 25)
    computer = random.randint(500, 2500)
    if number < 1:
        number = 5
    elif number > 10:
        number = 2

    if number2 < 1:
        number2 = 10
    elif number2 > 25:
        number2 = 15

    def __init__(self, number, number2, computer):
        Number.__init__(self, number, number2, computer)
        self.number = number
        self.number2 = number2
        self.computer = computer


    @staticmethod
    def update():
        Number.number2 = random.randint(1, 25)
        Number.number = random.randint(1, 10)
        Number.computer = random.randint(500, 2500)

        print(Number.number)
        print(Number.number2)
        print(Number.computer)


# Game buttons created from the Button superclass
class NewGameButton(Button):
    def __init__(self, parent, position=(300, 336)):
        Button.__init__(self, parent, 'New Game', pygame.image.load('data/sprites/backbut.png'), position)

    @staticmethod
    def on_click(**kwargs):
        print("clicked")
        game()


class HighScoreButton(Button):
    def __init__(self, parent, position=(300, 500)):
        Button.__init__(self, parent, 'High score', pygame.image.load('data/sprites/scorebut.png'), position)

    @staticmethod
    def on_click(**kwargs):
        print("clicked")
        highScore()


class MuteButton(Button):
    def __init__(self, parent, position=(728, 468)):  # 467, 325
        Button.__init__(self, parent, 'Mute', pygame.image.load('data/sprites/mute2.png'), position)

    @staticmethod
    def on_click(**kwargs):
        print("clicked")
        pygame.mixer.music.set_volume(0.0)
        pygame.mixer.Sound.set_volume(sound1, 0.0)


class UnMuteButton(Button):
    def __init__(self, parent, position=(728, 543)):  # 470, 372
        Button.__init__(self, parent, 'Mute', pygame.image.load('data/sprites/unmute2.png'), position)

    @staticmethod
    def on_click(**kwargs):
        print("clicked")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.Sound.set_volume(sound1, 0.5)


class TinyMuteButton(Button):
    def __init__(self, parent, position=(745, 5)):  # 467, 325
        Button.__init__(self, parent, 'Mute', pygame.image.load('data/sprites/mute5.png'), position)

    @staticmethod
    def on_click(**kwargs):
        print("clicked")
        pygame.mixer.music.set_volume(0.0)


class TinyUnMuteButton(Button):
    def __init__(self, parent, position=(770, 5)):  # 470, 372
        Button.__init__(self, parent, 'Mute', pygame.image.load('data/sprites/unmute5.png'), position)

    @staticmethod
    def on_click(**kwargs):
        print("clicked")
        pygame.mixer.music.set_volume(0.2)


# Class sprite, animated, and has pop up text when player collides with bouncer.
# In game loop 1 and 2
class Bouncer(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = []
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer1.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer2.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer3.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer4.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer5.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer6.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer7.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer8.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer9.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer10.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer11.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer12.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer13.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer14.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer15.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer16.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer17.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer18.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer19.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer20.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer21.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer22.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer23.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer24.png"))
        self.sprites.append(pygame.image.load("data/sprites/Bouncer/bouncer25.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.rect.x = x
        self.rect.y = y

        self.is_collidable = False

    def update(self):
        self.current_sprite += 0.3

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        elif pygame.sprite.groupcollide(bouncer, player, False, False):
            self.is_collidable = True
            textSquare = pygame.image.load("data/sprites/textsquare.png")
            txtSquareRect = textSquare.get_rect()
            txtSquareRect.center = (screen.get_width() / 1.5, screen.get_height() / 1.9)
            screen.blit(textSquare, txtSquareRect)

        self.image = self.sprites[int(self.current_sprite)]


# Stand still sprite with pop up text when player collides with desk
# In game loop 3
class TradingDesk(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("sprites/Trade.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.rect.x = x
        self.rect.y = y
        self.is_collidable = False

    def update(self):
        if pygame.sprite.groupcollide(objects, player, False, False):
            textSquare2 = pygame.image.load("data/sprites/textsquare2.png")
            txtSquareRect = textSquare2.get_rect()
            txtSquareRect.center = (screen.get_width() / 1.7, screen.get_height() / 1.9)
            screen.blit(textSquare2, txtSquareRect)

# Player has animation, can move left, right, and jumps. Collides with bouncer and desk.
# Used in game loop 1 and 3
# Will change suit color based on user choice
class Player(pygame.sprite.Sprite):
    jumping = False
    vel_y = 13

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.is_collidable = False
        self.is_collidable2 = False
        self.jumping = False

        print(userData)
        self.sprites = []
        if userData['Suit'] == 'Blue':

            self.sprites.append(pygame.image.load("data/walk/L.png"))
            self.sprites.append(pygame.image.load("data/walk/L1.png"))
            self.sprites.append(pygame.image.load("data/walk/L2.png"))
            self.sprites.append(pygame.image.load("data/walk/L3.png"))
            self.sprites.append(pygame.image.load("data/walk/R1.png"))
            self.sprites.append(pygame.image.load("data/walk/R2.png"))
            self.sprites.append(pygame.image.load("data/walk/R3.png"))

        elif userData['Suit'] == 'Purple':
            self.sprites.append(pygame.image.load("data/walk_purple/L.png"))
            self.sprites.append(pygame.image.load("data/walk_purple/L1.png"))
            self.sprites.append(pygame.image.load("data/walk_purple/L2.png"))
            self.sprites.append(pygame.image.load("data/walk_purple/L3.png"))
            self.sprites.append(pygame.image.load("data/walk_purple/R1.png"))
            self.sprites.append(pygame.image.load("data/walk_purple/R2.png"))
            self.sprites.append(pygame.image.load("data/walk_purple/R3.png"))

        elif userData['Suit'] == 'Red':
            self.sprites.append(pygame.image.load("data/walk_red/L.png"))
            self.sprites.append(pygame.image.load("data/walk_red/L1.png"))
            self.sprites.append(pygame.image.load("data/walk_red/L2.png"))
            self.sprites.append(pygame.image.load("data/walk_red/L3.png"))
            self.sprites.append(pygame.image.load("data/walk_red/R1.png"))
            self.sprites.append(pygame.image.load("data/walk_red/R2.png"))
            self.sprites.append(pygame.image.load("data/walk_red/R3.png"))

        elif userData['Suit'] == 'Green':
            self.sprites.append(pygame.image.load("data/walk_green/L.png"))
            self.sprites.append(pygame.image.load("data/walk_green/L1.png"))
            self.sprites.append(pygame.image.load("data/walk_green/L2.png"))
            self.sprites.append(pygame.image.load("data/walk_green/L3.png"))
            self.sprites.append(pygame.image.load("data/walk_green/R1.png"))
            self.sprites.append(pygame.image.load("data/walk_green/R2.png"))
            self.sprites.append(pygame.image.load("data/walk_green/R3.png"))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 10
        self.vel_y = 13

    def update(self):
        key = pygame.key.get_pressed()
        if Player.jumping is False and key[K_UP]:
            Player.jumping = True

        if Player.jumping:
            self.rect.y -= self.vel_y
            self.vel_y -= 1
            if self.vel_y < -13:
                self.vel_y = 13
                Player.jumping = False

        if key[K_LEFT] and self.rect.x > 0:
            self.rect.left -= 5
            self.current_sprite -= 0.2

            if self.current_sprite > 3 or self.current_sprite < 1:
                self.current_sprite = 3

        elif key[K_RIGHT] and self.rect.x < 700:
            self.rect.left += 5
            self.current_sprite += 0.3

            if self.current_sprite < 4 or self.current_sprite >= len(self.sprites):
                self.current_sprite = 4

        elif pygame.sprite.groupcollide(player, objects, False, False):
            self.is_collidable2 = True
            print("Duh")

        elif pygame.sprite.groupcollide(player, bouncer, False, False):
            self.is_collidable = True
            print("Good job")

        elif key[K_SPACE] and self.is_collidable2:
            player.remove(self)
            player.empty()
            objects.empty()
            game4()
            print("hurray")

        elif key[K_y] and self.is_collidable:
            player.remove(self)
            player.empty()
            score.empty()
            game4()
            print("hurray")

        else:
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]


def game():
    arena = backGround()
    arenas = pygame.sprite.RenderPlain(arena)
    clock = pygame.time.Clock()
    keep_going = True
    print(Number.number)
    print(Number.number2)
    # Adding Class Objects to Sprite Groups
    the_exchange = Exchange(x=600, y=68)
    exchanges.add(the_exchange)

    the_player = Player(x=10, y=428)
    player.add(the_player)

    the_score = Score(x=200, y=50)
    score.add(the_score)

    the_bouncer = Bouncer(x=470, y=428)
    bouncer.add(the_bouncer)
    button = TinyMuteButton("Mute")
    button2 = TinyUnMuteButton("Unmute")
    # Main Loop
    while keep_going:
        clock.tick(30)
        # input

        for event in pygame.event.get():
            key = pygame.key.get_pressed()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    player.empty()
                    bouncer.empty()
                    score.empty()
                    keep_going = False

                elif pygame.sprite.groupcollide(player, bouncer, False, False) and key[K_y]:
                    Number.update()
                    print("Number 1: " + str(Number.number))
                    player.empty()
                    bouncer.empty()
                    score.empty()
                    score.remove(the_score)

                    game2()
                    # keep_going = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    position = pygame.mouse.get_pos()
                    button.check_click(position)
                    button2.check_click(position)

        screen.fill((255, 255, 255))
        arenas.draw(screen)
        exchanges.draw(screen)
        player.draw(screen)
        bouncer.draw(screen)
        score.draw(screen)
        button.draw(screen)
        button2.draw(screen)

        player.update()
        score.update()
        bouncer.update()
        arenas.update()
        pygame.display.flip()


def game2():
    pygame.mixer.music.play(-1)
    arena = bossBG()
    arenas = pygame.sprite.RenderPlain(arena)
    clock = pygame.time.Clock()
    keep_going = True
    # Defines menu, option functions, and option display. For example,
    # Changing "Start" to "Begin" will display Begin, instead of start.
    menuTitle = StockMenu(
        ["Pick a number 1-10."],
        ["What is the secret number?"],
        ["Chances: 3"])

    menu = StockMenu(
        ["One", option14],
        ["Two", option15],
        ["Three", option16],
        ["Four", option17],
        ["Five", option18],
        ["Six", option19],
        ["Seven", option20],
        ["Eight", option21],
        ["Nine", option22],
        ["Ten", option23], )

    menuTitle.center_at(633, 111)
    menuTitle.set_font(pygame.font.Font("data/fonts/arial.ttf", 23))
    menuTitle.set_highlight_color((0, 0, 0))
    menuTitle.set_normal_color((0, 0, 0))

    # Menu settings
    menu.center_at(533, 300)
    menu.set_font(pygame.font.Font("data/fonts/arial.ttf", 25))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((255, 0, 0))
    Points.counter = 0

    the_bouncer = Bouncer(x=100, y=428)
    bouncer.add(the_bouncer)
    button = TinyMuteButton("Mute")
    button2 = TinyUnMuteButton("Unmute")

    while keep_going:
        clock.tick(30)

        # Events
        events = pygame.event.get()

        # Update Menu
        menu.update(events)

        # Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    score.empty()

                    bouncer.empty()
                    Points.reset()
                    keep_going = False
                    main()

                elif e.key == pygame.K_RETURN:
                    pygame.mixer.music.fadeout(1000)

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    position = pygame.mouse.get_pos()
                    button.check_click(position)
                    button2.check_click(position)

        # Resets the game after a few tries
        # if Points.counter >= 5:
        if Points.counter >= 3:
            bouncer.empty()
            score.empty()
            Points.reset()
            sound5.play()
            return main()

        # Draw
        screen.fill((255, 255, 255))  # This one might have changed
        arenas.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        bouncer.draw(screen)
        button.draw(screen)
        button2.draw(screen)

        bouncer.update()
        arenas.update()
        pygame.display.flip()


# Options for the first number game, made using classes from file Stockmenu.py
# option14() - option23() or (1-10)
def option14():
    sound1.play()
    # Points.update()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 1 == Number.number:
        bouncer.empty()
        sound4.play()
        pygame.time.delay(2000)

        game3()
        # return Points.counter
        return Points.counter
        # pygame.mixer.music.fadeout()
        # pygame.mixer.music.play(-1)
    elif 1 >= Number.number:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")
        # return Points.counter
        return Points.counter

    elif 1 <= Number.number:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()

        print("Too Low")
        return Points.counter


def option15():
    sound1.play()
    Points.update()
    # Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))

    if 2 > Number.number:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")
        return Points.counter

    if 2 < Number.number:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")
        return Points.counter

    if 2 == Number.number:
        bouncer.empty()
        sound4.play()
        pygame.time.delay(2000)

        game3()
        return Points.counter


def option16():
    sound1.play()
    Points.update()
    # Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 3 > Number.number:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")
        return Points.counter

    if 3 < Number.number:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")
        return Points.counter

    if 3 == Number.number:
        bouncer.empty()
        sound4.play()
        pygame.time.delay(2000)

        game3()
        return Points.counter


def option17():
    sound1.play()
    Points.update()
    # Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))

    if 4 > Number.number:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")
        return Points.counter

    if 4 < Number.number:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")
        return Points.counter

    if 4 == Number.number:
        bouncer.empty()
        sound4.play()
        pygame.time.delay(2000)

        game3()
        return Points.counter


def option18():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))

    if 5 > Number.number:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")
        return Points.counter

    if 5 < Number.number:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")
        return Points.counter

    if 5 == Number.number:
        bouncer.empty()
        sound4.play()
        pygame.time.delay(2000)

        game3()
        return Points.counter


def option19():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 6 > Number.number:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")
        return Points.counter

    if 6 < Number.number:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")
        return Points.counter

    if 6 == Number.number:
        bouncer.empty()
        sound4.play()
        pygame.time.delay(2000)

        game3()
        return Points.counter


def option20():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))

    if 7 > Number.number:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")
        return Points.counter

    if 7 < Number.number:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")
        return Points.counter

    if 7 == Number.number:
        bouncer.empty()
        sound4.play()
        pygame.time.delay(2000)

        game3()
        return Points.counter


def option21():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))

    if 8 > Number.number:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")
        return Points.counter

    if 8 < Number.number:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")
        return Points.counter

    if 8 == Number.number:
        bouncer.empty()
        sound4.play()
        pygame.time.delay(2000)

        game3()
        return Points.counter


def option22():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))

    if 9 > Number.number:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")
        return Points.counter

    if 9 < Number.number:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")
        return Points.counter

    if 9 == Number.number:
        bouncer.empty()
        sound4.play()
        pygame.time.delay(2000)
        game3()
        return Points.counter


def option23():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))

    if 10 > Number.number:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")
        return Points.counter

    if 10 < Number.number:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")
        return Points.counter

    if 10 == Number.number:
        bouncer.empty()
        sound4.play()
        pygame.time.delay(2000)
        game3()
        return Points.counter


################################################################################
def game3():
    pygame.mixer.music.play(-1)
    arena = tradeBG()
    arenas = pygame.sprite.RenderPlain(arena)
    pygame.mixer.music.play(-1)
    # Set Clock
    clock = pygame.time.Clock()
    keep_going = True

    the_score = Score(x=200, y=50)
    score.add(the_score)

    the_player = Player(x=10, y=428)
    player.add(the_player)

    the_trading = TradingDesk(x=385, y=408)
    objects.add(the_trading)

    the_tvs = Tv(x=66, y=211)
    tv.add(the_tvs)

    the_tvs2 = Tv2(x=298, y=208)
    tv.add(the_tvs2)

    the_tvs3 = Tv3(x=528, y=208)
    tv.add(the_tvs3)

    # the_wall = tradeBG()
    the_wall = arenas
    BG.add(the_wall)
    button = TinyMuteButton("Mute")
    button2 = TinyUnMuteButton("Unmute")
    Points.count1 = Points.counter
    print("Count1: " + str(Points.count1))
    Points.reset()
    print("Counter in game 3, should be 0: " + str(Points.counter))
    # Main Loop
    while keep_going:

        clock.tick(30)
        # input
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    position = pygame.mouse.get_pos()
                    button.check_click(position)
                    button2.check_click(position)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    player.empty()
                    score.empty()
                    objects.empty()
                    tv.empty()
                    BG.empty()
                    Number.update()
                    print("Number 1: " + str(Number.number))
                    keep_going = False
                    game2()

                elif pygame.sprite.groupcollide(player, objects, False, False) and key[K_SPACE]:
                    # print("Number 2: " + str(Number-2.number2))
                    player.empty()
                    tv.empty()
                    score.empty()
                    BG.empty()
                    objects.empty()
                    Number.update()
                    print("Number 2: " + str(Number.number2))
                    # Number2.update()
                    game4()

        screen.fill((255, 255, 255))
        BG.draw(screen)
        objects.draw(screen)
        tv.draw(screen)
        player.draw(screen)
        score.draw(screen)
        button.draw(screen)
        button2.draw(screen)

        tv.update()
        objects.update()
        player.update()
        score.update()
        BG.update()
        pygame.display.flip()


def game4():
    arena = window()
    arenas = pygame.sprite.RenderPlain(arena)
    clock = pygame.time.Clock()
    keep_going = True

    menuTitle = StockMenu(
        ["FireWall Activated!"],
        ["Chances: 7"])

    menu = StockMenu(
        ["1", optionA],
        ["2", optionB],
        ["3", optionC],
        ["4", optionD],
        ["5", optionE],
        ["6", optionF],
        ["7", optionG],
        ["8", optionH],
        ["9", optionI],
        ["10", optionJ],  #
        ["11", optionK],
        ["12", optionL],
        ["13", optionM],
        ["14", optionN],
        ["15", optionO],
        ["16", optionP],
        ["17", optionQ],
        ["18", optionR],
        ["19", optionS],
        ["20", optionT],  #
        ["21", optionU],
        ["22", optionV],
        ["23", optionW],
        ["24", optionX],
        ["25", optionY])  #

    # Title
    menuTitle.center_at(391, 100)
    menuTitle.set_font(pygame.font.Font("data/fonts/arial.ttf", 17))
    menuTitle.set_highlight_color((0, 0, 0))

    # Menu settings
    menu.center_at(527, 373)
    menu.set_font(pygame.font.Font("data/fonts/arial.ttf", 15))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((255, 0, 0))

    Points.counter = 0
    button = TinyMuteButton("Mute")
    button2 = TinyUnMuteButton("Unmute")
    while keep_going:
        clock.tick(30)
        # Events
        events = pygame.event.get()
        # Update Menu
        menu.update(events)

        # Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    player.empty()
                    bouncer.empty()
                    Points.reset()
                    keep_going = False
                    game2()
                    # return main()

                elif e.key == pygame.K_RETURN:
                    pygame.mixer.music.fadeout(1000)

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    position = pygame.mouse.get_pos()
                    button.check_click(position)
                    button2.check_click(position)

        # Resets the game after a few tries
        if Points.counter >= 7:
            player.empty()
            bouncer.empty()
            Points.reset()
            sound5.play()
            return main()

        # Draw
        screen.fill((222, 222, 222))  # This one changed
        arenas.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        button.draw(screen)
        button2.draw(screen)
        pygame.display.flip()


def optionA():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 1 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 1 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 1 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionB():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 2 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 2 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 2 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionC():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 3 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 3 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 3 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionD():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 4 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 4 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 4 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionE():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 5 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 5 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 5 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionF():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 6 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 6 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 6 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionG():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 7 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 7 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 7 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionH():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 8 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 8 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 8 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionI():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 9 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 9 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 9 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionJ():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 10 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 10 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 10 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionK():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 11 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 11 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 11 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionL():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 12 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 12 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 12 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionM():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 13 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 13 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 13 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionN():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 14 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 14 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 14 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionO():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 15 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 15 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 15 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionP():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 16 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 16 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 16 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionQ():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 17 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 17 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 17 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionR():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 18 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 18 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 18 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionS():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 19 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 19 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 19 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionT():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 20 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 20 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 20 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionU():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 21 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 21 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 21 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionV():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 22 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 22 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 22 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionW():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 23 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 23 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 23 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionX():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 24 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 24 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 24 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def optionY():
    sound1.play()
    Points.update()
    font2 = pygame.font.SysFont("Times New Roman, Arial", 30)
    text = font2.render("Too high!.", True, (0, 0, 0))
    text2 = font2.render("Too low!.", True, (0, 0, 0))
    if 25 > Number.number2:
        screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too High")

    if 25 < Number.number2:
        screen.blit(text2, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        print("Too Low")

    if 25 == Number.number2:
        sound4.play()
        pygame.time.delay(2000)
        game5()


def game5():  # Stock Game
    stockPrice2 = [["MSFT", 270], ["BBIG", 3], ["AMC", 15], ["GME", 182]]
    pygame.mixer.music.play(-1)
    arena = desktop()
    arenas = pygame.sprite.RenderPlain(arena)
    clock = pygame.time.Clock()
    keep_going = True

    menuTitle = StockMenu(
        ["Time to play stocks?"],
        ["Choose one!"])

    menu = StockMenu(
        ["MSFT", optionMSFT],
        ["BBIG", optionBBIG],
        ["AMC", optionAMC],
        ["GME", optionGME])  #

    # Title
    menuTitle.center_at(450, 85)
    menuTitle.set_font(pygame.font.Font("data/fonts/arial.ttf", 20))
    menuTitle.set_highlight_color((0, 0, 0))

    # Menu settings
    menu.center_at(422, 227)
    menu.set_font(pygame.font.Font("data/fonts/arial.ttf", 28))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((255, 0, 0))
    Points.count2 = Points.counter
    print("Count2: " + str(Points.count2))
    Points.counter = 0
    scoreFont = pygame.font.SysFont("arial", 16)

    the_boss = BossKenG(x=300, y=346)
    boss.add(the_boss)
    button = TinyMuteButton("Mute")
    button2 = TinyUnMuteButton("Unmute")
    Points.reset()
    print("Points in Game five, should be 0: " + str(Points.counter))

    while keep_going:

        clock.tick(5)
        # Events
        events = pygame.event.get()
        # Update Menu
        menu.update(events)
        stockPrice2[0][1] = random.randint(1, 4000)  # Stock 1 price MSFT
        stockPrice2[1][1] = random.randint(40, 4750)  # Stock 2 price BBIG
        stockPrice2[2][1] = random.randint(3, 4900)  # Stock 3 price AMC
        stockPrice2[3][1] = random.randint(3, 4100)  # Stock 4 price GME

        color1 = (0, 255, 0)
        if stockPrice2[0][1] < stockPrice2[1][1] and \
                stockPrice2[0][1] < stockPrice2[2][1] and \
                stockPrice2[0][1] < stockPrice2[3][1]:
            color1 = (255, 0, 0)

        color2 = (0, 255, 0)
        if stockPrice2[1][1] < stockPrice2[0][1] and \
                stockPrice2[1][1] < stockPrice2[2][1] and \
                stockPrice2[1][1] < stockPrice2[3][1]:
            color2 = (255, 0, 0)

        color3 = (0, 255, 0)
        if stockPrice2[2][1] < stockPrice2[0][1] and \
                stockPrice2[2][1] < stockPrice2[1][1] and \
                stockPrice2[2][1] < stockPrice2[3][1]:
            color3 = (255, 0, 0)

        color4 = (0, 255, 0)
        if stockPrice2[3][1] < stockPrice2[0][1] and \
                stockPrice2[3][1] < stockPrice2[1][1] and \
                stockPrice2[3][1] < stockPrice2[2][1]:
            color4 = (255, 0, 0)

        MSFT = scoreFont.render("MSFT: " + str(stockPrice2[0][1]), True, (0, 0, 0), color1)
        BBIG = scoreFont.render("BBIG: " + str(stockPrice2[1][1]), True, (0, 0, 0), color2)
        AMC = scoreFont.render("AMC: " + str(stockPrice2[2][1]), True, (0, 0, 0), color3)
        GME = scoreFont.render("GME: " + str(stockPrice2[3][1]), True, (0, 0, 0), color4)
        # Quit Event

        for e in events:

            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    position = pygame.mouse.get_pos()
                    button.check_click(position)
                    button2.check_click(position)

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    boss.empty()
                    boss.remove(the_boss)
                    Number.update()
                    print("Number 2: " + str(Number.number2))
                    game4()

                elif e.key == pygame.K_RETURN:
                    boss.empty()
                    boss.remove(the_boss)
                    # return main()

        # Draw
        screen.fill((200, 200, 200))  # This one changed
        arenas.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        boss.draw(screen)
        button.draw(screen)
        button2.draw(screen)
        boss.update()
        screen.blit(MSFT, (235, 70))
        screen.blit(BBIG, (235, 160))
        screen.blit(AMC, (235, 260))
        screen.blit(GME, (235, 420))
        pygame.display.flip()


def optionMSFT():
    pygame.mixer.music.play(-1)
    sound1.play()
    arena = MSFTbg()
    arenas = pygame.sprite.RenderPlain(arena)
    clock = pygame.time.Clock()
    keep_going = True

    menuTitle = StockMenu(
        ["You chose Microsoft, a very good choice."],
        ["Definitely a good stock for the long-term."],
        ["Its more expensive to invest in this stock, but"],
        ["they are a market leader in software, and they"],
        ["have a very profitable product market."],
        ["This company will probably be around until"],
        ["either a scandal happens, or until the world"],
        ["puffs up in smoke. Either way, its sure to last."],
        [""],
        ["To win the game your stock needs to be higher"],
        ["Than the stock chosen by the computer."],
        ["Good luck. You may choose another stock as well."])

    menu = StockMenu(
        ["Keep this one.", optionGoMSFT],
        ["BBIG", optionBBIG],
        ["AMC", optionAMC],
        ["GME", optionGME])  #

    # Title
    menuTitle.center_at(693, 249)
    menuTitle.set_font(pygame.font.Font("data/fonts/arial.ttf", 14))
    menuTitle.set_highlight_color((0, 0, 0))

    # Menu settings
    menu.center_at(522, 360)
    menu.set_font(pygame.font.Font("data/fonts/arial.ttf", 20))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((255, 0, 0))

    Points.counter = 0

    scoreFont = pygame.font.SysFont("arial", 30)
    button = TinyMuteButton("Mute")
    button2 = TinyUnMuteButton("Unmute")
    while keep_going:
        stockPrice[0][1] = random.randint(1, 3000)
        MSFT = scoreFont.render("MSFT: " + str(stockPrice[0][1]), True, (255, 255, 255), (0, 0, 0))
        clock.tick(5)
        # Events
        events = pygame.event.get()
        # Update Menu
        menu.update(events)

        # Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    game5()

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    position = pygame.mouse.get_pos()
                    button.check_click(position)
                    button2.check_click(position)
        # Draw
        screen.fill((200, 200, 200))
        arenas.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        button.draw(screen)
        button2.draw(screen)
        screen.blit(MSFT, (130, 220))

        pygame.display.flip()

    print("cool")


def optionBBIG():
    pygame.mixer.music.play(-1)
    sound1.play()
    arena = BBIGbg()
    boss.empty()
    arenas = pygame.sprite.RenderPlain(arena)
    clock = pygame.time.Clock()
    keep_going = True

    menuTitle = StockMenu(
        ["You chose Vinco Ventures, a very risky choice."],
        ["Definitely a good stock for short term gains."],
        ["The only thing that is special about this stock"],
        ["is that it is resilient in the market. Also, it is"],
        ["a very cheap stock, with a lot of up-side potential."],
        [""],
        ["To win the game your stock needs to be higher"],
        ["Than the stock chosen by the computer."],
        ["Good luck. You may choose another stock as well."])

    menu = StockMenu(
        ["Keep this one.", optionGoBBIG],
        ["MSFT", optionMSFT],
        ["AMC", optionAMC],
        ["GME", optionGME])  #

    # Title
    menuTitle.center_at(693, 220)
    menuTitle.set_font(pygame.font.Font("data/fonts/arial.ttf", 13))
    menuTitle.set_highlight_color((0, 0, 0))

    # Menu settings
    menu.center_at(522, 360)
    menu.set_font(pygame.font.Font("data/fonts/arial.ttf", 20))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((255, 0, 0))

    Points.counter = 0
    scoreFont = pygame.font.SysFont("arial", 30)
    button = TinyMuteButton("Mute")
    button2 = TinyUnMuteButton("Unmute")
    while keep_going:
        stockPrice[1][1] = random.randint(40, 1750)  # Stock 2 price
        BBIG = scoreFont.render("BBIG: " + str(stockPrice[1][1]), True, (255, 255, 255), (0, 0, 0))
        clock.tick(5)
        # Events
        events = pygame.event.get()

        # Update Menu
        menu.update(events)

        # Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    game5()

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    position = pygame.mouse.get_pos()
                    button.check_click(position)
                    button2.check_click(position)
        # Draw
        screen.fill((200, 200, 200))
        arenas.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        button.draw(screen)
        button2.draw(screen)
        screen.blit(BBIG, (130, 220))

        pygame.display.flip()


def optionAMC():
    pygame.mixer.music.play(-1)
    sound1.play()
    arena = AMCbg()
    arenas = pygame.sprite.RenderPlain(arena)
    clock = pygame.time.Clock()
    keep_going = True

    boss.empty()
    menuTitle = StockMenu(
        ["Definitely a good stock for a good cause."],
        ["Fun fact, through research retail investors learned"],
        ["that the stock market is actually rigged against"],
        ["the individual investor. As investors dig more into the"],
        ["evidence, they uncovered more than they wanted to know."],
        [""],
        ["It seems that everything is tied together, and that"],
        ["the SEC, the CFTC, the FED, the GOV't, Market Makers,"],
        ["politicians and other wealthy individuals are working"],
        ["together to transfer money from your pocket to theirs in"],
        ["many ways that you may not understand just yet."],
        ["Anyways, To win the game your stock needs to be higher"],
        ["than the stock chosen by the computer."],
        ["Good luck. You may choose another stock as well."])

    menu = StockMenu(
        ["Keep this one.", optionGoAMC],
        ["BBIG", optionBBIG],
        ["MSFT", optionMSFT],
        ["GME", optionGME])  #

    # Title
    menuTitle.center_at(735, 267)
    menuTitle.set_font(pygame.font.Font("data/fonts/arial.ttf", 12))
    menuTitle.set_highlight_color((0, 0, 0))

    # Menu settings
    menu.center_at(522, 360)
    menu.set_font(pygame.font.Font("data/fonts/arial.ttf", 20))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((255, 0, 0))

    Points.counter = 0

    scoreFont = pygame.font.SysFont("arial", 30)
    button = TinyMuteButton("Mute")
    button2 = TinyUnMuteButton("Unmute")
    while keep_going:
        stockPrice[2][1] = random.randint(3, 2900)  # Stock 3 price
        AMC = scoreFont.render("AMC: " + str(stockPrice[2][1]), True, (255, 255, 255), (0, 0, 0))
        clock.tick(5)
        # Events
        events = pygame.event.get()
        # Update Menu
        menu.update(events)

        # Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    game5()

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    position = pygame.mouse.get_pos()
                    button.check_click(position)
                    button2.check_click(position)
        # Draw
        screen.fill((200, 200, 200))
        arenas.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        button.draw(screen)
        button2.draw(screen)
        screen.blit(AMC, (130, 220))

        pygame.display.flip()


def optionGME():
    pygame.mixer.music.play(-1)
    sound1.play()
    arena = GMEbg()
    arenas = pygame.sprite.RenderPlain(arena)
    clock = pygame.time.Clock()
    keep_going = True
    boss.empty()
    menuTitle = StockMenu(
        ["Definitely a good stock for the long-term, also a beloved company."],
        ["They sell games, accessories, systems and so much more."],
        ["During the Covid pandemic the hedge funds targeted countless"],
        ["companies listed on exchanges, and Gamestop was one of them."],
        ["People on reddit noticed and decided to get together and help"],
        ["the company by becoming shareholders. These investors told one"],
        ["another, and eventually saved Gamestop, this hurt hedge funds."],
        ["Hedge funds survived by relying on corruption and manipulation."],
        [""],
        ["High-freq trading algorithms brought GameStop's price down."],
        ["Infrastructures in America are built to ensure no one will"],
        ["succeed unless they are close with someone who is successful."],
        ["To win the game your stock needs to be higher."],
        ["Than the stock chosen by the computer."],
        ["Good luck. You may choose another stock as well."])

    menu = StockMenu(
        ["Keep this one.", optionGoGME],
        ["BBIG", optionBBIG],
        ["AMC", optionAMC],
        ["MSFT", optionMSFT])  #

    # Title
    menuTitle.center_at(773, 277)
    menuTitle.set_font(pygame.font.Font("data/fonts/arial.ttf", 11))
    menuTitle.set_highlight_color((0, 0, 0))

    # Menu settings
    menu.center_at(522, 360)
    menu.set_font(pygame.font.Font("data/fonts/arial.ttf", 20))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((255, 0, 0))

    Points.counter = 0

    scoreFont = pygame.font.SysFont("arial", 30)
    button = TinyMuteButton("Mute")
    button2 = TinyUnMuteButton("Unmute")
    while keep_going:
        stockPrice[3][1] = random.randint(3, 2100)
        GME = scoreFont.render("GME: " + str(stockPrice[3][1]), True, (255, 255, 255), (0, 0, 0))
        clock.tick(5)
        # Events
        events = pygame.event.get()
        # Update Menu
        menu.update(events)

        # Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    game5()
                    # pygame.quit()
                    # return main()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    position = pygame.mouse.get_pos()
                    button.check_click(position)
                    button2.check_click(position)
        # Draw
        screen.fill((200, 200, 200))
        arenas.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        button.draw(screen)
        button2.draw(screen)
        screen.blit(GME, (130, 220))
        pygame.display.flip()


def optionGoMSFT():
    sound1.play()
    stockPrice[0][1] = random.randint(1, 3200)  # Stock 1 price
    # StockScore.update()
    computerNum = Number.computer
    print("Old computer #: " + str(Number.computer))
    print("New computer # " + str(Number.computer))

    if stockPrice[0][1] < Number.computer:
        endGameMSFT()
        print("Stock price: " + str(stockPrice[0][1]))
        return stockPrice[0][1]

    elif stockPrice[0][1] > Number.computer:
        StockScore.update()
        print("Stock price: " + str(stockPrice[0][1]))
        winGameMSFT()
        print("computerNum: " + str(computerNum))
        return stockPrice[0][1]


def optionGoBBIG():
    sound1.play()
    print("Old computer #: " + str(Number.computer))
    print("New computer # " + str(Number.computer))
    stockPrice[1][1] = random.randint(40, 2950)  # Stock 2 price

    if stockPrice[1][1] > Number.computer:
        StockScore.update()
        winGameBBIG()
        print("Stock price: " + str(stockPrice[1][1]))
        return stockPrice[1][1]

    elif stockPrice[1][1] < Number.computer:
        endGameBBIG()
        print("Stock price: " + str(stockPrice[1][1]))
        return stockPrice[1][1]


def optionGoAMC():
    print("Old computer #: " + str(Number.computer))
    print("New computer # " + str(Number.computer))
    sound1.play()
    stockPrice[2][1] = random.randint(300, 3500)  # Stock 3 price

    if stockPrice[2][1] > Number.computer:
        StockScore.update()
        winGameAMC()
        print("Stock price: " + str(stockPrice[2][1]))
        return stockPrice[2][1]

    elif stockPrice[2][1] < Number.computer:
        endGameAMC()
        print("Stock price: " + str(stockPrice[2][1]))
        return stockPrice[2][1]


def optionGoGME():
    print("Old computer #: " + str(Number.computer))
    print("New computer # " + str(Number.computer))
    sound1.play()
    # stockPrice[3][1] = random.randint(300, 3900)  # Stock 4 price

    if stockPrice[3][1] > Number.computer:
        StockScore.update()
        winGameGME()
        print("Stock price: " + str(stockPrice[3][1]))
        return stockPrice[3][1]

    elif stockPrice[3][1] < Number.computer:
        endGameGME()
        print("Stock price: " + str(stockPrice[3][1]))
        return stockPrice[3][1]


def winGameMSFT():

    pygame.mixer.music.fadeout(500)
    sound3.play()
    pygame.time.delay(700)
    pygame.mixer.music.play(-1)
    arena = wonG()
    arenas = pygame.sprite.RenderPlain(arena)
    clock = pygame.time.Clock()
    keep_going = True
    menuTitle = StockMenu(["You beat Pystocks!"])

    # Title
    menuTitle.center_at(375, 100)
    menuTitle.set_font(pygame.font.Font("data/fonts/arial.ttf", 30))
    menuTitle.set_highlight_color((255, 255, 255))
    menuTitle.set_normal_color((255, 255, 255))
    userData["Stock Chosen"] = "MSFT"
    menu = StockMenu(["Play Again?", optionPlay],
                     ["Roll Credits", optionCredits],
                     ["Leaderboards", highScore])
    # Menu settings
    menu.center_at(395, 460)
    menu.set_font(pygame.font.Font("data/fonts/arial.ttf", 30))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((255, 0, 0))
    scoreFont = pygame.font.SysFont("arial", 30)
    MSFT = scoreFont.render("MSFT: " + str(stockPrice[0][1]), True, (0, 0, 255))
    PC = scoreFont.render("Computer: " + str(Number.computer), True, (255, 0, 0))
    print("Stockscore: " + str(StockScore.stockScore))
    score1 = scoreFont.render("Score: " + str(StockScore.stockScore), True, (255, 255, 255))
    # win = scoreFont.render("Wins: " + str(Win.wins), True, (255, 255, 255)) # Add number of times player won
    # alertHS = scoreFont.render("NEW HIGH-SCORE!", True, (255, 255, 255)) # Draw 'New High-Score!' to the screen
    # when player gets a new high score
    button = TinyMuteButton("Mute")
    button2 = TinyUnMuteButton("Unmute")
    WinLooper.update()
    # winLoop(StockScore.stockScore)
    while keep_going:

        clock.tick(30)
        # Events
        events = pygame.event.get()
        # Update Menu
        menu.update(events)

        # Quit Event
        for e in events:

            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    Number.update()
                    keep_going = False

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    position = pygame.mouse.get_pos()
                    button.check_click(position)
                    button2.check_click(position)
        # Draw

        screen.fill((0, 0, 0))
        arenas.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        button.draw(screen)
        button2.draw(screen)
        screen.blit(score1, (330, 250))
        screen.blit(MSFT, (335, 200))
        screen.blit(PC, (315, 150))
        arenas.update()
        pygame.display.flip()

    print("WinGame")


def endGameMSFT():
    pygame.mixer.music.fadeout(500)
    sound6.play()
    pygame.time.delay(700)
    pygame.mixer.music.play(-1)
    arena = endG()
    arenas = pygame.sprite.RenderPlain(arena)
    clock = pygame.time.Clock()
    keep_going = True
    userData["Stock Chosen"] = "MSFT"
    menuTitle = StockMenu(["So sorry, I guess you ran out of luck!"],
                          ["Would you like to try again?"])
    # Title
    menuTitle.center_at(393, 56)
    menuTitle.set_font(pygame.font.Font("data/fonts/arial.ttf", 30))
    menuTitle.set_highlight_color((255, 255, 255))
    menuTitle.set_normal_color((255, 255, 255))
    menu = StockMenu(["Try Again?", optionTry],
                     ["Quit Game", optionQuit],
                     ["Leaderboards", highScore])
    # Menu settings
    menu.center_at(700, 440)
    menu.set_font(pygame.font.Font("data/fonts/arial.ttf", 30))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((255, 0, 0))

    scoreFont = pygame.font.SysFont("arial", 35)
    stockScore = (stockPrice[0][1] - Number.computer + 1000)
    score1 = scoreFont.render("Score: " + str(stockScore), True, (255, 255, 0))

    MSFT = scoreFont.render("MSFT: " + str(stockPrice[0][1]), True, (255, 0, 0))
    PC = scoreFont.render("Computer: " + str(Number.computer), True, (0, 0, 255))
    button = TinyMuteButton("Mute")
    button2 = TinyUnMuteButton("Unmute")
    while keep_going:
        clock.tick(30)
        # Events
        events = pygame.event.get()
        # Update Menu
        menu.update(events)

        # Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    Number.update()
                    keep_going = False

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    position = pygame.mouse.get_pos()
                    button.check_click(position)
                    button2.check_click(position)
        # Draw
        screen.fill((0, 0, 0))
        arenas.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        button.draw(screen)
        button2.draw(screen)
        screen.blit(score1, (50, 500))

        screen.blit(MSFT, (50, 400))
        screen.blit(PC, (50, 450))
        pygame.display.flip()
    print("Endgame")


def winGameBBIG():
    pygame.mixer.music.fadeout(500)
    sound3.play()
    pygame.time.delay(700)
    pygame.mixer.music.play(-1)
    arena = wonG()
    arenas = pygame.sprite.RenderPlain(arena)
    clock = pygame.time.Clock()
    keep_going = True
    userData["Stock Chosen"] = "BBIG"
    menuTitle = StockMenu(["You beat Pystocks!"])
    # Title
    menuTitle.center_at(375, 100)
    menuTitle.set_font(pygame.font.Font("data/fonts/arial.ttf", 30))
    menuTitle.set_highlight_color((255, 255, 255))
    menuTitle.set_normal_color((255, 255, 255))

    menu = StockMenu(["Play Again?", optionPlay],
                     ["Roll Credits", optionCredits],
                     ["Leaderboards", highScore])
    # Menu settings
    menu.center_at(395, 460)
    menu.set_font(pygame.font.Font("data/fonts/arial.ttf", 30))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((255, 0, 0))

    scoreFont = pygame.font.SysFont("arial", 30)
    BBIG = scoreFont.render("BBIG: " + str(stockPrice[1][1]), True, (0, 0, 255))
    PC = scoreFont.render("Computer: " + str(Number.computer), True, (255, 0, 0))

    score1 = scoreFont.render("Score: " + str(StockScore.stockScore), True, (255, 255, 255))
    button = TinyMuteButton("Mute")
    button2 = TinyUnMuteButton("Unmute")
    WinLooper.update()
    # winLoop(StockScore.stockScore)
    while keep_going:
        clock.tick(30)
        # Events
        events = pygame.event.get()

        # Update Menu
        menu.update(events)

        # Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    Number.update()
                    keep_going = False

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    position = pygame.mouse.get_pos()
                    button.check_click(position)
                    button2.check_click(position)
        # Draw
        screen.fill((0, 0, 0))
        arenas.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        button.draw(screen)
        button2.draw(screen)
        screen.blit(score1, (330, 250))
        screen.blit(BBIG, (335, 200))
        screen.blit(PC, (315, 150))
        arenas.update()
        pygame.display.flip()
    print("WinGame")


def endGameBBIG():
    pygame.mixer.music.fadeout(500)
    sound6.play()
    pygame.time.delay(700)
    pygame.mixer.music.play(-1)
    arena = endG()
    arenas = pygame.sprite.RenderPlain(arena)
    clock = pygame.time.Clock()
    keep_going = True
    userData["Stock Chosen"] = "BBIG"
    menuTitle = StockMenu(["So sorry, I guess you ran out of luck!"],
                          ["Would you like to try again?"])
    # Title
    menuTitle.center_at(393, 56)
    menuTitle.set_font(pygame.font.Font("data/fonts/arial.ttf", 30))
    menuTitle.set_highlight_color((255, 255, 255))
    menuTitle.set_normal_color((255, 255, 255))
    menu = StockMenu(["Try Again?", optionTry],
                     ["Quit Game", optionQuit],
                     ["Leaderboards", highScore])
    # Menu settings
    menu.center_at(700, 440)
    menu.set_font(pygame.font.Font("data/fonts/arial.ttf", 30))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((255, 0, 0))

    scoreFont = pygame.font.SysFont("arial", 35)
    BBIG = scoreFont.render("BBIG: " + str(stockPrice[1][1]), True, (255, 0, 0))
    PC = scoreFont.render("Computer: " + str(Number.computer), True, (0, 0, 255))
    stockScore = (stockPrice[1][1] - Number.computer + 1000)
    score1 = scoreFont.render("Score: " + str(stockScore), True, (255, 255, 0))
    button = TinyMuteButton("Mute")
    button2 = TinyUnMuteButton("Unmute")
    while keep_going:
        clock.tick(30)
        # Events
        events = pygame.event.get()

        # Update Menu
        menu.update(events)
        # Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    Number.update()
                    keep_going = False

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    position = pygame.mouse.get_pos()
                    button.check_click(position)
                    button2.check_click(position)
        # Draw
        screen.fill((0, 0, 0))
        arenas.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        button.draw(screen)
        button2.draw(screen)
        screen.blit(score1, (50, 500))

        screen.blit(BBIG, (50, 400))
        screen.blit(PC, (50, 450))
        pygame.display.flip()
    print("Endgame")


def winGameAMC():
    pygame.mixer.music.fadeout(500)
    sound3.play()
    pygame.time.delay(700)
    pygame.mixer.music.play(-1)
    arena = wonG()
    arenas = pygame.sprite.RenderPlain(arena)
    clock = pygame.time.Clock()
    keep_going = True
    userData["Stock Chosen"] = "AMC"
    menuTitle = StockMenu(["You beat Pystocks!"])
    # Title
    menuTitle.center_at(375, 100)
    menuTitle.set_font(pygame.font.Font("data/fonts/arial.ttf", 30))
    menuTitle.set_highlight_color((255, 255, 255))
    menuTitle.set_normal_color((255, 255, 255))

    menu = StockMenu(["Play Again?", optionPlay],
                     ["Roll Credits", optionCredits],
                     ["Leaderboards", highScore])
    # Menu settings
    menu.center_at(395, 460)
    menu.set_font(pygame.font.Font("data/fonts/arial.ttf", 30))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((255, 0, 0))

    Points.counter = 0

    scoreFont = pygame.font.SysFont("arial", 30)
    AMC = scoreFont.render("AMC: " + str(stockPrice[2][1]), True, (0, 0, 255))
    PC = scoreFont.render("Computer: " + str(Number.computer), True, (255, 0, 0))

    # v = random.randint(1, 5)
    score1 = scoreFont.render("Score: " + str(StockScore.stockScore), True, (255, 255, 255))
    button = TinyMuteButton("Mute")
    button2 = TinyUnMuteButton("Unmute")
    WinLooper.update()
    # winLoop(StockScore.stockScore)
    while keep_going:
        clock.tick(30)
        # Events
        events = pygame.event.get()
        # Update Menu
        menu.update(events)

        # Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    Number.update()
                    keep_going = False

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    position = pygame.mouse.get_pos()
                    button.check_click(position)
                    button2.check_click(position)
        # Draw
        screen.fill((0, 0, 0))
        arenas.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        button.draw(screen)
        button2.draw(screen)
        screen.blit(score1, (330, 250))
        screen.blit(AMC, (335, 200))
        screen.blit(PC, (315, 150))
        arenas.update()
        pygame.display.flip()
    print("WinGame")


def endGameAMC():
    pygame.mixer.music.fadeout(500)
    sound6.play()
    pygame.time.delay(700)
    pygame.mixer.music.play(-1)
    arena = endG()
    arenas = pygame.sprite.RenderPlain(arena)
    clock = pygame.time.Clock()
    keep_going = True
    userData["Stock Chosen"] = "AMC"
    menuTitle = StockMenu(["So sorry, I guess you ran out of luck!"],
                          ["Would you like to try again?"])
    # Title
    menuTitle.center_at(393, 56)
    menuTitle.set_font(pygame.font.Font("data/fonts/arial.ttf", 30))
    menuTitle.set_highlight_color((255, 255, 255))
    menuTitle.set_normal_color((255, 255, 255))
    menu = StockMenu(["Try Again?", optionTry],
                     ["Quit Game", optionQuit],
                     ["Leaderboards", highScore])
    # Menu settings
    menu.center_at(700, 440)
    menu.set_font(pygame.font.Font("data/fonts/arial.ttf", 30))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((255, 0, 0))

    scoreFont = pygame.font.SysFont("arial", 35)
    AMC = scoreFont.render("AMC: " + str(stockPrice[2][1]), True, (255, 0, 0))
    PC = scoreFont.render("Computer: " + str(Number.computer), True, (0, 0, 255))
    stockScore = (stockPrice[2][1] - Number.computer + 1000)
    score1 = scoreFont.render("Score: " + str(stockScore), True, (255, 255, 0))
    button = TinyMuteButton("Mute")
    button2 = TinyUnMuteButton("Unmute")
    while keep_going:
        clock.tick(30)
        # Events
        events = pygame.event.get()
        # Update Menu
        menu.update(events)

        # Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    Number.update()
                    keep_going = False
                    # pygame.quit()
                    # return main()

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    position = pygame.mouse.get_pos()
                    button.check_click(position)
                    button2.check_click(position)
        # Draw
        screen.fill((0, 0, 0))
        arenas.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        button.draw(screen)
        button2.draw(screen)
        screen.blit(score1, (50, 500))
        screen.blit(AMC, (50, 400))
        screen.blit(PC, (50, 450))
        pygame.display.flip()
    print("Endgame")


def winGameGME():
    pygame.mixer.music.fadeout(500)
    sound3.play()
    pygame.time.delay(700)
    pygame.mixer.music.play(-1)
    arena = wonG()
    arenas = pygame.sprite.RenderPlain(arena)
    clock = pygame.time.Clock()
    keep_going = True
    userData["Stock Chosen"] = "GME"
    menuTitle = StockMenu(["You beat Pystocks!"])
    # Title
    menuTitle.center_at(375, 100)
    menuTitle.set_font(pygame.font.Font("data/fonts/arial.ttf", 30))
    menuTitle.set_highlight_color((255, 255, 255))
    menuTitle.set_normal_color((255, 255, 255))

    menu = StockMenu(["Play Again?", optionPlay],
                     ["Roll Credits", optionCredits],
                     ["Leaderboards", highScore])
    # Menu settings
    menu.center_at(395, 460)
    menu.set_font(pygame.font.Font("data/fonts/arial.ttf", 30))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((255, 0, 0))
    scoreFont = pygame.font.SysFont("arial", 30)
    GME = scoreFont.render("GME: " + str(stockPrice[3][1]), True, (0, 0, 255))
    PC = scoreFont.render("Computer: " + str(Number.computer), True, (255, 0, 0))

    score1 = scoreFont.render("Score: " + str(StockScore.stockScore), True, (255, 255, 255))
    button = TinyMuteButton("Mute")
    button2 = TinyUnMuteButton("Unmute")
    # winLoop(StockScore.stockScore)
    WinLooper.update()
    while keep_going:
        clock.tick(30)
        # Events
        events = pygame.event.get()
        # Update Menu
        menu.update(events)

        # Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    Number.update()
                    keep_going = False

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    position = pygame.mouse.get_pos()
                    button.check_click(position)
                    button2.check_click(position)
        # Draw
        screen.fill((0, 0, 0))
        arenas.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        button.draw(screen)
        button2.draw(screen)
        screen.blit(score1, (330, 250))
        screen.blit(GME, (335, 200))
        screen.blit(PC, (315, 150))
        arenas.update()
        pygame.display.flip()
    print("WinGame")


def endGameGME():
    pygame.mixer.music.fadeout(500)
    sound6.play()
    pygame.time.delay(700)
    pygame.mixer.music.play(-1)
    arena = endG()
    arenas = pygame.sprite.RenderPlain(arena)
    clock = pygame.time.Clock()
    keep_going = True
    userData["Stock Chosen"] = "GME"
    menuTitle = StockMenu(["So sorry, I guess you ran out of luck!"],
                          ["Would you like to try again?"])
    # Title
    menuTitle.center_at(393, 56)
    menuTitle.set_font(pygame.font.Font("data/fonts/arial.ttf", 30))
    menuTitle.set_highlight_color((255, 255, 255))
    menuTitle.set_normal_color((255, 255, 255))
    menu = StockMenu(["Try Again?", optionTry],
                     ["Quit Game", optionQuit],
                     ["Leaderboards", highScore])
    # Menu settings
    menu.center_at(700, 440)
    menu.set_font(pygame.font.Font("data/fonts/arial.ttf", 30))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((255, 0, 0))

    scoreFont = pygame.font.SysFont("arial", 35)
    GME = scoreFont.render("GME: " + str(stockPrice[3][1]), True, (255, 0, 0))
    PC = scoreFont.render("Computer: " + str(Number.computer), True, (0, 0, 255))
    stockScore = (stockPrice[3][1] - Number.computer + 1000)
    score1 = scoreFont.render("Score: " + str(stockScore), True, (255, 255, 0))
    button = TinyMuteButton("Mute")
    button2 = TinyUnMuteButton("Unmute")

    while keep_going:
        clock.tick(30)
        # Events
        events = pygame.event.get()
        # Update Menu
        menu.update(events)

        # Quit Event
        for event in events:

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Number.update()
                    keep_going = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    position = pygame.mouse.get_pos()
                    button.check_click(position)
                    button2.check_click(position)

        screen.fill((0, 0, 0))
        arenas.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        button.draw(screen)
        button2.draw(screen)
        screen.blit(score1, (50, 500))
        screen.blit(GME, (50, 400))
        screen.blit(PC, (50, 450))
        pygame.display.flip()
        print("Endgame")


def optionPlay():
    Number.update()
    exchanges.empty()
    player.empty()
    score.empty()
    bouncer.empty()
    objects.empty()
    BG.empty()
    boss.empty()
    sound5.play()
    main()
    print('play')


def optionTry():
    print('Try')
    Number.update()
    game5()


def optionQuit():
    print('Quit')
    pygame.quit()
    sys.exit()


def optionCredits():
    print('credits')
    arena = stonksBg()
    arenas = pygame.sprite.RenderPlain(arena)
    clock = pygame.time.Clock()
    keep_going = True

    menuTitle = StockMenu(["ITCS-1950 Intro to Game Programming"],
                          ["Teacher: G. Schleiss"],
                          ["Project: Make My Own Game."],
                          ["Class Code Credits and Resources: "],
                          ["SpaceShooter Game."],
                          ["CannonBall Game."],
                          ["Ping Pong Game."],
                          ["Clone of Tetris Game."],
                          ["YouTube Tutorials"],
                          ["I had a ton of fun making this game."],
                          ["I plan on making many more applications and games."],
                          ["I am pursuing a career in software engineering, that"],
                          ["has a game design feel for users."],
                          ["Look MOM, I made a GAME!"],
                          ["For the sake of humanity, my sanity, and the good of"],
                          ["our nation. If there is one thing that you can"],
                          ["learn from this, then let it be this."],
                          ["Like my game, the Stock Market is an illusion."],
                          ["Just like how I can change stuff, and make this program"],
                          ["do whatever I want, stock exchanges can do the same."],
                          ["believe it or not, THEY DO IT ALL THE TIME."],
                          ["The SEC and many other agencies have been bought out"],
                          ["by these criminals, so that they can continue to rig"],
                          ["America and essentially our way of life as Americans."],
                          [""],
                          ["Anyways, look out for newer versions of the game! Peace."])
    # Title
    menuTitle.center_at(383, 370)
    menuTitle.set_font(pygame.font.Font("data/fonts/arial.ttf", 15))
    menuTitle.set_highlight_color((255, 255, 255))
    menuTitle.set_normal_color((255, 255, 255))

    menu1 = StockMenu(["New Game", main],
                      ["Play Stocks", game5],
                      ["My Game", option2],
                      ["About", option3],
                      ["Leaderboards", highScore],
                      ["Quit", optionQuit])
    # Menu settings
    menu1.center_at(598, 350)
    menu1.set_font(pygame.font.Font("data/fonts/arial.ttf", 30))
    menu1.set_highlight_color((0, 255, 0))
    menu1.set_normal_color((255, 0, 0))

    while keep_going:
        clock.tick(30)
        # Update Menu
        events = pygame.event.get()
        # Update Menu
        menu1.update(events)
        # input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keep_going = False

        # Draw
        screen.fill((0, 0, 0))  # This one changed
        arenas.draw(screen)
        menuTitle.draw(screen)
        menu1.draw(screen)
        pygame.display.flip()


def saveScore():
    keep_going = True
    clock = pygame.time.Clock()
    # Input box position factors X ,  Y  , W  , H
    input_box = InputBox(300, 205, 200, 50)
    arena = nameBg()
    arenas = pygame.sprite.RenderPlain(arena)
    button = NewGameButton("New Game")
    button2 = HighScoreButton("See High Scores")

    BG.add(arenas)
    button3 = MuteButton("Mute")
    button4 = UnMuteButton("Unmute")
    while keep_going:
        clock.tick(200)
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                InputBox.handle_event(input_box, event)

                if pygame.mouse.get_pressed() == (1, 0, 0):
                    position = pygame.mouse.get_pos()
                    button.check_click(position)
                    button2.check_click(position)
                    button3.check_click(position)
                    button4.check_click(position)
            elif event.type == pygame.KEYDOWN:
                InputBox.handle_event(input_box, event)

                if event.key == pygame.K_RETURN:
                    InputBox.handle_event(input_box, event)

                elif event.key == pygame.K_ESCAPE:
                    screen.fill((30, 30, 30))
                    BG.empty()
                    keep_going = False

            else:
                screen.fill((0, 0, 0))
                BG.draw(screen)
                InputBox.draw(input_box, screen)
                InputBox.update(input_box)
                NewGameButton.draw(button, screen)
                HighScoreButton.draw(button2, screen)
                button3.draw(screen)
                button4.draw(screen)
                text1 = font.render("Investor Name Saved...", 3, (0, 0, 0), (255, 255, 255))
                textRect = text1.get_rect()
                textRect.center = (400, 475)
                if key[K_RETURN] and input_box.active:
                    screen.blit(text1, textRect)

                BG.update()
                pygame.display.flip()
                clock.tick(30)


def highScore():
    arena = shine()
    arenas = pygame.sprite.RenderPlain(arena)
    clock = pygame.time.Clock()
    keep_going = True
    text_file = open('highscores.txt', 'r')
    hs = text_file.read()

    font3 = pygame.font.SysFont("Liberation Sans", 30)
    message = TextScroll(pygame.Rect(170, 150, 460, 321), font3, WHITE, BLACK, hs, ms_per_line=665)

    menu = StockMenu(["Quit", optionQuit],
                     ["Go Back", saveScore])

    menu.center_at(580, 497)
    menu.set_font(pygame.font.Font("data/fonts/arial.ttf", 25))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((255, 0, 0))
    screen.fill((30, 30, 30))  # This one changed
    arenas.draw(screen)
    while keep_going:
        clock.tick(30)
        events = pygame.event.get()
        menu.update(events)

        for event in events:

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    keep_going = False
                    screen.fill((30, 30, 30))

                else:
                    text_file.close()

        menu.draw(screen)

        text_file.close()
        message.draw(screen)
        message.update()
        pygame.display.flip()


def user2():
    arena = Arena()
    arenas = pygame.sprite.RenderPlain(arena)
    clock = pygame.time.Clock()
    keep_going = True

    # Defines menu, option functions, and option display. For example,
    # Changing "Start" to "Begin" will display Begin, instead of start.
    menuTitle = StockMenu(
        ["What Trader Are You?"])

    menu = StockMenu(
        ["Bull", option9],
        ["Bear", option10],
        ["Swing", option11],
        ["Value", option12])

    # Title
    menuTitle.center_at(194, 80)
    menuTitle.set_font(pygame.font.Font("data/fonts/ls.ttf", 91))
    menuTitle.set_highlight_color((255, 255, 255))

    # Menu settings
    menu.center_at(362, 244)
    menu.set_font(pygame.font.Font("data/fonts/arial.ttf", 40))
    menu.set_highlight_color((128, 0, 128))
    menu.set_normal_color((0, 0, 0))
    button = MuteButton("Mute")
    button2 = UnMuteButton("Unmute")
    while keep_going:
        clock.tick(30)
        # Events
        events = pygame.event.get()
        # Update Menu
        menu.update(events)

        # Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                return

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    return user()
            elif e.type == pygame.MOUSEBUTTONDOWN:

                if pygame.mouse.get_pressed() == (1, 0, 0):
                    position = pygame.mouse.get_pos()
                    button.check_click(position)
                    button2.check_click(position)

        # Draw
        screen.fill((0, 0, 0))  # This one changed
        arenas.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        button.draw(screen)
        button2.draw(screen)
        arenas.update()
        pygame.display.flip()


def user():
    arena = Arena()
    arenas = pygame.sprite.RenderPlain(arena)
    clock = pygame.time.Clock()
    keep_going = True

    # Defines menu, option functions, and option display. For example,
    # Changing "Start" to "Begin" will display Begin, instead of start.
    menuTitle = StockMenu(
        ["Choose Your Suit Color"])

    menu = StockMenu(
        ["Blue", option5],
        ["Purple", option6],
        ["Red", option7],
        ["Green", option8])

    # Title
    menuTitle.center_at(185, 80)
    menuTitle.set_font(pygame.font.Font("data/fonts/ls.ttf", 91))
    menuTitle.set_highlight_color((255, 255, 255))

    # Menu settings
    menu.center_at(362, 244)
    menu.set_font(pygame.font.Font("data/fonts/arial.ttf", 40))
    menu.set_highlight_color((128, 0, 128))
    menu.set_normal_color((0, 0, 0))
    button = MuteButton("Mute")
    button2 = UnMuteButton("Unmute")
    while keep_going:
        clock.tick(30)
        # Events
        events = pygame.event.get()
        # Update Menu
        menu.update(events)

        # Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                return

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    return main()
            elif e.type == pygame.MOUSEBUTTONDOWN:

                if pygame.mouse.get_pressed() == (1, 0, 0):
                    position = pygame.mouse.get_pos()
                    button.check_click(position)
                    button2.check_click(position)
        # Draw
        screen.fill((0, 0, 0))  # This one changed
        arenas.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        button.draw(screen)
        button2.draw(screen)
        arenas.update()
        pygame.display.flip()


def missionMenu():
    # Arena
    arena = howToPlay()
    arenas = pygame.sprite.RenderPlain(arena)

    # Title for Option Menu
    menuTitle = StockMenu(
        ["How to Play!"])

    # Option Menu Text
    instructions = StockMenu(
        ["Left and Right Arrow keys to move the player!"],
        [""],
        ["Learn the other buttons throughout the game."],
        [""],
        ["Press 'Y' when you get to first boss"],
        ["This game has mouse control with the text box"],
        [""],
        ["Use the up/down arrow keys for menu choices."],
        [""],
        ["Once you get to the trading desk, you must press"],
        ["the 'Space Bar' to start the number game."],
        ["When choosing stocks in the game, please"],
        ["understand each stock price changes after"],
        ["each time a menu option is chosen."],
        ["Trading in the stock market takes guts."],
        ["Do you have what it takes?"],
        [""],
        ["Have fun, try to get the highest price that you can!"],
        [""],
        ["                   PRESS ESC TO RETURN                    "])

    # Title
    menuTitle.center_at(250, 45)
    menuTitle.set_font(pygame.font.Font("data/fonts/ls.ttf", 50))
    menuTitle.set_highlight_color((255, 255, 255))
    # Title Center
    instructions.center_at(500, 350)
    # Menu Font
    instructions.set_font(pygame.font.Font("data/fonts/arial.ttf", 15))
    # Highlight Color
    instructions.set_normal_color((0, 0, 0))
    # Set Clock
    clock = pygame.time.Clock()
    keep_going = True

    while keep_going:
        clock.tick(30)
        # input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keep_going = False
        # Draw
        screen.fill((113, 113, 113))
        arenas.draw(screen)
        menuTitle.draw(screen)
        instructions.draw(screen)
        arenas.update()
        pygame.display.flip()


def aboutMenu():
    # Arena
    arena = howToPlay()
    arenas = pygame.sprite.RenderPlain(arena)

    # About Menu Text
    # Title for Option Menu
    menuTitle = StockMenu(
        ["About menu!"])

    info = StockMenu(
        ["World of Stocks Python Pygame."],
        ["Developed by Wayne Williams."],
        [""],
        ["Student from Mr.Schleiss' class:ITCS-1950."],
        ["Macomb Community College."],
        [""],
        ["Let's go Brandon!"],
        [""],
        ["Started creating game in April 2022."],
        ["Finished game around August 2022."],
        [""],
        ["Link to my github:"],
        ['https://github.com/wayne6092?tab=repositories'],
        [""],
        ["              PRESS ESC TO RETURN            "])

    # Citation: I used some classes from SpaceShooter, a classic game among the best
    # I believe my teacher allowed me permission to use this code for my assignments.

    # About Title Font color, alignment, and font type
    menuTitle.center_at(250, 45)
    menuTitle.set_font(pygame.font.Font("data/fonts/ls.ttf", 50))
    menuTitle.set_highlight_color((255, 255, 255))

    # About Menu Text Alignment
    info.center_at(480, 300)

    # About Menu Font
    info.set_font(pygame.font.Font("data/fonts/arial.ttf", 17))

    # About Menu Font Color
    info.set_normal_color((0, 0, 0))

    # Set Clock
    clock = pygame.time.Clock()
    keep_going = True

    while keep_going:
        clock.tick(30)
        # input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keep_going = False
        # Draw
        screen.fill((113, 113, 113))
        arenas.draw(screen)
        menuTitle.draw(screen)
        info.draw(screen)
        arenas.update()
        pygame.display.flip()


# Functions
def option1():
    sound1.play()
    user()


def option2():
    sound1.play()
    missionMenu()


def option3():
    sound1.play()
    aboutMenu()


def option4():
    sound1.play()
    pygame.quit()
    sys.exit()


def option5():
    sound1.play()
    userData['Suit'] = 'Blue'
    user2()
    return userData


def option6():
    sound1.play()
    userData['Suit'] = 'Purple'
    user2()
    return userData


def option7():
    sound1.play()
    userData['Suit'] = 'Red'
    user2()
    return userData


def option8():
    sound1.play()
    userData['Suit'] = 'Green'
    user2()
    return userData


def option9():
    sound1.play()
    userData['Type of trader'] = 'Bull'
    saveScore()
    return userData


def option10():
    sound1.play()
    userData['Type of trader'] = 'Bear'
    saveScore()
    return userData


def option11():
    sound1.play()
    userData['Type of trader'] = 'Swing'
    saveScore()
    return userData


def option12():
    sound1.play()
    userData['Type of trader'] = 'Value'
    saveScore()
    return userData


# Main
def main():
    # Arena
    arena = Arena()
    arenas = pygame.sprite.RenderPlain(arena)

    # Defines menu, option functions, and option display. For example,
    # Changing "Start" to "Begin" will display Begin, instead of start.
    menuTitle = StockMenu(
        ["World of Stocks"])

    menu = StockMenu(
        ["Start", option1],
        ["My Game", option2],
        ["About", option3],
        ["Quit", option4])

    # Title
    menuTitle.center_at(245, 80)
    menuTitle.set_font(pygame.font.Font("data/fonts/ls.ttf", 91))
    menuTitle.set_highlight_color((255, 255, 255))

    # Menu settings
    menu.center_at(362, 244)
    menu.set_font(pygame.font.Font("data/fonts/arial.ttf", 40))
    menu.set_highlight_color((128, 0, 128))
    menu.set_normal_color((0, 0, 0))
    button = MuteButton("Mute")
    button2 = UnMuteButton("Unmute")
    clock = pygame.time.Clock()
    keep_going = True

    while keep_going:
        clock.tick(30)

        # Events
        events = pygame.event.get()

        # Update Menu
        menu.update(events)

        # Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                return
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(1)

            elif e.type == pygame.MOUSEBUTTONDOWN:

                if pygame.mouse.get_pressed() == (1, 0, 0):
                    position = pygame.mouse.get_pos()
                    button.check_click(position)
                    button2.check_click(position)

        # Draw
        screen.fill((0, 0, 0))
        arenas.draw(screen)
        menu.draw(screen)
        button.draw(screen)
        button2.draw(screen)
        arenas.update()
        menuTitle.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
