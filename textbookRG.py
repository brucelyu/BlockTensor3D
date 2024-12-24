#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : textbookRG.py
# Author            : Xinliang(Bruce) Lyu <lyu@issp.u-tokyo.ac.jp>
# Date              : 23.02.2023
# Last Modified Date: 23.02.2023
# Last Modified By  : Xinliang(Bruce) Lyu <lyu@issp.u-tokyo.ac.jp>
"""
Given the RG flow at criticality,
linearize the RG map and extract scaling dimensions
"""
import argparse
from tensornetworkrg import rg3d_pres as rg3d

# argument parser
argdesp = ("Extract scaling dimensions from linearzed RG map")
parser = argparse.ArgumentParser(description=argdesp)
parser.add_argument("--scheme", type=str,
                    help="TNRG scheme (default is --hotrg3d--)",
                    default="hotrg3d")
parser.add_argument("--ver", type=str,
                    help="TNRG scheme version (default is --base--)",
                    default="base")
parser.add_argument("--chi", type=int,
                    help="bond dimension (default: 2)",
                    default=2)
parser.add_argument("--rgstart", type=int,
                    help="starting RG step (default: 1)",
                    default=1)
parser.add_argument("--rgend", type=int,
                    help="ending RG step (default: 8)",
                    default=8)
parser.add_argument("--sectorChoice", type=str,
                    help="sector of operators (default is --both--)",
                    default="both",
                    choices=["both", "even", "odd"])
parser.add_argument("--outDir", type=str,
                    help="output directory to save rg flows and Tc",
                    default="./")
parser.add_argument("--isParal",
                    help="whether to use parallel computation codes",
                    action="store_true")

# read argument
args = parser.parse_args()
scheme = args.scheme
ver = args.ver
chi = args.chi
rgstart = args.rgstart
rgend = args.rgend
sectorChoice = args.sectorChoice
outDir = args.outDir
isParal = args.isParal

# take care of the parallelization
if isParal:
    from mpi4py import MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
else:
    comm = None
    rank = 0

pars = {"isZ2": True, "rg_n": 0,
        "chi": chi, "cg_eps": 1e-8, "display": False,
        "dataDir": None, "determPhase": False}

# extracting scaling dimensions
if sectorChoice == "both":
    rg3d.linRG2scaleD(scheme, ver, pars,
                      rgstart, rgend, evenN=10, oddN=10,
                      outDir=outDir, comm=comm)
else:
    rg3d.linRG2scaleD1rg(scheme, ver, pars,
                         rgn=rgstart, scaleN=10,
                         outDir=outDir, comm=comm,
                         sectorChoice=sectorChoice)
