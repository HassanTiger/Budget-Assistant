'''
This program helps you read the csv file that you can download from BofA
'''
def main():
    file_name=input("Enter your csv file name: ")
    file= open(file_name,"r")
    transactions=[]
    for i in range(9):
        file.readline()
    
    for line in file:
        line= line.split(",")
        tran= line[2][1:len(line[2])-1]
        if not tran.isalpha():

            tran= (float(tran))
            transactions.append(tran)
            
        
    print("Total Spending:",sum(transactions))
    
    
main()