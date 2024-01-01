import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(scores, mean_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.show(block=False)
    plt.pause(.1)
    
# import matplotlib.pyplot as plt

# def plot(scores, mean_scores):
#     """
#     Plot scores and average scores.

#     Parameters:
#     - scores (list): A list of numerical scores.
#     - mean_scores (list): A list of numerical average scores.
#     """
#     plt.clf()
#     plt.figure(figsize=(10, 6))  # Adjust the figure size if needed

#     plt.plot(scores, label='Scores')
#     plt.plot(mean_scores, label='Average Scores', linestyle='--')

#     plt.title('Training...')
#     plt.xlabel('Game Number')
#     plt.ylabel('Score')
#     plt.legend()  # Show legend with labels

#     plt.grid(True)
#     plt.show()