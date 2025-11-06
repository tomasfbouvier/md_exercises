from ovito.io import *
from ovito.modifiers import *
from ovito.data import *
from ovito.pipeline import *

# Data import:
pipeline = import_file('G_C', atom_style = 'atomic')


data=pipeline.compute()


export_file(pipeline, "final.data", "lammps/dump",
    columns = ["Particle Identifier", "Position.X", "Position.Y", "Position.Z"])
