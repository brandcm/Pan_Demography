#!/usr/bin/python3
# pan be model
import msprime
import os, sys, time

def usage():
    print("Usage: ./msp.py [options]")
    print("  where options may include:")
    print("  -r or --run: run simulation. Default: run")
    print("               DemographyDebugger")
    sys.exit(1)

do_simulation = False
for arg in sys.argv[1:]:
    if arg == "-r" or arg == "--run":
        do_simulation = True
    else:
        usage()

# time parameters in generations
Tbecnw = 75200
Tecnw = 39497.5
Tnw = 4563.02
Tec = 1338.41   
Tbeta = 20417.9  
Tepsilon = 669.205     

# population sizes, estimated by legofit except where noted
Nbecnw = 75353.2/2.0
Necnw = 31659.2/2.0
Nnw = 161827/2.0
Nec = 291883/2.0
Nb = 2214660/2.0
Ne = 292816/2.0
Nc = 36550 # from Prado-Martinez
Nn = 27750 # from Prado-Martinez
Nw = 927800/2.0

# admixture
mBeta = 0.00603518
mEpsilon = 0.21402

nchromosomes = 1000     # number of chromosomes
basepairs = 2e6   # number of nucleotides per chromosome
u_per_site = 1.5e-8 # mutation

# Recombination rate.  recomb is the probability of recombination
# between sites at opposite ends of the simulated sequence.
c = 1.2e-8 # rate per base pair per generation

# One haploid sample from each of 5 populations: all modern (b,e,c,n,w).
samples = [
    msprime.Sample(population=0, time=0),  # population b
    msprime.Sample(population=1, time=0),  # population e
    msprime.Sample(population=2, time=0), # population c
    msprime.Sample(population=3, time=0),  # population n
    msprime.Sample(population=4, time=0)  # population w
]

lbl = ("b", "e", "c", "n", "w")
npops = len(lbl)

# associate sample sizes with population labels
sampsize = {}
for s in lbl:
    sampsize[s] = 0

for samp in samples:
    ndx = samp.population
    assert ndx < len(lbl)
    assert lbl[ndx] in sampsize
    sampsize[lbl[ndx]] = 1

for s in lbl:
    if not (sampsize[s] > 0):
        print("Population %s has no samples" % s, file=sys.stderr)
        sys.exit(1)

# Population configurations. No sample sizes are listed here, because
# those are specified above in "samples".
popconf = [
    msprime.PopulationConfiguration(initial_size=Nb),
    msprime.PopulationConfiguration(initial_size=Ne),
    msprime.PopulationConfiguration(initial_size=Nc),
    msprime.PopulationConfiguration(initial_size=Nn),
    msprime.PopulationConfiguration(initial_size=Nw)
]

events = [
    msprime.MassMigration(
        time=Tepsilon,
        source=1,
        dest=4,
        proportion=mEpsilon), # w->e gene flow
    msprime.MassMigration(
        time=Tec,
        source=1,
        dest=2,
        proportion=1.0), # ec split
    msprime.PopulationParametersChange(
        time=Tec,
        initial_size=Nec,
        population_id=2),	# ec size change
    msprime.MassMigration(
        time=Tnw,
        source=3,
        dest=4,
        proportion=1.0), # nw split
    msprime.PopulationParametersChange(
        time=Tnw,
        initial_size=Nnw,
        population_id=4), # nw size change
    msprime.MassMigration(
        time=Tbeta,
        source=2,
        dest=0,
        proportion=mBeta), # b->ec gene flow
    msprime.MassMigration(
        time=Tecnw,
        source=2,
        dest=4,
        proportion=1.0), # ecnw split
    msprime.PopulationParametersChange(
        time=Tecnw,
        initial_size=Necnw,
        population_id=4), # ecnw size change
    msprime.MassMigration(
        time=Tbecnw,
        source=4,
        dest=0,
        proportion=1.0), # becnw split
    msprime.PopulationParametersChange(
        time=Tbecnw,
        initial_size=Nbecnw,
        population_id=0) # becnw size change
]

if do_simulation:
    # run simulation
    seed = int(time.time()) ^ os.getpid()
    sim = msprime.simulate(samples = samples,
                           population_configurations = popconf,
                           demographic_events = events,
                           length = basepairs,
                           recombination_rate = c,
                           mutation_rate = u_per_site,
                           num_replicates = nchromosomes,
                           random_seed = seed)

    # header
    print("npops = %d" % len(lbl))
    print("%s %s" % ("pop", "sampsize"))
    for s in lbl:
        print("%s %d" % (s, sampsize[s]))

    for i, chromosome in enumerate(sim):
        for variant in chromosome.variants():
            print(i, end=" ")
            for g in variant.genotypes:
                print(g, end=" ")
            print()

else:
    # Run demography debugger and quit
    dd = msprime.DemographyDebugger(
        population_configurations=popconf,
        demographic_events=events)
    dd.print_history()
    print("Use \"./sim -r\" to run simulation")
