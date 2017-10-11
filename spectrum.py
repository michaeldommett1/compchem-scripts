#! /usr/bin/env python

import numpy as np
import math
from sys import argv
from os import system
import argparse
#########
sd=0.4  #standard deviation in eV
#########
"""
see http://gaussian.com/uvvisplot/ for implementation details

"""
parser = argparse.ArgumentParser()
parser.add_argument("-i","--input",required=True,help="Log file of Gaussian 09 TD job")
parser.add_argument("-gnu",help="Plot a spectrum using gnuplot",action="store_true")
parser.add_argument("-mpl",help="Plot a spectrum using matplotlib",action="store_true")
args=parser.parse_args()

def read_es(file):
    energies=[]
    os_strengths=[]
    for line in file:
        if " Excited State " in line:
            energies.append(float(line.split()[6]))
            os_strengths.append(float(line.split()[8][2:]))
    return energies,os_strengths

def abs_max(f,lam,ref):
    a=1.3062974e8
    b=f/(1e7/3099.6)
    c=np.exp(-(((1/ref-1/lam)/(1/(1240/0.4)))**2))
    return a*b*c

def gnu_plot(xaxis,yaxis):
    with open("data","w") as d:
        for i in range(len(xaxis)):
            d.write("{0} {1} {2}\n".format(i+1,xaxis[i],yaxis[i]))
        d.close()

    with open("plot","w") as p:
        p.write("set xlabel \"Energy (nm)\"\nset ylabel \"Absorption Coeff.(E)\"\n")
        p.write("plot 'data' using 2:3 title '' with lines lt 1 lw 2,\\\n")
        p.close()

    system("gnuplot -persist plot")
    system("rm -f plot data")

    return

def mpl_plot(xaxis,yaxis):
    import matplotlib.pyplot as plt
    plt.scatter(xaxis,yaxis,s=5,c="r")
    plt.plot(xaxis,yaxis,color="k")
    plt.show()
    return

infile=open(args.input,"r").read().splitlines()
energies,os_strengths=read_es(infile)

x=np.linspace(max(energies)+100,min(energies)-100,1000)
sum=[]


for ref in x:
    tot=0
    for i in range(len(energies)):
        tot+=abs_max(os_strengths[i],energies[i],ref)
    sum.append(tot)

if args.gnu:
    gnu_plot(x,sum)

elif args.mpl:
    mpl_plot(x,sum

else:
    "Please specify -mpl or -gnu to plot with matplotlib or gnuplot"