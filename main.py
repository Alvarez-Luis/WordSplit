import tkinter

root = tkinter.Tk()

def open_frame():
    list = ["abcgefd", "a,ab,abc,abcg,b,c,dog,e,efd,zzzz"]
    list2 = list[1].split(',')
    new_list = []
    len_word = 0
    for data in list2:
        if list[0][0:len(data)] == data:
            #len_word = len(data)
            if list[0][len(data):] in list2:
                len_word = len(data)
    
    if len_word:
        text = list[0][0:len_word]+','+list[0][len_word:]
    else:
        text = 'La cadena no es posible'
    label = tkinter.Label(frame, text=text)
    label.pack()

canvas = tkinter.Canvas(root, height=300, width=500, bg='#263D42')
canvas.pack()

frame = tkinter.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)

openFile = tkinter.Button(root, text='Search in dict', padx=10, pady=5, fg='white', bg='#263D42', command=open_frame)
openFile.pack()

root.mainloop()