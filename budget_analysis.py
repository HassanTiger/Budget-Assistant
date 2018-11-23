'''
This program helps you read the csv file that you can download from BofA
SEARCH FOR: #enter the name of transaction you looking for
'''
def main():
    helper= open("README.md", 'r')
    helper_file= helper.readlines()
    transactions_dictionary= load_file()
    print("Total Spending:",sum(transactions_dictionary.values()))
    while True: 
        order= input("Other Inqueries: ")
        if order.startswith("SEARCH FOR"):
            search_for(transactions_dictionary, order)
        elif order.startswith("HIGHEST"):
            highest_tran(transactions_dictionary, order)
        elif order.startswith("HELP"):
            print(helper_file)

    
    
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
            if line[1] in transactions_dictionary.keys():
                transactions_dictionary[line[1]]+= tran
            else:
                transactions_dictionary[line[1]]= tran
    return transactions_dictionary

def search_for(my_dict, order):
    sentence= order.strip().split("FOR")
    return my_dict[sentence[2].strip()]
    
def highest_tran(tran_dict, order):
    sentence= order.strip().split(" ")
    for i in range(sentence[1]):
        highest= min(tran_dict.values())
        for keys, values in tran_dict.items():
            if values== highest:
                high= keys + " with a value of "+ str(highest)
                del tran_dict[keys]
                return high
main()
