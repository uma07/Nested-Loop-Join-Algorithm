# Implementation of the nested loop join algorithm, given 2 text files containing records of 2 tables.

# RUN : python nested_join.py <left_table> <right_table> <column_number> <output_file>




import sys
import csv



if len(sys.argv) < 5:
    print("SORRY !!! You should be entering 5 arguments\n")
    print("python nested_join.py <left_table> <right_table> <column_number> <output_file>")
    sys.exit(1)

left = sys.argv[1]
right = sys.argv[2]
col = int(sys.argv[3])
output = sys.argv[4]



with open(output,"w") as out:
    writer = csv.writer(out)
    
    with open(left) as file1:
        with open(right) as file2:
            r1 = csv.reader(file1)
            r2 = csv.reader(file2)
            l1 = next(r1)
            l2 = next(r2)
            l = l1+l2
            writer.writerow(l)
            
            for row1 in r1:
                r2 = csv.reader(file2)
                
                for row2 in r2:
                    if(row1[col] == row2[col]):
                        row = row1+row2
                        writer.writerow(row)
                        
                file2.seek(0)
                file2.readline()


