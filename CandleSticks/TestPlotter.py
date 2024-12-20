from CandleStick import CandleStickPlotter
cs = CandleStickPlotter()

# filePath = 'AxisData.csv'
# resistanceLevels = [1125, 1130, 1135]
# supportLevels = [1119, 1120, 1128]
# candleIndex = [4,12,20,28]
# cursor = True
# priceDifference = 1.5

filePath = 'AsianPaintsData.csv'
resistanceLevels = [3360, 3375, 3379]
supportLevels = [3340, 3358, 3365]
candleIndex = [3,6,9,12]
cursor = True

cs.plotCandleSticks(filePath, resistanceLevels, supportLevels, candleIndex, cursor)