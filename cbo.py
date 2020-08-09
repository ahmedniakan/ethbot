
import trend

import cbpro
import time
import threading

def getCurrentPrice():
        ticker = public_client.get_product_ticker(product_id='ETH-USD')
        currentPrice = ticker["price"]
        return float(currentPrice)
    
#open client
public_client = cbpro.PublicClient()


#init starting metrics

#update price change realtime
while True:
    timeInSeconds = 0;
    Trend = trend.Trend(getCurrentPrice());
    while Trend.isPotentiallyIncreasing():
        time.sleep(30)
        Trend.updateTrend(getCurrentPrice())
        timeInSeconds = timeInSeconds + 30
    else:
        if Trend.declareSell():
                timeInMinutes = timeInSeconds/60
                print("Price Started at", Trend.priceAtStart)
                print("Price ended at", Trend.currentPrice)
                print("Total change of ", Trend.priceChangeSinceStart(), " in ", timeInMinutes, " Minutes")
                print("Selling...")


# use sleep as a coutner for seconds. divide increasing price by counter to see if price is aggresively increasing. if so, stay in state of isPump.

#if isPump == true for 104% increase of buy && $4 increase since last !isPump, then sell immediately once !isPump
# if !isPump occurs after isPump begins being true, but above states arent satisfied, do nothing

