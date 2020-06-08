from Deck import Deck


class Player(Deck):
    Name = " "
    Score = 0

    def Drawcard2(self, deck):
        Temp = deck.Drawcard()
        self.Rawdeck.append(Temp)

    def countScores(self):
        haselement = True
        it = iter(self.Rawdeck)
        self.Score = 0
        while haselement:
            try:
                Temp = next(it)
                self.Score += Temp.number
            except StopIteration:
                haselement = False
                # print("no more element")
        # print(self.Score)
        # return self.Score

    def Display(self):
        iterator = iter(self.Rawdeck)
        haselement = False
        while not haselement:
            try:
                Temp = next(iterator)
                print(Temp.type  + " " + str(Temp.number))
            except StopIteration:
                haselement = True

