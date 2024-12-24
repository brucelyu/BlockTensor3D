#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : bisectTc.py
# Author            : Xinliang(Bruce) Lyu <lyu@issp.u-tokyo.ac.jp>
# Date              : 21.02.2023
# Last Modified Date: 21.02.2023
# Last Modified By  : Xinliang(Bruce) Lyu <lyu@issp.u-tokyo.ac.jp>
import argparse
from tensornetworkrg import rg3d_pres as rg3d

# argument parser
argdesp = ("Find critical temperature given---" +
           "1) 3D TNRG scheme and 2) bond dimension")
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
                    help="maximal rg iteration (default: 12)",
                    default=12)
parser.add_argument("--itern", type=int,
                    help="iteration of finding the Tc (default:6)",
                    default=6)
parser.add_argument("--outDir", type=str,
                    help="output directory to save rg flows and Tc",
                    default="./")
parser.add_argument("--Tlow", type=float,
                    help="Estimated lower bound for critical temperature",
                    default=4.0)
parser.add_argument("--Thi", type=float,
                    help="Estimated higher bound for critical temperature",
                    default=5.0)
parser.add_argument("--isParal",
                    help="whether to use parallel computation codes",
                    action="store_true")

# read argument
args = parser.parse_args()
scheme = args.scheme
ver = args.ver
chi = args.chi
rg_n = args.rgn
iter_n = args.itern
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

pars = {"isZ2": True, "rg_n": rg_n,
        "chi": chi, "cg_eps": 1e-8, "display": False,
        "dataDir": None, "determPhase": True}

Tlow = args.Tlow
Thi = args.Thi

# find Tc
rg3d.findTc(iter_n, Tlow, Thi,
            scheme, ver,
            pars, outDir,
            comm=comm)
