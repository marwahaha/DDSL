#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import os
import csv
import numpy as np

print('Now processing CFD data...')

# Process data
def process_airfoil_data(directory='Rectangle Test'):
    '''
    Get airfoil shape from preprocessed numpy files and CFD
    information from webscraped csv files.
    Files are retrieved from the airfoil-data directory by default.
    Output is a pandas dataframe containing the following information:
    - Case name
    - Rectangle shape
    - Aspect Ratio
    '''
    
    # Initialize lists
    ar_list=[]
    case_list=[]
    casedir_list=[]



    # Go through files
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath=os.path.join(root, file)

            # Get airfoil directory to retrieve numpy files later
            casedir=root.replace(directory+'/', '') # Get folder name to get airfoil shape numpy file name
            for index in range(len(file)):
                if file[index] == '_':
                    name_cut = index
                    break
            
            case_name = file[0:4] + file[5:name_cut]
            
            casedir_list.append(casedir)
            case_list.append(case_name)
            ar_list.append(float(file[name_cut+7:len(file)-4]))
            print(file[name_cut+7:len(file)-4])
            
            

    # Notify that all files have been processed
    print('All files processed!')
    print('Creating dataframe...')

    # Initialize dataframe
    airfoil_df=pd.DataFrame(columns=['Name','Directory','AR'])

    # Add data lists to dataframe
    airfoil_df['Name']=case_list
    airfoil_df['Directory']=casedir_list
    airfoil_df['AR']=ar_list

    # Notify that dataframe has been created
    print('Dataframe created!')

    return airfoil_df


# Fix data types in dataframe
def fix_df_dtypes(airfoil_df, datatypes=['str', 'str', 'float']):
    # Fix data types
    airfoil_df['Name']=airfoil_df['Name'].astype(datatypes[0])
    airfoil_df['Directory']=airfoil_df['Directory'].astype(datatypes[1])
    airfoil_df['AR']=airfoil_df['AR'].astype(datatypes[2])


    return airfoil_df


def normalize_data(csv_file):
    norm_csv_file=csv_file.replace('.csv', '')+'_normalized.csv'
    mstd_csv_file=csv_file.replace('.csv', '')+'_mean_std.csv'

    df=pd.read_csv(csv_file).drop('Unnamed: 0', axis=1)
    variables=['AR']
    mean=df.loc[:, variables].mean()
    std=df.loc[:, variables].std()
    df.loc[:, variables]=(df.loc[:, variables]-mean)/std
    df.to_csv(norm_csv_file)

    df=pd.DataFrame({'mean':mean, 'std':std})
    df.to_csv(mstd_csv_file)


# Run process airfoil data function
airfoil_df=process_airfoil_data()

# Run fix data types function
airfoil_df=fix_df_dtypes(airfoil_df)
airfoil_df.dtypes

# Save dataframe
airfoil_df.to_csv('processed_data/airfoil_data.csv')

# Create normalized data csv and save mean and standard deviation values
normalize_data('processed_data/airfoil_data.csv')
