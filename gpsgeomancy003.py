import sys
import argparse
from pprint import pprint
import numpy as np
import ephem
import datetime
import urllib2
import random
import time
import  pytz 
from math import pi
from yahoo_finance import Share

from time import sleep
import os
import socket
import logging

# uncomment

#import req_admxi
#from ib.ext.Contract import Contract
#from ib.ext.Order import Order
#from ib.opt import ibConnection, message
#import mysql.connector

company_dict={'Fire': ['ACN', 'ACE', 'ATVI', 'ADBE', 'AFL', 'AMG', 'AKAM', 'ADS', 'ALL', 'GOOGL', 'GOOG', 'ALTR', 'AXP', 'AIG', 'AMT', 'AMP', 'ADI', 'AON', 'AIV', 'AAPL', 'AMAT', 'AIZ', 'ADSK', 'ADP', 'AVGO', 'AVB', 'BAC', 'BK', 'BBT', 'BRK-B', 'BLK', 'HRB', 'BXP', 'BRCM', 'CA', 'COF', 'CBG', 'SCHW', 'CB', 'CINF', 'CSCO', 'C', 'CTXS', 'CME', 'CTSH', 'CMA', 'CSC', 'CCI', 'DFS', 'ETFC', 'EBAY', 'EA', 'EMC', 'EFX', 'EQIX', 'EQR', 'ESS', 'FFIV', 'FB', 'FIS', 'FITB', 'FSLR', 'FISV', 'BEN', 'GGP', 'GNW', 'GS', 'HRS', 'HIG', 'HCP', 'HPQ', 'HST', 'HCBK', 'HBAN', 'INTC', 'ICE', 'IBM', 'INTU', 'IVZ', 'JPM', 'JNPR', 'KEY', 'KIM', 'KLAC', 'LRCX', 'LM', 'LUK', 'LNC', 'LLTC', 'L', 'MTB', 'MAC', 'MMC', 'MA', 'MHFI', 'MET', 'MCHP', 'MU', 'MSFT', 'MCO', 'MS', 'MSI', 'NDAQ', 'NAVI', 'NTAP', 'NFLX', 'NTRS', 'NVDA', 'ORCL', 'PAYX', 'PYPL', 'PBCT', 'PCL', 'PNC', 'PFG', 'PGR', 'PLD', 'PRU', 'PSA', 'QRVO', 'QCOM', 'O', 'RHT', 'RF', 'CRM', 'SNDK', 'STX', 'SPG', 'SWKS', 'SLG', 'STT', 'STI', 'SYMC', 'TROW', 'TEL', 'TDC', 'TXN', 'TRV', 'TMK', 'TSS', 'USB', 'UNM', 'VTR', 'VRSN', 'V', 'VNO', 'WFC', 'HCN', 'WDC', 'WU', 'WY', 'XRX', 'XLNX', 'XL', 'YHOO', 'ZION'], 'Earth': ['MMM', 'ADT', 'AES', 'GAS', 'APD', 'ARG', 'AA', 'ALLE', 'AEE', 'AAL', 'AEP', 'AME', 'APH', 'APC', 'APA', 'AVY', 'BHI', 'BLL', 'BA', 'CHRW', 'COG', 'CAM', 'CAT', 'CNP', 'CF', 'CHK', 'CVX', 'XEC', 'CTAS', 'CMS', 'CPGX', 'COP', 'CNX', 'ED', 'GLW', 'CSX', 'CMI', 'DHR', 'DE', 'DAL', 'DVN', 'DO', 'D', 'DOV', 'DOW', 'DTE', 'DD', 'DUK', 'DNB', 'EMN', 'ETN', 'ECL', 'EIX', 'EMR', 'ESV', 'ETR', 'EOG', 'EQT', 'ES', 'EXC', 'EXPD', 'XOM', 'FAST', 'FDX', 'FE', 'FLIR', 'FLS', 'FLR', 'FMC', 'FTI', 'FCX', 'GD', 'GE', 'GWW', 'HAL', 'HP', 'HES', 'HON', 'ITW', 'IR', 'IP', 'IFF', 'IRM', 'JEC', 'JBHT', 'KSU', 'KMI', 'LLL', 'LEG', 'LMT', 'LYB', 'MRO', 'MPC', 'MLM', 'MAS', 'WRK', 'MON', 'MOS', 'MUR', 'NOV', 'NFX', 'NEM', 'NEE', 'NLSN', 'NI', 'NBL', 'NSC', 'NOC', 'NRG', 'NUE', 'OXY', 'OKE', 'OI', 'PCAR', 'PH', 'PNR', 'POM', 'PCG', 'PSX', 'PNW', 'PXD', 'PBI', 'PPG', 'PPL', 'PX', 'PCP', 'PEG', 'PWR', 'RRC', 'RTN', 'RSG', 'RHI', 'ROK', 'COL', 'ROP', 'R', 'SCG', 'SLB', 'SEE', 'SRE', 'SHW', 'SIAL', 'SO', 'LUV', 'SWN', 'SE', 'SRCL', 'TE', 'TSO', 'TXT', 'RIG', 'TYC', 'UNP', 'UAL', 'UPS', 'URI', 'UTX', 'VLO', 'VRSK', 'VMC', 'WM', 'WMB', 'WEC', 'XEL', 'XYL'], 'Water': ['ABT', 'ABBV', 'AAP', 'AET', 'A', 'AGN', 'ALXN', 'MO', 'AMZN', 'ABC', 'AMGN', 'ADM', 'AN', 'AZO', 'BCR', 'BXLT', 'BAX', 'BDX', 'BBBY', 'BBY', 'BIIB', 'BWA', 'BSX', 'BMY', 'BF-B', 'CVC', 'CPB', 'CAH', 'HSIC', 'KMX', 'CCL', 'CBS', 'CELG', 'CERN', 'CMG', 'CI', 'CLX', 'COH', 'KO', 'CCE', 'CL', 'CMCSA', 'CMCSK', 'CAG', 'STZ', 'COST', 'CVS', 'DHI', 'DRI', 'DVA', 'DLPH', 'XRAY', 'DISCA', 'DISCK', 'DG', 'DLTR', 'DPS', 'EW', 'ENDP', 'EL', 'EXPE', 'ESRX', 'F', 'FOSL', 'GME', 'GPS', 'GRMN', 'GIS', 'GM', 'GPC', 'GILD', 'GT', 'HBI', 'HOG', 'HAR', 'HAS', 'HCA', 'HD', 'HRL', 'HUM', 'IPG', 'ISRG', 'JNJ', 'JCI', 'K', 'GMCR', 'KMB', 'KSS', 'KHC', 'KR', 'LB', 'LH', 'LEN', 'LLY', 'LOW', 'M', 'MNK', 'MAR', 'MAT', 'MKC', 'MCD', 'MCK', 'MJN', 'MDT', 'MRK', 'KORS', 'MHK', 'TAP', 'MDLZ', 'MNST', 'MYL', 'NWL', 'NWSA', 'NWS', 'NKE', 'JWN', 'ORLY', 'OMC', 'PDCO', 'PEP', 'PKI', 'PRGO', 'PFE', 'PM', 'RL', 'PCLN', 'PG', 'PHM', 'PVH', 'DGX', 'REGN', 'RAI', 'ROST', 'RCL', 'SNI', 'SIG', 'SJM', 'SNA', 'STJ', 'SWK', 'SPLS', 'SBUX', 'HOT', 'SYK', 'SYY', 'TGT', 'TGNA', 'THC', 'HSY', 'TMO', 'TIF', 'TWX', 'TWC', 'TJX', 'TSCO', 'TRIP', 'FOXA', 'FOX', 'TSN', 'UA', 'UNH', 'UHS', 'URBN', 'VFC', 'VAR', 'VRTX', 'VIAB', 'WMT', 'WBA', 'DIS', 'WAT', 'ANTM', 'WHR', 'WFM', 'WYN', 'WYNN', 'YUM', 'ZBH', 'ZTS'], 'Air': ['T', 'CTL', 'FTR', 'LVLT', 'VZ']}


