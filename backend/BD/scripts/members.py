import xlrd
import sys


f = open('../turtle/members.ttl', 'w')
sys.stdout = f

workbook = xlrd.open_workbook("../csv/TeamMembers_ROA_6_8_2019.xlsx")

worksheet = workbook.sheet_by_index(0)

total_rows = worksheet.nrows

for person in range(total_rows):
    if worksheet.cell(person, 0).value != 'Function' and worksheet.cell(person, 0).value != 'UCI ROAD Team Members':
        if(worksheet.cell(person, 0).value != 'Rider'):
            print(":staff_" + str(int(worksheet.cell(person, 10).value)) + " rdf:type owl:NamedIndividual, :Staff ;",
                  "\t:job \"" + worksheet.cell(person, 0).value + "\";",
                  "\t:name \"" +
                  worksheet.cell(person, 1).value + " " +
                  worksheet.cell(person, 2).value + "\";",
                  "\t:birthdate \"" + worksheet.cell(person, 3).value + "\";",
                  "\t:country \"" + worksheet.cell(person, 6).value + "\".\n",
                  sep="\n")

            if(worksheet.cell(person, 8).value):
                print(":staff_" + str(int(worksheet.cell(person, 10).value)) +
                      " :isStaffOf :team_" + worksheet.cell(person, 8).value + ".\n")

        else:
            print(":athlete_" + str(int(worksheet.cell(person, 10).value)) + " rdf:type owl:NamedIndividual, :Athlete ;",
                  "\t:name \"" +
                  worksheet.cell(person, 1).value + " " +
                  worksheet.cell(person, 2).value + "\";",
                  "\t:birthdate \"" +
                  worksheet.cell(person, 3).value + "\";",
                  "\t:country \"" +
                  worksheet.cell(person, 6).value + "\".\n",
                  sep="\n")

            if(worksheet.cell(person, 8).value):
                print(":athlete_" + str(int(worksheet.cell(person, 10).value)) +
                      " :hasTeam :team_" + worksheet.cell(person, 8).value + ".\n")
