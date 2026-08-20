# Pearson Correlation Matrix Calculator

![CI](https://github.com/Dezerdvs/higher-math-stats-python/actions/workflows/ci.yml/badge.svg)

A small statistics utility that loads a CSV dataset and computes the **Pearson correlation coefficient** between every pair of numeric columns.

## What it does

- Loads a CSV file with `pandas`
- Cleans up numbers that use a comma as the decimal separator (common in European-locale exports)
- Computes and prints the full pairwise Pearson correlation matrix using `pandas`/`scipy`

## Tech stack

Python, `pandas`, `scipy`.

## Running

```bash
pip install pandas scipy
python Pirson.py
```

> Note: update the `file_path` variable at the top of the script to point at your own CSV file before running.

## Why it matters

Correlation analysis is a standard first step in exploratory data analysis / statistics coursework — this script automates it for any tabular numeric dataset.
