# CISA KEV Vulnerability Heatmap

This Python script generates a heatmap chart of the Cybersecurity and Infrastructure Security Agency (CISA) Known Exploited Vulnerabilities (KEV) data.

## Heatmap example
![2023-08-16 07_02_37-heatmap pdf - Brave](https://github.com/iamthefrogy/CISA-KEV-Heatmap-Generator/assets/8291014/d7657bfd-dd06-4ed0-82f3-ca7de75851e9)

## Prerequisites

The script requires the following Python packages to be installed:

- `numpy`
- `matplotlib`
- `pandas`
- `seaborn`

You can install these packages using the following command:

```bash
pip install numpy matplotlib pandas seaborn
```

## Usage
1. Clone Repository

```bash
git clone https://github.com/iamthefrogy/CISA-KEV-Heatmap-Generator.git
cd CISA-KEV-Heatmap-Generator
```

2.Download and prepare your CISA KEV vulnerability in CSV format and put that into the same location where your script is - https://www.cisa.gov/known-exploited-vulnerabilities-catalog

3. Run the script.
```bash
python3 heatmap.py
```

## Output
The script will generate a heatmap.pdf chart and save it in the current directory.
