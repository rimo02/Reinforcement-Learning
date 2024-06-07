import matplotlib.pyplot as plt
from IPython import display

plt.ion()


def plot(scores, meanscores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(meanscores)
    plt.ylim(ymin=0)
    plt.text(len(scores) - 1, scores[-1], str(scores[-1]))
    plt.text(len(meanscores)-1, meanscores[-1], str(meanscores[-1]))
