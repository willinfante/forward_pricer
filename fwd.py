import decimal

print('FORWARD POINT PRICER:\n')

SOFR_rates = {'USD': .0452, 'NOK': .0458, 'SEK': .024, 'EUR': 0.0233, 'CHF': 0.0006, 'GBP': .0463, 'JPY': 0.0052}
sb = input('Single spot rate (1) or bid-offer (2): ')
    

def check_pips(pair):
    if 'JPY' in pair:
        pip_size = 0.01
    else:
        pip_size = 0.0001 

    return pip_size

def main(z):
    if z == '1':
        
        currency = input('Enter currency pair: ')
        spot_rate = float(input('Spot rate: '))

        dom_rate = float(input('Dominant interest rate: '))
        sec_rate = float(input('Secondary interest rate: '))
        maturity = float(input('Maturity in days: '))

        ## Determine which currency is the terms and which is the base
        points = spot_rate * (sec_rate - dom_rate) * (maturity / 360) * 100
    
        fwd_rate = spot_rate  + (points * check_pips(currency))

        print('\n')
        print('FORWARD POINTS: ', points)
        print('FORWARD RATE: ', fwd_rate)
        print('\n')

    elif z == '2':
        currency = input('Enter currency pair: ')
        spot_rate = str(input('Input bid-offer in format [ BID/OFFER ]: '))
        x = spot_rate.split('/')
    
        # Get number of decimal places
        d = decimal.Decimal(x[0])
        num_decimals = d.as_tuple().exponent * -1

        # Convert 2nd number (offer) to full number
        seclen =  len(x[1])  
        base_length =  len(x[0])  -   len(x[1])  
        base = x[0][:base_length]
        offer_rate_top = x[1]

        offer_rate_full = base + offer_rate_top

        dom_rate = float(input('Dominant Interest Rate: '))
        sec_rate = float(input('Secondary Interest Rate: '))
        t = float(input('Days to Maturity: '))

        bid_points = float(x[0]) * (sec_rate - dom_rate) * (t / 360) * 100
        offer_points = float(offer_rate_full) * (sec_rate - dom_rate) * (t / 360) * 100

        fwd_offer = float(offer_rate_full) + (offer_points * check_pips(currency))
        fwd_bid = float(x[0]) + (bid_points * check_pips(currency))

        if dom_rate > sec_rate:
            print(round(fwd_offer, num_decimals), '/', round(fwd_bid, num_decimals)) # Just reversed the two here - not sure if this is how it is really done
        else:
            print(round(fwd_bid, num_decimals), '/', round(fwd_offer, num_decimals))
        print('\n')

    elif z == 'HELP' or z == 'help':

        input()

    else:
        exit()

main(sb)

