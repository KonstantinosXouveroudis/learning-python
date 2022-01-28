import matplotlib.pyplot as plt
# matplotlib inline

if __name__ == '__main__':
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [50, 51, 52, 48, 47, 49, 46]

    plt.plot(x, y)  # Create plot
    plt.savefig("plots\\plot1.jpg")  # Save plot to a jpg

    plt.show()  # Display plot.
    plt.clf()  # Clear figure. Alternatively, cla() clears the axes.

    plt.plot(x, y, linewidth=3, linestyle='--')
    plt.savefig("plots\\plot2.jpg")

    plt.clf()

    plt.title('Weather')  # Add title and labels.
    plt.xlabel('Day')
    plt.ylabel('Temperature')
    plt.plot(x, y, color='purple', linewidth=5, linestyle=':')
    plt.savefig("plots\\plot3.jpg")

    plt.show()
    plt.cla()

    plt.plot(x, y, color='green', ls='-')
    plt.savefig("plots\\plot4.jpg")

    plt.close()
