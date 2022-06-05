import csv
import re
import pandas as pd 
  
# reading the csv file 
# df = pd.read_csv("AllDetails.csv") 
  
# updating the column value/data 
# df.loc[5, 'Name'] = 'SHIV CHANDRA'
  
# writing into the file 
# df.to_csv("AllDetails.csv", index=False) 

def reader_csv(xl_file):
 
    with open(xl_file) as csv_file:
        csv_reader = csv.reader(csv_file)
        # to_csv_file = csv.writer(csv_file)
        count = 0
       
        for row in csv_reader:
            if count == 0:
                headers = row
                count +=1 
                print(headers)
            else:
                cand_name = row[0]
                object_id = row[1]
                doc_name = row[2]
                cloud_drop = row[3]
                doc_type = row[4]
                note = row[5]

                id = object_id
                
                while id == object_id:

                    if doc_name == 'Mumps' and (cloud_drop !=0 or doc_type == "Medical"):

                        txt = "Refer to Mumps"
                        for each_row in row :
                            ["".join(each_row), row.replace(note,txt)]
                            print(row)
                

       
        # print(unique_usa)
        # print(unique_canada)
        # for el in unique_usa:
        #     print(f"usa {el} = {events_usa.count(el)}")

        # for el in unique_canada:
        #     print(f"canada {el} = {events_canada.count(el)}")       
           
            
if __name__ == "__main__":
    # xl_file = "/Users/serg/Downloads/October.csv"
    # xl_file = "/Users/serg/Downloads/November.csv"
    # xl_file = "/Users/serg/Downloads/December.csv"
    # xl_file = "/Users/serg/Downloads/January.csv"
    # xl_file = "/Users/serg/Downloads/Transactions.csv"
    xl_file = "/medical.csv"
    reader_csv(xl_file)