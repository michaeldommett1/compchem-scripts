#!/usr/bin/env python

# script in the ONIOM preparation process. Takes a set of atom types (AMBER), charges, and an xyz file, and writes out the gaussian-style atomtype-charge x y z file 

from sys import argv

atomtypes =  open(argv[1],"r").read().splitlines()
charges = open(argv[2],"r").read().splitlines()
xyz = open(argv[3],"r").read().splitlines()
writefile=open(argv[4],"w")
writefile.write("{0}\n\n".format(len(atomtypes)))

for i in range(len(atomtypes)):
	writefile.write("{0}-{1:1.6f} {2:>12.6f} {3:>12.6f} {4:>12.6f}\n".format(atomtypes[i],float(charges[i]),float(xyz[i+2].split()[1]),float(xyz[i+2].split()[2]),float(xyz[i+2].split()[3])))
