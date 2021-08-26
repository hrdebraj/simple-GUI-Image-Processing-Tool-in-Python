from tkinter import *
from PIL import Image, ImageFilter, ImageDraw, ImageFont
from PIL.ImageFilter import (EDGE_ENHANCE, CONTOUR)

""" 
                    This Code is Written by 
                        Debraj Basak 
    (CEH v11 , CCNA 3.0 , CPENT , NPT , WAPT , RE & MA) 
Cyber Security Research Analyst at ISOAH Data Securities Pvt. Ltd.


"""

p = Tk()
p.title("Image Processing Tools by Debraj Basak")
p.geometry("500x700")
p['bg'] = "#3CF0A1"

fname_var = StringVar()

wname_var = StringVar()
ftname_var = StringVar()


def newWindow():
    q = Toplevel(p)
    q.geometry("500x330")
    q.title("Water Marking Section")
    q.resizable(False, False)
    q['bg'] = "#F1C245"

    Label(q, text="Water Marking Section", font=("Roboto", 20, "bold"), fg="red", padx=10, pady=10).place(x=79,
                                                                                                          y=20)

    Label(q, text="Enter the Text", font=("Roboto", 15, "bold"), fg="black", padx=5, pady=5).place(x=20, y=120)
    Entry(q, textvariable=wname_var, font=("Roboto", 15, "normal"), fg="black").place(x=200, y=125)

    Label(q, text="Enter the Font", font=("Roboto", 15, "bold"), fg="black", padx=5, pady=5).place(x=20, y=180)
    Entry(q, textvariable=ftname_var, font=("Roboto", 15, "normal"), fg="black").place(x=200, y=185)

    btn = Button(q, text="Click to Insert", font=("Roboto", 15, "bold"), fg="white", bg="red", padx=5, pady=5,
                 command=watermark).place(
        x=165, y=250)

    q.mainloop()


new_name_var = StringVar()


def newWindow2():
    q = Toplevel(p)
    q.geometry("500x330")
    q.title("Image Merging Section")
    q.resizable(False, False)
    q['bg'] = "#F1C245"

    Label(q, text="Image Merging Section", font=("Roboto", 20, "bold"), fg="red", padx=10, pady=10).place(x=79,
                                                                                                          y=20)

    Label(q, text="Enter other Image", font=("Roboto", 15, "bold"), fg="black", padx=5, pady=5).place(x=20, y=120)
    Entry(q, textvariable=new_name_var, font=("Roboto", 15, "normal"), fg="black").place(x=230, y=125)

    btn = Button(q, text="Click to Merge", font=("Roboto", 15, "bold"), fg="white", bg="red", padx=5, pady=5,
                 command=merge).place(
        x=165, y=220)

    q.mainloop()


height_var = IntVar()
width_var = IntVar()


def newWindow3():
    q = Toplevel(p)
    q.geometry("500x330")
    q.title("Image Resizer Section")
    q.resizable(False, False)
    q['bg'] = "#F1C245"

    Label(q, text="Image Resizer Section", font=("Roboto", 20, "bold"), fg="red", padx=10, pady=10).place(x=79,
                                                                                                          y=20)

    Label(q, text="Enter the Height", font=("Roboto", 15, "bold"), fg="black", padx=5, pady=5).place(x=20, y=120)
    Entry(q, textvariable=height_var, font=("Roboto", 15, "normal"), fg="black").place(x=230, y=125)
    Label(q, text="Enter the width", font=("Roboto", 15, "bold"), fg="black", padx=5, pady=5).place(x=20, y=180)
    Entry(q, textvariable=width_var, font=("Roboto", 15, "normal"), fg="black").place(x=230, y=185)
    btn = Button(q, text="Click to Resize", font=("Roboto", 15, "bold"), fg="white", bg="red", padx=5, pady=5,
                 command=resize).place(
        x=165, y=240)

    q.mainloop()


def blur():
    fname = fname_var.get()
    img = Image.open(fname)
    img.show()
    bl_img = img.filter(ImageFilter.GaussianBlur(5))
    bl_img.show()
    s_name = f"new-{fname}"
    bl_img.save(s_name)


def e_enhance():
    fname = fname_var.get()
    img = Image.open(fname)
    img.show()
    bl_img = img.filter(EDGE_ENHANCE)
    bl_img.show()
    s_name = f"new-{fname}"
    bl_img.save(s_name)


