# -*- coding: utf-8 -*-
# -*- mode: python -*-
#"""Functions for file IO"""
#from __future__ import print_function, division, absolute_import

import numpy
import tables

fullFile = tables.open_file(r'C:\Users\lasya\crcns-vim1-lp3wv\data\EstimatedResponses.mat')
print(fullFile.list_nodes)  # Show all variables available

'''
cxReg value = cortex region
0 = other
1 = V1
2 = V2
3 = V3
4 = V3A
5 = V3B
6 = V4
7 = Lateral Occipital Area
'''


def BOLD_testing(subj, cxReg, imageStart=0, imageStop=1750):

    assert subj == "S1" or "S2", "please enter a valid subject"
    idx = []
    resp = []

    if subj == "S1":
        dat = fullFile.get_node('/dataValS1')[:]
        ROI = fullFile.get_node('/roiS1')[:].flatten()
        idx = numpy.nonzero(ROI == cxReg)[0]
        resp = dat[:, idx]

        return resp[imageStart:imageStop]

    else:
        dat = fullFile.get_node('/dataValS2')[:]
        ROI = fullFile.get_node('/roiS2')[:].flatten()
        idx = numpy.nonzero(ROI == cxReg)[0]
        resp = dat[:, idx]

        return resp[imageStart:imageStop]



def BOLD_training(subj, cxReg, imageStart=0, imageStop=1750):
    assert subj == "S1" or "S2", "please enter a valid subject"
    idx = []
    resp = []

    if subj == "S1":
        dat = fullFile.get_node('/dataTrnS1')[:]
        ROI = fullFile.get_node('/roiS1')[:].flatten()
        idx = numpy.nonzero(ROI == cxReg)[0]
        resp = dat[:, idx]

        return resp[imageStart:imageStop]

    else:
        dat = fullFile.get_node('/dataTrnS2')[:]
        ROI = fullFile.get_node('/roiS2')[:].flatten()
        idx = numpy.nonzero(ROI == cxReg)[0]
        resp = dat[:, idx]

        return resp[imageStart:imageStop]


test = BOLD_training("S2", 7, 0, 1)
print(test)

test = BOLD_testing("S2", 7, 0, 1)
print(test)
