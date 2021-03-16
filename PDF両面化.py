import os
import sys
import io
import datetime

import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait

#だみぃページ作る
def dummy_page():
	buffer = io.BytesIO()
	# A4の新規PDFファイルを作成
	page = canvas.Canvas(buffer, pagesize=portrait(A4))
	
	# 文字書き込み
	page.setFillColorRGB(255,255,255)
	page.drawString(0,0,"dummy")
	# PDFファイルとして保存
	page.save()
	buffer.seek(0)
	return PyPDF2.PdfFileReader(buffer).getPage(0)

#メイン
def main(sourcefile):
	print("開始")

	filename = os.path.basename(sourcefile)
	filedir = os.path.dirname(sourcefile)
	file_size = os.path.getsize(sourcefile)
	
	print(sourcefile)
	print(filename)
	print(filedir)
	print(file_size)

	#出力ファイル名設定
	now = datetime.datetime.now()
	now_str = now.strftime("%Y%m%d%H%M%S")
	out_filename = "両面印刷用" + now_str + "_" + filename
	out_file = os.path.join(filedir,out_filename)
	print(out_file)
	
	dummy = dummy_page()
	
	writer = PyPDF2.PdfFileWriter()
	reader = PyPDF2.PdfFileReader(sourcefile)
	pages = reader.getNumPages()
	
	#ページ数分だみぃページを追加する
	for i in range(pages):
		page = reader.getPage(i)
		writer.addPage(page)
		writer.addPage(dummy)
	
	#ファイル保存
	with open(out_file,"wb") as f:
		writer.write(f)

#プログラム実行
if __name__ == "__main__":
	#ファイル入力
	if len(sys.argv) == 1:
		sourcefile = "6danshinseisyo.pdf"

	else:
		sourcefile = sys.argv[-1]

	main(sourcefile)
