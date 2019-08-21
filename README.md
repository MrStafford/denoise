# denoise

It applies a medium filter to a csv file and generates a filtered data csv and both an unfiltered and filtered plot of the data.

## Requirements

1. Python3 (https://www.python.org/downloads/)

## Install

```bash
  git clone https://github.com/MrStafford/denoise.git
  cd denoise
  pip3 install -r requirements.txt
```

## Usage

1. Simplest example

```bash
  # inpout_path : must be a CSV file
  # output_path : must be a CSV file
  python3 denoise/denoise.py --input_path denoise/resources/P-SOI2.csv --output_path P-SOI2.csv
```

2. With dpi settings

```bash
  # dpi : int(200-2400)
  python3 denoise/denoise.py --input_path denoise/resources/P-SOI2.csv --output_path P-SOI2.csv --dpi 600
```

3. With window size settings

```bash
  # window_size : must be an odd number in the form of x, y
  python3 denoise/denoise.py --input_path denoise/resources/P-SOI2.csv --output_path P-SOI2.csv --window_size 3,3
```
