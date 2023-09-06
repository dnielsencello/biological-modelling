# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 12:39:46 2022

@author: Keith Roper
"""
import math
import os
import numpy as np
import matplotlib.pyplot as plt

os.getcwd()

def pcr_plot():
    pcr_comp = []
    pcr_comp = np.loadtxt('pcr_mod_a.csv', delimiter = ',')

    plt.figure(1)                                       # Create Figure 1
    plt.scatter(pcr_comp[:,0],pcr_comp[:,1], c="red", marker="<", label="template copies")  # Scatter plot: ([T] vs cycle)
    plt.title("PCR")                      # plot title
    plt.xlabel("cycle")                          # x axis label
    plt.ylabel("template copies")                   # y axis label
    plt.legend(loc="upper left")                        # Place legend in upper left of plot
    #plt.show()                                          # Show the plot

def pcr_plot2(): # example of double - y axes (twin)
    pcr_comp = []
    pcr_comp = np.loadtxt('pcr_mod_a.csv', delimiter = ',')
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    line1, = ax1.plot(pcr_comp[:,0],pcr_comp[:,1], 'b--')
    line2, = ax2.plot(pcr_comp[:,0],pcr_comp[:,2], 'r^')

    plt.title('Competitive Inhibitor PCR')


    ax1.set_xlabel('cycles')
    ax1.set_ylabel('target', color = 'blue')
    ax2.set_ylabel('inhibitor', color = 'red')
    ax1.tick_params('y', colors = 'blue')
    ax2.tick_params('y', colors = 'red')
    ax1.legend((line1,line2), ('target','inhibitor'), loc = 'lower right')

    ax1.plot(pcr_comp[:,0],pcr_comp[:,1], 'b--')
    ax2.plot(pcr_comp[:,0],pcr_comp[:,2], 'r^')
    #ranges
    ax1.set_ylim([0,20000])
    ax2.set_ylim([0,2000])
    #plt.ylim([-100,1250])
    #plt.show()