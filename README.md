
# Dictionaries lab

### Introduction

In this lesson, we'll use our knowledge of dictionaries to retrieve data about various cities.

### Objectives

* Practice retreiving information from dictionaries
* Practice assigning new information to dictionaries
* Practice retriving information from a list of dictionaries

### Working with a single dictionary

Here is a dictionary representing the city of Greenville, North Carolina.  The area is in kilometers squared.


```python
greenville = {'Area': 68, 'City': 'Greenville', 'Country': 'USA', 'Population': 84554}
```

> Remember to press shift + enter to run the code.

Let's retrieve the population of the city and assign it to the variable `greenville_population`.


```python
greenville_population = None # change None
greenville_population # 84554
```

Now retrieve the area of Greenville and assign it to the variable `area`.


```python
area = None
area # 68
```

Now let's take a look at all of the keys in the `greenville` dictionary and coerce them into a list.  Assign this variable to the list `city_keys`.


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

Once again, we can retrieve our data from a Google Sheet of Travel Cities and Countries [shown here](https://docs.google.com/spreadsheets/d/1BTJMMFH9t4p5UmHj5kiC6PGfMN6yaaaZkocx0mDqTK0/edit#gid=0).  

![](./countries-cities.png)

We already followed the steps of the previous lesson to download the spreadsheet and move it to the current folder.  You can find the file [in the github repository](https://github.com/learn-co-curriculum/python-lists-lab).  So next, we get this data into Python code.  We have written the code for reading excel into Python for you.


```python
import pandas
file_name = './cities.xlsx'
travel_df = pandas.read_excel(file_name)
cities = travel_df.to_dict('records')
```

> Remember to press shift + enter.

Cool.  We have them!


```python
cities
```




    [{'City': 'Solta', 'Country': 'Croatia', 'Population': 1700, 'Area': 59},
     {'City': 'Greenville', 'Country': 'USA', 'Population': 84554, 'Area': 68},
     {'City': 'Buenos Aires',
      'Country': 'Argentina',
      'Population': 13591863,
      'Area': 4758},
     {'City': 'Los Cabos',
      'Country': 'Mexico',
      'Population': 287651,
      'Area': 3750},
     {'City': 'Walla Walla Valley',
      'Country': 'USA',
      'Population': 32237,
      'Area': 33},
     {'City': 'Marakesh', 'Country': 'Morocco', 'Population': 928850, 'Area': 200},
     {'City': 'Albuquerque',
      'Country': 'New Mexico',
      'Population': 559277,
      'Area': 491},
     {'City': 'Archipelago Sea',
      'Country': 'Finland',
      'Population': 60000,
      'Area': 8300},
     {'City': 'Iguazu Falls',
      'Country': 'Argentina',
      'Population': 0,
      'Area': 672},
     {'City': 'Salina Island', 'Country': 'Italy', 'Population': 4000, 'Area': 27},
     {'City': 'Toronto', 'Country': 'Canada', 'Population': 630, 'Area': 2731571},
     {'City': 'Pyeongchang',
      'Country': 'South Korea',
      'Population': 2581000,
      'Area': 3194}]



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

Now calculate the number of cities in the list and assign the number to the variabale `city_count`.


```python
city_count = None
city_count # 12
```

Finally, change the spelling of the South Korean city, Pyeongchang, to the string `'PyeongChang'`, its alternative spelling.


```python
cities[11]['City'] # 'PyeongChang'
```

Now let's work on retrieving a collection of information about a dictionary.  Use the appropriate dictionary function to return a list of values in the dictionary regarding Pyeongchang.   Assign the list to the variable `pyeongchang_values`.


```python
pyeongchang_values = None

pyeongchang_values # ['PyeongChang', 'South Korea', 2581000, 3194]
type(pyeongchang_values) # list
```




    NoneType



And now set `pyeongchang_keys` equal to a list of keys in the dictionary regarding Pyeongchang.


```python
pyeongchang_keys = None


pyeongchang_keys # ['City', 'Country', 'Population', 'Area']
type(pyeongchang_keys) # list
```




    NoneType



### Summary

In this section we saw how to retrieve and alter data in a dictionary.  We saw how we can retrieve a collection of information about a dictionary, like a list of it's keys and values, and we saw how to work with a list of dictionaries.
