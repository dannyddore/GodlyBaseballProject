import pandas as pd

#This file contains dataframes for pitching data from 2006 to 2017:

#Make dataframes of pitching stats from 2006 to 2017:
twoThousandSixPitchers = pd.read_csv('YearlyPitcherStats/2006Pitchers.csv', header = 0)
twoThousandSevenPitchers = pd.read_csv('YearlyPitcherStats/2007Pitchers.csv', header = 0)
twoThousandEightPitchers = pd.read_csv('YearlyPitcherStats/2008Pitchers.csv', header = 0)
twoThousandNinePitchers = pd.read_csv('YearlyPitcherStats/2009Pitchers.csv', header = 0)
twoThousandTenPitchers = pd.read_csv('YearlyPitcherStats/2010Pitchers.csv', header = 0)
twoThousandElevenPitchers = pd.read_csv('YearlyPitcherStats/2011Pitchers.csv', header = 0)
twoThousandTwelvePitchers = pd.read_csv('YearlyPitcherStats/2012Pitchers.csv', header = 0)
twoThousandThirteenPitchers = pd.read_csv('YearlyPitcherStats/2013Pitchers.csv', header = 0)
twoThousandFourteenPitchers = pd.read_csv('YearlyPitcherStats/2014Pitchers.csv', header = 0)
twoThousandFifteenPitchers = pd.read_csv('YearlyPitcherStats/2015Pitchers.csv', header = 0)
twoThousandSixteenPitchers = pd.read_csv('YearlyPitcherStats/2016Pitchers.csv', header = 0)
twoThousandSeventeenPitchers = pd.read_csv('YearlyPitcherStats/2017Pitchers.csv', header = 0)

print(twoThousandSixPitchers)