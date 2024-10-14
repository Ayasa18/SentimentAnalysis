from google_play_scraper import app
import pandas as pd
import numpy as np

"""# **Scraping Data**"""

from google_play_scraper import Sort, reviews

result, continuation_token = reviews(
  'com.traveloka.android',
  lang='id',
  country='id',
  sort=Sort.MOST_RELEVANT,
  count=10000,
  filter_score_with=None)

df_baru = pd.DataFrame(np.array(result),columns=['review'])
df_baru = df_baru.join(pd.DataFrame(df_baru.pop('review').tolist()))
df_baru.head()

len(df_baru.index)

df_baru[['score', 'content']].head()

new_df = df_baru[['userName', 'score', 'at', 'content']]
new_df.head()

new_df.to_csv("traveloka_scraping_data_new.csv", index = False)
