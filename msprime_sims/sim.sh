# msp_pan.py is a Python script that executes msprime and generates output
# in the "sim" format, which is described in the document of simpat,
# within the Legofit package.  simpat is a program that reads sim
# format and tabulates site patterns.
ofile=sim${1}.opf
efile=sim${1}.err
python3 msp_pan.py -r | simpat 1>${ofile} 2>${efile}
