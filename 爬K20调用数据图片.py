import pypyodbc,openpyxl
import pandas as pd,re,time,os,pyperclip
import requests
import xlwt
import json
import random
from retrying import retry
#http://fund.eastmoney.com/fundguzhi.html
from shutil import copyfile
from zichuan import duxiebiao
def fiddle获取json数据():
    c1 = zichuan.huoquzhantieshuju()
    c =[]
    for x in c1:
        x = x.replace('Key: ','').replace(' Value: ','')
        x = x.split(';')
        c.append(f"'{x[0]}' :'{x[1]}'")
    pyperclip.copy(',\n'.join(c))
def main():	
	st = pd.read_excel(r'E:\er\py\v20查数据\V20产品库\K20调用目录.xlsx')
	# st = st.loc[st.dir4.apply(lambda a : 'D四列' in a)].loc[st.status.apply(lambda a : 1== a)][['modelno','pic','mirror_pic']]
	st = st.loc[st.dir3.apply(lambda a : '2吊柜' in a)].loc[st.status.apply(lambda a : 1== a)][['modelno','pic','mirror_pic']]
	
	# st = st.loc[st.modelno.apply(lambda a : 'ZC' in a)]
	# print(st)
	# assert()
	# st = pd.read_excel(r'E:\er\py\v20查数据\V20产品库\背景墙调用.xlsx')
	# st = st.loc[st.modelno.apply(lambda a : 'QAA-B002' in a)][['modelno']]
	for x in range(0,st.shape[0]):

		# try:
		baseurl=f'https://wsaiosscdn.yfway.com/ws-kitsys/WardrobeSun/release/kitproduct/preview/removedoor/{st.iloc[x,0].lower()}.jpg'
		# baseurl=f'https://wsaiosscdn.yfway.com/ws-kitsys/WardrobeSun/release/kitproduct/preview/{st.iloc[x,0].lower()}.jpg'
		
		# baseurl=st.iloc[x,1]
		# print(baseurl)
		response = requests.get(baseurl,headers=headers)
		# print(response.status_code)
		# print(response.content)
		if response.status_code ==404:
			# copyfile(os.path.join(r'E:\er\33\覆盖包\kitproduct\preview',x+'.jpg'),os.path.join(r'E:\er\py\v20门板图片\图片',x+'.jpg'))
			print(st.iloc[x,0])
		response= response.content
		with open(f'preview\\{st.iloc[x,0].lower()}.jpg', 'wb') as f: # 打开文件
			f.write(response)

		with open(f'preview\\removedoor\\{st.iloc[x,0].lower()}.jpg', 'wb') as f: # 打开文件
			f.write(response)
		# except:
		# 	print(st.iloc[x,0])
@retry(stop_max_attempt_number=3) 
def getdata(baseurl):
	user_agent_list = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36']
	
	
	
	response = requests.get(baseurl,headers=headers)
	#response = requests.post(baseurl,data=data,headers=headers)
	# print(response.url)
	# print(type(response))
	# print(response.status_code)
	# print(type(response.text))
	# print(response.json())
	#print(response.text)
	response.encoding="gbk"
	if response.status_code == 200:
		with open("123.txt","w",encoding="gbk") as f:
			f.write(str(response.text))
		return response.text
def getdata1(baseurl,x1,x2):
	user_agent_list = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36']
	
	headers = {
	"User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
	"authorization":"bearereyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvengwMTA4LWRldmVsb3AueWZ3YXkuY29tXC9hcGlcL3VzZXJcL2xvZ2luIiwiaWF0IjoxNjI3ODkyOTU0LCJleHAiOjE2Mjc5NzkzNTQsIm5iZiI6MTYyNzg5Mjk1NCwianRpIjoiVmFBRGN1Nm9jNXdOanp3YSIsInN1YiI6NywicHJ2IjoiODdlMGFmMWVmOWZkMTU4MTJmZGVjOTcxNTNhMTRlMGIwNDc1NDZhYSIsInBpZCI6ODJ9.HmXM_n8XDZP6JAfPurnZ5FEBfZk9iWX9K_vBUWRgHfo"
		}
	data = {} #,params=data
	params= {
	'doorstyle':f'系统柜门\\{x1}\\{x2}\\\\\\',
	}
	response = requests.get(baseurl,headers=headers,params=params)
	#response = requests.post(baseurl,data=data,headers=headers)
	# print(response.url)
	# print(type(response))
	# print(response.status_code)
	# print(type(response.text))
	# print(response.json())
	#print(response.text)
	if response.status_code == 200:
		with open("123.txt","w",encoding="utf-8") as f:
			f.write(str(response.text))
		return response.json()
