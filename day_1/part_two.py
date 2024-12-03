from collections import Counter

import pandas as pd

if __name__ == '__main__':
    # import list
    input_df = pd.read_csv("input.txt", sep=',', header=None, names=['list_one', 'list_two'])
    # create an empty DataFrame to hold data for calculation.
    output = pd.DataFrame()
    # copy 'list_one' to the output DataFrame
    output['list_one'] = input_df['list_one'].copy()
    # count each occurrence of each number within 'list_one' and store it in output DataFrame
    c = Counter(input_df['list_two'].tolist())
    output['count'] = [c.get(v) for v in output['list_one'].tolist()]
    # Calculate the similarity
    output['similarity'] = output['list_one'] * output['count']
    # output the sum of similarity
    print(output['similarity'].sum())

    # Ans: 18805872