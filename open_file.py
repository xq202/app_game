from tkinter import *
from tkinter import filedialog
import setting

def openFiles():
	filedir = filedialog.askopenfilename(initialdir = "/",
										title = "Select a File",
										filetypes = (("Text files",
														"*.py*"),
													("all files",
														"*.*")))
	
	# Change label contents
	# label_file_explorer.configure(text="File Opened: "+filedir)
	filename = ''
	i = len(filedir)-1
	while(i>=0 and filedir[i]!='/'):
		filename = filedir[i] + filename
		i-=1
	filedir = filedir.replace('/','\\')
	setting.dirfile = filedir
# window  = Tk()
# # Set window title
# window.title('File Explorer')

# # Set window size
# window.geometry("500x500")

# #Set window background color
# window.config(background = "white")

# # Create a File Explorer label
# label_file_explorer = Label(window,
# 							text = "File Explorer using Tkinter",
# 							width = 100, height = 4,
# 							fg = "blue")

	
# button_explore = Button(window,
# 						text = "Browse Files",
# 						command = browseFiles)

# button_exit = Button(window,
# 					text = "Exit",
# 					command = exit)

# # Grid method is chosen for placing
# # the widgets at respective positions
# # in a table like structure by
# # specifying rows and columns
# label_file_explorer.grid(column = 1, row = 1)

# button_explore.grid(column = 1, row = 2)

# button_exit.grid(column = 1,row = 3)

# # Let the window wait for any events
# window.mainloop()
	