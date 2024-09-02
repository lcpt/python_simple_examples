import numpy, matplotlib
import matplotlib.pyplot as plt

xData = numpy.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0])
yData = numpy.array([21.05, 21.21, 20.76, 20.34, 20.27, 20.78, 20.60, 20.55, 19.95, 19.23, 19.64, 19.92, 19.91, 19.56, 19.39, 19.31, 19.35, 18.97, 18.69, 19.00, 19.15, 19.08, 18.97, 19.26, 19.52, 19.56, 19.28, 19.47, 19.85, 19.77])

# polynomial curve fit the test data
fittedParameters = numpy.polyfit(xData, yData, 3)


##########################################################
# graphics output section
def ModelAndScatterPlot(graphWidth, graphHeight):
    f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
    axes = f.add_subplot(111)

    # first the raw data as a scatter plot
    axes.plot(xData, yData,  'D')

    # create data for the fitted equation plot
    xModel = numpy.linspace(min(xData), max(xData))
    yModel = numpy.polyval(fittedParameters, xModel)

    # now the model as a line plot
    axes.plot(xModel, yModel)

    axes.set_xlabel('X Data') # X axis data label
    axes.set_ylabel('Y Data') # Y axis data label

    # polynomial derivative from numpy
    deriv = numpy.polyder(fittedParameters)

    # for plotting
    minX = min(xData)
    maxX = max(xData)

    # value of derivative (slope) at a specific X value, so
    # that a straight line tangent can be plotted at the point
    # you might place this code in a loop to animate
    pointVal = 15.0 # example X value
    y_value_at_point = numpy.polyval(fittedParameters, pointVal)
    slope_at_point = numpy.polyval(deriv, pointVal)

    ylow = (minX - pointVal) * slope_at_point + y_value_at_point
    yhigh = (maxX - pointVal) * slope_at_point + y_value_at_point

    # now the tangent as a line plot
    axes.plot([minX, maxX], [ylow, yhigh])

    plt.show()
    plt.close('all') # clean up after using pyplot


graphWidth = 800
graphHeight = 600
ModelAndScatterPlot(graphWidth, graphHeight)
