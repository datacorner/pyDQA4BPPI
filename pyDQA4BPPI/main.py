import pandas as pd
import sys
from report import Report
from datasource import DataSource

# First argument is the dataset file to check & validate
# Test with
# cd C:\Git\bppi\pibppidqa
# py DQA4BPPI.py InternationalDeclarations.csv id concept:name time:timestamp

def check_cols_in_dataset(ds_df, pfi, sn, t):
    pfi_ok = False
    sn_ok = False
    t_ok = False
    pot_attr = []
    error_msg = ""
    for col in ds_df.columns:
        if (col == pfi):
            pfi_ok = True
        if (col == sn):
            sn_ok = True
        if (col == t):
            t_ok = True
        else:
            pot_attr.append(col)
    if (not pfi_ok):
        error_msg = error_msg + "> ERROR: Timeline ID column has not been found.\n"
    if (not sn_ok):
        error_msg = error_msg + "> ERROR: Event ID column has not been found.\n"
    if (not t_ok):
        error_msg = error_msg + "> ERROR: Timestamp column has not been found."
    if (pfi_ok and sn_ok and t_ok):
        print("INFO> Potential attributes: ", pot_attr)
    return (pfi_ok and sn_ok and t_ok), error_msg

def colfreq_10first(ds_df, col):
    counts = ds_df[col].value_counts()[:10]
    colName = counts.index
    colFreq = counts
    res = pd.DataFrame(columns=["Column", "Frequency"])
    res["Column"] = colName
    res["Frequency"] = colFreq.values
    return res

if __name__ == "__main__":
    # Chack arguments
    if len( sys.argv ) != 5:
        print( "DQA For BPPI Report generator" )
        print( "\tusage: python3 DQA4BPPI.py <datasettocheck.csv> <PFI> <PS> <PT>" )
        exit()

    # Convert the file and create a new CSV file
    dataset_filename = sys.argv[1]
    pfi_key = sys.argv[2]
    ps_key = sys.argv[3]
    t_key = sys.argv[4]
    ds = DataSource(dataset_filename, pfi_key, ps_key, t_key)
    ds.open()
    if (ds.isOpened()):
        print ("INFO> Data Quality Check for the file <", dataset_filename, ">" )
    
    try:
        # Check if the 3 fields really exists in the dataset
        print ("INFO> Load dataset ...")
        dataset_df = pd.read_csv(dataset_filename)
        
        print ("INFO> Dataset loaded")
        check, error_message = check_cols_in_dataset(dataset_df, pfi_key, ps_key, t_key)
        
        if (check):
            print("INFO> DQA CHECK OK: The 3 mandatory fields/columns have been identified in the dataset")
            dataset_df_first10 = dataset_df.head(10)
            print("INFO> Display the firsts 10 records")
            print(dataset_df_first10)
        else:
            print(error_message)
            exit()
    except Exception as e:
        print ("ERROR> Error while opening the file, error ->", e)
    print ("\n")
    
    #Global counts on the dataset
    print ("INFO> Number of columns: ", dataset_df.shape[1])
    print ("INFO> Number of lines: ", dataset_df.shape[0])
    print ("\n")
    
    # Counts & freq distrib for the Timeline ID
    print ("INFO> Number of different values for <", pfi_key, ">",len(dataset_df[pfi_key].value_counts()))
    pfi_freq_df = colfreq_10first(dataset_df, pfi_key)
    print ("INFO> First 10 values for <", pfi_key, ">\n", pfi_freq_df) 
    print ("\n")
    
    # Counts & freq distrib for the Event ID
    print ("INFO> Number of different values for <", ps_key, ">",len(dataset_df[ps_key].value_counts()))
    ps_freq_df = colfreq_10first(dataset_df, ps_key)
    print ("INFO> First 10 values for <", ps_key, ">\n", ps_freq_df)
    print ("\n")
    
    