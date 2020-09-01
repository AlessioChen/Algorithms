import matplotlib.pyplot as plt


def in_oder_plot(x, y1, y2, times):
    plt.figure()
    plt.title("ABR vs ARN INORDER ")
    plt.grid()
    plt.xlabel("number of nodes ")
    plt.ylabel('avg time in seconds of {} runs'.format(times))
    plt.plot(x, y1, label="ABR")
    plt.plot(x, y2, label="ARN")
    plt.legend(loc="best")
    plt.gcf()
    plt.tight_layout()
    plt.savefig('Inorder.png')


def in_order_lenght_plot(x, y1, y2):
    plt.figure()
    plt.title("ABR vs ARN INORDER ")
    plt.grid()
    plt.xlabel("number of nodes ")
    plt.ylabel('height')
    plt.plot(x, y1, label="ABR")
    plt.plot(x, y2, label="ARN")
    plt.legend(loc="best")
    plt.gcf()
    plt.tight_layout()
    plt.savefig('Inorder_height.png')


def randomized_plot(x, y1, y2, times):
    plt.figure()
    plt.title("ABR vs ARN RANDOMIZED ")
    plt.grid()
    plt.xlabel("number of nodes ")
    plt.ylabel('avg time in seconds of {} runs'.format(times))
    plt.plot(x, y1, label="ABR")
    plt.plot(x, y2, label="ARN")
    plt.legend(loc="best")
    plt.gcf()
    plt.tight_layout()
    plt.savefig('Randomized.png')

def randomized_lenght_plot(x, y1, y2):
    plt.figure()
    plt.title("ABR vs ARN RANDOMIZED ")
    plt.grid()
    plt.xlabel("number of nodes ")
    plt.ylabel('Height')
    plt.plot(x, y1, label="ABR")
    plt.plot(x, y2, label="ARN")
    plt.legend(loc="best")
    plt.gcf()
    plt.tight_layout()
    plt.savefig('Randomized_height.png')
