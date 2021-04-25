# project_2 - Twitch Gaming Visualization
The gaming industry is worth billions and so many technologies drive and are driven by it, in order to get a better understanding of a small piece of the industry we decided to take a look at the Twitch data and get an idea of where we could learn.  

The app.py is a dashboard-style website referencing a series of datasets that look into each aspect of these noted categories and explore the metrics used to understanding various games and video interaction.

In the folder labeled "Priya Notebooks" you will find the respective folders of the website, the black-dashboard templates along with the respective notebooks noted for specific data extractions. The main folder also has some notebooks that look at the data we have also collected.  

## Technologies
All data cleaning, exploration and analysis occurred in jupyter notebooks and later uploaded into a sqlite database for later use in the app.py flask. Utilizing template HTML and CSS along with js chart visualizations, we were able to take the data to help generate a variety of visualizations that aided in the construction of the dashbaords.

## Data
All respective data sets were pulled from kaggle.com or the Twitch API. The kaggle datasets provided hisotrical data for the Top 200 Games from 2016-2020 each month. The Twitch API data was pulled and converted to CSVs and uploaded into the sqlite database for easy cleaning, structuring and referencing. 

The recipes and user intreaction datasets were too large so we had to put in a drive and save it locally to run the scripts. Please find the links for the respectve datasets below prior to running the notebooks.

[Reviews & Interactions Link](https://www.kaggle.com/rankirsh/evolution-of-top-games-on-twitch "Top Games on Twitch 2016-2021")

## Twitch API Data
Using the Twitch developers platform, I generated a client ID that allowed me access to their API to pull any necessary gaming data that I may need. In order to access the Twitch API I first downloaded the following package

```python
pip3 install python-twitch-client
```
Which then allows you to import TwitchClient from twitch.

## Notebooks 
Each notebook is titled accordingly - please reference each notebook for any additional details & process.

# Cleaning & Transformations 
The datasets in kaggle were already relatively clean where the only cleaning was required was to clean any additional columns and reset any column titles as needed.

For the Twitch API, the data required a pprint to be able to appropriately read the data, but was relatively cleaned. The transformation to a dataframe required parsing through the various items for each game to be able to extract each of the names, viewers and channels for the associated games to convert to a dataframe within pandas. 

# Loading
The initial upload required the creation of a new database in postgres, but I used the psycogp2 package in order to create a connection into the postgres server aand create the database rather than using pgAdmin and creating it within that interface. Further steps are noted in the jupyter notebook. 

After closing that connection, I used sqlalchemy to upload and create the tables for each of the dataframes within the gaming_db to upload my data. I had chosen sqlalchemy for it's ease of use and later versatility when I wanted to transform the data or for later updates into the database. 

# Additional Notes
Please noted for the Twitch API, you will need your own client ID in order to access the APIs and for the postgres access through sqlalchemy or psycogp2 you will also need to use your own local username, password, host and port as needed. 
