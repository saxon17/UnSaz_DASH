
# -*- coding:utf-8 -*-
# file: TkinterCanvas.py
#
from hsx import *
from Tkinter import *         # 导入Tkinter模块
from PIL import Image, ImageTk
import tkMessageBox
import tkFileDialog
import xlrd
import  os
import FileDialog

global PATH
from tkFont import Font
from ttk import *
# from VB_SearchModule import Application
# from ModifyModule import Mocation


#search Class
class SearchApp_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类SearchApp中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Search')
        self.master.geometry('491x179')
        self.createWidgets()



        # 
        # ['Meter equipment identifier','Device Type','Delivery Date','Wasion Batch Number','SMSC Oder Number','Warranty To','Remark','NCR Number']
        # 'WasionBatchNumber'
        # 'SMSC_Order_No'
        # 'Warranty To'
        # 'Remark'
        # 'NCR Number' 


    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('TFrame1.TLabelframe', font=('宋体',9))
        self.style.configure('TFrame1.TLabelframe.Label', font=('宋体',9))
        self.Frame1 = LabelFrame(self.top, text='Chose you wanna search', style='TFrame1.TLabelframe')
        self.Frame1.place(relx=0.049, rely=0.089, relwidth=0.898, relheight=0.765)

        self.Combo1List = ['Meter equipment identifier','Device Type','Delivery Date','Wasion Batch Number','SMSC Oder Number','Warranty To','Remark','NCR Number']


        #	Rename
        # 'Meter equipment identifier'
        # 'DeviceType'
        # 'DeliveryDate'
        # 'WasionBatchNumber'
        # 'SMSC_Order_No'
        # 'Warranty To'
        # 'Remark'
        # 'NCR Number' 




        self.Combo1Var = StringVar(value='MEID')
        self.Combo1 = Combobox(self.Frame1, text='Add items in design or code!', textvariable=self.Combo1Var, values=self.Combo1List, font=('宋体',9))
        self.Combo1.place(relx=0.109, rely=0.467, relwidth=0.819, relheight=0.146)
        self.Combo1Var.trace('w', self.Combo1_Change)
