import csv

if __name__ == "__main__":
    # variable to store safe report count
    safe_report_count = 0

    data = []
    # read data from file
    f = open('./input.txt', 'r')
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        data.append(row)

    # function to check if data is safe and ordered
    def is_safe_and_ordered(data_list):
        # check if data is ordered either ascending or descending
        is_ordered = (all(data_list[j] < data_list[j + 1] for j in range(len(data_list) - 1)) or
                      all(data_list[j] > data_list[j + 1] for j in range(len(data_list) - 1)))
        # check if data steps are between 1 and 3
        is_safe = all(1 <= abs(data_list[j] - data_list[j + 1]) <= 3 for j in range(len(data_list) - 1))
        return is_ordered and is_safe

    # loop through all rows in the data
    for i in range(len(data)):
        if is_safe_and_ordered(data[i]):
            safe_report_count += 1
    print("Safe Reports: ", safe_report_count)

    # Ans: 606