def contour():
    fname = fname_var.get()
    img = Image.open(fname)
    img.show()
    bl_img = img.filter(CONTOUR)
    bl_img.show()
    s_name = f"new-{fname}"
    bl_img.save(s_name)


def watermark():
    wname = wname_var.get()
    fname = fname_var.get()
    ftname = ftname_var.get()

    img = Image.open(fname)
    img.show()
    width, height = img.size

    draw = ImageDraw.Draw(img)
    txt = wname

    font = ImageFont.truetype(ftname, 28)
    t_width, t_height = draw.textsize(txt, font)

    margin = 10
    x = width - t_width - margin
    y = height - t_height - margin

    draw.text((x, y), txt, font=font)
    img.show()
    name = f"watermark-{fname}"
    img.save(name)


def merge():
    fname = fname_var.get()
    new_name = new_name_var.get()

    img1 = Image.open(fname)
    img1.show()
    img2 = Image.open(new_name)
    img2.show()

    img1 = img1.resize((600, 450))
    img2 = img2.resize((600, 450))

    img1_size = img1.size
    img2_size = img2.size

    new_img = Image.new('RGB', (2 * img1_size[0], img1_size[1]), (250, 250, 250))  # (format, (size , info) , color)

    new_img.paste(img1, (0, 0))
    new_img.paste(img2, (img1_size[0], 0))

    d = f"merged-{new_name}&{fname}"
    new_img.save(d)
    new_img.show()


def resize():
    height = height_var.get()
    width = width_var.get()
    fname = fname_var.get()

    img = Image.open(fname)
    img.show()

    r_img = img.resize((width, height))
    r_img.show()
    r_img.save(f"Resized-{fname}")


Label(p, text="Image Processing Tool", font=("Pacifico.ttf", 20, "bold"), fg="red", padx=10, pady=10).place(x=79, y=20)

Label(p, text="Enter Your Image Name", font=("Roboto", 15, "bold"), fg="black", padx=5, pady=5).place(x=20, y=120)
Entry(p, textvariable=fname_var, font=("Roboto", 15, "normal"), fg="black").place(x=265, y=125)
Label(p, text="Blur", font=("Roboto", 15, "bold"), fg="black", padx=5, pady=5).place(x=20, y=190)

btn1 = Button(p, text="Click Me", font=("Roboto", 15, "bold"), fg="white", bg="red", padx=5, pady=5,
              command=blur).place(
    x=275, y=180)

Label(p, text="Edge Enhance", font=("Roboto", 15, "bold"), fg="black", padx=5, pady=5).place(x=20, y=260)

btn2 = Button(p, text="Click Me", font=("Roboto", 15, "bold"), fg="white", bg="red", padx=5, pady=5,
              command=e_enhance).place(
    x=275, y=250)

Label(p, text="Contour", font=("Roboto", 15, "bold"), fg="black", padx=5, pady=5).place(x=20, y=330)

btn3 = Button(p, text="Click Me", font=("Roboto", 15, "bold"), fg="white", bg="red", padx=5, pady=5,
              command=contour).place(
    x=275, y=320)

Label(p, text="Add Water-Mark", font=("Roboto", 15, "bold"), fg="black", padx=5, pady=5).place(x=20, y=400)

btn4 = Button(p, text="Click Me", font=("Roboto", 15, "bold"), fg="white", bg="red", padx=5, pady=5,
              command=newWindow).place(
    x=275, y=390)

Label(p, text="Merge With Other Image", font=("Roboto", 15, "bold"), fg="black", padx=5, pady=5).place(x=20, y=470)

btn5 = Button(p, text="Click Me", font=("Roboto", 15, "bold"), fg="white", bg="red", padx=5, pady=5,
              command=newWindow2).place(
    x=275, y=460)

Label(p, text="Resize Image", font=("Roboto", 15, "bold"), fg="black", padx=5, pady=5).place(x=20, y=550)

btn6 = Button(p, text="Click Me", font=("Roboto", 15, "bold"), fg="white", bg="red", padx=5, pady=5,
              command=newWindow3).place(
    x=275, y=540)

Label(p, text="Made with   \u2764\ufe0fby Debraj Basak", font=("Roboto", 10, "bold"), fg="red", padx=5, pady=5).place(
    x=125, y=650)

p.mainloop()
