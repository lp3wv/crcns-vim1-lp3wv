
Edit this file to describe how to retrieve the data set. Except for very small data files, it's not recommended to check data into version control.

To retrieve the vim-1 data set, it must first be downloaded from the CRCNS site, which I did from the web interface. I downloaded the EstimatedResponses.mat and Stimuli.mat files, as they were the comprehensive ones applicable for further mass-analysis. To load the data into python, the researchers have included code which imports the data into table format directly into python and made available the python script (code and documentation) on github. 

To get all V1 voxel responses in the training data set:

import tables,numpy
f = tables.openFile('EstimatedResponses.mat')
f.ListNodes # Show all variables available
Dat = f.getNode('/dataTrnS1')[:]
ROI = f.getNode('/roiS1')[:].flatten()
V1idx = numpy.nonzero(ROI==1)[0]
V1resp = Dat[:,V1idx]

def read_neuron(id, param_1=default_1):
   """Describe what the arguments of the function mean and what the function returns"""
   body_of_the_function
