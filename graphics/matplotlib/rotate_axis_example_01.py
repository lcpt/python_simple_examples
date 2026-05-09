# Source - https://stackoverflow.com/a/42978441
# Posted by Mr Tsjolder from codidact, modified by community. See post 'Timeline' for change history
# Retrieved 2026-04-16, License - CC BY-SA 3.0
import numpy as np
from matplotlib import pyplot, transforms

x= np.array([351,345,339,336,333,330,327,324,318,312])
y= np.array([84, 84, 83, 82, 81, 80, 80, 79, 78, 77])
rotate= True


# define transformed line
if(rotate):
    # first of all, the base transformation of the data points is needed
    base = pyplot.gca().transData
    rot = transforms.Affine2D().rotate_deg(90)
    line = pyplot.plot(x, y, transform= rot + base)
else:
     line = pyplot.plot(x, y)
# or alternatively, use:
# line.set_transform(rot + base)

pyplot.show()
