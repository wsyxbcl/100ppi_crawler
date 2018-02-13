import pandas as pd

def table_crawler(url):
    try:
        data = pd.read_html(url)
        return data[0]
    except ValueError:
        # No table found
        return -1

if __name__ == '__main__':
    url = input('Aimed URL: ')
    table = table_crawler(url)
    if table is -1:
        print("No table found")
    else:
        writer = pd.ExcelWriter('大宗商品'+url[-16:-7]+'.xlsx')
        table.to_excel(writer, 'Sheet1', index=False, header=False)
        writer.save()