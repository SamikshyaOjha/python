import pandas as pd
#1 definhe raw data dictionary
data={
    "name":["surakshya","pragya","selvianana"],
    "age": [19,18,20]
}
#2. Create structured Dataframe
 df= pd.DataFrame(data)
#3. Print Dataframe and compute average
print(df)
print(df["age"].mean()) 30,0 average age