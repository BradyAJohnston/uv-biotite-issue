from tempfile import gettempdir

import biotite.database.rcsb as rcsb
import biotite.structure.io as strucio
from biotite import structure as struc


def test_example():
    # Download and parse file
    file = rcsb.fetch("3vkh", "cif", gettempdir())
    array = strucio.load_structure(file)
    array.bonds = struc.bonds.connect_via_residue_names(array, inter_residue=True)
