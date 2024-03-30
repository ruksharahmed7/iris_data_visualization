import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
Identify which one of the following types of charts would provide optimal visualisation for a
single attribute of a single species from the Iris dataset (5 marks):
- Line Chart
- Bar Chart
- Box Plot Chart
Justify your choice with maximum 5 sentences (5 marks).

ANSWER:

Choosing a Box Plot Chart to visualize a single attribute of a specific species 
from the Iris dataset is the optimal choice. 

Box plots offer a concise representation of the data distribution, showcasing key 
statistical measures like median, quartiles, and outliers. This visualization method 
enables easy comparison of the attribute's variability within the chosen species, 
helping in understanding the range of values present. It is useful for 
realizing the spread and central tendency of the attribute across different species, 
giving users valuable insights into species-specific characteristics.
'''

'''
Choose one species and one attribute from the Iris dataset and visualise its 
values by using the selected type of chart (5 marks). In this case, the data will 
be one-dimensional. Provide the Python code and the resulting visualisation.
'''
def draw_box_plot(feature: str = 'Sepal width', species:str='Setosa', csv_file_path: str = 'Iris.csv'):
    """
    A function to draw a box plot for a given feature  and species in a dataset.
    Parameters:
    - feature: str, the feature for which statistics are calculated (default is 'Sepal width')
    - species: str, the species for which the box plot is drawn (default is 'Setosa')
    - csv_file_path: str, the file path for the dataset in CSV format (default is 'Iris.csv')
    """
    df = pd.read_csv(csv_file_path) # read the dataset from a csv file in pandas dataframe
    feature_df = df[[feature, 'Species']] # Select the feature and the target column

    # Filter the dataframe to only include the desired species
    filtered_df = feature_df[feature_df['Species'] == species]
    
    # Plot the boxplot
    plt.boxplot(filtered_df[feature])
    plt.title(f'Box Plot of {feature} for {species}')
    plt.ylabel(feature)
    plt.show()
if __name__ == '__main__':
    draw_box_plot()