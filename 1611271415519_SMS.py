from tkinter import *
import pandas as pd
df= pd.DataFrame()





# creating window
root= Tk()
root.title("School Management System")
root.geometry("1000x650")
# "Regno", 
st_col= ["Student Name", "Class", "Section", "DoB", "Student Email", "Student Contact", "Student Adhar", "Father Name", "Father Email", "Father Contact", "Father Adhar", "Mother Name", "Mother Email ", "Mother Contact", "Mother Adhar" ]
try:
	df = pd.read_csv('data.csv')
except:	
	df = pd.DataFrame(columns=st_col)
	df.to_csv('data.csv',index=False)



frame_h= LabelFrame(root, bg="#610D0D")
frame_h.place(relx=0, rely= 0, relwidth= 1, relheight= 0.3)
heading= Label(root, text= "School Management System", font= ('times', 44, "bold"), bg="#F27F57")
heading.place(relx=0, rely= 0.05, relwidth= 1, relheight= 0.2)





#defining home page buttons
	 ## creating entry form and variables to store entrybox values


def button_entry():
	 frame_entry= Frame(root, bg= "#F3B48B")
	 frame_entry.place(relx=0, rely= 0.3, relwidth= 1, relheight= 0.7)
	
   
	 label_st= Label(frame_entry, text="Student's Details", font=("Times", 18), bg= "#F3B48B")
	 label_st.place(relx=0, rely=0, relwidth= 0.4, relheight= 0.1)


	 stn_var= StringVar()
	 label_stn= Label(frame_entry, text="Enter Student's Name : ", font=("Times", 15), bg= "#F3B48B")
	 label_stn.place(relx=0, rely=0.120, relwidth=0.2, relheight=0.07)

	 enter_stn= Entry(frame_entry, textvariable= stn_var, font=("Times", 15))
	 enter_stn.place(relx=0.2, rely= 0.120, relwidth= 0.3, relheight= 0.07)

	 class_var= StringVar()
	 label_class= Label(frame_entry, text="Enter Class : ", font=("Times", 15), bg= "#F3B48B")
	 label_class.place(relx=0, rely=0.235, relwidth=0.2, relheight=0.07)

	 enter_class= Entry(frame_entry, textvariable= class_var, font=("Times", 15))
	 enter_class.place(relx=0.2, rely= 0.235, relwidth= 0.3, relheight= 0.07)

	 sec_var= StringVar()
	 label_sec= Label(frame_entry, text="Enter Section : ", font=("Times", 15), bg= "#F3B48B")
	 label_sec.place(relx=0, rely=0.350, relwidth=0.2, relheight=0.1)

	 enter_sec= Entry(frame_entry, textvariable= sec_var, font=("Times", 15))
	 enter_sec.place(relx=0.2, rely= 0.350, relwidth= 0.3, relheight= 0.07)

	 dob_var= StringVar()
	 label_dob= Label(frame_entry, text="Enter DoB : ", font=("Times", 15), bg= "#F3B48B")
	 label_dob.place(relx=0, rely=0.465, relwidth=0.2, relheight=0.1)

	 enter_dob= Entry(frame_entry, textvariable= dob_var, font=("Times", 15))
	 enter_dob.place(relx=0.2, rely= 0.465, relwidth= 0.3, relheight= 0.07)

	 sadhr_var= StringVar()
	 label_sadhr= Label(frame_entry, text="Enter Adhaar no. : ", font=("Times", 15), bg= "#F3B48B")
	 label_sadhr.place(relx=0, rely=0.580, relwidth=0.2, relheight=0.07)

	 enter_sadhr= Entry(frame_entry, textvariable= sadhr_var, font=("Times", 15))
	 enter_sadhr.place(relx=0.2, rely= 0.580, relwidth= 0.3, relheight= 0.07)

	 scntct_var= StringVar()
	 label_scntct= Label(frame_entry, text="Enter Contact 1 : ", font=("Times", 15), bg= "#F3B48B")
	 label_scntct.place(relx=0, rely=0.695, relwidth=0.2, relheight=0.07)

	 enter_scntct= Entry(frame_entry, textvariable= scntct_var, font=("Times", 15))
	 enter_scntct.place(relx=0.2, rely= 0.695, relwidth= 0.3, relheight= 0.07)

	 seml_var= StringVar()
	 label_seml= Label(frame_entry, text="Enter Email : ", font=("Times", 15), bg= "#F3B48B")
	 label_seml.place(relx=0, rely=0.810, relwidth=0.2, relheight=0.07)

	 enter_seml= Entry(frame_entry, textvariable= seml_var, font=("Times", 15))
	 enter_seml.place(relx=0.2, rely= 0.810, relwidth= 0.3, relheight= 0.07)



	 label_pt= Label(frame_entry, text="Parent's Details", font=("Times", 18), bg= "#F3B48B")
	 label_pt.place(relx=0.6, rely=0, relwidth= 0.4, relheight= 0.1)

	 ftn_var= StringVar()
	 label_ftn= Label(frame_entry, text="Enter Father's Name : ", font=("Times", 15), bg= "#F3B48B")
	 label_ftn.place(relx=0.5, rely=0.12, relwidth=0.2, relheight=0.07)

	 enter_ftn= Entry(frame_entry, textvariable= ftn_var, font=("Times", 15))
	 enter_ftn.place(relx=0.7, rely= 0.12, relwidth= 0.3, relheight= 0.07)

	 fcntct_var= StringVar()
	 label_fcntct= Label(frame_entry, text="Enter Contact 2 : ", font=("Times", 12), bg= "#F3B48B")
	 label_fcntct.place(relx=0.5, rely=0.22, relwidth=0.2, relheight=0.05)

	 enter_fcntct= Entry(frame_entry, textvariable= fcntct_var, font=("Times", 12))
	 enter_fcntct.place(relx=0.7, rely= 0.22, relwidth= 0.3, relheight= 0.05)

	 fadhr_var= StringVar()
	 label_fadhr= Label(frame_entry, text="Enter Adhaar Number : ", font=("Times", 12), bg= "#F3B48B")
	 label_fadhr.place(relx=0.5, rely=0.32, relwidth=0.2, relheight=0.05)

	 enter_fadhr= Entry(frame_entry, textvariable= fadhr_var, font=("Times", 12))
	 enter_fadhr.place(relx=0.7, rely= 0.32, relwidth= 0.3, relheight= 0.05)

	 feml_var= StringVar()
	 label_feml= Label(frame_entry, text="Enter Email : ", font=("Times", 12), bg= "#F3B48B")
	 label_feml.place(relx=0.5, rely=0.42, relwidth=0.2, relheight=0.05)

	 enter_feml= Entry(frame_entry, textvariable= feml_var, font=("Times", 12))
	 enter_feml.place(relx=0.7, rely= 0.42, relwidth= 0.3, relheight= 0.05)




	 mtn_var= StringVar()
	 label_mtn= Label(frame_entry, text="Enter Mother's Name : ", font=("Times", 15), bg= "#F3B48B")
	 label_mtn.place(relx=0.5, rely=0.52, relwidth=0.2, relheight=0.07)

	 enter_mtn= Entry(frame_entry, textvariable= mtn_var, font=("Times", 15))
	 enter_mtn.place(relx=0.7, rely= 0.52, relwidth= 0.3, relheight= 0.07)

	 mcntct_var= StringVar()
	 label_mcntct= Label(frame_entry, text="Enter Contact 3 : ", font=("Times", 12), bg= "#F3B48B")
	 label_mcntct.place(relx=0.5, rely=0.62, relwidth=0.2, relheight=0.05)

	 enter_mcntct= Entry(frame_entry, textvariable= mcntct_var, font=("Times", 12))
	 enter_mcntct.place(relx=0.7, rely= 0.62, relwidth= 0.3, relheight= 0.05)

	 madhr_var= StringVar()
	 label_madhr= Label(frame_entry, text="Enter Adhaar Number : ", font=("Times",12), bg= "#F3B48B")
	 label_madhr.place(relx=0.5, rely=0.72, relwidth=0.2, relheight=0.05)

	 enter_madhr= Entry(frame_entry, textvariable= madhr_var, font=("Times", 12))
	 enter_madhr.place(relx=0.7, rely= 0.72, relwidth= 0.3, relheight= 0.05)

	 meml_var= StringVar()
	 label_meml= Label(frame_entry, text="Enter Email : ", font=("Times", 12), bg= "#F3B48B")
	 label_meml.place(relx=0.5, rely=0.82, relwidth=0.2, relheight=0.05)

	 enter_meml= Entry(frame_entry, textvariable= meml_var, font=("Times", 12))
	 enter_meml.place(relx=0.7, rely= 0.82, relwidth= 0.3, relheight= 0.05)


	 #defining entry page buttons

	 def button_back():
		  frame_entry.lower()
	   
	 button_back= Button(frame_entry, text= "Back", command=button_back, bg="#F9D6B1", font=("Times", 13))
	 button_back.place(relx=0.01, rely=0.91, relwidth=0.08, relheight=0.085 )

	 def button_submit():

		 df_st = pd.read_csv("data.csv")
		 st_name= str(enter_stn.get())
		 st_class= str(enter_class.get())
		 st_sec= str(enter_sec.get())
		 st_dob= str(enter_dob.get())
		 st_adhr= str(enter_sadhr.get())
		 st_cntct= str(enter_scntct.get())
		 st_eml= str(enter_seml.get())

		 ft_name= str(enter_ftn.get())
		 ft_cntct= str(enter_fcntct.get())
		 ft_adhr= str(enter_fadhr.get())
		 ft_eml= str(enter_feml.get())

		 mt_name= str(enter_mtn.get())
		 mt_cntct= str(enter_mcntct.get())
		 mt_adhr= str(enter_madhr.get())
		 mt_eml= str(enter_meml.get())
	
		 df_row = pd.DataFrame([[st_name, st_class, st_sec, st_dob, st_adhr, st_cntct, st_eml, ft_name, ft_cntct, ft_adhr, ft_eml, mt_name, mt_cntct, mt_adhr, mt_eml]], columns= st_col) 
		 df_st = pd.concat([df_st,df_row])
		 df_st.reset_index(drop=True, inplace=True)	
		 df_st.to_csv('data.csv',columns=st_col,index=False)
	 #Extracting data from entryboxes

	 st_name= str(enter_stn.get())
	 st_class= str(enter_class.get())
	 st_sec= str(enter_sec.get())
	 st_dob= str(enter_dob.get())
	 st_adhr= str(enter_sadhr.get())
	 st_cntct= str(enter_scntct.get())
	 st_eml= str(enter_seml.get())

	 ft_name= str(enter_ftn.get())
	 ft_cntct= str(enter_fcntct.get())
	 ft_adhr= str(enter_fadhr.get())
	 ft_eml= str(enter_feml.get())

	 mt_name= str(enter_mtn.get())
	 mt_cntct= str(enter_mcntct.get())
	 mt_adhr= str(enter_madhr.get())
	 mt_eml= str(enter_meml.get())

	 button_submit= Button(frame_entry, text= "Submit", command=button_submit, bg="#F9D6B1", font=("Times", 13))
	 button_submit.place(relx=0.58, rely=0.91, relwidth=0.08, relheight=0.085 )




 
  
def button_editR():
        return
        
        
	



def button_removeR():
        return
	

def button_record():
        return
	 








#Home page 

frame_1= Frame(root, bg= "#F3B48B")
frame_1.place(relx=0, rely= 0.3, relwidth= 1, relheight= 0.7)

button_entry= Button(frame_1, text="Make an Entry", command=button_entry, bg= "#F9D6B1", font=("Times", 13))
button_entry.place(relx=0.2, rely= 0.3, relwidth= 0.25, relheight= 0.15)

button_editR= Button(frame_1, text="Edit Record", command=button_editR, bg= "#F9D6B1", font=("Times", 13))
button_editR.place(relx=0.6, rely= 0.3, relwidth= 0.25, relheight= 0.15)

button_removeR= Button(frame_1, text="Remove Record", command=button_removeR, bg= "#F9D6B1", font=("Times", 13))
button_removeR.place(relx=0.2, rely= 0.6, relwidth= 0.25, relheight= 0.15)

button_record= Button(frame_1, text="View Records", command=button_record, bg= "#F9D6B1", font=("Times", 13))
button_record.place(relx=0.6, rely= 0.6, relwidth= 0.25, relheight= 0.15)












root.mainloop()
