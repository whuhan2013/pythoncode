import xlwt
import json

def load_data(file_path):
    f=open(file_path,"r")
    return json.load(f)

def write_to_xls(data):
    xls=xlwt.Workbook()
    sheet=xls.add_sheet("number")

    for i in range(len(data)):
        for j in range(len(data[i])):
            sheet.write(i,j,data[i][j])

    xls.save("numbeer.xls")


if __name__=='__main__':
    data=load_data("number.txt")
    write_to_xls(data)