# import libraries
import pickle
import pandas as pd
import numpy as np
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



# get model
with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

categorical = ['PULocationID', 'DOLocationID']

# read inpput file and set-up dataframe
def read_data(filename):
    print("Reading file: ", filename)
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df

# input read data into dataframe
file = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_' + str(args.year) + '-' + str(args.month) + '.parquet'
df = read_data(file)

# train model
dicts = df[categorical].to_dict(orient='records')
X_val = dv.transform(dicts)

# make prediction
y_pred = model.predict(X_val)

print("Standard deviation:", np.std(y_pred))
print("Mean: ", np.mean(y_pred))
