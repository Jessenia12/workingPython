import pandas as pd

print('ok............')


serData = pd.Series(data=[10, 20, 30, 40], index=['carlos', 'juan', 'pepe', 'maria'])

print(serData)
print(serData.index)
print(serData['carlos'])
print('Jesse' in serData)
serData1=serData*2
print('*********DATAFRAME***********')

diccionario = {
    'one': pd.Series(data=[1, 2, 3, 4, 5], index=['carlos', 'juan', 'pepe', 'maria', 'lucas']),
    'two': pd.Series(data=[10, 20, 30, 40, 50], index=['carlos', 'juan', 'pepe', 'maria', 'lucas'])}

df=pd.DataFrame(diccionario)
print(df)
print(df.index)
print(df.columns)

df['three']=df['one']=df['two']
print(df)

df['filter']=df['three']>45
print(df)


del df['filter']
print(df)

df.insert(1,'copy of one', df['one'])
print(df)

print('-----------------Importing CSV FILES ---------------------')
movies=pd.read_csv('movies.csv')
#print(movies.head(3))

print(movies.columns)
print(movies.shape)

print('-----------------Importing CSV FILES ---------------------')
ratings=pd.read_csv('ratings.csv')
#print(movies.head(3))

print(ratings.columns)
print(ratings.shape)


print('-----------------Importing CSV FILES ---------------------')
tags=pd.read_csv('tags.csv')
#print(movies.head(3))

print(tags.columns)
print(tags.shape)

print(tags.tail(2))

# Eliminamos columna timestamp
del ratings['timestamp']
del tags['timestamp']

print('Variables de tags:')
print(tags.columns)
print('Variables de ratings:')
print(ratings.columns)

print(tags.iloc[0])

print(tags.iloc[[0,22,500]])
print(tags.index)

print('-------------------ratings---------------------------')
print(ratings.head(5))
print(ratings['rating'].describe())
print(ratings['rating'].mean())
print(ratings['rating'].min())
print(ratings['rating'].max())


is_highly_rated=ratings['rating']>=4
print(ratings[is_highly_rated].head(4))
print(ratings.shape)
print(ratings[is_highly_rated].head(4).shape)
print(movies.columns)

print(movies.head(2))

is_animation=movies['genres'].str.contains('Animation')
print(movies.shape)
print(movies[is_animation].shape)
print('movies')
print(movies.columns)
print('ratings')
print(ratings.columns)



highly_rated_animation = ratings[is_highly_rated].merge(
    movies[is_animation],
    on='movieId'  # Asumiendo que ambos DataFrames tienen la columna 'movieId'
)

# Mostrar los primeros 5 resultados
print(highly_rated_animation.head())

# Información de las dimensiones
print('Total ratings:', ratings.shape)
print('Total películas animation:', movies[is_animation].shape)
print('Total películas animation con rating >= 4:', highly_rated_animation.shape)