def main22():	

	# print(st)
	# assert()
	# st = pd.read_excel(r'E:\er\py\v20查数据\V20产品库\背景墙调用.xlsx')
	# st = st.loc[st.modelno.apply(lambda a : 'QAA-B002' in a)][['modelno']]
	for x in os.listdir(r'E:\er\py\v20门板图片\preview'):

		# try:
		# baseurl=f'https://wsaiosscdn.yfway.com/ws-kitsys/WardrobeSun/release/kitproduct/preview/removedoor/{st.iloc[x,0].lower()}.jpg'
		baseurl=f'https://wsaiosscdn.yfway.com/ws-kitsys/WardrobeSun/release/kitproduct/preview/{x}'
		
		# baseurl=st.iloc[x,1]
		# print(baseurl)
		response = requests.get(baseurl,headers=headers)
		# print(response.status_code)
		# print(response.content)
		if response.status_code ==404:
			# copyfile(os.path.join(r'E:\er\33\覆盖包\kitproduct\preview',x+'.jpg'),os.path.join(r'E:\er\py\v20门板图片\图片',x+'.jpg'))
			print(x)
		response= response.content
		# with open(f'preview\\{st.iloc[x,0].lower()}.jpg', 'wb') as f: # 打开文件
		# 	f.write(response)
		
		with open(f'preview\\removedoor\\{x}', 'wb') as f: # 打开文件
			f.write(response)
		# except:
		# 	print(st.iloc[x,0])
def main33():	

	# print(st)
	# assert()
	# st = pd.read_excel(r'E:\er\py\v20查数据\V20产品库\背景墙调用.xlsx')
	# st = st.loc[st.modelno.apply(lambda a : 'QAA-B002' in a)][['modelno']]
	for x in os.listdir(r'E:\er\py\v20门板图片\preview\removedoor'):

		# try:
		# baseurl=f'https://wsaiosscdn.yfway.com/ws-kitsys/WardrobeSun/release/kitproduct/preview/removedoor/{st.iloc[x,0].lower()}.jpg'
		baseurl=f'https://wsaiosscdn.yfway.com/ws-kitsys/WardrobeSun/release/kitproduct/preview/removedoor/{x}'
		
		# baseurl=st.iloc[x,1]
		# print(baseurl)
		response = requests.get(baseurl,headers=headers)
		# print(response.status_code)
		# print(response.content)
		if response.status_code ==404:
			# copyfile(os.path.join(r'E:\er\33\覆盖包\kitproduct\preview',x+'.jpg'),os.path.join(r'E:\er\py\v20门板图片\图片',x+'.jpg'))
			print(x)
		response= response.content
		# with open(f'preview\\{st.iloc[x,0].lower()}.jpg', 'wb') as f: # 打开文件
		# 	f.write(response)
		
		with open(f'preview\\{x}', 'wb') as f: # 打开文件
			f.write(response)
		# except:
		# 	print(st.iloc[x,0])