class SearchApp(SearchApp_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在SearchApp_ui中。
    def __init__(self, master=None):
        SearchApp_ui.__init__(self, master)

    def Combo1_Change(self, *args):
        #TODO, Please finish the function here!
        print 'i love you '
        print self.Combo1.get()
        print 'ready to rename '+self.Combo1.get()+'to '+Rename(self.Combo1.get())
        SearchKey = Rename(self.Combo1.get())


        rooot = Toplevel()
                # root = Tk()
        frame1 = Frame(rooot)
        frame1.pack()
    

         #文件名输入  
  
        label1 = Label(frame1, text = "Search "+SearchKey+":")  
  
        

        var1 = StringVar()  #button按钮后，SearchUI里面的var1值变了，但这时候传过去的值已经是0
        var2 = StringVar()


          #MEID专用
        if SearchKey=="MEID":
               
            text1 = Entry(frame1,name = 'text1',textvariable=var1,width = 20)  
      
            text2 = Entry(frame1,name = 'mowei ',textvariable=var2,width = 20)  

            
      
            button2 = Button(frame1,text="Search",command=lambda:self.Search(SearchKey,text1.get(),text2.get()))  #CollectValueAndSearch(vari,var1,var2)  就在点击的一瞬间var1才的得到
      
            print text1.get()
            print text2.get()
       
      
            label1.pack(side=LEFT,padx=5)  
      
            text1.pack(side=LEFT, padx=2)   
            text2.pack(side=LEFT, padx=2)   
            button2.pack(side=LEFT, padx =5)  

        else:

        	
            text1 = Entry(frame1,name = 'text1',textvariable=var1,width = 20)
      
           
      
            button2 = Button(frame1,text="Search",command=lambda:self.Search(SearchKey,text1.get(),text1.get()) )  
      
              
       
      
            label1.pack(side=LEFT,padx=5)  
      
            text1.pack(side=LEFT, padx=2)   
           
            button2.pack(side=LEFT, padx =5)  



        print 'UpdateValue: ' + SearchKey


    def Search(self,keyfield,a,b):
		pass
		


#Modi Class
class ModiApp_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类ModiApp中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Search')
        self.master.geometry('453x422')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('TFrame1.TLabelframe', font=('宋体',9))
        self.style.configure('TFrame1.TLabelframe.Label', font=('宋体',9))
        self.Frame1 = LabelFrame(self.top, text='Modify', style='TFrame1.TLabelframe')
        self.Frame1.place(relx=0.053, rely=0.057, relwidth=0.885, relheight=0.874)

        self.style.configure('TFrame2.TLabelframe', font=('宋体',9))
        self.style.configure('TFrame2.TLabelframe.Label', font=('宋体',9))
        self.Frame2 = LabelFrame(self.Frame1, text='choose the field you want to medify', style='TFrame2.TLabelframe')
        self.Frame2.place(relx=0.12, rely=0.087, relwidth=0.761, relheight=0.263)

        self.Combo1List = ['Meter equipment identifier','Device Type','Delivery Date','Wasion Batch Number','SMSC Oder Number','Warranty To','Remark','NCR Number']
        self.Combo1Var = StringVar(value='Choose the field you want to modify!')
        self.Combo1 = Combobox(self.Frame2, text='Add items in design or code!', textvariable=self.Combo1Var, values=self.Combo1List, font=('宋体',9))
        self.Combo1.place(relx=0.105, rely=0.412, relwidth=0.79, relheight=0.206)
        self.Combo1Var.trace('w', self.Combo1_Change)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.Frame1, textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.2, rely=0.499, relwidth=0.601, relheight=0.176)
        self.Text1Var.trace('w', self.Text1_Change)

        self.style.configure('TCommand1.TButton', font=('宋体',9))
        self.Command1 = Button(self.Frame1, text='Modify修改', command=self.modifycmd, style='TCommand1.TButton')
        self.Command1.place(relx=0.2, rely=0.715, relwidth=0.601, relheight=0.22)

        self.style.configure('TLabel1.TLabel', anchor='w', font=('宋体',9))
        self.Label1 = Label(self.Frame1, text='请输入你要添加的值', style='TLabel1.TLabel')
        self.Label1.place(relx=0.2, rely=0.39, relwidth=0.601, relheight=0.068)
