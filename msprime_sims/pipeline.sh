#!/bin/bash

# Slurm pipeline.  sbatch returns a string of form "Submitted batch
# job 123456". We only want the last word in this string. The sbatch
# steps below initially set a variable equal to the entire
# string. Then we extract the last word with a command like j1=${j1##*
# }. The syntax here is obscure to me but seems to work.

export SBATCH_ACCOUNT=rogersa-kp
export SBATCH_PARTITION=rogersa-kp

# Stage 1 of analysis.
j2=$(sbatch --array=0-49 a1boot.slr)
j2=${j2##* }

# Stage 2 of analysis.
j4=$(sbatch --dependency=afterok:$j2 --array=0-49 a2boot.slr)
j4=${j4##* }

# Rewrite .lgo file in terms of principal components. This makes
# file b.lgo.
j5=$(sbatch --dependency=afterok:$j4 pclgo.slr)
j5=${j5##* }

# Stage 1 for model b
j7=$(sbatch --dependency=afterok:$j5 --array=0-49 b1boot.slr)
j7=${j7##* }

# Stage 2 for model b
sbatch --dependency=afterok:$j7 --array=0-49 b2boot.slr
