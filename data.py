import pandas as pd

df = pd.read_csv('test.csv')

print(df[df['company']=='บริษัท เนชั่นแนล ไอทีเอ็มเอ๊กซ์ จำกัด'].value_counts())