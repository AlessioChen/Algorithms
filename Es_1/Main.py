from Test import Test
import Table
import Plot

N = 1000

t = Test(N)

isb = t.InsertionSortBest()
ism = t.InsertionSortRandom()
isw = t.InsertionSortWorst()
msb = t.MergeSortBest()
msm = t.MergeSortRandom()
msw = t.MergeSortWorst()

Plot.GraphicPlot(N, isb, ism, isw, msb, msm, msw)
Table.ExperimentalDataTable(isb, ism, isw, msb, msm, msw)