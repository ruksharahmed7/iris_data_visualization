import pandas as pd 
import numpy as np

#Read the dataset into a suitable data structure and print on the screen its first 10 rows (5 marks).
def read_into_dataframe(csv_file_path: str):
    """
    Reads a CSV file into a pandas DataFrame and prints the first 10 rows.

    Parameters:
        csv_file_path (str): The path to the CSV file.

    Returns:
        None
    """
    df = pd.read_csv(csv_file_path)
    print(df.head(10))

'''
By considering only the Petal width, obtain the following statistical information for each one
of the three species of iris from the dataset:
- Measures of Central Tendency (mean and median) (5 marks)
- Measures of Dispersion (standards deviation, range) (5 marks)
'''
def feature_stats_info(feature: str = 'Sepal width', csv_file_path: str = 'Iris.csv'):
    """
    A function to calculate various statistics (mean, median, standard deviation, range) for a given feature in a dataset, grouped by species. 
    Parameters:
    - feature: str, the feature for which statistics are calculated (default is 'Sepal width')
    - csv_file_path: str, the file path for the dataset in CSV format (default is 'Iris.csv')
    """
    df = pd.read_csv(csv_file_path) # read the dataset from a csv file in pandas dataframe
    feature_df = df[[feature, 'Species']] # Select the feature and the target column

    # Measures of Central Tendency(mean and median) for each of the 3 species: Setosa, Versicolor and Virginica
    #using groupby method to calculate mean per species
    feature_mean = feature_df.groupby('Species')[feature].mean()
    # add a column name 'mean' to the newly calculated dataframe
    feature_mean = pd.DataFrame({'Species':feature_mean.index, 'Mean':feature_mean.values}) #https://stackoverflow.com/questions/28503445/assigning-column-names-to-a-pandas-series
    # make the species column the index of the dataframe
    feature_mean.set_index('Species', inplace=True)

    #using groupby method to calculate median per species
    feature_median = feature_df.groupby('Species')[feature].median()
    # add a column name 'median' to the newly calculated dataframe
    feature_median = pd.DataFrame({'Species':feature_median.index, 'Median':feature_median.values})
    # make the species column the index of the dataframe
    feature_median.set_index('Species', inplace=True)

    # Measures of Dispersion(standards deviation, range) for each of the 3 species: Setosa, Versicolor and Virginica
    #using groupby method to calculate standard deviation per species
    feature_std = feature_df.groupby('Species')[feature].std()
    # add a column name 'std' to the newly calculated dataframe
    feature_std = pd.DataFrame({'Species':feature_std.index, 'Std':feature_std.values})
    # make the species column the index of the dataframe
    feature_std.set_index('Species', inplace=True)

    #using groupby method to calculate range per species
    feature_range = feature_df.groupby('Species')[feature].max() - feature_df.groupby('Species')[feature].min()
    # add a column name 'range' to the newly calculated dataframe
    feature_range = pd.DataFrame({'Species':feature_range.index, 'Range':feature_range.values})
    # make the species column the index of the dataframe
    feature_range.set_index('Species', inplace=True)

    #Concatenate the 4 dataframes together 
    feature_stats = pd.concat([feature_mean, feature_median, feature_std, feature_range], axis=1)
    print(feature_stats)



if __name__ == '__main__':
    # Call the read_into_dataframe function
    #read_into_dataframe('Iris.csv')
    feature_stats_info()