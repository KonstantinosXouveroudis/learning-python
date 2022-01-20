def process_file(stocks, output):
    with open(stocks, "r") as file, \
            open(output, "w") as out:
        next(file)  # Skip headers.
        out.write("Company Name,PE Ration,PB Ratio\n")
        for line in file:
            tokens = line.split(",")
            company = tokens[0]
            price = float(tokens[1])
            earnings = float(tokens[2])
            book_value = float(tokens[3])
            pe = round(price / earnings, 2)
            pbr = round(price / book_value, 2)
            out.write(f"{company},{pe},{pbr}\n")


if __name__ == '__main__':
    stocks_file = "C://Users//Kostas//PycharmProjects//learningBasics310//exercises//stocks.csv"
    output_file = "C://Users//Kostas//PycharmProjects//learningBasics310//exercises//stocks_output.csv"
    process_file(stocks_file, output_file)

