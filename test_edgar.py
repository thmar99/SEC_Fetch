from sec_tester import *
'''testing samples based on S&P sectors. 2 companies tested per sector, 4 for financials. 
3 10-k requests per company, 2 10-1 request per company, totaling 120 requests to edgar
A comment #passed will denote up to which test the fecterh has succesfulyl worked'''

#form types and time parameters
forms = ['10-k','10-q']
yr_ind1 = '20201231'
yr_ind2 = '20151231'
yr_ind3 = '20101231'
yr_ind1qtr = '20200701'
yr_ind2qtr = '20100701'

#Industrials

comp1 = 'ba'
comp2 = 'cat'
#EdgarFetcher(yr_ind1,'ba',forms[0])#, index columns have '=' in them, thorinw off excel as it thinks its a function (statement of operations) PASSED
#EdgarFetcher(yr_ind2,comp1,forms[0])#, index columns have '=' in them, thorinw off excel as it thinks its a function (statement of operations), also its not removing trailing '-' in data
#EdgarFetcher(yr_ind3,comp1,forms[0]) #no url column attached, indeces are wiped & it has random charcters in it
#EdgarFetcher(yr_ind1qtr,comp1,forms[1])
#EdgarFetcher(yr_ind2qtr,comp1,forms[1]) #this is an xml format
#EdgarFetcher(yr_ind1,comp2,forms[0])
#EdgarFetcher(yr_ind2,comp2,forms[0]) # '-' found in index values
#EdgarFetcher(yr_ind3,comp2,forms[0])
#EdgarFetcher(yr_ind1qtr,comp2,forms[1])
EdgarFetcher(yr_ind2qtr,comp2,forms[1])

#Tech
comp1 = 'aapl'
comp2 = 'msft'
EdgarFetcher(yr_ind1,comp1,forms[0])
EdgarFetcher(yr_ind2,comp1,forms[0])
EdgarFetcher(yr_ind3,comp1,forms[0])
EdgarFetcher(yr_ind1qtr,comp1,forms[1])
EdgarFetcher(yr_ind2qtr,comp1,forms[1])
EdgarFetcher(yr_ind1,comp2,forms[0])
EdgarFetcher(yr_ind2,comp2,forms[0])
EdgarFetcher(yr_ind3,comp2,forms[0])
EdgarFetcher(yr_ind1qtr,comp2,forms[1])
EdgarFetcher(yr_ind2qtr,comp2,forms[1])

#Consumer Discretionary
comp1 = 'nke'
comp2 = 'hd'
EdgarFetcher(yr_ind1,comp1,forms[0])
EdgarFetcher(yr_ind2,comp1,forms[0])
EdgarFetcher(yr_ind3,comp1,forms[0])
EdgarFetcher(yr_ind1qtr,comp1,forms[1])
EdgarFetcher(yr_ind2qtr,comp1,forms[1])
EdgarFetcher(yr_ind1,comp2,forms[0])
EdgarFetcher(yr_ind2,comp2,forms[0])
EdgarFetcher(yr_ind3,comp2,forms[0])
EdgarFetcher(yr_ind1qtr,comp2,forms[1])
EdgarFetcher(yr_ind2qtr,comp2,forms[1])

#Consumer Staples
comp1 = 'ko'
comp2 = 'cl'
EdgarFetcher(yr_ind1,comp1,forms[0])
EdgarFetcher(yr_ind2,comp1,forms[0])
EdgarFetcher(yr_ind3,comp1,forms[0])
EdgarFetcher(yr_ind1qtr,comp1,forms[1])
EdgarFetcher(yr_ind2qtr,comp1,forms[1])
EdgarFetcher(yr_ind1,comp2,forms[0])
EdgarFetcher(yr_ind2,comp2,forms[0])
EdgarFetcher(yr_ind3,comp2,forms[0])
EdgarFetcher(yr_ind1qtr,comp2,forms[1])
EdgarFetcher(yr_ind2qtr,comp2,forms[1])

#Utilities
comp1 = 'pcg'
comp2 = 'nee'
EdgarFetcher(yr_ind1,comp1,forms[0])
EdgarFetcher(yr_ind2,comp1,forms[0])
EdgarFetcher(yr_ind3,comp1,forms[0])
EdgarFetcher(yr_ind1qtr,comp1,forms[1])
EdgarFetcher(yr_ind2qtr,comp1,forms[1])
EdgarFetcher(yr_ind1,comp2,forms[0])
EdgarFetcher(yr_ind2,comp2,forms[0])
EdgarFetcher(yr_ind3,comp2,forms[0])
EdgarFetcher(yr_ind1qtr,comp2,forms[1])
EdgarFetcher(yr_ind2qtr,comp2,forms[1])

