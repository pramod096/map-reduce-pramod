# Map-Reduce

- Learning the basics of **_MapReduce_** for large datasets in **_Python_**.

## Data Description:

- This Data Set consists details of all the **_Movies and TV Shows, available in Netflix_**, like their names, release year, duration etc...
- The Dataset is a free resource from **_[Kaggle](https://www.kaggle.com)_** and can be viewed **_[here](netflix_titles.csv)_**.

## Study:

- For this Dataset, I want to find out the total count of Movies and TV Shows, Netflix has released each year.

## Execution:

- A **_Mapper Script_** extracts the year from each row in the dataset, which is used as a **_Key_** and a **_Value_** of 1 is assigned to each Key. This is given as input to the **_Sorter_** which sorts all the years in descending order. Based on the output of the Sorter, which is passed as input to the **_Reducer Script_**, combines all the similar years and increments the count.

## Powershell Command:

- **_cat netflix_titles.csv | python 21mapper.py | python 22sorter.py | python 23reducer.py > PRAMODoutput.txt_**

## Summary:

- By examining the final output, we can understand the **_growth of Netflix_** in recent years, due to improvements in the Technology and access to Internet. More the **_80%_** of Netflix content was released in the last **_5 years_**.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![Chart](images/netflix_shows.PNG)
