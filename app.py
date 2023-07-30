# def sum_n(n):
#     if type(n)!=int or n<=0:
#         raise ValueError('Invalid Type or Value')
#     res=(n*(n+1)/2)
#     print(res)
#     return 

from dask import dataframe as dd
def main():
    print('File format conversion started')
    df=dd.read_csv(
        'data/nyse_all/nyse_data/NYSE*.txt.gz',
        names=['ticker', 'trade_date', 'open_price', 'low_price',
                'high_price', 'close_price', 'volume'],
        blocksize=None
    )
    print('DataFrame is created and will be written in json format')
    df.to_json(
    'data/nyse_all/nyse_json/part-*.json.gz',
    orient='records',
    lines=True,
    compression='gzip',
    name_function=lambda i:'%05d' %i
    )
    print('File format conversion completed')

if __name__=='__main__':
    main()