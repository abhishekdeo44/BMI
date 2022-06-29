from tkinter import Tk , Button, Entry, Label, font , messagebox


def calculate_bmi(weight,height):
    height = height/100
    bmi = (weight/(height**2))
    return bmi



def alter_display():
 try:
     height= float (height_entry.get())
     weight= float(weight_entry.get())
     bmi= calculate_bmi(weight,height)
     answer_entry.config(state='normal')
     answer_entry.delete(0,'end')
     answer_label.grid(row=2,column=0,padx=10,pady=10)
     answer_entry.grid(row=2,column=1,padx=10,pady=10)
     answer_entry.insert(0,round(bmi,2))
     answer_entry.config(state='readonly')
 except ValueError:
     messagebox.showerror('Error', 'Only number are accpeted not string')
    




font =('Consolar',20 , 'bold')
bg ='#002b36'
bg2= '#002b45'
fg='white'
root= Tk()
root.title('BMI Calculator')
root.config(background=bg)



 
weight_label = Label(root, text='Enter Weight (in kg)', 
                     font=font,bg=bg, fg=fg)
weight_entry = Entry(root,width=20, 
                     font=font,bg=bg2,fg=fg , insertbackground=fg)
height_label=Label(root,text='Enter Height(in cm)',
                   font=font,bg=bg,fg=fg)
height_entry = Entry(root, width=20,
                     font=font,bg=bg2,fg=fg,insertbackground=fg)
calculate_button = Button(root, text='Calculate',
                          font=font,bg='orange',fg=fg , command=alter_display)




answer_label=Label(root,text='BMI',font=font,bg=bg,fg=fg)
answer_entry=Entry(root,width=20,font=font,readonlybackground=bg2,fg=fg)
answer_entry.config(state='readonly')

weight_label.grid(row=0, column=0, padx=10, pady=10)
weight_entry.grid(row=0,column=1,padx=10, pady=10)
height_label.grid(row=1,column=0,padx=10,pady=10)
height_entry.grid(row=1,column=1,padx=10,pady=10)
calculate_button.grid(row=3,column=0,columnspan=2, sticky='ew',padx=10,pady=10)

root.mainloop()