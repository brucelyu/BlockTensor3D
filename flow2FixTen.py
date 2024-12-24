#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : flow2FixTen.py
# Author            : Xinliang(Bruce) Lyu <lyu@issp.u-tokyo.ac.jp>
# Date              : 22.02.2023
# Last Modified Date: 22.02.2023
# Last Modified By  : Xinliang(Bruce) Lyu <lyu@issp.u-tokyo.ac.jp>
import argparse
from tensornetworkrg import rg3d_pres as rg3d


# argument parser
argdesp = ("Generate the RG flow at Tc" )
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
parser.add_argument("--rgn", type=int,
                    help="maximal rg iteration (default: 15)",
                    default=15)
parser.add_argument("--outDir", type=str,
                    help="output directory to save rg flows and Tc",
                    default="./")
parser.add_argument("--plotRGmax", type=int,
                    help="maximal rg plot (default: 15)",
                    default=15)
parser.add_argument("--isParal",
                    help="whether to use parallel computation codes",
                    action="store_true")

# read argument
args = parser.parse_args()
scheme = args.scheme
ver = args.ver
chi = args.chi
rg_n = args.rgn
outDir = args.outDir
plotRGmax = args.plotRGmax
isParal = args.isParal

# take care of the parallelization
if isParal:
    from mpi4py import MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
else:
    comm = None
    rank = 0

if rank == 0:
    isPrint = True
else:
    isPrint = False

pars = {"isZ2": True, "rg_n": rg_n,
        "chi": chi, "cg_eps": 1e-8, "display": isPrint,
        "dataDir": None, "determPhase": False}

# generate RG flow
rg3d.generateRGflow(scheme, ver, pars,
                    outDir, plotRGmax,
                    comm=comm)
