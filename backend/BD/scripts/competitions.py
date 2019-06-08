import requests
import json
import re
import sys

f = open('../turtle/competitions.ttl', 'w')
sys.stdout = f

payload = {
    'disciplineId': '10',
    'take': '332',
    'skip': '0',
    'page': '1',
    'pageSize': '332',
    'sort[0][field]': 'StartDate',
    'sort[0][dir]': 'desc',
    'filter[filters][0][field]'	: "RaceTypeId",
    'filter[filters][0][value]'	: '0',
    'filter[filters][1][field]'	: "CategoryId",
    'filter[filters][1][value]'	: '0',
    'filter[filters][2][field]'	: "SeasonId",
    'filter[filters][2][value]'	: '132'
}

r = requests.post(
    'https://dataride.uci.ch/Results/iframe/Competitions/', data=payload)


competitions = json.loads(r.text)

for competition in competitions['data']:
    # if(re.search(r"(?<!W)WT", competition['ClassCode'])):
    if(competition['ClassCode'] == "1.UWT"):
        print("\n:competition_" + str(competition['CompetitionId']) + " rdf:type owl:NamedIndividual, :Classic ;",
              "\t:country \"" + competition['CountryName'] + "\";",
              "\t:date \"" + competition['Date'] + "\";",
              "\t:name \"" + competition['CompetitionName'] + "\".",
              sep="\n")

    if(competition['ClassCode'] == "2.UWT"):
        print("\n:competition_" + str(competition['CompetitionId']) + " rdf:type owl:NamedIndividual, :Tour ;",
              "\t:country \"" + competition['CountryName'] + "\";",
              "\t:date \"" + competition['Date'] + "\";",
              "\t:name \"" + competition['CompetitionName'] + "\".",
              sep="\n")
