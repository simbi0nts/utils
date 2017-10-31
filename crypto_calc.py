#!/usr/bin/python

from datetime import datetime
import os

from coinmarketcap import Market
coinmarketcap = Market()
coins_info = coinmarketcap.ticker(convert='RUB')

# CHANGE THIS
my_score = dict(
    BTC=0.05,
    BCH=0.05,
    ETH=2.1,
    ONION=100.0
)
c_symbol = [s for s in my_score.keys()]

total_in_c = dict()

total_usd = 0.0
total_rub = 0.0
for coin in coins_info:
    _c = coin['symbol']
    if _c in c_symbol:
        total_in_c[_c] = dict()
        price_usd = float(coin['price_usd'])
        price_rub = float(coin['price_rub'])

        total_in_c[_c]['price_usd'] = price_usd * my_score[_c]
        total_in_c[_c]['price_rub'] = price_rub * my_score[_c]

        total_usd += total_in_c[_c]['price_usd']
        total_rub += total_in_c[_c]['price_rub']

## Archive ##

file_name = 'cryp_calc_archive.txt'
dir_name = os.path.dirname(os.path.abspath(__file__)) + '/'

sp = 3
def r(n):
    return round(n, sp)

score_to_str = ['total_{}: {} (usd:{}, rub:{})\n'.
                    format(str(c), str(v), str(r(total_in_c[c]['price_usd'])), str(r(total_in_c[c]['price_rub'])))
                for c, v in my_score.iteritems()]

template = '''
{}
Date: {}

{}

Total_usd: {}
Total_rub: {}

'''.format('#'*45, datetime.now(), ''.join(score_to_str), total_usd, total_rub)

print template

with open(dir_name+file_name, "a") as f:
    f.write(template)
