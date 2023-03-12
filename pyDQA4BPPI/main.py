import sys
from report import Report
from datasource import DataSource

# First argument is the dataset file to check & validate
# Test with
# cd C:\Git\bppi\pibppidqa
# py DQA4BPPI.py InternationalDeclarations.csv id concept:name time:timestamp

if __name__ == "__main__":
    # Check arguments
    trace = Report()
    if len( sys.argv ) != 5:
        trace.info( "DQA For BPPI Report generator" )
        trace.info( "\tusage: python3 DQA4BPPI.py <datasettocheck.csv> <PFI> <PS> <PT>" )
        exit()

    # Convert the file and create a new CSV file
    dataset_filename = sys.argv[1]
    pfi_key = sys.argv[2]
    ps_key = sys.argv[3]
    t_key = sys.argv[4]
    ds = DataSource(dataset_filename, pfi_key, ps_key, t_key)
    
    ds.open()
    if (ds.isOpened()):
        trace.info ("Data Quality Check for the file <", dataset_filename, ">" )
    
    try:
        trace.info ("Dataset loaded")
        check, message = ds.checkColumns()
        trace.info(message)
        
        if (check):
            trace.info("DQA CHECK OK: The 3 mandatory fields/columns have been identified in the dataset")
            dataset_df_first10 = ds.head(10)
            trace.info("Display the firsts 10 records")
            print(dataset_df_first10)
        else:
            exit()
    except Exception as e:
        trace.error("Error while opening the file, error ->", e)
    print ("\n")
    
    #Global counts on the dataset
    print ("Number of columns: ", ds.colsCount())
    print ("Number of lines: ", ds.rowsCount())
    print ("\n")
    
    # Counts & freq distrib for the Timeline ID
    print ("Number of different values for <", pfi_key, ">", ds.countDiffValues(pfi_key))
    pfi_freq_df = ds.countDiffValues(pfi_key)
    print ("First 10 values for <", pfi_key, ">\n", pfi_freq_df) 
    print ("\n")
    
    # Counts & freq distrib for the Event ID
    print ("Number of different values for <", ps_key, ">", ds.countDiffValues(ps_key))
    ps_freq_df = ds.countDiffValues(ps_key)
    print ("First 10 values for <", ps_key, ">\n", ps_freq_df)
    print ("\n")
    
    