def main222():	#爬取背景墙
	a3 =pyperclip.paste().split("\n")
	for x in range(0,len(a3)):
	    if '\r' in a3[x]:
	        a3[x] = a3[x].replace('\r','')
	for x in a3[:]:
	    if '' == x:
	        a3.remove(x)
	# print(st)
	# assert()
	# st = pd.read_excel(r'E:\er\py\v20查数据\V20产品库\背景墙调用.xlsx')
	# st = st.loc[st.modelno.apply(lambda a : 'QAA-B002' in a)][['modelno']]
	for x in a3:
	# for x in ['YABB3-A003A', 'YABB4-A003A', 'YABB5-A003A', 'YABA3-A005Y', 'YABA3-A007Y', 'YABA3-A009Y', 'YABA4-A005Y', 'YABA5-A009Y', 'YABA4-A007Y', 'YABA4-A009Y', 'YABA5-A005Y', 'YABA5-A007Y', 'YABA3-A003A', 'YABA4-A003A', 'YABA5-A003A', 'YAAB3-A011', 'YAAB4-A009', 'YAAB5-A007', 'YAAB5-A009', 'YAAB6-A007', 'YAAA3-A013Y', 'YAAA3-A015Y', 'YAAA3-A017Y', 'YAAA4-A011Y', 'YAAA4-A013Y', 'YAAA4-A015Y', 'YAAA5-A011Y', 'YAAA5-A013Y', 'YAAA5-A015Y', 'YAAA6-A009Y', 'YAAA6-A011Y', 'YAAA6-A013Y', 'YAAA3-A011', 'YAAA4-A009', 'YAAA5-A007', 'YAAA5-A009', 'YAAA6-A007', 'YABB3-A004A', 'YABB4-A004A', 'YABB5-A004A', 'YABA3-A006Y', 'YABA3-A008Y', 'YABA3-A010Y', 'YABA4-A006Y', 'YABA5-A010Y', 'YABA4-A008Y', 'YABA4-A010Y', 'YABA5-A006Y', 'YABA5-A008Y', 'YABA3-A004A', 'YABA4-A004A', 'YABA5-A004A', 'YAAB3-A012', 'YAAB4-A010', 'YAAB5-A008', 'YAAB5-A010', 'YAAB6-A008', 'YAAA3-A014Y', 'YAAA3-A016Y', 'YAAA3-A018Y', 'YAAA4-A012Y', 'YAAA4-A014Y', 'YAAA4-A016Y', 'YAAA5-A012Y', 'YAAA5-A014Y', 'YAAA5-A016Y', 'YAAA6-A010Y', 'YAAA6-A012Y', 'YAAA6-A014Y', 'YAAA3-A012', 'YAAA4-A010', 'YAAA5-A008', 'YAAA5-A010', 'YAAA6-A008']:

		# try:
		# baseurl=f'https://wsaiosscdn.yfway.com/ws-kitsys/WardrobeSun/release/kitproduct/preview/removedoor/{st.iloc[x,0].lower()}.jpg'
		baseurl=f'https://wsaiosscdn.yfway.com/ws-kitsys/WardrobeSun/release/kitproduct/preview/{x.lower()}.jpg'
		
		# baseurl=st.iloc[x,1]
		# print(baseurl)
		response = requests.get(baseurl,headers=headers)
		# print(response.status_code)
		# print(response.content)
		if response.status_code ==404:
			print(x)
		response= response.content
		with open(f'preview\\{x.lower()}.jpg', 'wb') as f: # 打开文件
			f.write(response)
		baseurl=f'https://wsaiosscdn.yfway.com/ws-kitsys/WardrobeSun/release/kitproduct/preview/removedoor/{x.lower()}.jpg'
		response = requests.get(baseurl,headers=headers)
		if response.status_code ==404:
			print(x)
		response= response.content
		with open(f'preview\\removedoor\\{x.lower()}.jpg','wb') as f: # 打开文件
			f.write(response)
def main223():	#根据型号找图片

	# print(st)
	# assert()
	# st = pd.read_excel(r'E:\er\py\v20查数据\V20产品库\背景墙调用.xlsx')
	# st = st.loc[st.modelno.apply(lambda a : 'QAA-B002' in a)][['modelno']]
	# for x in os.listdir(r'E:\wps\WeChat Files\wxid_17o69gjxn9t722\FileStorage\File\2021-11\第二批预览图'):
	for x in['XALC1-A028', 'XALC1-A018', 'XALC1-A009', 'XALC1-A026', 'XALC1-A024', 'XALC1-A031', 'XALC1-A029', 'XALC1-A015', 'XALC1-A016', 'XALC1-A033', 'XALC1-A037', 'XALC1-A035', 'XALC1-A020', 'XALC1-A013', 'XALC1-A011', 'XALC1-A022', 'XALC1-A005', 'XALC1-A001', 'XALC1-A007', 'XALC1-A003', 'XALC1-A019', 'XALC1-A010', 'XALC1-A027', 'XALC1-A025', 'XALC1-A032', 'XALC1-A030', 'XALC1-A017', 'XALC1-A034', 'XALC1-A038', 'XALC1-A036', 'XALC1-A021', 'XALC1-A014', 'XALC1-A012', 'XALC1-A023', 'XALC1-A006', 'XALC1-A002', 'XALC1-A008', 'XALC1-A004']:

		# try:
		baseurl=f'https://wsaiosscdn.yfway.com/ws-kitsys/WardrobeSun/release/kitproduct/preview/removedoor/{x.lower()}.jpg'
		# baseurl=f'https://wsaiosscdn.yfway.com/ws-kitsys/WardrobeSun/release/kitproduct/preview/{x.lower()}?x-oss-process=image/resize,h_142,w_142'
		
		# baseurl=st.iloc[x,1]
		# print(baseurl)
		response = requests.get(baseurl,headers=headers)
		# print(response.status_code)
		# print(response.content)
		if response.status_code ==404:
			print(x)
		response= response.content
		with open(f'preview\\{x.lower()}.jpg', 'wb') as f: # 打开文件
			f.write(response)
		baseurl=f'https://wsaiosscdn.yfway.com/ws-kitsys/WardrobeSun/release/kitproduct/preview/removedoor/{x.lower()}.jpg?x-oss-process=image/resize,h_142,w_142'
		response = requests.get(baseurl,headers=headers)
		if response.status_code ==404:
			print(x)
		response= response.content
		with open(f'preview\\removedoor\\{x.lower()}.jpg','wb') as f: # 打开文件
			f.write(response)
