import argparse

# Set-up argument parser
parser = argparse.ArgumentParser(description='Model to prdict trip duration')

# Add parameters
parser.add_argument('--year', help='Enter datafile year (yyyy)')
parser.add_argument('--month', help='Enter datafile moth (mm)')

# Parse the command-line arguments
args = parser.parse_args()

# Access the parameter values
if args.year:
    print('Year:', args.year)

if args.month:
    print('Month:', args.month)

file = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_' + str(args.year) + '-' + str(args.month) + '.parquet'

print("File: ", file)