# TODO: test and tweak buy and sell *eg. ticker*, updating and accounting


def loadTLE(path):
    """ Loads a TLE file and creates a list of satellites."""
    f = urllib2.urlopen(path)
    satlist = []
    l1 = f.readline()
    while l1:
        l2 = f.readline()
        l3 = f.readline()
        sat = ephem.readtle(l1,l2,l3)
        satlist.append(sat)
#        print sat.name
        l1 = f.readline()
    f.close()
    # print "%i satellites loaded into list"%len(satlist)
    return satlist


def makesatdict(location):
    """
    makes a dictionary with prn as a key and values as a list e.g.
    prn:[ele, azi, snr] FOR over horizon
    """
    satdict = {}
    oursatlist=loadTLE("http://www.celestrak.com/NORAD/elements/gps-ops.txt")

    for sat in oursatlist:
        sat.compute(location)
        if sat.alt>0:
#            print sat.name, np.rad2deg(sat.alt), np.rad2deg(sat.az), sat.sublat*(180/pi)
#            prn= sat.name.split('(', 1)[1].split(')')[0]
            # how to cut out PRN from: GPS BIIF-10  (PRN 08) 2.87929015028 17.146908166 ?
#            print int(prn[4:])
            prno=sat.name.split('(', 1)[1].split(')')[0]
            prn=int(prno[4:])
            satdict[prn] = [int(np.rad2deg(sat.alt)), int(np.rad2deg(sat.az)), int(sat.sublat*(180/pi))]
    return satdict

