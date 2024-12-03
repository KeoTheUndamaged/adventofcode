import pandas as pd


if __name__ == "__main__":
    # import list
    input_df = pd.read_csv("input.txt", sep='\t', header=None, names=['list_one', 'list_two'])
    # create an empty DataFrame to hold data for calculation.
    output = pd.DataFrame()
    # sort the two lists so they are in Ascending order and store in the output DataFrame.
    output['list_one'] = input_df['list_one'].sort_values(ascending=True, ignore_index=True)
    output['list_two'] = input_df['list_two'].sort_values(ascending=True, ignore_index=True)
    # calculate the difference between the two numbers
    output['diff'] = output['list_one'] - output['list_two']
    # output the absolute difference between the two lists
    print(output['diff'].abs().sum())

    # Ans: 3714264
