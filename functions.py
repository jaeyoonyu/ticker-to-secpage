def ticker_to_cik (ticker, csv_file= 'tick_cik.csv'):
    """
    get CIK from tic_cik.csv, which is generated from save_tic_cik_csv.ipynb   
    """

    import csv
    with open(csv_file) as f:
        reader= csv.reader(f)
        for row in reader:
            if row[0]==ticker.lower():
                cik= row[1]
                return cik



def ticker_to_sec (key):
    """
    get sec-webpage from ticker
    """    
    import re
    if key=="":
        return
    # get cik if key is ticker.
    if re.search(r'[a-zA-Z]', key):
        cik= ticker_to_cik(key)        
        # if no cik is found, skip the rest of the function.
        if cik==None:
            return                
    else:
        cik= key
    firm_url= rf"https://www.sec.gov/cgi-bin/browse-edgar?CIK={cik}&count=100&owner=exclude"
    return firm_url