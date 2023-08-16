# CISA KEV Vulnerability Heatmap

This Python script generates a heatmap chart of the Cybersecurity and Infrastructure Security Agency (CISA) Known Exploited Vulnerabilities (KEV) data.

## Heatmap example
![image](https://github.com/iamthefrogy/cisa-kev-heatmap/assets/8291014/2d9f7a4e-b875-4ac6-8a96-ea12c57bac2d)

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

2. Download and prepare your CISA KEV vulnerability in CSV format and put that into the same location where your script is - https://www.cisa.gov/known-exploited-vulnerabilities-catalog

3. Run the script.
```bash
python3 heatmap.py
```

## Output
The script will generate a heatmap.pdf chart and save it in the current directory.
