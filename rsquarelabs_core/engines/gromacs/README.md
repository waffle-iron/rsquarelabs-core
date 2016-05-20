# R2_GROMACS

R2_GROMACS is the wrapper built around the gromacs (http://www.gromacs.org) - a molecular dynamics package.

## Terminology:
1. Protein - protein molecule, typically in *.pdb or *.gro formats
2. Ligand - typically drug molecule or in some cases other small protein or peptide that can bind to Protein molecule,
 typically in *.gro for this tool (it can be *.mol or *.sdf or more)
3. Topology file - contains the structure of the molecule (atomic positions ) mapped in cartesian coordinates, typically
in *.top format.
4. Ligand Topology - file ligand.itp generated from third party tools which will be included into the *.top file
5. *.mdp file - the confiration used to run the simulations


## Command from gromacs:
1. gmx pdb2gmx - Converts the input pdb file to gromacs file format(*.gro), using some forcefields and etc.
Read more at http://manual.gromacs.org/programs/gmx-pdb2gmx.html
Example Usage:  `gmx pdb2gmx  -f  protein.pdb -o protein.gro -ignh -p  topol.top -i posre.itp -ff gromos53a6 -water spc`

2. gmx editconf - Defines the unit cell for simulation to happen within
Read more at http://manual.gromacs.org/programs/gmx-edifconf.html
Example Usage: `gmx editconf -f complex.gro -o newbox.gro -bt dodecahedron -d 1.0`

3. gmx solvate - Solvates the unit cell with specified solution
Read more at http://manual.gromacs.org/programs/gmx-solvate.html
Example Usage: `gmx solvate -cp newbox.gro -cs spc216.gro -p topol.top -o solv.gro`
 
4. gmx grompp -  The gromacs preprocessor-  reads a molecular topology file, checks the validity of the files before running the simulation,
Read more at http://manual.gromacs.org/programs/gmx-grompp.html
Example Usage: `gmx grompp -f em.mdp -c solv.gro -p topol.top -o ions.tpr`

5. gmx genion - randomly replaces solvent molecules with monoatomic ions to neutralise or add charge to the system.
Read more at http://manual.gromacs.org/programs/gmx-genion.html
Example Usage: `gmx genion -s ions.tpr -o solv_ions.gro -p topol.top -pname NA -nname CL -nn 6`

6. gmx mdrun -  is the main computational chemistry engine within GROMACS. Obviously, it performs Molecular Dynamics simulations, 
but it can also perform Stochastic Dynamics, Energy Minimization, test particle insertion or (re)calculation of energies.
Read more at http://manual.gromacs.org/programs/gmx-mdrun.html
Example Usage: `gmx mdrun -v -deffnm em`

7. gmx genrestr - produces an #include file for a topology containing the three force constants for the x-, y-, and z-direction. 
This is used for positional restraining ie., fixing the molecule in a specific position with very less moment in x, y, z directions specified as force constants.
Read more at http://manual.gromacs.org/programs/gmx-genrestr.html
Example Usage: `gmx genrestr -f jz4.gro -o posre_jz4.itp -fc 1000 1000 1000`

8. 

 
