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

    if(not competition['IsInProgress']):

        r = 0

        if(re.search(r"^1\.", competition['ClassCode'])):
            print("\n:competition_" + str(competition['CompetitionId']) + " rdf:type owl:NamedIndividual, :Classic ;",
                  "\t:country \"" + competition['CountryName'] + "\";",
                  "\t:date \"" + competition['Date'] + "\";",
                  "\t:class \"" + competition['ClassCode'] + "\";",
                  "\t:name \"" + competition['CompetitionName'] + "\".",
                  sep="\n")
            r = 1

        if(re.search(r"^2\.", competition['ClassCode']) and r == 0):
            print("\n:competition_" + str(competition['CompetitionId']) + " rdf:type owl:NamedIndividual, :Tour ;",
                  "\t:country \"" + competition['CountryName'] + "\";",
                  "\t:date \"" + competition['Date'] + "\";",
                  "\t:class \"" + competition['ClassCode'] + "\";",
                  "\t:name \"" + competition['CompetitionName'] + "\".",
                  sep="\n")
            r = 1

        if(r == 0):
            continue

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
            if(stage['RaceName'] != "Final Classification"):
                print("\n:stage_" + str(stage['Id']) + " rdf:type owl:NamedIndividual, :Stage ;",
                      "\t:date \"" + stage['Date'] + "\";",
                      "\t:name \"" + stage['RaceName'] + "\".",
                      sep="\n")
                print("\n:competition_" + str(
                    competition['CompetitionId']) + " :hasStage :stage_" + str(stage['Id']) + " .\n")
            else:

                getClassifications = {
                    'disciplineId': '10',
                    'raceId': str(stage['Id'])
                }

                r3 = requests.post(
                    'https://dataride.uci.ch/Results/iframe/Events/', data=getClassifications)

                classifications = json.loads(r3.text)

                for classification in classifications:
                    if(classification['EventName'] == "General classification"):
                        print(
                            "\n:general_" + str(classification['EventId']) + " rdf:type owl:NamedIndividual , :General .\n ")
                        print("\n:competition_" + str(competition['CompetitionId']) + " :hasGeneral :general_" + str(
                            classification['EventId']) + " .\n")

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
                            if(not position['TeamName']):
                                position['TeamName'] = "--"
                            if(not position['ResultValue']):
                                position['ResultValue'] = "--:--:--"
                            if(not position['IndividualDisplayName']):
                                position['IndividualDisplayName'] = "Not Available"

                            print("\n:position_" + str(position['ResultId']) + " rdf:type owl:NamedIndividual, :Position ;",
                                  "\t:value \"" +
                                  position['ResultValue'] + "\";",
                                  "\t:rank \"" +
                                  str(position['SortOrder']) + "\";",
                                  "\t:team \"" + position['TeamName'] + "\";",
                                  "\t:name \"" +
                                  position['IndividualDisplayName'] + "\".",
                                  sep="\n")

                            print("\n:general_" + str(classification['EventId']) + " :hasPosition :position_" + str(
                                position['ResultId']) + " .\n")

                    if(classification['EventName'] == "Points Classification"):
                        print(
                            "\n:points_" + str(classification['EventId']) + " rdf:type owl:NamedIndividual , :Points .\n ")
                        print("\n:competition_" + str(competition['CompetitionId']) + " :hasPoints :points_" + str(
                            classification['EventId']) + " .\n")

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
                            if(not position['TeamName']):
                                position['TeamName'] = "--"
                            if(not position['ResultValue']):
                                position['ResultValue'] = "--:--:--"
                            if(not position['IndividualDisplayName']):
                                position['IndividualDisplayName'] = "Not Available"

                            print("\n:position_" + str(position['ResultId']) + " rdf:type owl:NamedIndividual, :Position ;",
                                  "\t:value \"" +
                                  position['ResultValue'] + "\";",
                                  "\t:rank \"" +
                                  str(position['SortOrder']) + "\";",
                                  "\t:team \"" + position['TeamName'] + "\";",
                                  "\t:name \"" +
                                  position['IndividualDisplayName'] + "\".",
                                  sep="\n")

                            print("\n:points_" + str(classification['EventId']) + " :hasPosition :position_" + str(
                                position['ResultId']) + " .\n")

                    if(classification['EventName'] == "Youth Classification"):
                        print(
                            "\n:youth_" + str(classification['EventId']) + " rdf:type owl:NamedIndividual , :Youth .\n ")
                        print("\n:competition_" + str(competition['CompetitionId']) + " :hasYouth :youth_" + str(
                            classification['EventId']) + " .\n")

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
                            if(not position['TeamName']):
                                position['TeamName'] = "--"
                            if(not position['ResultValue']):
                                position['ResultValue'] = "--:--:--"
                            if(not position['IndividualDisplayName']):
                                position['IndividualDisplayName'] = "Not Available"

                            print("\n:position_" + str(position['ResultId']) + " rdf:type owl:NamedIndividual, :Position ;",
                                  "\t:value \"" +
                                  position['ResultValue'] + "\";",
                                  "\t:rank \"" +
                                  str(position['SortOrder']) + "\";",
                                  "\t:team \"" + position['TeamName'] + "\";",
                                  "\t:name \"" +
                                  position['IndividualDisplayName'] + "\".",
                                  sep="\n")

                            print("\n:youth_" + str(classification['EventId']) + " :hasPosition :position_" + str(
                                position['ResultId']) + " .\n")

                    if(classification['EventName'] == "Mountain Classification"):
                        print("\n:mountain_" + str(
                            classification['EventId']) + " rdf:type owl:NamedIndividual , :Mountain .\n ")
                        print("\n:competition_" + str(competition['CompetitionId']) + " :hasMountain :mountain_" + str(
                            classification['EventId']) + " .\n")

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
                            if(not position['TeamName']):
                                position['TeamName'] = "--"
                            if(not position['ResultValue']):
                                position['ResultValue'] = "--:--:--"
                            if(not position['IndividualDisplayName']):
                                position['IndividualDisplayName'] = "Not Available"

                            print("\n:position_" + str(position['ResultId']) + " rdf:type owl:NamedIndividual, :Position ;",
                                  "\t:value \"" +
                                  position['ResultValue'] + "\";",
                                  "\t:rank \"" +
                                  str(position['SortOrder']) + "\";",
                                  "\t:team \"" + position['TeamName'] + "\";",
                                  "\t:name \"" +
                                  position['IndividualDisplayName'] + "\".",
                                  sep="\n")

                            print("\n:mountain_" + str(classification['EventId']) + " :hasPosition :position_" + str(
                                position['ResultId']) + " .\n")
