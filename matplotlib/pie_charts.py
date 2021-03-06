import matplotlib.pyplot as plt

if __name__ == '__main__':
    exp_vals = [1400, 600, 300, 410, 250]  # Expense values.
    exp_labels = ["Home Rent", "Food", "Phone/Internet Bill", "Car", "Other Utilities"]  # Expense Labels.

    # plt.axis("equal")  # For a perfect circle.
    plt.pie(exp_vals, labels=exp_labels)
    # plt.show()

    plt.cla()
    plt.pie(exp_vals, labels=exp_labels,
            radius=1.2,  # Increase size.
            autopct='%0.1f%%',  # Percentage. 0.1 means we want one decimal in our %. 0.2 for 2 and so on.
            # startangle=45,  # In case you want to rotate the pie by degrees.
            explode=[0, 0.2, 0, 0, 0.5]  # Split certain pieces of the pie from it. Specify distance.
            )

    # With bbox_inches we make sure pie chart is saved without any missing data around the edges.
    plt.savefig("plots\\pie_chart.jpg", bbox_inches="tight")
    plt.show()