# dict for figures
figdict={'0010': ['Puer','Mars','Fire','Aries','+','Boy, yellow, beardless'], '0101': ['Amissio','Venus','Earth','Taurus','-','Loss, comprehended without'], '1101': ['Albus','Mercury','Air','Gemini','-','White, fair'], '1111': ['Populus','Moon','Water','Cancer','-','People, congregation'], '1100': ['Fortuna Major','Sun','Fire','Leo','+','Greater fortune, greater aid,safeguard entering'], '1001': ['Conjunctio','Mercury','Earth','Virgo','+','Conjunction, assembling'], '0100': ['Puella','Venus','Air','Libra','+','A girl, beautiful'], '1011': ['Rubeus','Mars','Water','Scorpio','-','Red, reddish'], '1010': ['Acquisitio','Jupiter','Fire','Sagitarrius','+','Obtaining, comprehending without'], '0110': ['Carcer','Saturn','Earth','Capricorn','+','A prison, bound'], '1110': ['Tristitia','Saturn','Air','Aquarius','-','Sadness, damned, cross'], '0111': ['Laetitia','Jupiter','Water','Pisces','-','Joy, laughing, healthy, bearded'], '0001': ['Cauda Draconis','Saturn & Mars','Fire','Scorpio','-','The threshold lower, or going out'], '1000': ['Caput Draconis',' Jupiter & Venus','Earth','Capricorn','+','The Head, the threshold entering, the upper threshold'], '0011': ['Fortuna Minor','Sun','Fire','Leo','-','Lesser Fortune, lesser aid, safeguard going out'], '0000': ['Via','Moon','Water','Cancer','+','Way, journey']}

roman=['0','I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI']

#mapped to Crowley
crowley=['0','X','I','IV','VII','XI','II','V','VIII','XII','III','VI','IX','XIII','XIV','XV','XVI']

def parse_arguments():
    parser = argparse.ArgumentParser(description='Geomancy with GPS satellite positions')
    parser.add_argument('-v', '--verbose',
                        help="Print verbose outputs to screen (intermediate selections etc.)",
                        action='store_true',
                        default=False)
    return (parser.parse_args())



def directionclassify(satdict):
    """
    Appends compass direction onto end of list for each satellite.
    Also appends a 'score' of how near the satellite is to the
    cardinal point, which is the number of degrees away from the
    due cardinal points (N=0, E=90, S=180, W=270)

    Sample output
    {2: [7, 132, 16, 'East', 42],
     6: [19, 94, 27, 'East', 4],
     12: [70, 259, 29, 'West', 11],
     14: [28, 312, 31, 'West', 42],
     15: [16, 187, 32, 'South', 7],
     17: [24, 46, 25, 'East', 44],
     22: [4, 280, 0, 'West', 10],
     24: [77, 150, 50, 'South', 30],
     25: [29, 255, 32, 'West', 15],
     32: [4, 347, 0, 'North', 13],
     39: [28, 165, 46, 'South', 15]}
    """
    for prn in satdict:
        azi = satdict[prn][1]
        if azi >= 315 or azi <= 45: # fixed >=bug
            satdict[prn].append("North")
            if azi >= 180:
                azideviation = 360 - azi
            else:
                azideviation = azi
            satdict[prn].append(azideviation)
        if azi > 45 and azi <= 135:
            satdict[prn].append("East")
            azideviation = abs(azi - 90)
            satdict[prn].append(azideviation)
        if azi > 135 and azi <= 225:
            satdict[prn].append("South")
            azideviation = abs(azi - 180)
            satdict[prn].append(azideviation)
        if azi > 225 and azi < 315:
            satdict[prn].append("West")
            azideviation = abs(azi - 270)
            satdict[prn].append(azideviation)

    return satdict


