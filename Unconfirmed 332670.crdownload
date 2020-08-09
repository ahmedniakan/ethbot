import json
import cbpro
import time
import threading 

#open client
public_client = cbpro.PublicClient()

def lol():
    print("hehe")




#init starting metrics
previousPrice = "0"
dollarChange = 0
realtimeTicker = public_client.get_product_ticker(product_id='ETH-USD')




#update price change realtime
while True:
    realtimeTicker = public_client.get_product_ticker(product_id='ETH-USD')
    currentPrice = realtimeTicker["price"]
    dollarChange = float(currentPrice) - float(previousPrice)


    #when pumpCheck goes from false to true, start timing, watch increase in price. if price ever decreases by a dollar, pumpCheck becomes false, check if price has increased $8 since pumpCheck became true && 104% of buy price


    #if pumpCheck == true
    #timer = threading.Timer(3.0, lol)
    #timer.start()
    
    print("Current Price", currentPrice)
    print("change in Value",  dollarChange)

        
    previousPrice = currentPrice
    timeElapsed = timeElapsed + 1
    
    print(timeElapsed)
    time.sleep(1)

    #updates state of change, sees if price is increasing aggresively
def isIncreasing(currentPrice, startingPrice):
    
    
    
    
    

    



# use sleep as a coutner for seconds. divide increasing price by counter to see if price is aggresively increasing. if so, stay in state of isPump.

#if isPump == true for 104% increase of buy && $4 increase since last !isPump, then sell immediately once !isPump
# if !isPump occurs after isPump begins being true, but above states arent satisfied, do nothing

