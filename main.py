import pandas as pd
import os
from datetime import date, timedelta
from crawler import table_crawler

save_dir = os.getcwd()+'/result'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

date_start = date(2018, 1, 1)
date_end = date(2018, 2, 13)

delta = date_end - date_start

for i in range(delta.days + 1):
    date = date_start + timedelta(days=i)
    print('Getting'+' '+str(date))
    url = 'http://top.100ppi.com/zdb/detail-day-{}-1.html'.format(str(date)[:7]+str(date)[8:])
    table = table_crawler(url)
    if table is -1:
        print("No table found")
    else:
        writer = pd.ExcelWriter(save_dir+'/大宗商品'+url[-16:-7]+'.xlsx')
        table.to_excel(writer, 'Sheet1', index=False, header=False)
        writer.save()