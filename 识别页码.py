# encoding=gbk
def open_page(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()
def find_page_number(dict,n):
    list = dict['words_result']
    result = list[n]['words']
    #开始判断是否为页码
    sum = 0
    for i in result:
        try:
            if int(i) >= 0 and int(i) <= 9:
                sum *= 10
                sum += int(i)

        except:
            pass
    if sum==0:
        return -1
    else :
        return sum
if __name__ == '__main__':
    dicts=eval(open_page('result.txt'))
    n=0
    result=find_page_number(dicts,n)
    if result!=-1:
        print(result)
    elif result==-1:
        n=-1
        result=find_page_number(dicts,n)
        if result!=-1:
            print(result)
        else:
            print('未找到页码')


