#!/bin/bash

# Create and Activate Environment
'''bash
conda create -n wineq python=3.12.2 -y
'''

'''bash
conda activate wineq
'''
# Install Dependencies
'''bash
pip install -r requirements.txt
'''

# Initialize Git and DVC
'''bash
git init
'''
'''bash
dvc init
'''
'''bash
dvc add data_given/winequality.csv
'''

# Make Your First Commit
'''bash
git add .
'''
'''bash
git commit -m "first commit"
'''

# Update README in One Line
'''bash
git add .; git commit -m "update Readme.md"
'''

# Link to GitHub Repository
'''bash
git remote add origin https://github.com/mayankmankar10/wine-mlops-project.git
'''
'''bash
git branch -M main
'''
'''bash
git push -u origin main
'''