def selectsats(satdict):
    """Choose four satellites to form the reading based on the
    following criteria, applied in order:

    1. Closeness of satellite to the azimuth of the direction based
    on azideviation score from directionclassify

    2. Signal to noise (highest number wins)

    """
    chosenfour = {}

    for prn in satdict:
#        print(prn)
 #       print(satdict[prn])
        direction = satdict[prn][3]
        aziscore = satdict[prn][4]
        if direction in chosenfour:  # if the key is already in the dict
            # select by lowest azi deviation
            if aziscore < chosenfour[direction][4]:
                chosenfour[direction] = [prn,
                                         satdict[prn][0],
                                         satdict[prn][1],
                                         satdict[prn][2],
                                         aziscore]
            # in the unlikely case that two satellites share the same azi
            elif aziscore == chosenfour[direction][4]:
                # select by highest snr
                if satdict[prn][2] > chosenfour[direction][3]: # fixed keyerror here
                    chosenfour[direction] = [prn,
                                             satdict[prn][0],
                                             satdict[prn][1],
                                             satdict[prn][2],
                                             aziscore]
        else:
            chosenfour[direction] = [prn,
                                     satdict[prn][0],
                                     satdict[prn][1],
                                     satdict[prn][2],
                                     aziscore]

    return chosenfour


def getsatellites(gps, verbose):
    """
    main reiterating loop which reads the incoming nmea sentences
    from the gps, sends to parser and catches user interrupt:
    ctrl-c
    """
    gsvlist = []
    while gsvlist == []:
        try:
            line = gps.readline()
            if line.startswith('$GPGSV'):
                line = formatline(line, verbose)

                # formatline performs checksum and returns None if
                # it fails
                if line is None:
                    break

                gsvlist = parseGSV(line, gps, verbose)
                gsvlist = formatgsvlist(gsvlist)

                return gsvlist

        except KeyboardInterrupt:
            # user sent ctrl-c to stop script
            gps.close()
            print """
user interrupt, shutting down"""
            sys.exit()


def inttodot(integer):
    """
    Convert an integer to divination dots, two dots if the integer
    is even, one if odd, two if zero

    Takes an integer argument, returns a string of two dotchars or
    one

    """
    dotchar = "*"
    if integer % 2 == 0:
        dot = dotchar * 2
    else:
        dot = dotchar + " "  # The addition of a space helps the
                             # final diagram line up

    return dot

def oddoreven(integer):
    if integer % 2 == 0:
        dot = 1
    else:
        dot = 0
    return dot
    
def domothers(chosenfour):
    """ Append binary representation 0 as O/odd, 1 as OO/even
    """
    motherlist=[]
    for elemental in ["South", "East", "North", "West"]:
        binrep=[]
        for body in range(4): 
            binrep.append(oddoreven(chosenfour[elemental][body]))
        motherlist.append(binrep)
    return motherlist

def dodaughters(motherlist):
    daughterlist=[]
    body=zip(*motherlist)
    for parts in body:
        daughterlist.append(parts)
    return daughterlist

def madd(x,y):
    return int(not(x ^ y))    

def donephews(mlist,dlist):
    nlist=[]
    nlist.append([madd(mlist[0][0],mlist[1][0]),madd(mlist[0][1],mlist[1][1]),madd(mlist[0][2],mlist[1][2]),madd(mlist[0][3],mlist[1][3])])
    nlist.append([madd(mlist[2][0],mlist[3][0]),madd(mlist[2][1],mlist[3][1]),madd(mlist[2][2],mlist[3][2]),madd(mlist[2][3],mlist[3][3])])
    nlist.append([madd(dlist[0][0],dlist[1][0]),madd(dlist[0][1],dlist[1][1]),madd(dlist[0][2],dlist[1][2]),madd(dlist[0][3],dlist[1][3])])
    nlist.append([madd(dlist[2][0],dlist[3][0]),madd(dlist[2][1],dlist[3][1]),madd(dlist[2][2],dlist[3][2]),madd(dlist[2][3],dlist[3][3])])
    return nlist

