# Copyright (c) 2010 Timothy Lovorn
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from numpy import arange

import FileDict

class Grapher(object):
    def __init__(self, configPaths):
        self.configPaths = configPaths
        self.readOutputs()
        # graphing parameter defaults
        self.axis_label_fontsize = 20
        self.num_ticks = 5
        self.tick_formatstr = "%.2f"

    def addConfigs(self, configPaths):
        self.configPaths.extend(configPaths)
        self.readOutputs()

    def readOutputs(self):
        self.outputDataList = [(filePath, 
            FileDict.readReferencedDict(filePath, "outputLogName")) 
            for filePath in self.configPaths]

    def extractVar(self, section, var):
        varValues = []
        for (fileName, outputData) in self.outputDataList:
            try:
                varValues.append(outputData.getLatestVar(section, var))
            except KeyError:
                print("warning: couldn't read var %s in section %s of file %s"
                      % (var, section, fileName))
        return varValues

    def simple2D(self, xSection, xVar, ySection, yVar, fig=None, axes=None):
        # if either axes or figure is passed in as None, we ignore both
        if (fig is None) or (axes is None):
            fig = plt.figure()
            axes = fig.add_subplot(1,1,1)

        xData = self.extractVar(xSection, xVar)
        yData = self.extractVar(ySection, yVar)

        axes.plot(xData, yData, "k-")
        self.setxTicks(axes, xData)
        self.setyTicks(axes, yData)
        return fig, axes

    def setAxisLabels(self, axes, xLabel, yLabel):
        axes.set_xlabel(xLabel, fontsize=self.axis_label_fontsize)
        axes.set_ylabel(yLabel, fontsize=self.axis_label_fontsize)

    def setxTicks(self, axes, data):
        axes.set_xticks(self.tickRange(data))
        axes.xaxis.set_major_formatter(FormatStrFormatter(self.tick_formatstr))

    def setyTicks(self, axes, data):
        axes.set_yticks(self.tickRange(data))
        axes.yaxis.set_major_formatter(FormatStrFormatter(self.tick_formatstr))

    def tickRange(self, data):
        data, start, stop = sorted(data), float(data[0]), float(data[-1])
        step = (stop - start) / (self.num_ticks - 1)
        return arange(start, stop + step / 100.0, step)

    def saveFigure(self, fig, figurePath):
        fig.savefig(figurePath + ".png")
        fig.savefig(figurePath + ".eps")
