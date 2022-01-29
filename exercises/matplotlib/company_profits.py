import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    # Read the company_sales_data dataset and create a line plot showcasing their total profit per month.
    df = pd.read_csv("datasets\\company_sales_data.csv")
    print(df)

    plt.plot(df['month_number'], df['total_profit'])
    plt.yticks([100000, 200000, 300000, 400000, 500000])
    plt.title("Company Profit Per Month")
    plt.xlabel("Month Number")
    plt.ylabel("Total Profit")
    # plt.show()
    plt.savefig("plots\\monthly_profits_1.jpg")

    plt.cla()

    # Same plot, but stylize it further.
    plt.plot(df['month_number'], df['total_profit'], color='red', linestyle='dotted', linewidth=3,
             label='Profit data of last year', marker='o', markerfacecolor='black')
    plt.yticks([100000, 200000, 300000, 400000, 500000])
    plt.title("Company Profit Per Month")
    plt.xlabel("Month Number")
    plt.ylabel("Total Profit")
    plt.grid()
    plt.legend()
    # plt.show()
    plt.savefig("plots\\monthly_profits_2.jpg")

    plt.cla()

    # New plot, showcasing every product separately.
    plt.plot(df['month_number'], df['facecream'], label='Face cream', marker='o')
    plt.plot(df['month_number'], df['facewash'], label='Face wash', marker='o')
    plt.plot(df['month_number'], df['toothpaste'], label='Tooth paste', marker='o')
    plt.plot(df['month_number'], df['bathingsoap'], label='Bathing soap', marker='o')
    plt.plot(df['month_number'], df['shampoo'], label='Shampoo', marker='o')
    plt.plot(df['month_number'], df['moisturizer'], label='Moisturizer', marker='o')
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    plt.title("Company Profit Per Month")
    plt.xlabel("Month Number")
    plt.ylabel("Total Profit")
    plt.grid()
    plt.legend()
    # plt.show()
    plt.savefig("plots\\monthly_profits_3.jpg")
