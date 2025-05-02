from tempfile import gettempdir

import biotite.database.rcsb as rcsb
import biotite.structure.io as strucio

# Download and parse file
file = rcsb.fetch("3vkh", "cif", gettempdir())
atom_array = strucio.load_structure(file)
