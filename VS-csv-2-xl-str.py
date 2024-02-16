#!/usr/bin/env python3

import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
from rdkit.Chem import Descriptors
from rdkit.Chem import PandasTools
from rdkit import RDConfig
import os, sys
import xlsxwriter

## Headers
####################################################################
#  Prepare the final hit list from SD files for virtual screening  #
#  Computational Biophysics & Drug Design (Kireev lab)             #
#  Developed by Xiaowen Wang                                       #
####################################################################

inputfile = sys.argv[1]
outputfile = sys.argv[2]

df = pd.read_csv(inputfile)

#print([str(x) for x in df.columns])
#print(df)

PandasTools.AddMoleculeColumnToFrame(df,'SMILES','Mole',includeFingerprints=True)
PandasTools.SaveXlsxFromFrame(df,outputfile, molCol='Mole', size=(250,250))
