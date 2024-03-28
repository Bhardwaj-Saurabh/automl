import pandas as pd
import os

def clean_dataframe(df, save=False, save_path=None):
    """
    Cleans the DataFrame based on specified criteria and optionally saves the cleaned DataFrame:
    1. Deletes columns where more than 95% of the values are unique or the same.
    2. Drops any column with more than 80% missing values.
    3. Deletes duplicate rows.
    
    Parameters:
    - df: pandas.DataFrame to be cleaned.
    - save: Boolean indicating whether to save the cleaned DataFrame.
    - save_path: Path (including filename) where the cleaned DataFrame should be saved.
    
    Returns:
    - Cleaned pandas.DataFrame.
    """
    
    # Copy the dataframe to avoid modifying the original
    df_cleaned = df.copy()
    
    # Calculate the threshold for unique/same values and missing values
    unique_threshold = len(df) * 0.95
    missing_threshold = len(df) * 0.8
    
    # 1. Delete columns with more than 95% unique or same values
    for column in df.columns:
        # Count of unique values
        n_unique = df[column].nunique(dropna=False)
        # Check if unique values are more than 95% or if a single value occupies more than 95%
        if n_unique > unique_threshold or n_unique <= 1:
            df_cleaned.drop(columns=[column], inplace=True)
    
    # 2. Drop columns with more than 80% missing values
    df_cleaned.dropna(axis=1, thresh=missing_threshold, inplace=True)
    
    # 3. Delete duplicate rows
    df_cleaned.drop_duplicates(inplace=True)
    
    # Save the cleaned DataFrame if requested
    if save and save_path:
        # Ensure the directory exists; if not, create it
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        # Save the DataFrame
        df_cleaned.to_csv(save_path, index=False)    
    return df_cleaned
