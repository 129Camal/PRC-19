import xlrd
import sys


f = open('../turtle/teams.ttl', 'w')
sys.stdout = f

workbook = xlrd.open_workbook("../csv/Teams_ROA_6_7_2019.xlsx")

worksheet = workbook.sheet_by_index(0)

total_rows = worksheet.nrows

for team in range(total_rows):
    if worksheet.cell(team, 0).value != 'Code' and worksheet.cell(team, 0).value != 'UCI ROAD Teams':
        print(":team_" + str(worksheet.cell(team, 0).value) + " rdf:type owl:NamedIndividual, :Team ;",
              "\t:continent \"" + worksheet.cell(team, 4).value + "\";",
              "\t:country \"" + worksheet.cell(team, 3).value + "\";",
              "\t:email \"" + worksheet.cell(team, 6).value + "\";",
              "\t:name \"" + worksheet.cell(team, 1).value + "\";",
              "\t:teamCategory \"" + worksheet.cell(team, 2).value + "\";",
              "\t:website \"" + worksheet.cell(team, 7).value + "\".\n",
              sep="\n")
