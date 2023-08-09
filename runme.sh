source /home/vijaya/nyse-converter/nc-venv/bin/activate
export SRC_DIR=/home/vijaya/nyse-converter/data/nyse_all/nyse_data
export LOG_FILE_PATH=/home/vijaya/nyse-converter/logs/nc.log
mkdir -p /home/vijaya/nyse-converter/logs

rm -rf /home/vijaya/nyse-converter/data/nyse_all/nyse_json
nc
deactivate