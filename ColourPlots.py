import matplotlib.pyplot as plt
import numpy as np

def plot_readability_score(score):
    """
    Plots the readability score on a color gradient from green to red.

    Parameters:
        score (float): The readability score ranging from 0 to 100.

    Returns:
        None
    """
    # Define the color map from green to red
    cmap = plt.get_cmap('RdYlGn')

    # Normalize the score to fit within [0, 1] for the color map
    normalized_score = score / 100.0

    # Plot a single pixel to display the color bar
    plt.imshow([[normalized_score]], cmap=cmap, aspect='auto')

    # Hide the axes
    plt.axis('off')

    # Display the plot
    plt.show()

if __name__ == "__main__":
    # Example usage:
    readability_score = 10
    plot_readability_score(readability_score)
