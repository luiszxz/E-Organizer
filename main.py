#-----------------------------------------------------------------------------------------------------------------------
# Core GUI Libraries
from tkinter import *
from tkinter import ttk          # Theme extension for Combobox widget
from tkinter import filedialog   # Dialog for folder selection
from tkinter import messagebox   # Dialog for alerts (Exit, Success, Error)

# System and File Operations
import os        # Used for path manipulation (join, isfile, listdir)
import shutil    # Used for high-level file operations (moving files)

#-----------------------------------------------------------------------------------------------------------------------

class Organizer_App:
    # The constructor method, called when an object of the class is created
    def __init__(self, root):
        self.root = root

        # title of the window
        #self.root.title(" E-Organizer Application")
        #self.root.geometry("1300x650+0+0")
        #self.root.resizable(False, False)

        # Change the color of the window background
        self.root.config(bg="#5eb6f1")

        # close the mini,exit,resize
        # Makes the window borderless and removes the standard minimize/maximize/close buttons
        self.root.overrideredirect(True)  # forclose,mini off
# -----------------------------------------------------------------------------------------------------------------------


        # --------------------------------------- CENTER -----------------------------------------------------------------
        window_width = 850
        window_height = 635

        # Get screen dimensions
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate coordinates for centering
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)

        # Set the geometry: width x height + x_offset + y_offset
        root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
        # --------------------------------------------------------------------------------------------------------------


        # --------------------------------------- HEADED PHOTO-----------------------------------------------------------
        # Load images (assuming these files exist in a "LOGO" directory)
        self.logo_icon = PhotoImage(file="LOGO/Logo.png")
        self.logo_icon1 = PhotoImage(file="LOGO/search_icon1.png")
        # --------------------------------------------------------------------------------------------------------------


        # --------------------------------------- HEADED LOGO AND TITLTE ------------------------------------------------
        # Dark blue header bar at the top
        title = Label(self.root, text="  ", padx=260, image=self.logo_icon, compound=LEFT, font=("impact", 25),bg="#204b8e",
        fg="white", anchor="w").place(x=0, y=0, relwidth=1)

        TITLE = Label(self.root, text="E-Organizer", font=("impact", 40), bg="#204b8e", fg="white").place(x=350, y=5)
        # --------------------------------------------------------------------------------------------------------------


        # ---------------------------------------- CODE FOR BROWSE DIRECTORY---------------------------------------------
        # A Tkinter variable to hold the path of the folder selected by the user
        self.brow_folder = StringVar()
        # --------------------------------------------------------------------------------------------------------------


        # ------------------------------------ SELECT FOLDER TEXT AND PATH DISPLAY BOX ----------------------------------
        # Label for "Select Folder"
        select_folder_text = Label(self.root, text="Select Folder", font=("times new roman", 20, "bold"), fg="white",
        bg="#5eb6f1").place(x=20, y=102)

        # Entry widget to display the selected folder path
        # state="readonly" prevents the user from typing in the path manually
        tiles_browse = Entry(self.root, textvariable=self.brow_folder, font=("times new roman", 10), state="readonly",
        bg="lightyellow").place(x=185, y=100, height=32, width=500)

        # Icon placed inside the path display box
        logo = Label(self.root, image=self.logo_icon1, fg="black").place(x=648, y=101)
        # --------------------------------------------------------------------------------------------------------------


        # ---------------------------------- BROWSE BUTTON ---------------------------------------------------------------

        # Button that calls the self.func_browse method to open the directory selection dialog
        browse_button = Button(self.root, command=self.func_browse, text="BROWSE", font=("times new roman", 15, "bold"),
        bg="#f0ad4e", fg="white",cursor="hand2", activebackground="#204b8e", activeforeground="black").place(x=700, y=100,height=32,width=130)

        # A horizontal separator line
        line = Label(self.root, bg="#204b8e").place(x=0, y=145, height=2, width=1550)
        # --------------------------------------------------------------------------------------------------------------


        # ---------------------------------- DEFINED EXTENSION FORMATS ------------------------------------------------------------
        # Lists of supported extensions for each category, including a title for the Combobox
        self.audio_extension = ["Audio Extension",".aac", ".aiff", ".au", ".flac", ".mp3", ".wv",".wav", ".wma"]
        self.doc_extension   = ["Document Extension",".bin", ".doc", ".docx", ".html", ".htm", ".odt",".pdf", ".ppt", ".pptx", ".txt", ".xlsx", ".xls"]
        self.image_extension = ["Image Extension", ".bmp", ".gif", ".jpg", ".jpeg", ".png",  ".psd", ".raw", ".tif", ".tiff" ]
        self.video_extension = ["Video Extension", ".avi", ".f4v", ".fiv", ".mp4", ".mpeg4", ".mkv",".mov",".wmv", ".webm"]
        # --------------------------------------------------------------------------------------------------------------


        # ----------------------------------- MAPPING FOLDER NAMES TO EXTENSIONS ----------------------------------------------------
        # Dictionary that maps the target folder name (key) to its list of extensions (value)
        self.folders = {
            'Audios': self.audio_extension,
            'Documents': self.doc_extension,
            'Images': self.image_extension,
            'Videos': self.video_extension,
        }
        # --------------------------------------------------------------------------------------------------------------




        # ----------------------------------- EXTENSION COMBO BOXES (READ-ONLY DROPDOWNS) ------------------------------------------------------------------
        # Label for "Supported Extension"
        Extension_txt = Label(self.root, text="Supported Extension", font=("times new roman", 20), fg="white",bg="#5eb6f1").place(x=20, y=160)

        # Audio Combobox
        self.audio_box = ttk.Combobox(self.root, values=self.audio_extension, state="readonly", justify=CENTER,font=("times new roman", 10,"bold"))
        self.audio_box.place(x=20, y=210, width=180, height=30)
        self.audio_box.current(0)

        # Document Combobox
        self.doc_box = ttk.Combobox(self.root, values=self.doc_extension, state="readonly", justify=CENTER,font=("times new roman", 10,"bold"))
        self.doc_box.place(x=230, y=210, width=180, height=30)
        self.doc_box.current(0)

        # Images Combobox
        self.image_box = ttk.Combobox(self.root, values=self.image_extension, state="readonly", justify=CENTER,font=("times new roman", 10,"bold" ))
        self.image_box.place(x=438, y=210, width=180, height=30)
        self.image_box.current(0)

        # Video Combobox
        self.video_box = ttk.Combobox(self.root, values=self.video_extension, state="readonly", justify=CENTER,font=("times new roman", 10,"bold"))
        self.video_box.place(x=650, y=210, width=180, height=30)
        self.video_box.current(0)
        # --------------------------------------------------------------------------------------------------------------


        # ---------------------------------- LOAD EXTENSION IMAGE ICONS --------------------------------------------------------
        self.image_icon = PhotoImage(file="Extension_icon/gall.png")
        self.video_icon = PhotoImage(file="Extension_icon/video.png")
        self.audio_icon = PhotoImage(file="Extension_icon/audio.png")
        self.doc_icon = PhotoImage(file="Extension_icon/doc.png")
        self.other_icon = PhotoImage(file="Extension_icon/others.png")
        # --------------------------------------------------------------------------------------------------------------


        # ----------------------------------- LOAD EXTENSION IMAGE ICONS  ----------------------------------------------------------
        self.totalfile_icon = PhotoImage (file="Status_icon/total_file.png")
        self.moved_icon = PhotoImage(file="Status_icon/move.png")
        self.left_icon = PhotoImage(file="Status_icon/left.png")
        self.total_icon = PhotoImage(file="Status_icon/total.png")
        # --------------------------------------------------------------------------------------------------------------


        # ---------------------------------- FRAME CONTAINER FOR CATEGORY AND STATUS BOXES ------------------------------------------------------------------
        # A container Frame to group and place the status labels
        Frame1 = Frame(self.root, bg="#5eb6f1")
        Frame1.place(x=5, y=245, width=1334, height=450)
        # --------------------------------------------------------------------------------------------------------------


        # --------------------------- AUDIO, DOCUMENT, IMAGE, VIDEO, OTHERS CATEGORY BOXES -------------------------------------------------
        # Labels to display the count of files for each category. They use an icon (compound=TOP) and a text label.
        self.Audio_total = Label(Frame1, image=self.audio_icon, compound=TOP,font=("times new roman", 12, "bold"), bg="#204b8e", fg="white")
        self.Audio_total.place(x=15, y=10, width=140, height=110)

        self.Doc_total = Label(Frame1, image=self.doc_icon, compound=TOP,font=("times new roman", 12, "bold"), bg="#204b8e", fg="white")
        self.Doc_total.place(x=180, y=10, width=140, height=110)

        self.Image_total = Label(Frame1, image=self.image_icon, compound=TOP,font=("times new roman", 12, "bold"), bg="#204b8e", fg="white")
        self.Image_total.place(x=350, y=10, width=140, height=110)

        self.Video_total = Label(Frame1, image=self.video_icon, compound=TOP,font=("times new roman", 12, "bold"), bg="#204b8e", fg="white")
        self.Video_total.place(x=520, y=10, width=140, height=110)

        self.Other_total = Label(Frame1, image=self.other_icon, compound=TOP,font=("times new roman", 12, "bold"), bg="#204b8e", fg="white")
        self.Other_total.place(x=685, y=10, width=140, height=110)
        # --------------------------------------------------------------------------------------------------------------


        # --------------------------------------- STATUS BOXES (TOTAL, MOVED, LEFT) ---------------------------------------------
        #Status text
        self.status_txt = Label(self.root, text="Status", font=("times new roman", 20),fg="white" , bg="#5eb6f1").place(x=20, y=380)

        # Total Files label (Total files found in the directory)
        self.total_file = Label(Frame1, image=self.totalfile_icon,compound=TOP, font=("times new roman", 12,"bold"), bg="#204b8e", fg="white")
        self.total_file.place(x=15, y=180, width=140, height=110)

        # Total Moved label (Count of files successfully moved during organization)
        self.total_moved=Label(Frame1,font=("times new roman", 12),image=self.moved_icon,compound=TOP, bg="#204b8e", fg="white")
        self.total_moved.place(x=180, y=180, width=140, height=110)

        # Total Left label (Count of files remaining to be moved)
        # Note: This placement is using root coordinates instead of Frame1, which might affect resizing/layout
        self.total_left=Label(self.root,font=("times new roman", 12),image=self.left_icon,compound=TOP, bg="#204b8e",fg="white")
        self.total_left.place(x=350, y=425, width=140, height=110)

        # 'Totals' - Used for displaying the overall total count (redundant with total_file?)
        self.totals = Label(self.root, font=("times new roman", 12),image=self.total_icon,compound=TOP, bg="#204b8e", fg="white")
        self.totals.place(x=520, y=425, width=140, height=110)
        # --------------------------------------------------------------------------------------------------------------


        # --------------------------------------- EXIT CONFIRMATION FUNCTION ---------------------------------------------------------
        def exit():
            answer = messagebox.askyesno('Exit', 'Are you sure?')
            if answer:
                root.destroy() # Closes the main window
        # --------------------------------------------------------------------------------------------------------------


        # --------------------------------------- ACTION BUTTONS ----------------------------------------------------------------
        # Start Button - Calls self.start to begin the file organization process
        self.start_button = Button(self.root,command=self.start , text="START", font=("times new roman", 12, "bold"),
        bg="#f0ad4e", fg="white", cursor="hand2", activebackground="#204b8e", activeforeground="white")
        self.start_button.place(x=450, y=570, height=40, width=250)

        # Clear Button - Calls self.clear to reset the UI and selected folder
        self.clear_button = Button(self.root, text="CLEAR", command=self.clear, font=("times new roman", 12, "bold"),
        bg="#f0ad4e",fg="white", cursor="hand2", activebackground="#204b8e", activeforeground="white")
        self.clear_button.place(x=130, y=570, height=40, width=250)

        # Exit Button (the 'X' in the top right, made visible by overrideredirect(True))
        exitButton = Button(root, text="X", fg="White", bg="#204b8e", border=0, command=exit,
        font=('Calibri(Body)', 15, 'bold'))
        exitButton.pack()

        exitButton.place(x=820, y=0)
        # --------------------------------------------------------------------------------------------------------------


    # ----------------------------------- COUNTING EACH FILES FUNCTION ------------------------------------------------------------
    def c_total(self):
        # Initialize counters for each category
        Images=0
        Audios=0
        Videos=0
        Documents=0
        Others=0
        self.count=0 # Total number of files
        list_combine=[] # List to hold all supported extensions for checking 'Others'

        # Loop through all items (files and folders) in the selected directory
        for i in self.all_files:
            # Check if the item is a file (not a folder)
            if os.path.isfile(os.path.join(self.directry, i)) == True:
                self.count+=1
                ext = "." + i.split(".")[-1] # Extract the file extension (e.g., '.jpg')

                # Check the extension against all defined categories
                for folder_name in self.folders.items():
                    # print(folder_name)
                    for x in folder_name[1]:
                        list_combine.append(x)

                        # Check which category the extension belongs to and increment the counter
                    if ext.lower() in folder_name[1] and folder_name[0] == "Images":
                        Images += 1
                    if ext.lower() in folder_name[1] and folder_name[0] == "Audios":
                        Audios += 1
                    if ext.lower() in folder_name[1] and folder_name[0] == "Videos":
                        Videos += 1
                    if ext.lower() in folder_name[1] and folder_name[0] == "Documents":
                        Documents += 1

        # code for other files
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directry, i)) == True:
                ext = "." + i.split(".")[-1]
                if ext.lower() not in list_combine:
                    Others += 1
    # ------------------------------------------------------------------------------------------------------------------





        # ------------------------------ UPDATE UI WITH CALCULATED COUNTS ---------------------------------------------
        # Update the text of the category labels with the counts
        self.Image_total.config(text="Total Images\n" + str(Images))
        self.Video_total.config(text="Total Vidoes\n" + str(Videos))
        self.Audio_total.config(text="Total Audios\n" + str(Audios))
        self.Doc_total.config(text="Total Documents\n" + str(Documents))
        self.Other_total.config(text="Total Others\n" + str(Others))
        self.total_file.config(text="Total Files\n " + str(self.count))
        # --------------------------------------------------------------------------------------------------------------


    # ------------------------------- BROWSE FUNCTION (OPENS DIALOG) --------------------------------------------------------------------
    def func_browse(self):
        # Open the system directory selection dialog
        op = filedialog.askdirectory(title="Select folder for Organizing")
        if op != None: # If a folder was selected (not cancelled)
            self.brow_folder.set(str(op)) # Set the Tkinter variable with the path
            self.directry = self.brow_folder.get() # Store the path locally
            self.other_name = "Others" # Define the folder name for miscellaneous files
            self.rename()

            self.all_files = os.listdir(self.directry) # Get a list of all items (files/folders) in the directory
            length = len(self.all_files)
            count = 1
            self.c_total() # Call the function to count files and update the UI
            self.start_button.config(state=NORMAL)
            # print(self.all_files)
    # --------------------------------------------------------------------------------------------------------------

    # ------------------------------- START ORGANIZATION FUNCTION --------------------------------------------------------------------
    def start(self):
        # Check if a folder has been selected
        if self.brow_folder.get()!="":
            c=0 # Counter for files moved
            for i in self.all_files:
                    if os.path.isfile(os.path.join(self.directry, i)) == True:
                        c += 1
                        self.create(i.split(".")[-1], i)
                        self.totals.config(text="Total: "+str(self.count))
                        self.total_moved.config(text="Moved: " + str(c))
                        self.total_left.config(text="Left: " + str(self.count-c))

                        self.totals.update()
                        self.total_moved.update()
                        self.total_left.update()


            messagebox.showinfo("Success","All files has moved successfully")
            #self.start_button.config(state=DISABLED)
            #self.clear_button.config(state=NORMAL)
        else:
            messagebox.showerror("Error", "Please select folder")
    # --------------------------------------------------------------------------------------------------------------

    # ------------------------------- CLEAR FUNCTION (RESET UI) --------------------------------------------------------------------
    def clear(self):
        # Reset the folder path variable and clear all status and category counts
            #self.start_button.config(state=DISABLED)
            self.brow_folder.set("")
            self.totals.config(text="")
            self.total_moved.config(text="")
            self.total_left.config(text="")
            self.Image_total.config(text="")
            self.Video_total.config(text="")
            self.Audio_total.config(text="")
            self.Doc_total.config(text="")
            self.Other_total.config(text="")
            self.total_file.config(text="")

    def rename(self):
        for folder in os.listdir(self.directry):
            if os.path.isdir(os.path.join(self.directry, folder)) == True:
                os.rename(os.path.join(self.directry, folder), os.path.join(self.directry, folder.lower()))

    def create(self, ext, file_name):
        find = False
        for folder_name in self.folders:
            if "." + ext in self.folders[folder_name]:
                if folder_name not in os.listdir(self.directry):
                    os.mkdir(os.path.join(self.directry, folder_name))
                shutil.move(os.path.join(self.directry, file_name), os.path.join(self.directry, folder_name))
                find = True
                break
        if find != True:
            if self.other_name not in os.listdir(self.directry):
                os.mkdir(os.path.join(self.directry, self.other_name))
            shutil.move(os.path.join(self.directry, file_name), os.path.join(self.directry, self.other_name))
    # --------------------------------------------------------------------------------------------------------------


# -----------------------------------MAIN EXECUTION BLOCK---------------------------------------------------------------
# Create the main Tkinter window
root = Tk()
# Create an instance of the Organizer_App class
obj = Organizer_App(root)
# Start the Tkinter event loop (keeps the window open and responsive)
root.mainloop()