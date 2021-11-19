This repository contains data, models, and scripts used to run analyses from
Brand et al. 2021, an analysis of Pan evolutionary history using nucleotide
site patterns.

- Most directories are named by the demographic model used in that analysis.
a = alpha, b = beta, c = gamma, d = delta, e = epsilon, f = zeta, g = eta,
and h = theta. Models that end in "2" have a younger divergence time for
the ancestor of eastern and central chimpanzees, whereas models that do 
not end in 2 have a younger divergence for the ancestor of Nigeria-Cameroon
and western chimpanzees. Instances of "r" reflect the model contains a
reversed direction of the introgression event occurring immediately before
the letter (e.g., br is the beta event in the reverse direction).

- Null and null2 are null demographic models containing no intrgression events

- Each model directory also contains either det and/or det_X directories.
det is a deterministic analysis of all the autosomes while det_X is a 
deterministic analysis of the X chromosome

- The final parameter estimates for each model can be found in b2.legofit.
The estimated bepe for the real data and the bootstraps can found in *.bepe.
Parameters for the real data and the bootstraps are listed in *.flat.

- msprime_sims contains a bias analysis for the best fitting autosomal model.
50 simulated site patterns from that demographic history are generated using 
msprime and then fit to the model using a deterministic analysis.

- pan.opf contains the tabulated site patterns and boot contains the bootstrap replicates

- Chr5, chr7, chr8, and chrX contain individual analyses of those site patterns

- pan.booma and pan_chrX.booma contain the weights for the tested autosomal and
X chromosome models, respectively

Notes:
- original eh2 directory was deleted, replacement in progress
