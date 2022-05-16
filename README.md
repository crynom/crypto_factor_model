# Digital Asset Pricing With Technical Analysis
Skepticism around technical analysis is by no means rare.
This jupyter notebook requests open, high, low, close, vwap, volume, and trade count data from Kraken.
With this data, a sequential model is used to predict the close price for the interval t+1 using data from the interval t.

## Future Plans
Although traditional asset prices can be generally considered discrete because they are denominated in cents,
the model is effectively attempting to predict a continuous value which is shown in it's predictions carrying out several decimal points.
Furthermore, after extensive testing with different intervals, I found that expanding the time horizon to anything above a day significantly increases
the mean absolute percent error. To change this, I plan on discretizing the predictions by making the model predict a range of returns which would be closer to a multiclassification problem. The return bin width will likely be determined using the standard deviation of log returns (volatility), but a single bin will likely be thinner than a full standard deviation.

Perhaps another more traditional model can implement technical features as a way to model investor sentiment given it's rising importance in our current market conditions.