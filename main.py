from tkinter import *
IMAGE_HEIGHT = 400

window = Tk()
window.title('catto bop')
window.config(padx=0, pady=0)

canvas = Canvas(width=820, height=850)
catto_close_img = PhotoImage(file='catto close.png')
catto = canvas.create_image((410, IMAGE_HEIGHT), image=catto_close_img)
canvas.grid(column=0, row=0)
catto_bop_img = PhotoImage(file='catto bop.png')


def feed_catto():
    make_image(catto)


def make_image(catto):
    catto = canvas.create_image((410, IMAGE_HEIGHT), image=catto_bop_img)
    window.after(250, reset)

def reset():
    global catto
    catto = canvas.create_image((410, IMAGE_HEIGHT), image=catto_close_img)


button = Button(text='feed me', command=feed_catto, highlightthickness=0)
button.grid(column=0, row=1)






window.mainloop()
