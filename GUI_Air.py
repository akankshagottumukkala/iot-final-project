from tkinter import *
from keras.models import load_model
import numpy as np
from tkinter import messagebox as mb
def predict():
	value =[]
	value.append(int(e1.get()))
	value.append(int(e2.get()))
	value.append(int(e3.get()))
	value.append(int(e4.get()))
	value.append(int(e5.get()))
	value.append(int(e6.get()))
	value.append(int(e7.get()))
	value.append(int(e8.get()))
	value.append(int(e9.get()))
	value.append(int(e10.get()))
	value.append(int(e11.get()))
	value.append(int(e12.get()))
	value.append(int(e13.get()))
	value.append(int(e14.get()))
	value.append(int(e15.get()))
	print(value)

	new_model=load_model('/Users/saicharan/PycharmProjects/ComputerVision/Model_AirPollution.h5')
	values = ['Good', 'Satisfactory', 'Moderately', 'Poor', 'Very-Poor', 'Severe']
	# pre=new_model.predict_classes([value])
	pre = new_model.predict_classes(np.array([value]))
	print(values[pre[0]])
	mb.showinfo('Predicted', values[pre[0]])



master = Tk()
Label(master, text='AMB_TEMP').grid(row=1)
Label(master, text='RAINFALL').grid(row=2)
Label(master, text='RH').grid(row=3)
Label(master, text='WD_HR').grid(row=4)
Label(master, text='WIND_DIREC').grid(row=5)
Label(master, text='WIND_SPEED').grid(row=6)
Label(master, text='WS_HR').grid(row=7)
Label(master, text='CO').grid(row=8)
Label(master, text='NO').grid(row=9)
Label(master, text='NO2').grid(row=10)
Label(master, text='NOx').grid(row=11)
Label(master, text='O3').grid(row=12)
Label(master, text='PM10').grid(row=13)
Label(master, text='PM2.5').grid(row=14)
Label(master, text='SO2').grid(row=15)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)
e8 = Entry(master)
e9 = Entry(master)
e10 = Entry(master)
e11 = Entry(master)
e12 = Entry(master)
e13 = Entry(master)
e14 = Entry(master)
e15 = Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)
e7.grid(row=7, column=1)
e8.grid(row=8, column=1)
e9.grid(row=9, column=1)
e10.grid(row=10, column=1)
e11.grid(row=11, column=1)
e12.grid(row=12, column=1)
e13.grid(row=13, column=1)
e14.grid(row=14, column=1)
e15.grid(row=15, column=1)

tb_list =[]
for i in range(1,16):
	tb_list.append("e"+str(i))

btn7 = Button(master, text='Predict', command=predict, height=5, width=10)
btn7.grid(column=1, row=17)

mainloop()

