# -*- coding: utf-8 -*-
"""social_media.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DXN-aiTFPB3RlEz0lSfc4i8ULQSMU6z5
"""

#import necessary libraries
import pandas as pd
import numpy as np

#connect google colab to google drive
from google.colab import drive
drive.mount('/content/drive')

# Load the four datasets into Pandas DataFrames
facebook = pd.read_csv('/content/drive/MyDrive/DATASETS/stanbic_ibtc_facebook.csv')
instagram = pd.read_csv('/content/drive/MyDrive/DATASETS/stanbic_ibtc_instagram.csv')
linkedin = pd.read_csv('/content/drive/MyDrive/DATASETS/stanbic_ibtc_linkedin.csv')
twitter = pd.read_csv('/content/drive/MyDrive/DATASETS/stanbic_ibtc_twitter.csv')

#view first 5 rows of facebook dataset
facebook.head(5)

#view first 5 rows of instagram dataset
instagram.head(5)

#view first 5 rows of linkedin dataset
linkedin.head(5)

#view first 5 rows of twitter dataset
twitter.head(5)

#check for duplicates in facebook datasets
facebook.duplicated().sum()

#check for duplicates in instagram datasets
instagram.duplicated().sum()

#check for duplicates in linkedin datasets
linkedin.duplicated().sum()

#check for duplicates in twitter datasets
twitter.duplicated().sum()

#compile facebook column names into a list
column_f = facebook.columns.tolist()
print(column_f)

#compile instagram column names into a list
column_i = instagram.columns.tolist()
print(column_i)

#compile linkedin column names into a list
column_l = linkedin.columns.tolist()
print(column_l)

#compile twitter column names into a list
column_t = twitter.columns.tolist()
print(column_t)

# Merge the DataFrames on the social media platform name column
data = pd.concat([facebook, instagram,linkedin,twitter])

#view 5 random observations of new dataframe
data.sample(5)

#drop irrelevant columns
data = data.drop([ 'Sent by','Post', 'Linked Content','Paid Impressions', 'Fan Paid Impressions', 'Non-fan Paid Impressions', 'Paid Reach', 'Fan Paid Reach', 'Dislikes', 'Post Detail Expand Clicks', 'Post Photo View Clicks','Answers', 'App Engagements', 'App Install Attempts', 'App Opens', 'Follows from Post', 'Unfollows from Post', 'bit.ly Link Clicks', 'Engaged Users', 'Engaged Fans', 'Users Talking About This','Unique Answers', 'Unique Post Clicks', 'Unique Post Link Clicks', 'Unique Post Photo View Clicks', 'Unique Post Video Play Clicks', 'Unique Other Post Clicks', 'Unique Negative Feedback', 'Subscribers Gained from Video', 'Annotation Clicks', 'Card Clicks', 'Video Views', 'Media Views', 'Organic Video Views', 'Paid Video Views', 'Partial Video Views', 'Organic Partial Video Views', 'Paid Partial Video Views', 'Full Video Views', 'Full Video View Rate', 'Follow Video Views', 'For You Video Views', 'Hashtag Video Views', 'Business Account Video Views', 'Sound Video Views', 'Unspecified Video Views', 'Organic Full Video Views', 'Paid Full Video Views', 'Autoplay Video Views', 'Click to Play Video Views', 'Sound on Video Views', 'Sound off Video Views', '10-Second Video Views', 'Organic 10-Second Video Views', 'Paid 10-Second Video Views', 'Autoplay 10-Second Video Views', 'Click to Play 10-Second Video Views', 'Sound on 10-Second Video Views', 'Sound off 10-Second Video Views', 'Autoplay Partial Video Views', 'Click to Play Partial Video Views', 'Autoplay Full Video Views', 'Click to Play Full Video Views', '95% Video Views', 'Organic 95% Video Views', 'Paid 95% Video Views', 'Video Length (Seconds)', 'Paid Video View Time (Seconds)', 'Unique Video Views', 'Unique Organic Video Views', 'Unique Paid Video Views', 'Unique 10-Second Video Views', 'Unique Full Video Views', 'Unique Organic 95% Video Views', 'Unique Paid 95% Video Views', 'Video Ad Break Ad Impressions', 'Video Ad Break Ad Earnings', 'Video Ad Break Ad Cost per Impression (CPM)', 'YouTube Premium Views', 'Estimated Minutes Watched', 'Estimated Premium Minutes Watched', 'Story Taps Back', 'Story Taps Forward', 'Story Exits', 'Story Replies', 'Video Added to Playlists', 'Subscribers Lost from Video', 'Video Removed from Playlists', 'Annotation Impressions', 'Annotation Clickable Impressions', 'Annotation Closable Impressions', 'Annotation Closes', 'Card Impressions', 'Card Teaser Impressions', 'Card Teaser Clicks', 'Poll Votes'],axis=1)

#view dataset info
data.info()

#transpose dataset
data.transpose()

#fill null hashtag cells with "No_Tag"
data = data.fillna({'Tags': 'No_Tag'})

#fill other null values with zeros
data = data.fillna(0)

#view 5 random observations of new dataframe
data.sample(5)

#view dataset row and column count
data.shape

#Export the combined DataFrame to an excel file
data.to_excel('social_media_data.xlsx', index=False)