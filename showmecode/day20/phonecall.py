import xlrd

def phone_call(file_path):
    xls=xlrd.open_workbook(file_path)
    sheet=xls.sheet_by_index(0)

    minutes=0
    seconds=0

    for i in range(1,sheet.nrows):
        call = str(sheet.row_values(i)[3])
        print(call)
        if "分" in call:

            minute,second_phrase=call.split("分")
        else:

            minute=0
            second_phrase=call

        second,temp=second_phrase.split("秒")
        minutes+=int(minute)
        seconds+=int(second)

    return minutes,seconds


if __name__=='__main__':
    minutes,secondes=phone_call("2015年05月语音通信.xls")

    minutes+=secondes/60
    secondes=secondes%60

    print("通话时间总计：", minutes, "分", secondes, "秒")


