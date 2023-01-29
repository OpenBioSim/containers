
import platform
import shlex
import subprocess
import sys

if platform.machine() in ["arm64", "aarch64"]:
    cmd = "mamba install -y -n openbiosim -c 'openbiosim/label/dev' " \
          "biosimspace" # no ambertools, gromacs or plumed on linux/aarch64 " ambertools gromacs plumed"
else:
    cmd = "mamba install -y -n openbiosim -c 'openbiosim/label/dev' " \
          "biosimspace ambertools gromacs plumed"

subprocess.run(shlex.split(cmd), stdout=sys.stdout, stderr=sys.stderr)

subprocess.run(shlex.split("mamba clean -y --all"))
subprocess.run(shlex.split("rm -rf /home/openbiosim/.conda/pkgs/*"))