def main2231():	#根据型号找去门图片
	baseurl=f'https://168s.yfway.com/api/front/models/1439966?use_model_id=1&project=zhengzhuang'
		
	response = requests.get(baseurl,headers=headers)
	print(response.status_code)
	a1 =response.json()['model']
	# print(a1)
	for x in a1:
		# print(a1[x])
		if a1[x]==None:
			a1[x]=''
	# print(a1)
	pd.DataFrame([a1]).to_excel(r'123.xlsx',index=False)
	baseurl=f'https://168s.yfway.com/api/front/models/1435446?use_model_id=1&project=zhengzhuang'
		
	response = requests.get(baseurl,headers=headers)
	print(response.status_code)
	a1 =response.json()['model']
	for x in a1:
		# print(a1[x])
		if a1[x]==None:
			a1[x]=''
	pd.DataFrame([a1]).to_excel(r'1234.xlsx',index=False)
	# print(a1)
	# print(st)
	assert()
	# st = pd.read_excel(r'E:\er\py\v20查数据\V20产品库\背景墙调用.xlsx')
	# st = st.loc[st.modelno.apply(lambda a : 'QAA-B002' in a)][['modelno']]
	# for x in os.listdir(r'E:\wps\WeChat Files\wxid_17o69gjxn9t722\FileStorage\File\2021-11\第二批预览图'):
	for x in ['LGAM-01', 'LGAM-21', 'LGAM-02', 'LGAM-16', 'LGAM-14', 'LGAM-10', 'LGAM-11', 'LGAM-12', 'LGAM-13', 'LGJ-A002', 'LGJ-A001', 'LGJ-A003', 'LGJ-A004', 'XGAK-B008', 'XGAK-B010', 'LGAA-D002', 'LGJ-A032', 'XGAK-B009', 'LGJ-A033', 'XGAK-A013', 'LGFB-A003', 'XGAK-B013', 'LGFB-B001', 'LGFB-A001', 'XGAK-D002', 'LGJ-A035', 'LGJ-A036', 'LGAA-J003', 'LGAA-J002', 'LGAA-J001', 'LGJ-A005', 'LGJ-A014', 'XGAJ-D004', 'LGAG-A001', 'XGMJ-A009(廊桥)', 'LGJ-T005', 'XGMJ-A001', 'XGMJ-A002', 'XGMJ-A003', 'XGMJ-A004', 'XGMJ-A005', 'XGMJ-A006(转角01)', 'XGMJ-A007(转角02)', 'LGJ-F004', 'LGJ-F003', 'LGJ-A007', 'LGJ-A008', 'LGJ-A011', 'LGJ-A012', 'LGJ-A021', 'LGJ-A009', 'LGJ-B001', 'LGJ-B007', 'LGJ-B003', 'LGMJ-A001', 'LGJ2-B001', 'LGJ3-B001', 'LGJ-B002', 'LGJ-B004', 'LGJ-B008', 'LGJ2-B002', 'LGJ3-B002', 'LGJ-B016', 'LGJ-B018', 'LGJ-B017', 'XGCH-A013', 'LGJ2-B003', 'LGJ3-B003', 'LGAC-C001', 'LGJ-B014', 'LGJ-B009', 'LGJ-B013', 'LGJ-B010', 'LGJ-B012', 'LGJ-B011', 'LGJ-D006', 'LGJ-D005', 'LGJ-D002', 'LGJ-D004', 'LGJ-D001', 'LGJ-D003', 'LGAE-C001', 'LGJ-D014', 'LGJ-D013', 'LGJ-D012', 'LGJ-D011', 'LGAE-C002', 'XGAL-A100特殊材料专用', 'LGAE-D001', 'LGAE-D002', 'LGJ-T008', 'LGJ-T003', 'LGJ-T007', 'LGJ-T023', 'LGJ-T022', 'LGJ-T012', 'LGJ-T018', 'LGJ-T017', 'LGJ-T024', 'LGJ-T021', 'LGJ-T019', 'XGEG-A050', 'LGJ-T011', 'LGJ-T020', 'XGDK4-A014', 'XGDK4-A006', 'XGDK4-A015', 'XGDK4-A004', 'XGDK4-A016', 'XGDK4-A003', 'LGJ-C001', 'LGJ-A034', 'LGFA-C003', 'LGFA-C001', 'LGFA-C002', 'LGFA-C004', 'LGJ-C015', 'LGJ-C016', 'LGJ-C017', 'LGJ-C018', 'LGJ-C019', 'LGJ-C020', 'LGJ-C021', 'LGJ-C022', 'LGJ-C023', 'LGJ-C003', 'LGJ-C004', 'LGJ-C005', 'LGJ-C006', 'LGJ-C009', 'LGJ-C010', 'LGJ-C011', 'LGJ-C012', 'LGJ-C013', 'LGJ-C014', 'LGJ-C002', 'LGJ-C007', 'LGJ-C008', 'LGJ-C024', 'LGJ-C025', 'LGJ-C026', 'LGJ-C027', 'LGJ-C028', 'LGJ-C029', 'LGJ-C030', 'LGJ-C031', 'LGJ-C032', 'LGJ-C033', 'LGJ-T016', 'LGJ-M001', 'LGJ-M002', 'LGJ-M003', 'LGJ-M004', 'LGJ-A028', 'LGJ-A029', 'LGJ-A030', 'LGJ-A031', 'LGJ-A025', 'LGJ-A026', 'LGJ-A027', 'LGGA-E001', 'LGGA-E002', 'LGGA-E003', 'LGGB-ZA001', 'LGGB-ZA002', 'LGGB-ZA005', 'LGGB-ZA006', 'LGGB-ZA007', 'LGGB-ZA008', 'LGGB-ZA009', 'LGGB-ZA010', 'LGGB-ZA011', 'LGGB-ZA012', 'LGGB-ZA013', 'LGGB-ZA014', 'LGGB-ZA015', 'LGGB-ZA016', 'LGAC-T002', 'LGAC-T003', 'LGAC-T001', 'LGSA-B001', 'XHCD-A001', 'XHCD-A002', 'XHCD-A003', 'XHCD-A004', 'XHCE-A002A', 'XHCE-A002B', 'XHCE-A002C', 'XHCE-A002D', 'XHCE-A004A', 'XHCE-A004B', 'XHCE-A004C', 'XHCE-A004D', 'XHCE-A001A', 'XHCE-A001B', 'XHCE-A001C', 'XHCE-A001D', 'XHCC-A001', 'XHCC-A002', 'XHCC-A003', 'XHCC-A004', 'XHCC-A005', 'XHCC-A006', 'XHCA-A001', 'XHCA-A002', 'XHCA-A003', 'XHCA-A004', 'XHCC-A001A', 'XHCC-A002A', 'XHCC-A003A', 'XHCC-A004A', 'XHCC-A005A', 'XHCC-A006A', 'XHCE-A006A', 'XHCE-A006B', 'XHCE-A006C', 'XHCE-A006D', 'XHCE-A005A', 'XHCE-A005B', 'XHCE-A005C', 'XHCE-A005D', 'XHCB-A009', 'XHCB-A008', 'XHCB-A010', 'XGCH-A002', 'XGCH-A004', 'XGCH-A003', 'XHCB-A003A', 'XHCB-A001A', 'XHCB-A002A', 'XHCB-A004A', 'XHCB-A001', 'XHCB-A002', 'XHCB-A003', 'XHCB-A004', 'XHCB-A005', 'XHCB-A006', 'XHCB-A007', 'XHCE-A003A', 'XHCE-A003B', 'XHCE-A003C', 'XHCE-A003D', 'XHCC-A001C', 'XHCC-A002C', 'XHCC-A003C', 'XHCC-A004C', 'XHCC-A005C', 'XHCC-A006C', 'XHCC-A001B', 'XHCC-A002B', 'XHCC-A003B', 'XHCC-A004B', 'XHCC-A005B', 'XHCC-A006B', 'XHCB-A003C', 'XHCB-A003B', 'XHCB-A002C', 'XHCB-A002B', 'XHCB-A001C', 'XHCB-A001B', 'XHCB-A004C', 'XHCB-A004B', 'LGYB-A001', 'LGYB-B003', 'LGYB-B001', 'LGYB-B005', 'LGYB-A002', 'LGYB-B004', 'LGYB-B002', 'LGYB-B006', 'XHBD-A002A', 'XHBD-A002B', 'XHBD-A002C', 'XHBD-A002D', 'XHBD-A004A', 'XHBD-A004B', 'XHBD-A004C', 'XHBD-A004D', 'XHBD-A001A', 'XHBD-A001B', 'XHBD-A001C', 'XHBD-A001D', 'LGYB-ZB003', 'LGYB-ZB004', 'LGYB-ZB006', 'LGYB-ZB009', 'LGYB-ZB002', 'LGYB-ZB005', 'LGYB-ZB007', 'LGYB-ZB008', 'LGYB-ZA003', 'LGYB-ZA004', 'LGYB-ZA001', 'LGYB-ZA002', 'XHBC-A001', 'XHBC-A002', 'XHBC-A003', 'XHBC-A004', 'XHBC-A005', 'XHBC-A006', 'XHBC-A007', 'XHBC-A008', 'XHBC-A009', 'XHBC-A010', 'LGYB-ZB001', 'LGYB-ZB010', 'LGYB-ZB011', 'LGYB-ZB012', 'LGYB-ZB013', 'XHBA-A001', 'XHBA-A002', 'XHBA-A003', 'XHBA-A004', 'XHBC-A001A', 'XHBC-A002A', 'XHBC-A003A', 'XHBC-A004A', 'XHBC-A005A', 'XHBC-A006A', 'XHBC-A007A', 'XHBC-A008A', 'XHBD-A006A', 'XHBD-A006B', 'XHBD-A006C', 'XHBD-A006D', 'LGYB-ZA007', 'LGYB-ZA008', 'LGYB-ZA005', 'LGYB-ZA006', 'LGYB-ZA009', 'LGYB-ZA010', 'LGYA-B003', 'LGYA-B002', 'LGYA-B001', 'XHBD-A005A', 'XHBD-A005B', 'XHBD-A005C', 'XHBD-A005D', 'XHBB-A009', 'XHBB-A008', 'XHBB-A010', 'LGYA-B004', 'XHBB-A003A', 'XHBB-A001A', 'XHBB-A002A', 'XHBB-A004A', 'XHBB-A001', 'XHBB-A002', 'XHBB-A003', 'XHBB-A004', 'XHBB-A005', 'XHBB-A006', 'XHBB-A007', 'XHBD-A003A', 'XHBD-A003B', 'XHBD-A003C', 'XHBD-A003D', 'XHBC-A001C', 'XHBC-A002C', 'XHBC-A003C', 'XHBC-A004C', 'XHBC-A005C', 'XHBC-A006C', 'XHBC-A007C', 'XHBC-A008C', 'XHBC-A001B', 'XHBC-A002B', 'XHBC-A003B', 'XHBC-A004B', 'XHBC-A005B', 'XHBC-A006B', 'XHBC-A007B', 'XHBC-A008B', 'XHBB-A003C', 'XHBB-A003B', 'XHBB-A002C', 'XHBB-A002B', 'XHBB-A001C', 'XHBB-A001B', 'XHBB-A004C', 'XHBB-A004B', 'XHAB-A001', 'XHAB-A002', 'XHAA-C001', 'XHAA-C002', 'XHAA-A001', 'XHAA-B001', 'XHAA-B002', 'XHAA-B003', 'XHAA-E001', 'XHAA-B004', 'XHAA-B005', 'XGEG-A030', 'XGEG-A031', 'LGJ-T011', 'LGJ-T002', 'XGEG-A032', 'XGEG-A033', 'XGEG-A029', 'LGJ-T008', 'LGJ-T003', 'LGJ-T007', 'LGJ-T023', 'LGJ-T012', 'LGJ-T024', 'LGJ-T021', 'LGJ-T019', 'LGJ-T020', 'LGJ-T004', 'LGJ-T001', 'XGEE-A004', 'LGYA-C001', 'LGYA-C002', 'XHCE-A019', 'XHCE-A017', 'XHCE-A018', 'XHCE-A014', 'XHCE-A009A', 'XHCE-A009B', 'XHCE-A009C', 'XHCE-A009D', 'XHCE-A010A', 'XHCE-A010B', 'XHCE-A010C', 'XHCE-A010D', 'XHCE-A007A', 'XHCE-A007B', 'XHCE-A007C', 'XHCE-A007D', 'XHCE-A008A', 'XHCE-A008B', 'XHCE-A008C', 'XHCE-A008D', 'XHCE-A011A', 'XHCE-A011B', 'XHCE-A011C', 'XHCE-A011D', 'XHCE-A013A', 'XHCE-A013B', 'XHCE-A016', 'XHCE-A012A', 'XHCE-A012B', 'XHCE-A012C', 'XHCE-A012D', 'XHCE-A015', 'XGEG-A034', 'XGCH-A010A', 'XGCH-A010B', 'XGCH-A012', 'XGCH-A009', 'XGCH-A008', 'XGCH-A002A', 'XGCH-A019', 'XGCH-A011', 'CGMX-C004', 'CGMX-C005', 'CGAM-01真门-T', 'CGAM-01真门-B', 'CGAM-01假门-R', 'CGAM-01真门-R', 'CGAM-01假门-L', 'CGAM-01真门-L', 'CGAS-A001', 'CGAC-E001', 'CGAC-D001', 'CGAC-C002', 'CGAC-C001', 'CGAC-A003', 'CGAC-A001', 'CGAC-C005', 'CGAC-C006', 'CGAC-C004', 'CGAC-C003', 'CGCM-A001', 'CGCH-A001', 'CGCF-A001', 'CGCB-A001', 'CGCM-A002', 'CGKG-B003', 'CGKG-B004', 'CGKG-B002', 'CGKG-B001', 'CGKG-B007', 'CGKG-B005', 'CGKG-B008', 'CGKG-B006', 'CGKG-A009', 'CGKG-A010', 'CGKG-A006', 'CGKG-A007', 'CGKG-A008', 'CGKG-A004', 'CGKG-A005', 'CGKG-A001', 'CGKG-A002', 'CGKG-A003', 'CGKE-A005', 'CGKE-A002', 'CGKE-A011', 'CGKE-A004', 'CGKE-A001', 'CGKE-A010', 'CGKE-A003', 'CGKE-A007', 'CGKE-A006', 'CGKE-A009', 'CGKE-A008', 'CGKF-B008', 'CGKF-B007', 'CGKF-B009', 'CGKF-B005', 'CGKF-B004', 'CGKF-B006', 'CGKF-B001', 'CGKF-B011', 'CGKF-B003', 'CGKF-B002', 'CGKF-B010', 'CGKF-A008', 'CGKF-A007', 'CGKF-A009', 'CGKF-A001', 'CGKF-A005', 'CGKF-A004', 'CGKF-A003', 'CGKF-A002', 'CGKF-A006', 'CGKD-B008', 'CGKD-B006', 'CGKD-B009', 'CGKD-B012', 'CGKD-B010', 'CGKD-B011', 'CGKD-B007', 'CGKD-B001', 'CGKD-B003', 'CGKD-B004', 'CGKD-B002', 'CGKD-B005', 'CGKD-A004', 'CGKD-A006', 'CGKD-A002', 'CGKD-A007', 'CGKD-A008', 'CGKD-A005', 'CGKD-A003', 'CGKD-A001', 'CGBA-A017', 'CG-blum-矮抽', 'CG-blum-高抽', 'CG-U型-三节轨木抽高抽', 'CG-木抽-082450', 'CG-木抽-098450', 'CG-木抽-146450', 'CG-木抽-194450']:
		# try:
		baseurl=f'https://wsaiosscdn.yfway.com/ws-kitsys/WardrobeSun/release/kitproduct/preview/removedoor/{x.lower()}.jpg'
		# baseurl=f'https://wsaiosscdn.yfway.com/ws-kitsys/WardrobeSun/release/kitproduct/preview/{x.lower()}?x-oss-process=image/resize,h_142,w_142'
		
		# baseurl=st.iloc[x,1]
		# print(baseurl)
		response = requests.get(baseurl,headers=headers)
		print(response.status_code)
		# print(response.content)
		if response.status_code ==404:
			print(x)
		# response= response.content
		# with open(f'preview\\{x.lower()}.jpg', 'wb') as f: # 打开文件
		# 	f.write(response)

		if response.status_code ==404:
			baseurl=f'https://wsaiosscdn.yfway.com/ws-kitsys/WardrobeSun/release/kitproduct/preview/{x.lower()}.jpg'
			response = requests.get(baseurl,headers=headers)
			response= response.content
			with open(f'preview\\removedoor\\{x.lower()}.jpg','wb') as f: # 打开文件
				f.write(response)


