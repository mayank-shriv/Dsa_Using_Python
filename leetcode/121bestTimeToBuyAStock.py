stockProfits = [7,2,1,5,6,4,8]
sp = stockProfits
# length = 7
# brute force

# maxStockValue = 0

# for i in range(len(stockProfits)):
#     for j in range(i+1,len(stockProfits)):
#         stockPrice = stockProfits[j]-stockProfits[i]
#         if (stockPrice> maxStockValue):
#             maxStockValue = stockPrice
# print(maxStockValue)



# Optimal

maxStockPrice = 0
minStockPrice = float("inf")
l = len(stockProfits)
for i in range(l):
    minStockPrice = min(minStockPrice,stockProfits[i])
    maxStockPrice = max(maxStockPrice,stockProfits[i]-minStockPrice)

print(maxStockPrice)