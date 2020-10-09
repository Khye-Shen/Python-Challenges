import itertools
import random

class Cards:
    def __init__(self):
        self.suits = ['Spades','Hearts','Diamonds','Clubs']
        self.values = range(1,14)
        self.ActualCards = []
        for Card in itertools.product(self.suits,self.values):
            self.ActualCards.append(Card)

    def GetRandomCard(self):
        RandomNumber = random.randint(0,51)

        CardToBeReturned = self.ActualCards[RandomNumber]

        return (CardToBeReturned)

class Player:
    def __init__(self,ID,Card):
        self.PlayerID = ID
        self.CardForPlayer = Card

class Game:
    def __init__(self,NameOfGame):
        self.name = NameOfGame

class SimpleWar(Game):
    def __init__(self,NumberOfPlayers):
        self.NumberOfPlayers = NumberOfPlayers
        self.PlayerList = []

    def StartGame(self):
        DeckOfCards = Cards()
        for playerID in range(0,self.NumberOfPlayers):
            CardForPlayer = DeckOfCards.GetRandomCard()
            NewPlayer = Player(playerID,CardForPlayer)
            self.PlayerList.append(NewPlayer)
        self.DecideWinner()

    def DecideWinner(self):
        WinningID = self.PlayerList[0]
        for playerID in self.PlayerList:
            if(playerID.CardForPlayer[1]>WinningID.CardForPlayer[1]):
                WinningID = playerID
        print "Winner is Player "+str(WinningID.PlayerID)
        print "Her Card was "+ str(WinningID.CardForPlayer[1]) + " of " + str(WinningID.CardForPlayer[0])


if __name__=="__main__":
    NewGame = SimpleWar(2)
    NewGame.StartGame()