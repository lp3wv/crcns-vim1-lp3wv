
Edit this file to describe how to retrieve the data set. Except for very small data files, it's not recommended to check data into version control.

To retrieve the vim-1 data set, it must first be downloaded from the CRCNS site, which I did from the web interface.
https://portal.nersc.gov/project/crcns/download/index.php

The files EstimatedResponses.mat and Stimuli_Val_FullRes.mat must be downloaded into the folder and the file location must be updated in the notebook code, in 'fullFile' variable (for responses) and 'filepath' for Stimuli data.

To load the data into python, the researchers have included example code which imports the data directly into python, and I have expanded on this. This allows us to see the peak BOLD responses to each of the images for subject 1 and 2. There were two data sets for each subject, a training (n = 1750) and a testing (n = 120) set. For each image, there are about 25k voxels recorded (which are z-scored), so the units are standard deviations away from voxel mean. The original researchers used the training data to create a receptive field model to estimate responses to the testing set. 

I wrote two separate functions for the training and testing data set, in which the parameters are:subject, brain region, and image responses to examine (start and stop). In the function, the indices of nonzero responses are returned, and if multiple images are selected (default is all of them), an array of arrays will be returned. 



