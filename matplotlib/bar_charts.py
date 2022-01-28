import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    company = ['GOOGL', 'AMZN', 'MSFT', 'FB']
    revenue = [90, 136, 89, 27]
    profit = [40, 2, 34, 12]

    # Because the bar method doesn't accept strings in its parameters, we create this array.
    x_pos = np.arange(len(company))  # X Position

    plt.xticks(x_pos, company)  # Display the company names on the plot.

    # We add a little distance to the x_pos of profit so the 2 figures aren't on top of each other.
    # The numpy array makes this way simpler.
    plt.bar(x_pos, revenue, label='Revenue', width=0.6)
    plt.bar(x_pos + 0.15, profit, label='Profit', width=0.6)

    plt.legend()
    # plt.show()
    plt.clf()

    # We create the same bar, but horizontally with barh().
    plt.yticks(x_pos, company)  # Display the company names on the plot.

    plt.barh(x_pos, revenue, label='Revenue', color='purple')
    plt.barh(x_pos + 0.15, profit, label='Profit', color='yellow')

    plt.legend()
    plt.show()
