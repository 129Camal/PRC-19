import xlrd
import sys


f = open('../turtle/athletes.ttl', 'w')
sys.stdout = f

workbook = xlrd.open_workbook("../csv/IndividualRanking.xlsx")

worksheet = workbook.sheet_by_index(0)

total_rows = worksheet.nrows

for athlete in range(total_rows):
    if worksheet.cell(athlete, 0).value != 'Rank':
        print(":athlete_" + str(int(worksheet.cell(athlete, 1).value)) + " rdf:type owl:NamedIndividual, :Athlete ;",
              "\t:rank " + str(int(worksheet.cell(athlete, 0).value)) + ";",
              "\t:name \"" + worksheet.cell(athlete, 2).value + "\";",
              "\t:age " + str(int(worksheet.cell(athlete, 5).value)) + ";",
              "\t:points " + str(worksheet.cell(athlete, 6).value) + ";",
              "\t:nationality \"" + worksheet.cell(athlete, 3).value + "\".\n",
              sep="\n")
        
        if(worksheet.cell(athlete, 4).value):
            print(":athlete_" + str(int(worksheet.cell(athlete, 1).value)) + " :hasTeam :team_" + worksheet.cell(athlete, 4).value + ".\n") 
