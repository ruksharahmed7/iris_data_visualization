import pandas as pd
import matplotlib.pyplot as plt


def plot_parallel_coordinates(csv_file_path:str='Iris.csv'):
    """
    Plots a parallel coordinates plot of the Iris dataset.

    Parameters:
        csv_file_path (str): The path to the CSV file containing the Iris dataset. Defaults to 'Iris.csv'.

    Returns:
        None
    """
    
    # Load the Iris dataset
    iris_df = pd.read_csv(csv_file_path)

    # Create Parallel Coordinates plot
    plt.figure(figsize=(10, 6))
    #https://pandas.pydata.org/docs/reference/api/pandas.plotting.parallel_coordinates.html
    pd.plotting.parallel_coordinates(
        frame = iris_df, class_column ='Species', color=('#556270', '#4ECDC4', '#C7F464')
    )  
    # Add legend
    plt.legend(loc='upper right')

    # Add title and labels
    plt.title('Parallel Coordinates Plot of Iris Dataset')
    plt.xlabel('Features')
    plt.ylabel('Feature Values')

    # Show plot
    plt.show()

if __name__ == '__main__':
    plot_parallel_coordinates()


'''
By observing the Parallel Coordinates diagram, identify
which property can be used to classify the different species of iris and justify your choice
with maximum 3 sentences (5 mark).

ANSWER:

The property 'Petal length' can be used to classify the 3 different species of iris(Setosa, Versicolor 
and Virginica) because the values of 'Petal length' have the most easily discernable separate ranges/distributions for the 3 classes 
and so this feature can distinguish between the 3 classes. For both the 'Sepal length' and 'Sepal width' features, 
the values of the 3 classes overlap significantly in the plot making them unsuitable for classification. For 'Petal width',
the distributions of feature values for Virginica and Versicolor overlap in the plot making them unsuitable for classification.

'''
