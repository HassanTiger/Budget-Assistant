'''
This program helps you read the csv file that you can download from BofA
'''
def main():
    transactions_dictionary= load_file()
    print("Total Spending:",sum(transactions_dictionary.values()))
    
    high_times= int(input("Enter the number of high transactions you want to see: "))
    for i in range(high_times):
        print("highest transaction is:", highest_tran(transactions_dictionary))
    
    
def load_file():
    file_name=input("Enter your csv file name: ")
    file= open(file_name,"r")
    transactions_dictionary={}
    for i in range(9):
        file.readline()
    
    for line in file:
        line= line.split(",")
        tran= line[2][1:len(line[2])-1]
        if not tran.isalpha():

            tran= (float(tran))
            transactions_dictionary[line[1]]= tran
    return transactions_dictionary


def highest_tran(tran_dict):
    highest= min(tran_dict.values())
    for keys, values in tran_dict.items():
        if values== highest:
            high= keys + " with a value of "+ str(highest)
            del tran_dict[keys]
            return high
main()
