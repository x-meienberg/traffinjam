# Traffinjam

Algotrading project for personal use and experiments

## Use of platform Alpaca

[Alpaca](https://alpaca.markets/algotrading) is a great platform for testing one's algorithmic trading programs and one can freely test one's result for free by signing up. The [documentation](https://alpaca.markets/docs/) is great, however following resources offer additional, useful information:

- [Algotrader 101](https://algotrading101.com/learn/alpaca-trading-api-guide/) for the Alpaca Trading API
- [Alpaca Forum](https://forum.alpaca.markets/t/manually-trading-stocks-using-postman-and-the-alpaca-api/166) for the Alpaca API using Postman
- [PartTimeLarry](https://twitter.com/PartTimeLarry), a great youtuber explaining trading with Python via his [videos](https://www.youtube.com/c/parttimelarry) and

## Further platforms used in the community

- [Quandl](https://www.quandl.com) is a platform which conglomerates data from different companies and services and is supported by programming languages like R, MATLAB, Ruby and more. However, some datasets must be paid for
- [Yahoo Finance API](https://pypi.org/project/yfinance/) or alternatively [RapidAPI](https://rapidapi.com/). One problem here is that the yahoo finance API can only receive get commands (free verison, which is great for own calculations and simulations but not for **real** trading)
- **Google Finance API**, which however mianly not used via code, rather via Google Sheets (see documentation [here](https://support.google.com/docs/answer/3093281?hl=en) for details). Algotrading101 offers additional insights [here](https://algotrading101.com/learn/google-finance-api-guide/).
- **Alpha Vantage** wihtin the RapidAPI documentation [here](https://rapidapi.com/alphavantage/api/alpha-vantage) with 5 requests per minute rate limit and maximum 500 requests/day hard limit.
- Trading View (requires Pine Script) is alternative to the Google Finance API. Great to learn and share ideas, however does not include API. Might be interesting for new traders to start their career.
- [IEX](https://iexcloud.io) and [API](https://iexcloud.io/docs/api/) (Costs 9$/month) was previously free, however you can check how many requests you want to make via a free account (disclaimer: No guarantee that this is true)

### More resources on Python for Finance

- [Learn Data Science](https://www.learndatasci.com/tutorials/python-finance-part-yahoo-finance-api-pandas-matplotlib/) is a great starting point. Go to the following [GitHub](https://github.com/LearnDataSci/articles) to find all articles.
- [freeCodeCamp.org](https://www.youtube.com/watch?v=xfzGZB4HhEE) Algorithmic Trading using Python - Full Course by Nick McCullum

### Other resources for APIs and other projects

- [RapidAPI](https://rapidapi.com/collection/list-of-free-apis) - list of free APIs

### Trading Strategies of [Nick McCullum](https://github.com/nickmccullum/algorithmic-trading-python)

1. Equal weight S&P 500
2. Quantitative momentum strategy
3. Quantitative value strategy

### Automated Trading Strategies from Medium

1. [Alpaca Pt. 1](https://medium.com/automation-generation/ultimate-list-of-automated-trading-strategies-you-should-know-part-1-c9a333f58930)
    1. Time-series momentum/mean reversion
    2. Cross-sectional momentum/mean reversion
    3. Dollar cost averaging
    4. Market making
    5. Day trading automation
2. [Alpha Research](https://medium.com/swlh/how-to-build-quant-algorithmic-trading-model-in-python-12abab49abe3)