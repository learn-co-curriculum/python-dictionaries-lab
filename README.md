
# Dictionaries lab

### Introduction

Ok, let's start off with our google spreadsheet of data.

### Objectives

### Working with a single dictionary

Here is a dictionary representing the city of Greenville, North Carolina.  The area is in kilometers squared.  Let's retrieve the population of the city and assign it to the variable `greenville_population`.


```python
greenville = {'Area': 68, 'City': 'Greenville', 'Country': 'USA', 'Population': 84554}
```

> Remember to press shift + enter to run the code.


```python
greenville_population = None # change None
greenville_population # 84554
```

Now retrieve the area of Greenville and assign it to the variable `area`.


```python
area = None
area # 68
```

Ok, once that is working, let's take a look at all of the keys in the `greenville` dictionary and coerce them into a list.  Assign this variable to the list `city_attributes`.


```python
city_keys = None
city_keys # ['Area', 'City', 'Country', 'Population']
```

Alright, next let's get all of the values in our greenville dictionary and coerce it into a list.  Assign that list to the variable `city_values`.


```python
city_values = None
city_values # [68, 'Greenville', 'USA', 84554]
```

### Working with multiple cities

Once again, we will get our data from a Google Sheet of [Travel Cities and Countries](https://docs.google.com/spreadsheets/d/1BTJMMFH9t4p5UmHj5kiC6PGfMN6yaaaZkocx0mDqTK0/edit#gid=0).  

![](./countries-cities.png)

We already followed the steps of the previous lesson to download the spreadsheet and move it to the current folder.  You can find the file [in the github repository](https://github.com/learn-co-curriculum/python-lists-lab).

Now that we have this file in the folder we are working with, we can get this data into Python code.  We have written the code for reading excel into Python for you.


```python
import pandas
file_name = './cities.xlsx'
travel_df = pandas.read_excel(file_name)
cities = travel_df.to_dict('records')
```

Cool.  We have them!


```python
cities
```




    [{'Area': 59, 'City': 'Solta', 'Country': 'Croatia', 'Population': 1700},
     {'Area': 68, 'City': 'Greenville', 'Country': 'USA', 'Population': 84554},
     {'Area': 4758,
      'City': 'Buenos Aires',
      'Country': 'Argentina',
      'Population': 13591863},
     {'Area': 3750,
      'City': 'Los Cabos',
      'Country': 'Mexico',
      'Population': 287651},
     {'Area': 33,
      'City': 'Walla Walla Valley',
      'Country': 'USA',
      'Population': 32237},
     {'Area': 200, 'City': 'Marakesh', 'Country': 'Morocco', 'Population': 928850},
     {'Area': 491,
      'City': 'Albuquerque',
      'Country': 'New Mexico',
      'Population': 559277},
     {'Area': 8300,
      'City': 'Archipelago Sea',
      'Country': 'Finland',
      'Population': 60000},
     {'Area': 672,
      'City': 'Iguazu Falls',
      'Country': 'Argentina',
      'Population': 0},
     {'Area': 27, 'City': 'Salina Island', 'Country': 'Italy', 'Population': 4000},
     {'Area': 2731571, 'City': 'Toronto', 'Country': 'Canada', 'Population': 630},
     {'Area': 3194,
      'City': 'Pyeongchang',
      'Country': 'South Korea',
      'Population': 2581000}]



Ok, so the list of countries associated with each city has been assigned to the variable `cities`.  Now we will work with reading and manipulating this list of cities.

### Working with our list of cities

First, access the third to last element and set it equal to the variable `salina`.


```python
salina = None 
salina
# {'Area': 27, 'City': 'Salina Island', 'Country': 'Italy', 'Population': 4000}
```

Now access the fourth country in the list, and set it's population equal to a variable called `los_cabos_pop`.


```python
los_cabos_pop = None
los_cabos_pop # 287651
```

Now calculate the number of cities and set it equal to the variabale `city_count`.


```python
city_count = None
city_count # 12
```

Finally, change the spelling of the South Korean city in the list to the string, `'Pyongyang'`, the alternative spelling.


```python
cities[11]['City'] # Pyongyang
```




    'Pyeongchang'



### Summary

In this section we saw how to retrieve and alter data in a dictionary.  We saw how we can retrieve a collection of information about a dictionary, like a list of it's keys and values.  We also saw how to work with a list of dictionaries.
