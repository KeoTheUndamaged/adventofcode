import re

if __name__ == "__main__":
    # read file and remove carriage returns
    with open('input.txt', 'r') as file:
        data = file.read().replace('\n', '')
    # remove disabled mul() functions from the data
    clean_data = re.sub(r"don't\(\)(.*)", "", re.sub(r"(?=don't\(\))(.*?)(?=do\(\))", "", data))
    # create variable to store answer
    results = 0
    # find all enabled mul() functions in the cleaned data
    for mul in re.findall(r"mul\(\d+,\d+\)", clean_data):
        # extract the variables in the mul() function into a list
        numbers = re.findall(r"\d+", mul)
        results += int(numbers[0]) * int(numbers[1])
    print(results)

    # Ans: 106780429
