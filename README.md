This repository contains data, models, and scripts used to run analyses on
Pan evolutionary history using nucleotide site patterns by Brand, White, Rogers,
and Webster.

- Most directories are named by the demographic model used in that analysis.
a = alpha, b = beta, c = gamma, d = delta, e = epsilon, f = zeta, g = eta,
and h = theta. Models that end in "2" have a younger divergence time for
the eastern and central chimpanzee most recent common ancestor (MRCA), whereas 
models that do not end in 2 have a younger Nigeria-Cameroon and western chimpanzee
MRCA. Instances of "r" reflect the model contains a reversed direction of the 
introgression event occurring immediately before the letter (e.g., br is the 
beta event in the reverse direction).

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

- chr5, chr7, chr8, and chrX contain individual analyses of those site patterns

- pan.booma and pan_chrX.booma contain the weights for the tested autosomal and
X chromosome models, respectively

- figure_generation_and_model_correlation contains the code and data necessary
to generate most of the manuscript figures and run a correlation between
autosomal and X chromosome model ranks. The other manuscript figures are demographic
models and were generated in Inkscape.
