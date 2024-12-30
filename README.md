#!/bin/bash

# Create and Activate Environment
conda create -n wineq python=3.12.2 -y
conda activate wineq

# Install Dependencies
pip install -r requirements.txt

# Initialize Git and DVC
git init
dvc init
dvc add data_given/winequality.csv

# Make Your First Commit
git add .
git commit -m "first commit"

# Update README in One Line
git add .; git commit -m "update Readme.md"


# Link to GitHub Repository
git remote add origin https://github.com/mayankmankar10/wine-mlops-project.git
git branch -M main
git push -u origin main
