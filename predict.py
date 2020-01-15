#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from src import *

if __name__ == '__main__':
  horse_page_link_list = crawler.horse_page_link(sys.argv[1])
  df_horses_data = crawler.horse_data(horse_page_link_list[0])
  pre_df = preprocessing.add_race_data(df_horses_data)
  print(pre_df)
