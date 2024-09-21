
## For demonstation Purposes only , creates a generic class template on which Superfunds can be modelled on , please ignore up to line 22.
class SuperFund:
    def __init__(self, name , ESG):
        self.name = name
        self.ESG = ESG
        ESG = []

## List of Superfunds to be queried
Superlist = []

Superlist.append(SuperFund('AlexSuper',['Weapons','Renewables']))
Superlist.append(SuperFund('Tahlia Super',['Tobbacco','Firearms']))
Superlist.append(SuperFund('Luke Super',['Drugs','Healthcare']))

##Generate List to query (ESG Issues)
Querylist = ["null"]

for i in Superlist:
    print(i.name)
    print(i.ESG)

## List of Generated ESG Catergories from user prompt -> Currently filled with static values
ESGList =[]
ESGList.append('Weapons')
ESGList.append('Drugs')
## list of ALL ESG catergories (Will Remain Static)
ALLESGList =[]
ALLESGList.append('Weapons')
ALLESGList.append('Drugs')
ALLESGList.append('Firearms')
ALLESGList.append('Renewables')

## Generate Query Based on Superfund
def GenerateSuperfundQuery(SuperFundName):
    outputstring = 'Does '+SuperFundName+' Invest in '
    for x in ALLESGList:
        outputstring += x+', '

    outputstring += '?'

##Use this string to query Chat GPT ETC
    print(outputstring)
    
##Generate Query Based on ESG

def GenerateESGQuery(ESGList):
    outputstring = 'Show me Superfunds that Invest in '
    for x in ESGList:
        outputstring += x+' ,'
    outputstring +='.'
    print(outputstring)



GenerateESGQuery(ESGList)
GenerateSuperfundQuery('AlexSuper')