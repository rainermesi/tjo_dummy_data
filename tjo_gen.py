# Imports

import random
import pandas as pd

# Read in text file, generate rows

line_list = []

with open(r'\files\origin.txt',encoding='UTF-8') as file:
    for line in file:
        if len(line.rstrip()) > 5:
            line_list.append(line.rstrip())

split_list = '-&- '.join(''.join(line_list).split()).split('-&-')

def gen_line():
    return ''.join(random.choice(split_list) for _ in range(random.randrange(30,500)))

gen_list = []

rows = 0
while rows < 1000000:
    gen_list.append(gen_line())
    rows += 1

# Create a dataframe and add dummy cols

gen_df = pd.DataFrame(gen_list)

prod_list = ['Prod_1','Prod_2','Prod_3','Prod_4','Prod_5','Prod_6','Prod_7','Prod_8']
prod_list[random.randrange(0,len(prod_list))]

gen_df[1] = gen_df.apply(lambda x: prod_list[random.randrange(0,len(prod_list))],axis=1)
gen_df[2] = gen_df.apply(lambda x: prod_list[random.randrange(0,len(prod_list))],axis=1)
gen_df[3] = gen_df.apply(lambda x: random.randrange(0,10),axis=1)
gen_df[4] = gen_df.apply(lambda x: random.randrange(0,1000),axis=1)
gen_df[5] = gen_df.apply(lambda x: abs(hash(x[0])),axis=1)

gen_df.columns=['event_tx','prod_a_cd','prod_b_cd','metric_a_vl','metric_b_vl','event_id']
gen_df.to_csv('tjo_gen.csv')
