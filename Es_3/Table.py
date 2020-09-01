import openpyxl
'''
def ExperimentalDataTable(y1, y2):
    table = openpyxl.Workbook()
    sheet = table.active
    sheet.title = 'Experimental Data'

    sheet['A1'] = 'DFS VS SCC'
    sheet['B1'] = 10
    sheet['C1'] = 300
    sheet['D1'] = 600
    sheet['A2'] = 'DFS'
    sheet['A3'] = 'SCC'
    sheet['B2'] = ("{0:.4f}".format(y1[10]))
    sheet['B3'] = ("{0:.4f}".format(y2[10]))
    sheet['C2'] = ("{0:.4f}".format(y1[70]))
    sheet['C3'] = ("{0:.4f}".format(y2[70]))
    sheet['D2'] = ("{0:.4f}".format(y1[115]))
    sheet['D3'] = ("{0:.4f}".format(y2[115]))

    table.save('Experimental_data.xlsx')
'''

def SCCCounterTable(sscCounter, n):
    table = openpyxl.Workbook()
    sheet = table.active
    sheet.title = 'Experimental Data'
    sheet['A1'] = 'SCC'
    #Probability
    sheet['B1'] = 0
    sheet['C1'] = 20
    sheet['D1'] = 50
    sheet['E1'] = 70
    sheet['F1'] = 100
    #Number of nodes
    sheet['A2'] = 10
    sheet['A3'] = 25
    sheet['A4'] = 50
    sheet['A5'] = 75
    sheet['A6'] = 100
    if n == 100:
        sheet['B2'] = sscCounter[0]
        sheet['C2'] = sscCounter[19]
        sheet['D2'] = sscCounter[49]
        sheet['E2'] = sscCounter[69]
        sheet['F2'] = sscCounter[100]
        table.save('Experimental_data.xlsx')
#    if n == 25:
        sheet['B3'] = sscCounter[0]
        sheet['C3'] = sscCounter[19]
        sheet['D3'] = sscCounter[49]
        sheet['E3'] = sscCounter[69]
        sheet['F3'] = sscCounter[100]
        table.save('Experimental_data.xlsx')

 #   if n == 50:
        sheet['B4'] = sscCounter[0]
        sheet['C4'] = sscCounter[19]
        sheet['D4'] = sscCounter[49]
        sheet['E4'] = sscCounter[69]
        sheet['F4'] = sscCounter[100]
        table.save('Experimental_data.xlsx')
#    if n == 75:
        sheet['B5'] = sscCounter[0]
        sheet['C5'] = sscCounter[19]
        sheet['D5'] = sscCounter[49]
        sheet['E5'] = sscCounter[69]
        sheet['F5'] = sscCounter[100]
        table.save('Experimental_data.xlsx')
 #   if n == 100:
        sheet['B6'] = sscCounter[0]
        sheet['C6'] = sscCounter[19]
        sheet['D6'] = sscCounter[49]
        sheet['E6'] = sscCounter[69]
        sheet['F6'] = sscCounter[100]
        table.save('Experimental_data.xlsx')
