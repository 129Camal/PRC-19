import requests
import json
import re
import sys

# f = open('../turtle/stages.ttl', 'w')
# sys.stdout = f

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
    # if(competition['ClassCode'] == "1.UWT"):
    if(competition['ClassCode'] == "2.UWT"):

        getStages = {
            'disciplineId': '10',
            'competitionId': competition['CompetitionId'],
            'take': '40',
            'skip': '0',
            'page': '1',
            'pageSize': '40'
        }
        r2 = requests.post(
            'https://dataride.uci.ch/Results/iframe/Races/', data=getStages)

        stages = json.loads(r2.text)

        for stage in stages['data']:
            if(stage['RaceName'] == "Final Classification"):

                getClassifications = {
                    'disciplineId': '10',
                    'raceId': str(stage['Id'])
                }

                r3 = requests.post(
                    'https://dataride.uci.ch/Results/iframe/Events/', data=getClassifications)

                classifications = json.loads(r3.text)

                for classification in classifications:
                    if(classification['EventName'] ==  "General classification"):
                        getGeneral = {
                            'disciplineId': '10',
                            'eventId': classification['EventId'],
                            'take': '500',
                            'skip': '0',
                            'page': '1',
                            'pageSize': '500'
                        }

                        r4 = requests.post(
                            'https://dataride.uci.ch/Results/iframe/Results/', data=getGeneral)

                        generalClassification = json.loads(r4.text)

                        for position in generalClassification['data']:
                            print(position['IndividualDisplayName'])
        break
