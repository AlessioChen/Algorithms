import Test
import Plot

MAX_ITERATION = 800
TEST_TIMES = 1000
INCREMENT = 10

x, y1, y2, abr_lenght, arn_lenght, t = Test.test_inorder(TEST_TIMES, MAX_ITERATION, INCREMENT)
Plot.in_oder_plot(x, y1, y2, t)
Plot.in_order_lenght_plot(x, abr_lenght, arn_lenght)

x, y1, y2, abr_lenght, arn_lenght, t = Test.test_randomized(TEST_TIMES, MAX_ITERATION, INCREMENT)
Plot.randomized_plot(x, y1, y2,  t)
Plot.randomized_lenght_plot(x, abr_lenght, arn_lenght)

