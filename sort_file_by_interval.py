import glob
import os
import shutil
from tkinter import Tk, Button, Entry, Label, StringVar, filedialog, IntVar, ttk
root = Tk()
root.title('Sort files')


source = StringVar(root)
labelSource = Label(root, text='Source :')
entrySource = Entry(root, textvariable=source, width = 40)
labelSource.grid(row=0,column=1)
entrySource.grid(row=0,column=2)

dest = StringVar(root)
labelDest = Label(root, text='Dest :')
entryDest = Entry(root, textvariable=dest, width = 40)
labelDest.grid(row=1,column=1)
entryDest.grid(row=1,column=2)

interval = IntVar(root)
labelInterval = Label(root, text='Interval :')
entryInterval = Entry(root, textvariable=interval, width = 40)
labelInterval.grid(row=2,column=1)
entryInterval.grid(row=2,column=2)

pattern = StringVar(root)
labelPattern = Label(root, text='Pattern :')
entryPattern = Entry(root, textvariable=pattern, width = 40)
labelPattern.grid(row=3,column=1)
entryPattern.grid(row=3,column=2)
pattern.set("_tri")

extension = StringVar(root)
labelExtension = Label(root, text='Extension :')
entryExtension = Entry(root, textvariable=extension, width = 40)
labelExtension.grid(row=4,column=1)
entryExtension.grid(row=4,column=2)
extension.set(".txt")

def setSource():
    source.set(filedialog.askdirectory(initialdir="/",title='Please select a directory'))

def setDest():
    dest.set(filedialog.askdirectory(initialdir="/",title='Please select a directory'))

print_buttonSource = Button(root, text='Browse', command=setSource)
print_buttonSource.grid(row=0,column=3)
print_buttonDest = Button(root, text='Browse', command=setDest)
print_buttonDest.grid(row=1,column=3)
#progressbar = ttk.Progressbar(root, length=200, mode='indeterminate')
#progressbar.grid(row=6,column=1,columnspan=3,sticky='W'+'E'+'N'+'S')

def checkMandatory():
	return interval.get() and dest.get() and source.get() and pattern.get() and extension.get()

def mvFileByInterval():
	if checkMandatory():
		#progressbar.start()
		interval_int = interval.get()
		#create dir
		count = 0
		while count < interval_int:
			os.makedirs(dest.get()+"/"+str(count))
			count = count + 1

		#sort files
		files = glob.glob(source.get()+"/*"+extension.get())
		files.sort(key=lambda x: x.split(pattern.get())[1])#key=os.path.getctime)

		#move files
		for counter, file in enumerate(files):
			shutil.move(file, dest.get()+"/"+str(counter % interval_int))
		#print("\n".join(files))
		#progressbar.stop()

print_buttonDest = Button(root, text='GO',command=mvFileByInterval)
print_buttonDest.grid(row=7,column=2)

#exit_button = Button(root, text='Exit Program', command=root.destroy)
#exit_button.grid(row=4,column=3)

root.mainloop()