#Real Estate
comp1 = 'cbre'
comp2 = 'eqix'
EdgarFetcher(yr_ind1,comp1,forms[0])
EdgarFetcher(yr_ind2,comp1,forms[0])
EdgarFetcher(yr_ind3,comp1,forms[0])
EdgarFetcher(yr_ind1qtr,comp1,forms[1])
EdgarFetcher(yr_ind2qtr,comp1,forms[1])
EdgarFetcher(yr_ind1,comp2,forms[0])
EdgarFetcher(yr_ind2,comp2,forms[0])
EdgarFetcher(yr_ind3,comp2,forms[0])
EdgarFetcher(yr_ind1qtr,comp2,forms[1])
EdgarFetcher(yr_ind2qtr,comp2,forms[1])

#Materials
comp1 = 'dd'
comp2 = 'shw'
EdgarFetcher(yr_ind1,comp1,forms[0])
EdgarFetcher(yr_ind2,comp1,forms[0])
EdgarFetcher(yr_ind3,comp1,forms[0])
EdgarFetcher(yr_ind1qtr,comp1,forms[1])
EdgarFetcher(yr_ind2qtr,comp1,forms[1])
EdgarFetcher(yr_ind1,comp2,forms[0])
EdgarFetcher(yr_ind2,comp2,forms[0])
EdgarFetcher(yr_ind3,comp2,forms[0])
EdgarFetcher(yr_ind1qtr,comp2,forms[1])
EdgarFetcher(yr_ind2qtr,comp2,forms[1])

#Energy
comp1 = 'cop'
comp2 = 'xom'
EdgarFetcher(yr_ind1,comp1,forms[0])
EdgarFetcher(yr_ind2,comp1,forms[0])
EdgarFetcher(yr_ind3,comp1,forms[0])
EdgarFetcher(yr_ind1qtr,comp1,forms[1])
EdgarFetcher(yr_ind2qtr,comp1,forms[1])
EdgarFetcher(yr_ind1,comp2,forms[0])
EdgarFetcher(yr_ind2,comp2,forms[0])
EdgarFetcher(yr_ind3,comp2,forms[0])
EdgarFetcher(yr_ind1qtr,comp2,forms[1])
EdgarFetcher(yr_ind2qtr,comp2,forms[1])

#Financials
comp1 = 'blk'
comp2 = 'c'
comp3 = 'jpm'
comp4 = 'bk'
EdgarFetcher(yr_ind1,comp1,forms[0])
EdgarFetcher(yr_ind2,comp1,forms[0])
EdgarFetcher(yr_ind3,comp1,forms[0])
EdgarFetcher(yr_ind1qtr,comp1,forms[1])
EdgarFetcher(yr_ind2qtr,comp1,forms[1])
EdgarFetcher(yr_ind1,comp2,forms[0])
EdgarFetcher(yr_ind2,comp2,forms[0])
EdgarFetcher(yr_ind3,comp2,forms[0])
EdgarFetcher(yr_ind1qtr,comp2,forms[1])
EdgarFetcher(yr_ind2qtr,comp2,forms[1])
EdgarFetcher(yr_ind1,comp3,forms[0])
EdgarFetcher(yr_ind2,comp1,forms[0])
EdgarFetcher(yr_ind3,comp3,forms[0])
EdgarFetcher(yr_ind1qtr,comp3,forms[1])
EdgarFetcher(yr_ind2qtr,comp3,forms[1])
EdgarFetcher(yr_ind1,comp4,forms[0])
EdgarFetcher(yr_ind2,comp4,forms[0])
EdgarFetcher(yr_ind3,comp4,forms[0])
EdgarFetcher(yr_ind1qtr,comp4,forms[1])
EdgarFetcher(yr_ind2qtr,comp4,forms[1])

#Health Care
comp1 = 'abbv'
comp2 = 'cah'
EdgarFetcher(yr_ind1,comp1,forms[0])
EdgarFetcher(yr_ind2,comp1,forms[0])
EdgarFetcher(yr_ind3,comp1,forms[0])
EdgarFetcher(yr_ind1qtr,comp1,forms[1])
EdgarFetcher(yr_ind2qtr,comp1,forms[1])
EdgarFetcher(yr_ind1,comp2,forms[0])
EdgarFetcher(yr_ind2,comp2,forms[0])
EdgarFetcher(yr_ind3,comp2,forms[0])
EdgarFetcher(yr_ind1qtr,comp2,forms[1])
EdgarFetcher(yr_ind2qtr,comp2,forms[1])

#Communication Services
comp1 = 'nws'
comp2 = 'vz'
EdgarFetcher(yr_ind1,comp1,forms[0])
EdgarFetcher(yr_ind2,comp1,forms[0])
EdgarFetcher(yr_ind3,comp1,forms[0])
EdgarFetcher(yr_ind1qtr,comp1,forms[1])
EdgarFetcher(yr_ind2qtr,comp1,forms[1])
EdgarFetcher(yr_ind1,comp2,forms[0])
EdgarFetcher(yr_ind2,comp2,forms[0])
EdgarFetcher(yr_ind3,comp2,forms[0])
EdgarFetcher(yr_ind1qtr,comp2,forms[1])
EdgarFetcher(yr_ind2qtr,comp2,forms[1])
