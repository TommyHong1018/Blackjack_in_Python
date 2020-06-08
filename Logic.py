from Aimbotz import Aimbotz
from Deck import Deck
from Player import Player

Player1 = Player()
Deck1 = Deck()
Aimbotz1 = Aimbotz()

Resume = True

while Resume:
    Comdraw = True
    Playerdraw = True
    Game = True
    Player1.Score = 0
    Aimbotz1.Score = 0
    Deck1.Rawdeck = []
    Deck1.initdeck()
    Player1.Rawdeck = []
    Aimbotz1.Rawdeck = []

    while Game:
        print("-------------Game-------------")
        print("Now your score is " + str(Player1.Score))
        if (Playerdraw == False) and (Comdraw == False):
            Game = False
            break
        elif Player1.Score > 21 or Aimbotz1.Score > 21:
            Game = False
            break

        player = True
        com = True
        print("Draw? Input 1 to draw, 2 to give up drawing, 3 to examine your deck.")
        while player:
            Choice1 = input()
            Choice1 = int(Choice1)
            if Choice1 == 1:
                Player1.Drawcard2(Deck1)
                player = False
            if Choice1 == 2:
                player = False
                Playerdraw = False
            if Choice1 == 3:
                Player1.Display()
        while com:
            Comdraw = Aimbotz1.Drawornot(Deck1)
            com = False

        Player1.countScores()
        Aimbotz1.countScores()

    if Player1.Score is Aimbotz1.Score:
        print("Tie")
    elif Aimbotz1.Score > 21:
        print("You Win, Bot has more than 21 points")
    elif Player1.Score > 21:
        print("You Lose, You have more than 21 points")
    elif Aimbotz1.Score > Player1.Score:
        print("You Lose, Bots has " + str(Aimbotz1.Score) + " Scores")
    elif Aimbotz1.Score < Player1.Score:
        print("You Win, Bot has " + str(Aimbotz1.Score) + " Scores")


    print("----------Game Finish---------")
    print("Resume? 1 to resume playing, 2 to stop.")
    Choice2 = input()
    Choice2 = int(Choice2)
    if Choice2 == 1:
        pass
    elif Choice2 == 2:
        Resume = False
