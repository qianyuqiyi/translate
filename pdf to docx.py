from pdf2docx import Converter  #调用pdf2docx库
pdf_file=input("请输入pdf文件的路径")  #选择pdf文件路径
docx_file=input("请输入生成docx文件的路径")  #选择转成docx文件的路径
cv=Converter(pdf_file)
cv.convert(docx_file,start=0,end=None)
cv.close()