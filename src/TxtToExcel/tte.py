import xlwt

txt_data=[]
with open("../test/更新1/3010 携程纯评论(纯评论)2020.3.3.txt",'r',encoding='utf-8')as f:
    txt_data=f.readlines()

print('创建表格')    
myBook=xlwt.Workbook(encoding="utf-8")
mySheet=myBook.add_sheet('去哪儿评论')    

print('表格创建成功，正在写入表格~~~~')   
for i in range(0,len(txt_data)):   

    mySheet.write(i,0,txt_data[i])
     
myBook.save('../test/更新1/3010 携程纯评论(纯评论)2020.3.3.xls')





