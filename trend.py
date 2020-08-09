class Trend:
    
    def __init__(self, priceAtStart):
        self.priceAtStart = priceAtStart
        self.previousPrice = priceAtStart
        self.currentPrice = priceAtStart
        self.priceOneMinuteAgo = priceAtStart
        self.numBadUpdates = 0
        self.isPump = True

        
    def isDecreasing(self):
        return True if (self.previousPrice > self.currentPrice) else False

    
    def isStagnant(self):
        return True if (self.previousPrice + .03 >= self.currentPrice) else False

    
    def hasDecreasedTooFast(self):
        return True if (self.priceOneMinuteAgo - self.previousPrice <= -1.00) else False 

    
    def updateTrend(self, updatedPrice):
        self.priceOneMinuteAgo = self.previousPrice
        self.previousPrice = self.currentPrice
        self.currentPrice = updatedPrice
        
        if self.isDecreasing() or self.isStagnant():
            self.numBadUpdates = self.numBadUpdates + 1
        else:
            self.numBadUpdates = 0
        

    def isPotentiallyIncreasing(self):
        return True if (self.numBadUpdates != 8 and not self.hasDecreasedTooFast()) else False


    def priceChangeSinceStart(self):
        return self.currentPrice - self.priceAtStart

    def declareSell(self):
        return True if (self.priceChangeSinceStart() > 8) else False

        

    
