source /home/openbiosim/.conda/envs/openbiosim/bin/activate 

python -V

# Make sure we have the latest version
cd source && git pull && cd -

python source/actions/update_recipe.py

mkdir ./build

conda mambabuild -c conda-forge -c michellab/label/dev --croot ./build ./source/recipes/sire