def duquwenjian():
	with open("123.txt","r",encoding="utf-8") as f:
			a = f.read()
	f.close
	return a
class qingjiu(object):
	#简单请求
	def qingqiu1(self):
		url = "http://www.baidu.com"
		response = requests.get(url)
		# 查看响应url
		# print(response.url)
		# 查看响应状态码
		print(response.status_code)
		# 查看响应头
		# print(response.headers)
		# 查看请求头
		# print(response.request.headers)
		# print(response.encoding)
		# 查看响应源码的str类型数据
		response.encoding = 'utf-8'
		# print(response.text)
		#
		# 查看响应源码的bytes类型数据
		# print(response.content.decode())
	#带参数清楚  百度搜索python
	def qingqiu2(self):
		url = 'http://www.moguproxy.com/proxy/checkIp/ipList'

		params = {
		    "ip_ports[]": "61.29.96.146:8",
		    "ip_ports[]": "103.114.10.250:8",
		}

		headers = {
		    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
		}
		# response = requests.get(url, params=params, headers=headers).content.decode()
		return requests.get(url, params=params, headers=headers).text
	#带COOK参数请求
	def qingqiu3(self):
		url = 'https://github.com/exile-morganna'
		headers = {
	    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
	    'Cookie': '_ga=GA1.2.1190047373.1543731773; _octo=GH1.1.1199554731.1543731773; has_recent_activity=1; _gat=1; tz=Asia%2FShanghai; user_session=IsN0sqpV56zDyNOGBoUWHPRtiIe25zQ0y2cUCmBw0ubT7Zta; __Host-user_session_same_site=IsN0sqpV56zDyNOGBoUWHPRtiIe25zQ0y2cUCmBw0ubT7Zta; logged_in=yes; dotcom_user=exile-morganna; _gh_sess=T0NFUGJlZm5tQmJNQW8rdjhZUUVySm1adnF2TkNNZkpKdW9ZQWlIZFhhZ2QxaEhmWFJNMWZ1enIxWFZOQ2tzbjUxMG1keUtteXoyUWdUVndBRjAyS2cyUGs2RFhnSjJCQk1Ia2ZkNlJIK0ZoRWhQY1VsOG1TcTRQTXJJaVdIQW14OFZid1Ixbnd5NllIMjBMUmpRdndNM0V6VWRKd05vVjNrRXY4blQxNVVsdkE1dlhnMUFWcjhiOVhObGFxZ0lLLS15TzB6Rmg4Q0wxTktOTnVJU1lMdmlBPT0%3D--778a38d546dee1db9e70f8a7f12c7f46ee6878b9'
		}
		response = requests.get(url, headers=headers)
	def qingqiu4(self):
		url = 'http://httpbin.org/get'
		proxy = '102.164.252.150:8080'
		proxies = {
			'http' : 'http://'+proxy,
			'https' : 'https://'+proxy
				}
		response = requests.get(url, proxies=proxies)
		return response.text
if __name__ == '__main__':
	headers = {
	"User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
	# "authorization":"bearereyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvengwMTA4LWRldmVsb3AueWZ3YXkuY29tXC9hcGlcL3VzZXJcL2xvZ2luIiwiaWF0IjoxNjI4NDc3OTU2LCJleHAiOjE2Mjg1NjQzNTYsIm5iZiI6MTYyODQ3Nzk1NiwianRpIjoiSk5kcWRlRjVuSFZFclNpMCIsInN1YiI6NywicHJ2IjoiODdlMGFmMWVmOWZkMTU4MTJmZGVjOTcxNTNhMTRlMGIwNDc1NDZhYSIsInBpZCI6ODJ9.PORTz_oXMKJnvtLnpJHSqY2D1o_GHRwK2A6UjBDut1g"
	}
	a2 =r'E:\er\py\v20门板图片\preview\removedoor'
	if not os.path.exists(a2):
		os.makedirs(a2)
	# main()
	main222()
	
	# main33()
	for x in os.listdir(r'E:\er\py\v20门板图片\preview\removedoor'):
		print(x.split('.')[0].upper())

