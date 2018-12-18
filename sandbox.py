import os
import csv
from collections import Counter



def main_func():
    base_folder = os.path.dirname(__file__)
    file_path = os.path.join(base_folder, 'Days37-39CSVData/thanksgiving2015_copy.csv')
    
    us_regions = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            if row.get('US Region') not in us_regions:
                us_regions.append(row.get('US Region'))
        
        print(us_regions)
        
        for row in reader:
            print(row)



            

        


            
            
            
            
#        if row.get('US Region') == 'Pacific':
#                #print all main dishes
#                if row.get('main_dish') == 'Turkey':
#                    example.append(row.get('turkey_cooked?'))
##                    if row.get('turkey_cooked?') not in example:
##                        example.append(row.get('turkey_cooked?'))
##                if row.get('main_dish') not in example:
##                    example.append(row.get('main_dish'))
#        results = Counter(example)
#        print("The most common way to cook a Turkey is", results.most_common(1))
        


              

                





main_func()

                
                



                        
                        
                        
        
    

        
        

        


    
    