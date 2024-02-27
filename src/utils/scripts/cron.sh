#!/bin/bash

crontab -l > cronlist

echo "30 * * * 1-5 python3 $HOME/utils/dolar.py" >> cronlist
# echo "01 09-19 * * 1-5 python3 $HOME/utils/dolar.py" >> cronlist

#install new cron file
crontab cronlist
rm cronlist
