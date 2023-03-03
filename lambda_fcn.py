# A lambda function in Python is a simple, anonymous function that is defined without a name.
add_two = lambda x: x + 2

print(add_two(5))

import pandas as pd
 
df = pd.DataFrame({
   'name': ['Amy', 'Jackie', 'Sue'],
   'grades': [90, 84, 76]
})
 
# use the lambda function to multiply bump up the values in the grades column by 1.2!
# When we want to combine with other built-in functions such as map(), filter(), and apply() to filter for data
df['grades'] = df['grades'].apply(lambda x: x * 1.2)

print(df)