def dowitnesses(nlist):
    wlist=[]
    wlist.append([madd(nlist[0][0],nlist[1][0]),madd(nlist[0][1],nlist[1][1]),madd(nlist[0][2],nlist[1][2]),madd(nlist[0][3],nlist[1][3])])
    wlist.append([madd(nlist[2][0],nlist[3][0]),madd(nlist[2][1],nlist[3][1]),madd(nlist[2][2],nlist[3][2]),madd(nlist[2][3],nlist[3][3])])
    return wlist

def dojudge(wlist):
    jlist=[]
    jlist.append([madd(wlist[0][0],wlist[1][0]),madd(wlist[0][1],wlist[1][1]),madd(wlist[0][2],wlist[1][2]),madd(wlist[0][3],wlist[1][3])])
    return jlist

def dorec(jlist,mlist):
    rlist=[]
    rlist.append([madd(mlist[0][0],jlist[0][0]),madd(mlist[0][1],jlist[0][1]),madd(mlist[0][2],jlist[0][2]),madd(mlist[0][3],jlist[0][3])])
    return rlist

def preparemothers(chosenfour):
    """Turn the data from the four chosen satellites into the mothers
    diagram.

     West     North    East    South
prn    **        *      **       *
ele    **        *      **       *
azi    *         *      *        **
snr    *         **     **       **

    Earth    Water    Air     Fire
       IV       III     II       I
head   **        *      **       *
neck   **        *      **       *
body   *         *      *        **
feet   *         **     **       **
      West     North    East    South

    """
    spacer = "      "
    EOL = "\n"
    motherstring = """       Earth    Water    Air     Fire
        IV       III     II       I""" + EOL

    head = "head" + spacer
    neck = "neck" + spacer
    body = "body" + spacer
    feet = "feet" + spacer

    for d in ["West", "North", "East", "South"]:
        head += inttodot(chosenfour[d][0]) + spacer
        neck += inttodot(chosenfour[d][1]) + spacer
        body += inttodot(chosenfour[d][2]) + spacer
        feet += inttodot(chosenfour[d][3]) + spacer

    motherstring += head + EOL
    motherstring += neck + EOL
    motherstring += body + EOL
    motherstring += feet + EOL
    motherstring += "       West     North    East    South"

    return motherstring

def drawit(listere):
    """ run thru list and print whole list line by line"""
    # must reverse listy
    listy=list(listere)
    listy.reverse()
    body=zip(*listy)
    for parts in body:
        for part in parts:
            if part==1:
                print "O O   ",
            else:
                print " O    ",
        print

def drawfig(body):
    for part in body:
        if part==1:
            print "O O   ",
        else:
            print " O    ",
        print

numeral=0

def lookfig(figure):
    # convert list to string
    global numeral
    key=''.join(str(e) for e in figure)
    numeral+=1
    #    return (' '.join((roman[numeral]+". GD:",crowley[numeral]+".",figdict[key][0],figdict[key][2],figdict[key][5])))
#    return (' '.join((roman[numeral]+". ",figdict[key][0],": ",figdict[key][2],figdict[key][5],figdict[key][4])))
    return (' '.join((figdict[key][0],": ",figdict[key][2],figdict[key][5],figdict[key][4])))

portfolio={}
portfolio.setdefault("Earth",{})
portfolio.setdefault("Fire",{})
portfolio.setdefault("Air",{})
portfolio.setdefault("Water",{})

def exec_trade(trade_json):
    server = socket.create_connection(self.trade_serv)
    server.settimeout(10)  # 10 seconds
    msg = trade_json.encode('utf-8')
    try:
        server.sendall(msg)
        resp = server.recv(1024)
        logging.debug(("reply:", resp))
    except socket.timeout:
        logging.debug("Order service timed out! Try again later.")
    server.close()


def exec_buy(whichone, shares, price):
    # actually buy shares on the market.
    trade = {"pass_client": pass_key,
             "contract": {"m_symbol": whichone,
                          "m_secType": "STK",
                          "m_exchange": "SMART",
                          "m_currency": "USD"
                      },
                 "order": {"m_action": "BUY",
                           "m_totalQuantity": shares,
                           "m_orderType": "LMT",
                           "m_lmtPrice": float(price), # what is price?
                           "m_tif": "DAY",
                           "m_goodAfterTime": "",
                           "m_goodTillDate": ""
                       }
                 }
    trade_json = json.dumps(trade)
    logging.debug("buying", shares, "shares at", price)
    exec_trade(trade_json)

