def winsorise_data(data):
    temp = data.copy()
    quantiles = temp.quantile([0.05, 0.95])
    for col in quantiles.columns:
        temp = temp[(temp[col] >= quantiles.loc[0.05, col]) & (temp[col] <= quantiles.loc[0.95, col])]
        # print('After winsorising column ' + col + ' we are left with:')
        # print(temp.shape)
    return temp