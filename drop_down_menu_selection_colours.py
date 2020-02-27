try:
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
def select():
    sf = "value is %s" % var.get()
    root.title(sf)
    # optional
    color = var.get()
    root['bg'] = color
root = tk.Tk()
# use width x height + x_offset + y_offset (no spaces!)
#root.geometry("%dx%d+%d+%d" % (330, 80, 200, 150))
root.geometry("1024x768")
root.title("MM32_MICROCONTROLLER_DATA")
root.configure(background="light green")
#root.config(width=20, font=('Helvetica', 15))
var = tk.StringVar(root)


# initial value
var.set('MM32_SERIES')
MainMenu = ['MM32F_SERIES', 'MM32L_SERIES', 'MM32SPIN_SERIES', 'MM32W_SERIES','MM32P_SERIES']
#if var.set('MM32F_SERIES')=='MM32F_SERIES'
#print(var.set('MM32F_SERIES'))
SubMenu1 = ['MM32F003', 'MM32F031', 'MM32F032', 'MM32F103']
SubMenu2 = ['MM32L050', 'MM32L051', 'MM32L052', 'MM32L061','MM32L062','MM32L072','MM32L073']

option1 = tk.OptionMenu(root, var, *MainMenu)
option1.pack(side='left', padx=1, pady=1)
#print(option1)
#print("option selected is \n",option1)
#
option2 = tk.OptionMenu(root, var, *SubMenu1)
option2.pack(side='left', padx=1, pady=1)
#var= tk.StringVar(root)
#
option3 = tk.OptionMenu(root, var, *SubMenu2)
option3.pack(side='left', padx=1, pady=1)
#var = tk.StringVar(root)

button = tk.Button(root, text="SUBMIT", command=select)
button.pack(side='left', padx=20, pady=1)
root.mainloop()