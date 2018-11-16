# Data Wrangling with SQL, Python, R and Pyspark

**1. Use criteria to filter tables**

```sql
select Sepal_Length, Petal_Length from Iris where Petal_Width > 1 and Species='setosa';
```

```python
Iris[(Iris.Petal_Width > 1) & (Iris.Species=='setosa')][['Sepal_length','Petal_Length']]
```

```R
Iris %>% 
  filter(Petal_Length > 1, Species=='setosa') %>%
  select(Sepal_Length, Petal_Length)
```

```pyspark
Iris.filter((Iris.Petal_Length > 1) & (Iris.Species=='setosa')).select(Iris.Sepal_Length, Iris.Petal_Length)
```

**2. Derive aggregate statistics by groups**


```sql
select Species, count(Sepal_Length) as Sepal_Length_Count, avg(Sepal_Length) as Sepal_Length_mean from Iris group by Species;
```

```python
aggregated=Iris.groupby(by='Species',as_index=False).agg({'Sepal_Length': ['mean','count']})
aggregated.columns = ['_'.join(tup).rstrip('_') for tup in temp1.columns.values]
```

```R
Iris %>%
  group_by(Species) %>%
  mutate(Sepal_Length_mean=mean(Sepal_Length), Count=n())
```

```pyspark
from pyspark.sql import functions as F

Iris.groupBy(Iris.species).agg(F.mean(Iris.sepal_length).alias('sepal_length_mean'),F.count(Iris.sepal_length).alias('sepal_length_count'))
```

**3. Join tables to put features together**


```sql
select a.*, b.* from Iris a left join Iris_preference b on a.Species=b.Species;
```

```python
pd.merge(Iris, Iris_preference, how='left', on='Species')
```

```R
left_join(Iris, Iris_preference, by="Species")
```

```pyspark
Iris.join(Iris_preference,['Species'],"left_outer")
```

