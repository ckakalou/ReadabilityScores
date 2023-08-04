# Created by Christine Kakalou on 3/8/2023
# Project: ReadabilityScores
#
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FuncFormatter, MaxNLocator

raygory_lines2 = {3: [(8, 5.8), (24, 13.5)], 4: [(10, 5.5), (26, 12)], 5: [(11, 4.9), (28, 10.7)],
                  6: [(13, 4.6), (30, 10.2)], 7: [(18, 4), (32, 10)], 8: [(23, 3.8), (34, 9.7)],
                  9: [(24, 3.7), (35, 8.5)], 10: [(27, 3.5), (36, 7.8)], 11: [(29, 3.5), (38, 7.8)],
                  12: [(32, 3.3), (40, 7.7)], 13: [(36, 3.21), (42, 6.7)]
                  }


def circle(x, y, radius=0.5):
    from matplotlib.patches import Circle
    from matplotlib.patheffects import withStroke
    circle = Circle((x, y), radius, clip_on=False, zorder=10, linewidth=1,
                    edgecolor='black', facecolor=(0, 0, 0, .0125),
                    path_effects=[withStroke(linewidth=5, foreground='w')])
    ax.add_artist(circle)


def text(x, y, text, color='blue'):
    ax.text(x, y, text, backgroundcolor="white",
            ha='center', va='center', weight='bold', color=color)


# long sentences
from_y = 27
x_sent = []
y_sent = []
for y in range(3, 6):
    for x in range(6, from_y):
        x_sent.append(x)
        y_sent.append(y)
        # raygor_of_keys_to_ignore[f"{y}:{x}"] = 0
    from_y = from_y - 8

# long words
to_y = 44
x_word = []
y_word = []
for y in range(7, 29):
    to_y = to_y - 1
    for x in reversed(range(to_y, 45)):
        x_word.append(x)
        y_word.append(y)
        # raygor_of_keys_to_ignore[f"{y}:{x}"] = 0

fig, ax = plt.subplots(figsize=(12, 12))
tick_spacing = 1
k2 = 3
for i in raygory_lines2.keys():
    x1, x2 = raygory_lines2[i][0][0], raygory_lines2[i][1][0]
    y1, y2 = raygory_lines2[i][0][1], raygory_lines2[i][1][1]
    # Blue plot
    circle((x1 + x2) / 2, (y1 + y2) / 2)
    text((x1 + x2) / 2, (y1 + y2) / 2, k2)
    plt.plot([x1, x2], [y1, y2], 'ro-')
    k2 = k2 + 1

ax.set_xticks([i for i in range(6, 46, 2)])
y_label1 = [28, 23.0, 19.0, 16.0, 13.5, 12.0, 10.2, 9.0, 7.7,
            6.9, 6.3, 5.7, 5.2, 4.9, 4.6, 4.3, 4.0, 3.8, 3.6,
            3.4, 3.2]
plt.gca().yaxis.set_major_locator(plt.MultipleLocator(1))
ax.set_yticks(y_label1)
ax.yaxis.set_ticklabels([str(y3) for y3 in y_label1])
# ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

ax.set_title('Raygor Graph')
ax.set_xlabel('Value')
ax.axvline(x=18, linestyle='--')
ax.axhline(y=16, linestyle='--')
circle(18, 16)
text(18, 16, 'G', 'red')

tex = r'Long words'
text1 = 'Long Sentence'
ax.text(37, 25, tex, fontsize=10, va='bottom')
ax.text(8, 5.5, text1, fontsize=10, va='bottom')

# ax.fill_between([6,8,10],[4,3.4,3.2], interpolate=True)
plt.gca().invert_yaxis()
fig.tight_layout()
ax.tick_params(direction='in', length=6, width=2, colors='r', right=True, labelright='on')
# ax.fill_between([18,36,44,44],[28,12,7,28],1, interpolate=True)
plt.show()