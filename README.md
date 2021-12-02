# SQLAlchemy-Challenge
Surf's Up!

Introduction

In this skills practice the senariois I  have decided to treat myself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, I need to do come climate analysis on the area. Precipitation and Station Analysis was performed on the database.  

Methods

The climate analysis and data exploration was performed on a database utilizing SQLAlchemy ORM queries, Pandas, and Matplotlib.  On the second portion of the exercise a Flask API based on the initial queries is created.  Utlitizing Python in Jupyter Notebook and VS Code.  

Analysis/ Results

Using SQLAlchemy I was able to reflect the tables into classes.  I linked Python to the database by creating a session.  The last 12 months of precipitation in the dataset were queried and a dataframe created.  Those values were plotted creating the following chart.  

![Hawaii Precipitaiton](https://user-images.githubusercontent.com/88807979/144353031-0ab3a951-6d55-4f5f-9d8f-33db6b65d704.png)

Pandas was used to obtain summary statics for the precipitaion data.

![image](https://user-images.githubusercontent.com/88807979/144353159-e45cbb9a-e6c2-4bb0-b034-6b71fd9fa400.png)

Next the most active stations in the state were analyzed.  Using the most active station the lowest, highest and average temperatures were determined.  Additionally the last 12 months of temperature observation for the station was plotted into a histogram. 

![temp histo](https://user-images.githubusercontent.com/88807979/144353336-13a976c4-733e-46a7-ba0e-97d325f670e9.png)
 
Discussion/Conclusion 

The use of the reflect and inspect to access database was a much simplified way of manuipulating the data compared to having to create individual tables.  Once in the Jupyter notebook Pandas and Matplotlib further simiplified manipulation.   
