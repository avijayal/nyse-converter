# def sum_n(n):
#     if type(n)!=int or n<=0:
#         raise ValueError('Invalid Type or Value')
#     res=(n*(n+1)/2)
#     print(res)
#     return 

# make changes to nyse_converter to use environment variables
#   SRC_DIR:'data/nyse_all/nyse_data'
#   TGT_DIR:'data/nyse_all/nyse_json'
# make sure to run and validate the code after making changes using environment variables
# make sure to commit and push changes to remote git repository
import os
from dask import dataframe as dd
def main():
    src_dir = os.environ['SRC_DIR']
    tgt_dir = os.environ['TGT_DIR']
    print('File format conversion started')
    df=dd.read_csv(
        f'{src_dir}/NYSE*.txt.gz',
        names=['ticker', 'trade_date', 'open_price', 'low_price',
                'high_price', 'close_price', 'volume'],
        blocksize=None
    )
    print('DataFrame is created and will be written in json format')
    df.to_json(
    f'{tgt_dir}/part-*.json.gz',
    orient='records',
    lines=True,
    compression='gzip',
    name_function=lambda i:'%05d' %i
    )
    print('File format conversion completed')

if __name__=='__main__':
    main()