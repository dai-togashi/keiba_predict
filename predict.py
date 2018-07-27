import crawler
import preprocessing

horse_page_link_list = crawler.horse_page_link('https://www.nankankeiba.com/race_info/2018072719040410.do')
df_horses_data = crawler.horse_data(horse_page_link_list[0])
#print(df_horses_data)
pre_df = preprocessing.add_race_data(df_horses_data)
print(pre_df)
#hourse_data = preprocessing(df_horses_data, today_condition, race_len)