class Mocation(ModiApp_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在ModiApp_ui中。
    def __init__(self, master=None):
        ModiApp_ui.__init__(self, master)

    def Combo1_Change(self, *args):
        #TODO, Please finish the function here!
        pass

    def Text1_Change(self, *args):  #modify value

      	pass

        

    def modifycmd(self, event=None):


        ModiValue = self.Text1Var.get()

     
        # 打开数据库连接
        database = MySQLdb.connect (host="localhost", user = "saxon", passwd = "CcTqT29L4fwZ8pCs", db = "SMSC")

        # 使用cursor()方法获取操作游标 
        cursor = database.cursor()

        # global KeyA


        
        # global KeyB
        # global KEY
        print '正准被更新:项目%s      起：%s 止： %s' %(SEARCHKEYFIELD,KEYA,KEYB)


        # SQL 更新语句    SET: 下拉框   输入值ModiValue    WHERE:  搜索关键字 搜索A B
        upsql = '''UPDATE products_product 
                    SET %s = "%s"     WHERE %s BETWEEN %s and %s '''%(Rename(self.Combo1.get()),ModiValue,SEARCHKEYFIELD,KEYA,KEYB)
        
        print upsql
        try:
           # 执行SQL语句
           cursor.execute(upsql)
           # 提交到数据库执行
           database.commit()
        except:
           # 发生错误时回滚
           database.rollback()
        tkMessageBox.showinfo("showinfo demo", '''Update Success.Please resign in the @Web to check out''')
        # 关闭数据库连接
        database.close()
        # # Establish a MySQL connection 
        #   database = MySQLdb.connect (host="localhost", user = "saxon", passwd = "CcTqT29L4fwZ8pCs", db = "SMSC")
        #   # Get the cursor, which is used to traverse the database, line by line 
        #   cursor = database.cursor() 

        # up =   "UPDATE  products_product "+"SET 某一列 = 空白格"+" WHERE  下拉框 = %s" %("tablename")



def Rename(OriginalName):
    	#	Rename

		if OriginalName =='Meter equipment identifier':
			return 'MEID'
		if OriginalName == 'Device Type':
			return  'DType'
		if OriginalName == 'Delivery Date':
		    return 'D_Date'        	
		if OriginalName ==	'Wasion Batch Number':
			return   'Wasion Batch'
		if OriginalName == 'SMSC Oder Number':
			return  'SMSC_Order_No'
		if OriginalName == 'Warranty To':
			return  'Warranty'
		if OriginalName == 'NCR Number':
			return  'NCR'


def textereaIsGood():
	content = text.get("1.0","1.3").encode('utf8')
	
	if content == 'You':
		return False
	else:
		return True

#messagebox
def ShowInfo():
	tkMessageBox.showinfo("showinfo demo", '''Thanks For GitHub&python\n



	Author's Blog: http://blacksheepwall.sinaapp.com''')
def mAbout():
	tkMessageBox.showinfo(title="About",message="you cicked New")
	return

def mShowWarning():
	tkMessageBox.showwarning("Attention",'''Youtube_Pcap_Parser made by saxon
                     LGPL
            @ all rights Reserved 2015   ''')
	return

def mShowError():
	tkMessageBox.showerror("showerror demo", "Error")
	return
def mAsk():
	tkMessageBox.askokcancel("askokcancel demo", "OK?! CANCEL?!")
	return


#Real Function	

def donothing():
   win = Toplevel(DeskWindow)
   # button = Button(filewin, text="Do nothing button")
   # button.pack()
   
   SearchApp(win )

def xopen():
	#fopen = tkFileDialog.askopenfile()
	#print type(fopen)
 	fileroute = tkFileDialog.askopenfilename()
 	global PATH
 	PATH = fileroute
 	print PATH

	# a = tkMessageBox.askokcancel("Make sure then click OK",
	#  "If Pcap file is over 40mb , Please wait for few seconds %s" % fileroute)
    #
	# if a:
	import_xls()

  


def about(): 
	w = Label(DeskWindow,text='''开发者感谢\nGitHub
		\npython\n



	作者博客http://blacksheepwall.sinaapp.com''')    
	w.pack(side=TOP)






#var1 为表号始
  #var3 DeviceType

  #var4为BatchNumber
  #texterea = Remark
  #var6 DeliveryDate
  #var7 NcrOderNum


def CollectValueAndBatchcreate():
	first = var1.get()
	last =	var2.get()
	dtype = var3.get()
	BatchNumber = var4.get()
	date = var6.get()
	ncr = var7.get()
	Warranty = var8.get()
	remark = text.get("1.0",END).encode('utf8')
	print var110.get()
	smsc = entry110.get()
	print "smsc:"+str(smsc)

	Batchcreate(first,last,dtype,date,BatchNumber,ncr,remark,Warranty,smsc)
# 	def Batchcreate(begin,end,var2,var3,var4,var5,text1): 
#                  (begin,end,DType,D_Date,WasionBatch,SMSC_Order_No,Remark)



def import_xls():
    print  "Please wait ...."
    global PATH

    def WidthSplitString(string,width):
        return [string[x:x+width] for x in range(0,len(string),width)]
    def oneTimeFunc(s):
        Templst = WidthSplitString(s,1)
        return (map(lambda s:s.encode('hex'),Templst))
    def getInitialSegHexDict(SazFile):
        import zipfile
        import pandas as pd
        d = {}
        zf = zipfile.ZipFile(SazFile, 'r')

        html = zf.read("_index.htm")

        df = pd.read_html(html)[0]
        df2 = df.loc[:,['Host','#','Body','URL','Content-Type']]

        df2 = df2[df2['Content-Type'] == 'video/mp4']

        Host_Group =  df2.groupby('Host')
        Host_Seri = Host_Group.Body.sum()
        VideoHost = Host_Seri[Host_Seri == Host_Seri.max()].index[0]
        df2 = df2[df2['Host']== VideoHost]



        # InitialTxTPath =  'raw/0'+str(df2.iat[0,0])+'_s.txt'
        InitialTxTPath =  'raw/0'+str(df2.index[0]+1)+'_s.txt'

        try:
            zf.read(InitialTxTPath)
        except:
            InitialTxTPath =  'raw/'+str(df2.index[0]+1)+'_s.txt'
            try:
                zf.read(InitialTxTPath)
            except:
                InitialTxTPath =  'raw/00'+str(df2.index[0]+1)+'_s.txt'
        print 'txtPath:',InitialTxTPath
        txt =  WidthSplitString(zf.read(InitialTxTPath),16)
        sidx = zf.read(InitialTxTPath).find('sidx')
        for ix,line in enumerate(map(oneTimeFunc,txt)):
            # print( ix,line)
            d[ix*10] = line
        return d,sidx,df2

    ResultTuple =getInitialSegHexDict(PATH)
    d = ResultTuple[0]
    sidx_pos = ResultTuple[1]
    df2 = ResultTuple[2]
    lineMark = sorted(d)[-1]

    print 'sidx_pos:',sidx_pos
    Unknowpara = d[(sidx_pos+13)/16*10][(sidx_pos+13)%16]+\
        d[(sidx_pos+14)/16*10][(sidx_pos+14)%16]+\
        d[(sidx_pos+15)/16*10][(sidx_pos+15)%16]
    # print 'UnknowparaHex',Unknowpara
    # print sidx_pos/16*10,sidx_pos%16
    Unknowpara = int(Unknowpara,16)
    total_segments_count = int(d[(sidx_pos+27)/16*10][(sidx_pos+27)%16],16)
    fistVideo = d[(sidx_pos+33)/16*10][(sidx_pos+33)%16]+\
        d[(sidx_pos+34)/16*10][(sidx_pos+34)%16]+\
        d[(sidx_pos+35)/16*10][(sidx_pos+35)%16]


    print 'Segments_count',total_segments_count
    print 'Unknowpara:',Unknowpara
    print 'fistVideo',fistVideo



    # Unknowpara = int(d[sidx_pos+13][2]+d[710][3]+d[710][4],16)
    # print 'Unknowpara:',Unknowpara
    # print 'total segments count:',total_segments_count
    # print 'The first seg:' ,d[720][6],d[720][7],d[720][8]

    # next_Line = current_line = 720
    #
    # current_offset = 7
    def getVideoDurInHexTable(lineMark,current_line,offset):
        # print lineMark
        Vedio_count = 1
        videoDurFirstByte_lst= []
        while(1):
            if current_line > lineMark:
                break
            if current_line == lineMark and offset>len(d[lineMark])-1:
                break
            # print Vedio_count,d[current_line][offset],'(',current_line,offset,')'
            videoDurFirstByte_lst.append(d[current_line][offset])
            if offset+12 > 15:
                current_line += 10
                offset = (offset+12)%16
            else:
                offset += 12
            Vedio_count += 1
        return  videoDurFirstByte_lst
    def magic(string):
        return int(string,16)
    def getDoublueVideoSeg(lst):

        list1 = lst[::2]
        list2 = lst[1::2]
        # print list1
        # print list2
        DiFlen = len(list1)-len(list2)
    #     print 'DiFlen:',DiFlen
        if DiFlen > 0:
            list2 += [0] * DiFlen
        else:
            list1 += [0] * (-DiFlen)
        # print list1
        # print list2
        return [x+y for x, y in zip(list1, list2)]

    print '***lineMark:',lineMark
    A = getVideoDurInHexTable(lineMark,(sidx_pos+33)/16*10,(sidx_pos+33)%16)
    B = getVideoDurInHexTable(lineMark,(sidx_pos+34)/16*10,(sidx_pos+34)%16)
    C = getVideoDurInHexTable(lineMark,(sidx_pos+35)/16*10,(sidx_pos+35)%16)
    Seg_dur_hex_lst = map(lambda t,:t[0]+t[1]+t[2],zip(A,B,C))
    Seg_dur_hex_lst = map(magic,Seg_dur_hex_lst)



    Sigle_Segments_Duration_lst =  map(lambda x:float(x)/Unknowpara,Seg_dur_hex_lst)


    E = getVideoDurInHexTable(lineMark,(sidx_pos+29)/16*10,(sidx_pos+29)%16)
    F = getVideoDurInHexTable(lineMark,(sidx_pos+30)/16*10,(sidx_pos+30)%16)
    G = getVideoDurInHexTable(lineMark,(sidx_pos+31)/16*10,(sidx_pos+31)%16)

    Seg_Size_hex_lst = map(lambda t,:t[0]+t[1]+t[2],zip(E,F,G))
    # print Seg_Size_hex_lst
    Sigle_Segments_Size_lst = map(magic,Seg_Size_hex_lst)





    df_seg_dur_lst = []
    for index,dur in enumerate(getDoublueVideoSeg(Sigle_Segments_Duration_lst)):
        print 'video'+str(index+1),dur
        df_seg_dur_lst.append(dur)

    df_seg_size_lst = []
    for index,dur in enumerate(getDoublueVideoSeg(Sigle_Segments_Size_lst)):
        print 'size'+str(index+1),dur
        df_seg_size_lst.append(dur)
    # print df_seg_size_lst

    #
    # df2 = df2.reset_index()
    #
    # df2 = df2[1:]
    # df2['segment_duration'] = df_seg_dur_lst
    # df2   =  df2.drop(['URL','#','index'],axis = 1)
    # df2['PlaybackRate'] = df2.Body*8 / df2.segment_duration
    # df2.to_excel

    outPutDF = pd.DataFrame()
    outPutDF['SegmentDuration'] = df_seg_dur_lst
    outPutDF['SegmentSize'] = df_seg_size_lst
    outPutDF['BitRate'] = outPutDF['SegmentSize']*8/outPutDF['SegmentDuration']/1024
    outPutDF.index += 1

    outDIR = os.getcwd()+'\\Result\\'
    if  not os.path.exists(outDIR):
        os.mkdir(outDIR)
    outPutDF.to_excel(outDIR+os.path.basename(PATH).split('.')[0]+".xls")
    print('currentdir:',os.getcwd())
    # df2['PlaybackRate'] = df2.Body*8 / df2.segment_duration
    tkMessageBox.showinfo("showinfo demo", '''已导出excel结果到Result文件下''')
    # ShowInfo()













#GUI

DeskWindow = Tk()

DeskWindow.title ("made by Saxon")









# #Batch
# L1 = LabelFrame(DeskWindow,text = 'MEID')
# # 设置ipadx属性为20
# L1.pack()


# var1  = IntVar()           #var1为批号头
# var2  = IntVar()		   #var2为批号尾

# entry1 = Entry(L1,textvariable=var1,).pack(side=LEFT)
# lbB = Label(L1,text = '-').pack(side=LEFT)
# entry2 = Entry(L1,textvariable=var2,).pack(side=LEFT)






# L2 = LabelFrame(DeskWindow,text = '请输入检验批次、电表型号等')
# L2.pack()
# # 设置ipadx属性为20
# var3  = StringVar()     #var3 DeviceType
# var4  = StringVar()     #var4为BatchNumber
# var5  = StringVar()		#texterea = Remark
# var6  = StringVar()		#var6 DeliveryDate
# var7  = StringVar()		#var7 NcrOderNum
# var8  = StringVar()		#var8 Warranty
# var110 = StringVar()    #smsc Number

# Label(L2,text = '      DeviceType:      ').pack(side=LEFT)

# entry3 = Entry(L2,textvariable=var3,).pack(side=LEFT)    #var3为电表型号

# # Label(L2,text = '检验批次:').pack()

# # entry4 = Entry(L2,textvariable=var4,).pack()



# L4 = LabelFrame(DeskWindow,text = '')
# L4.pack()

# Label(L4,text = '      DeliveryDate:    ').pack(side=LEFT)
# entry4 = Entry(L4,textvariable=var6,).pack(side=LEFT)     #var6为D_Date









# L5 = LabelFrame(DeskWindow,text = '')
# L5.pack()

# Label(L5,text = '    BatchNumber:     ').pack(side=LEFT)
# entry4 = Entry(L5,textvariable=var4,).pack(side=LEFT)     #var4为BatchNumber


# L7 = LabelFrame(DeskWindow,text = '')
# L7.pack()
 
# Label(L7,text = '        NCR No.:        ').pack(side=LEFT)
# entry4 = Entry(L7,textvariable=var7,).pack(side=LEFT)     #var7为NCR No.

	

# L8 = LabelFrame(DeskWindow,text = '')
# L8.pack()
 
# Label(L8,text = 'Warranty Period to: ').pack(side=LEFT)
# entry8 = Entry(L8,textvariable=var8,).pack(side=LEFT)     #var7为NCR No.





# L110 = LabelFrame(DeskWindow,text = '')
# L110.pack()
 
# Label(L110,text = 'SMSC Order Number').pack(side=LEFT)
# entry110 = Entry(L110,textvariable=var110,)
# entry110.pack(side=LEFT)     #var110为 SmscOderNumber
# print entry110.get()





# L6 = LabelFrame(DeskWindow,text = '')
# L6.pack()

# # Label(L6,text = '      Remark:         ').pack(side=LEFT)
# # entry5 = Entry(L6,textvariable=var5,).pack(side=LEFT)     #var4为Remark
# text = Text(L6,width=38,height=5)
# text.insert(INSERT, '''You can add remark here.
# (if you do not want to remark,please make sure that this textarea is empty)如果不想添加remark，请用退格键或者delete清除本文本框中的内容''')
# # text.insert(END, "如果不想添加remark，请用退格键或者delete清楚本文本框中的内容")
# text.pack()

# text.tag_add("yellowtag", "1.0", "1.30")    #建立tag（头坐标，尾坐标）
# text.tag_add("greenblacktag", "2.0", "3.40")
# text.tag_config("yellowtag", background="yellow", foreground="blue")
# text.tag_config("greenblacktag", background="black", foreground="green")

# bottomFrame = Frame(DeskWindow)  #底部站位框
# bottomFrame.pack()
# bottomLable = Label(bottomFrame,text='                                         ').pack(side=LEFT)
# B1 = Button(bottomFrame,text='导入',command=CollectValueAndBatchcreate).pack(side=LEFT)














menubar = Menu(DeskWindow)     #manubar是一个横着的菜单

#File键list设置

filemenu = Menu(menubar, tearoff=0)     #filemenu是一个竖着的菜单（casecade瀑布样）
#filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=xopen)
#filemenu.add_command(label="Save", command=donothing)
#filemenu.add_command(label="Save as...", command=donothing)
#filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()


filemenu.add_command(label="Exit", command=DeskWindow.quit)
menubar.add_cascade(label="File", menu=filemenu) #File作瀑布样




#Editmenu
# Editmenu = Menu(menubar, tearoff=0)
# Editmenu.add_command(label="Search", command=donothing)
# Editmenu.add_command(label="Modify", command=donothing)
# menubar.add_cascade(label="Search", menu=Editmenu)









#helpmenu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Attention", command=mShowWarning)
helpmenu.add_command(label="About...", command=ShowInfo)
menubar.add_cascade(label="Help", menu=helpmenu)















DeskWindow.config(menu=menubar)









canvas = Canvas(DeskWindow,
    width = 500,      # 指定Canvas组件的宽度
    height = 400,      # 指定Canvas组件的高度
    bg = 'white')      # 指定Canvas组件的背景色
#im = Tkinter.PhotoImage(file='img.gif')     # 使用PhotoImage打开图片
image = Image.open("img.jpg")
im = ImageTk.PhotoImage(image)

canvas.create_image(250,180,image = im)      # 使用create_image将图片添加到Canvas组件中
canvas.create_text(302,340,       # 使用create_text方法在坐标（302，77）处绘制文字
   text = '''PcapFile_Parser made by saxon
                     LGPL
            all rights Reserved    '''      # 所绘制文字的内容
   ,fill = 'gray')       # 所绘制文字的颜色为灰色
# canvas.create_text(300,340,
#    text = '''PcapFile_Parser made by saxon
#    			LGPL @all rights Reserved	''',
#    fill = 'black')
canvas.pack()         # 将Canvas添加到主窗口























DeskWindow.mainloop()






'''
from Tkinter import *
mGui = Tk()
mGui.geometry('500x500+300+100')
mGui.title("Be a man ")


canvas_1 = Canvas(mGui,height=300,bg="red",width=300)
canvas_1.pack()





mGui.mainloop()
#canvas
'''