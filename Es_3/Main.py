import Test
import Plot

prob_inc = 1
nodes_dims = [10, 50, 100, 250, 500]
for n in nodes_dims:
    x, y = Test.SCCCounter(prob_inc, n)
    Plot.plot(x, y, n)
