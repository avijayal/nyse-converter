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
import glob
import logging
from dask import dataframe as dd
def main():
    log_file_path=os.environ['LOG_FILE_PATH']
    src_dir = os.environ['SRC_DIR']
    logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(levelname)s %(asctime)s %(message)s',
    datefmt='%Y-%m-%d %I:%M:%S %p'
    )
    logging.info('File format conversion started')
    # tgt_dir = os.environ['TGT_DIR']
    src_file_pattern = os.environ.setdefault('SRC_FILE_PATTERN','NYSE*.txt.gz')
    src_file_name = sorted(glob.glob(f'{src_dir}/{src_file_pattern}'))
    tgt_file_name = [
        file.replace('txt','json').replace('nyse_data','nyse_json')
        for file in src_file_name
    ]
    df=dd.read_csv(
        src_file_name,
        names=['ticker', 'trade_date', 'open_price', 'low_price',
                'high_price', 'close_price', 'volume'],
        blocksize=None
    )
    logging.info('DataFrame is created and will be written in json format')
    df.to_json(
    tgt_file_name,
    orient='records',
    lines=True,
    compression='gzip'
    )
    logging.info('File format conversion completed')

if __name__=='__main__':
    main()

# modularizing
# def process_file(src_dir,ds,tgt_dir):
#         print('File format conversion started')
#         df=dd.read_csv(
#             f'{src_dir}/NYSE*.txt.gz',
#             names=['ticker', 'trade_date', 'open_price', 'low_price',
#                     'high_price', 'close_price', 'volume'],
#             blocksize=None
#         )
#         print('DataFrame is created and will be written in json format')
#         df.to_json(
#         f'{tgt_dir}/part-*.json.gz',
#         orient='records',
#         lines=True,
#         compression='gzip',
#         name_function=lambda i:'%05d' %i
#         )
#         print('File format conversion completed')

# def main():
#     src_dir = os.environ['SRC_DIR']
#     tgt_dir = os.environ['TGT_DIR']
#     datasets = os.environ.get('DATASETS')
#     if not datasets:
#           if __path__ in glob.glob(f'{src_dir}/*'):
#             if os.path.isfile(__path__):
#                 process_file(src_dir,os.path.split(__path__)[1],tgt_dir)
#     else:
#           dirs=datasets.split(',')
#           for ds in dirs:
#                process_file(src_dir,ds,tgt_dir)


# if __name__=='__main__':
#      main()       
