# # write a GUI program to design a app
# # Different Fonts & colors
# from tkinter import*
# root=Tk()
# root.geometry("350x100")
# w=Label(root,text="Programming Language",font=40)
# w.pack()
# frame=Frame(root)
# frame.pack()
# bottomframe=Frame(root)
# bottomframe.pack(side=BOTTOM)
# b1_button=Button(frame,text="Python",fg="blue")
# b1_button.pack(side=LEFT)

# b2_button=Button(frame,text="Java",fg="blue")
# b2_button.pack(side=LEFT)

# b3_button=Button(frame,text="C++",fg="blue")
# b3_button.pack(side=LEFT)

# b4_button=Button(frame,text="HTML",fg="blue")
# b4_button.pack(side=BOTTOM)

# b5_button=Button(frame,text="CSS",fg="blue")
# b5_button.pack(side=BOTTOM)


from tkinter import*

# Create the main window
root = Tk()

# Set the initial size of the window
root.geometry("350x100")

# Create a label with a specific text and font
w = Label(root, text="Programming Language", font=("Helvetica", 16))
w.pack()

# Create a frame to contain the buttons
frame = Frame(root)
frame.pack()

# Create another frame at the bottom of the window
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

# Create buttons with different texts and colors, and pack them into the frame
b1_button = Button(frame, text="Python", fg="blue", font=("Arial", 12))
b1_button.pack(side=LEFT)

b2_button = Button(frame, text="Java", fg="blue", font=("Arial", 12))
b2_button.pack(side=LEFT)

b3_button = Button(frame, text="C++", fg="blue", font=("Arial", 12))
b3_button.pack(side=LEFT)

b4_button = Button(bottomframe, text="HTML", fg="blue", font=("Arial", 12))
b4_button.pack(side=BOTTOM)

b5_button = Button(bottomframe, text="CSS", fg="blue", font=("Arial", 12))
b5_button.pack(side=BOTTOM)

# Start the Tkinter event loop
root.mainloop()