def exec_sell(whichone,shares, price):
    # actually sell on the market
    trade = {"pass_client": pass_key,
             "contract": {"m_symbol": whichone,
                          "m_secType": "STK",
                          "m_exchange": "SMART",
                          "m_currency": "USD"
                      },
                 "order": {"m_action": "SELL",
                           "m_totalQuantity": shares,
                           "m_orderType": "LMT",
                           "m_lmtPrice": float(price),
                           "m_tif": "DAY",
                           "m_goodAfterTime": "",
                           "m_goodTillDate": ""
                       }
                 }
    trade_json = json.dumps(trade)
    logging.debug("selling", shares, "shares at", price)
    exec_trade(trade_json)

def update(self):
    cash = req_admxi.get_cash(ALGO)
    portfolio = req_admxi.get_portfolio(ALGO)
    # NOTE: this assumes we only have 1 issue in portfolio
    if len(portfolio) > 0:
        shares = int(portfolio[0][4])
        share.refresh()
        price = float(share.get_price())
        push_price(price)
        update_nav(price)


def whattodo(figure):
    # convert list to string
    key=''.join(str(e) for e in figure)
    action=figdict[key][4]
    if "-" in action:
        action="sell"
    else:
        action="buy"
    elemental=figdict[key][2]
#    elemental="Earth"
#    action="sell"
    whichone=random.choice(company_dict[elemental])

    if action=="buy":
        if portfolio[elemental].has_key(whichone):
            portfolio[elemental][whichone]+=1
        else:
            portfolio.setdefault(elemental, {})[whichone] = 1
        print "Buy", whichone
        bought=Share(whichone)
        print "Price", bought.get_price()

# do buy action

#exec_buy(whichone, 1, bought.get_price()):

    elif action=="sell":
        #choose a random from elemental dict
        if portfolio[elemental]:
            print portfolio
            whichone=random.choice(list(portfolio[elemental]))
            # unless it is zero decrement it
            if portfolio[elemental][whichone]>0:
                portfolio[elemental][whichone]-=1
                print "Sell", whichone
                sold=Share(whichone)
                print "Price", sold.get_price()
            else:
                print "No action taken"

# do sell action

#exec_sell(whichone, 1, sold.get_price()):

#    print portfolio    

    return (' '.join((action,whichone)))

def market_open():
    # returns True if NYSE is open (this does not work for holidays)
    ctime = datetime.datetime.now(pytz.timezone('US/Eastern'))
    chour = ctime.hour + (ctime.minute / 60.0)
    if (ctime.weekday() < 5) and (chour < 16) and (chour > 9.5):
        return True
    else:
        return False


def main():
    """
    """
    satdict = {}
    # What is Lat long of US stock exchange: 40.714353, -74.005973
    # Berlin here: 
    nyse = ephem.Observer()
    nyse.lat = np.deg2rad(40.714353)
    nyse.long = np.deg2rad(-74.005973)

    #consult at specific auspicious time which is opening of NYSE!

    while True:
    # wait for stock exchange to open 
        if market_open():
            nyse.date = datetime.datetime.now(pytz.timezone('US/Eastern')) # offset okay
            print nyse.date
            while ("West" not in str(satdict.values()) and "East" not in str(satdict.values()) and "North" not in str(satdict.values()) and "South" not in str(satdict.values())):
                satdict = makesatdict(nyse)
                satdict = directionclassify(satdict)
                chosenfour = selectsats(satdict)
                #            print "waitin"

            mlist=domothers(chosenfour)
            dlist=dodaughters(mlist)
            nlist=donephews(mlist,dlist)
            wlist=dowitnesses(nlist)
            jlist=dojudge(wlist)
            rlist=dorec(jlist,mlist)
            allfigures=mlist+dlist+nlist
            # add 1st 12 figures total 
            total=0
            for m in mlist: # more elegant?
                for mm in m:
                    total=total+mm
                    for m in dlist:
                        for mm in m:
                            total=total+mm
                    for m in nlist:
                        for mm in m:
                            total=total+mm
                            # divide by 12 and note remainder SKINNER p223
                            # gives number of house for fortune
                            house=total%12
                            chosen=allfigures[house]

            # print the chosen figure and its interpretation
            drawfig(chosen)
            print lookfig(chosen)

            # buy or sell
            whattodo(chosen)

            # update and print account details

        
if __name__ == '__main__':
    sys.exit(main())
