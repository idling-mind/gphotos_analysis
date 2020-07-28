import pandas as pd
# Convert the list of dict into a dataframe.
df = pd.DataFrame(items)

# Taking the column mediaMetadata and splitting it into individual columns
dfmeta = df.mediaMetadata.apply(pd.Series)

# Combining all the different columns into one final dataframe
photos = pd.concat(
    [
        df.drop('mediaMetadata', axis=1), 
        dfmeta.drop('photo', axis=1), 
        dfmeta.photo.apply(pd.Series)
    ], axis=1
)