import openpyxl

def ExperimentalDataTable(isb, ism, isw, msb, msm, msw):
    table = openpyxl.Workbook()
    sheet = table.active
    sheet.title = 'Experimental Data'

    sheet['A1'] = 'Insertion Sort'
    sheet['B1'] = 10
    sheet['C1'] = 100
    sheet['D1'] = 1000
    sheet['A2'] = 'Best'
    sheet['A3'] = 'Medium'
    sheet['A4'] = 'Worst'
    sheet['B2'] = ("{0:.6f}".format(isb[8]))
    sheet['B3'] = ("{0:.6f}".format(ism[8]))
    sheet['B4'] = ("{0:.6f}".format(isw[8]))
    sheet['C2'] = ("{0:.6f}".format(isb[98]))
    sheet['C3'] = ("{0:.6f}".format(ism[98]))
    sheet['C4'] = ("{0:.6f}".format(isw[98]))
    sheet['D2'] = ("{0:.6f}".format(isb[997]))
    sheet['D3'] = ("{0:.6f}".format(ism[997]))
    sheet['D4'] = ("{0:.6f}".format(isw[997]))

    sheet['A6'] = 'Merge Sort'
    sheet['B6'] = 10
    sheet['C6'] = 100
    sheet['D6'] = 1000
    sheet['A7'] = 'Best'
    sheet['A8'] = 'Medium'
    sheet['A9'] = 'Worst'
    sheet['B7'] = ("{0:.6f}".format(msb[8]))
    sheet['B8'] = ("{0:.6f}".format(msm[8]))
    sheet['B9'] = ("{0:.6f}".format(msw[8]))
    sheet['C7'] = ("{0:.6f}".format(msb[98]))
    sheet['C8'] = ("{0:.6f}".format(msm[98]))
    sheet['C9'] = ("{0:.6f}".format(msw[98]))
    sheet['D7'] = ("{0:.6f}".format(msb[998]))
    sheet['D8'] = ("{0:.6f}".format(msm[998]))
    sheet['D9'] = ("{0:.6f}".format(msw[998]))

    table.save('Experimental_data.xlsx')
