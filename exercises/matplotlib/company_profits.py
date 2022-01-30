import matplotlib.pyplot as plt
import pandas as pd


def line_plots(dfl, x_pos):
    print(dfl)

    # Read the company_sales_data dataset and create a line plot showcasing their total profit per month.
    plt.plot(dfl['month_number'], dfl['total_profit'])
    plt.yticks([100000, 200000, 300000, 400000, 500000])
    plt.title("Company Profit Per Month")
    plt.xlabel("Month Number")
    plt.ylabel("Total Profit")
    # plt.show()
    plt.savefig("plots\\monthly_profits_1.jpg", bbox_inches="tight", pad_inches=0.2)

    plt.cla()

    # Same plot, but stylize it further.
    plt.plot(dfl['month_number'], dfl['total_profit'], color='red', linestyle='dotted', linewidth=3,
             label='Profit data of last year', marker='o', markerfacecolor='black')
    plt.yticks([100000, 200000, 300000, 400000, 500000])
    plt.title("Company Profit Per Month")
    plt.xlabel("Month Number")
    plt.ylabel("Total Profit")
    plt.xticks(x_pos)
    plt.grid()
    plt.legend()
    # plt.show()
    plt.savefig("plots\\monthly_profits_2.jpg", bbox_inches="tight", pad_inches=0.2)

    plt.cla()

    # New plot, showcasing every product separately.
    plt.plot(dfl['month_number'], dfl['facecream'], label='Face cream', marker='o')
    plt.plot(dfl['month_number'], dfl['facewash'], label='Face wash', marker='o')
    plt.plot(dfl['month_number'], dfl['toothpaste'], label='Tooth paste', marker='o')
    plt.plot(dfl['month_number'], dfl['bathingsoap'], label='Bathing soap', marker='o')
    plt.plot(dfl['month_number'], dfl['shampoo'], label='Shampoo', marker='o')
    plt.plot(dfl['month_number'], dfl['moisturizer'], label='Moisturizer', marker='o')
    plt.xticks(x_pos)
    plt.title("Company Profit Per Month")
    plt.xlabel("Month Number")
    plt.ylabel("Total Profit")
    plt.grid()
    plt.legend()
    # plt.show()
    plt.savefig("plots\\monthly_profits_3.jpg")

    plt.close()


def scatter_plots(dfl, x_pos):
    plt.scatter(dfl['month_number'], dfl['toothpaste'], label='Tooth paste sales data', color='cyan', edgecolors='black', linewidths=1.5)
    plt.xticks(x_pos)
    plt.xlabel('Month Number')
    plt.ylabel('Number of units sold')
    plt.grid()
    plt.legend()
    # plt.show()
    plt.savefig("plots\\scatter_toothpaste.jpg")

    plt.close()


def bar_plots(dfl, x_pos):
    plt.bar(x_pos - 0.2, dfl['facecream'], width=0.4, label='Face Cream')
    plt.bar(x_pos + 0.2, dfl['facewash'], width=0.4, label='Face Wash')
    plt.title("Face Wash and Face Cream Sales Data")
    plt.xlabel('Month Number')
    plt.ylabel('Sale Units')
    plt.xticks(x_pos)
    plt.grid(linestyle='--')
    # plt.show()
    plt.savefig("plots\\bar_face_products.jpg")

    plt.close()


def histograms(dfl):
    profit_range = [150000, 200000, 250000, 300000, 350000, 400000, 450000]
    plt.hist(dfl['total_profit'], label='Profit Data', color='g',
             rwidth=0.90,
             bins=profit_range)

    plt.title("Total Profit Data")
    plt.xlabel("Profit Range in Dollars")
    plt.ylabel("# of months this range was accomplished")
    plt.grid(linestyle='--')
    # plt.show()
    plt.savefig("plots\\histogram_profits.jpg")

    plt.close()


if __name__ == '__main__':
    data = "datasets\\company_sales_data.csv"
    df = pd.read_csv(data)
    months = df['month_number']

    line_plots(df, months)
    scatter_plots(df, months)
    bar_plots(df, months)
    histograms(df)
