# -*- coding: utf-8 -*-
"""
Created on :10-02-2020
last modified:10-02-2020
@author: anil durgam
version:1.0.2
example:MM32 microcontroller drop down menu
"""

# ****************************library import sections****************
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as tkMessageBox
import sqlite3

# from PIL import ImageTk, Image
# from pprint import pprint
# scr = Tk()
path = 'F:\my_workspace\python_workspace\onyx-logo.png'

mc_list = {
    1: {
        'id': 'MM32f003NW',
        'processor': 'ARM Cortex M0',
        'frequency': '48',
        'flash': '16',
        'ram': '2',
        "gpio": "16",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "8x12bit",
        "eeprom": "0",
        "pack": "QFN20",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""

    },
    2: {
        "id": "MM32f003TW",
        "processor": "ARM Cortex M0",
        "frequency": "48",
        "flash": "16",
        "ram": "2",
        "gpio": "16",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "-",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "8x12bit",
        "eeprom": "0",
        "pack": "TSSOP20",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    ###############################################################
    # MM32f031 controller starte
    ###################################################################
    3: {
        "id": "MM32F031F4P6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "16",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "-",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "9x12bit",
        "eeprom": "",
        "pack": "TSSOP20",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    4: {
        "id": "MM32F031F4U6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "16",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "9x12bit",
        "eeprom": "",
        "pack": "QFN20",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    5: {
        "id": "MM32f031K4U6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    6: {
        "id": "MM32f031K4T6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "25",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "-",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "-",
        "pack": "LQFP32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    7: {
        "id": "MM32f031C4T6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "39",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    8: {
        "id": "MM32f031K4U6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    9: {
        "id": "MM32f031K4U6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    10: {
        "id": "MM32f031K4U6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    11: {
        "id": "MM32f031K4U6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    12: {
        "id": "MM32f031K4U6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    13: {
        "id": "MM32f031K4U6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    14: {
        "id": "MM32f031K4U6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    15: {
        "id": "MM32f031K4U6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    16: {
        "id": "MM32f031K4U6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    17: {
        "id": "MM32f031K4U6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    18: {
        "id": "MM32f031K4U6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    ############################################################################
    ##------------------MM32F032-----
    ##-------------total 8 controllers available------
    #############################################################################
    19: {
        "id": "MM32f032K4U6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    20: {
        "id": "MM32f032K4U6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    21: {
        "id": "MM32f032K4U6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    22: {
        "id": "MM32f032K4U6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    23: {
        "id": "MM32f032K4U6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    24: {
        "id": "MM32f032K4U6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    25: {
        "id": "MM32f032K4U6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    26: {
        "id": "MM32f032K4U6",
        "processor": "ARM Cortex M0",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    #########################################################
    ##------------------------MM32F103---cortext-m3
    ##
    ########################################################
    27: {
        "id": "MM32f103K4U6",
        "processor": "ARM Cortex M3",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    28: {
        "id": "MM32F103K4U6",
        "processor": "ARM Cortex M3",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    29: {
        "id": "MM32F103K4U6",
        "processor": "ARM Cortex M3",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    },
    30: {
        "id": "MM32F103K4U6",
        "processor": "ARM Cortex M3",
        "frequency": "72",
        "flash": "16",
        "ram": "4",
        "gpio": "27",
        "adv_tm": "1",
        "gptm": "5",
        "wdg": "2",
        "rtc": "",
        "uart": "1",
        "i2c": "1",
        "spi": "1",
        "adc": "10x12bit",
        "eeprom": "",
        "pack": "QFN32",
        "dac": "",
        "usb": "",
        "can": "",
        "sdio": "",
        "comp": "",
        "aes": "",
        "trng": ""
    }

}



class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Micro controller Selector")
        tk.Label(main_window, text="MM32 microcontroller selected", fg="blue", font="Times").pack()

        self.combo = ttk.Combobox(self)
        self.combo.place(x=50, y=120)
        self.combo["values"] = ["MM32F003NW",
                                "MM32F003TW",
                                "MM32F031F4P6",
                                "MM32F031K4U6",
                                "MM32F031K4T6",
                                "MM32F031C4T6",
                                "MM32F031F6P6",
                                "MM32F031F6U6",
                                "MM32F031K6U6",
                                "MM32F031K6T6",
                                "MM32F031C6T6",
                                "MM32L", "MM32W", "MM32SPIN", "MM32P"]
        self.combo.bind("<<ComboboxSelected>>", self.selection_changed)
        main_window.configure(width=1024, height=500)
        self.place(width=300, height=300)

    def details(processor,frequency,flash,ram,gpio,adv_tm,gptm,wdg,rtc,uart,i2c,spi,adc,eeprom="-",pack="-",dac="-",usb="",can="",sdio=0,comp=0,aes=0,trng=0,**para):
        T.insert(tk.END, "===========================================================================\n")
        T.insert(tk.END, "Max speed in hz\t\tFLASH\t\tRAM\t\tGPIO\n")
        T.insert(tk.END, "=========================================================================\n")
        T.insert(tk.END,"PROCESSOR::======>{}\n".format(processor))
        T.insert(tk.END,"Frequency Max speed ::====>{}Mhz\n".format(frequency))
        T.insert(tk.END,"FLASH::====>{}KBytes\n".format(flash))
        T.insert(tk.END,"RAM::====>{}KBytes\n".format(ram))
        T.insert(tk.END,"GPIO::====>{}Pins\n".format(gpio))
        T.insert(tk.END,"Advanced timer::====>{}\n".format(adv_tm))
        T.insert(tk.END,"GPTM::====>{}\n".format(gptm))
        T.insert(tk.END,"WDG::====>{}\n".format(wdg))
        T.insert(tk.END,"RTC::====>{}\n".format(rtc))
        T.insert(tk.END,"UART::====>{}\n".format(uart))
        T.insert(tk.END,"I2C::====>{}\n".format(i2c))
        T.insert(tk.END,"SPI::====>{}\n".format(spi))
        T.insert(tk.END,"ADC::====>{}x12bit\n".format(adc))
        T.insert(tk.END,"EEPROM::====>{}KBytes\n".format(eeprom))
        T.insert(tk.END,"PACk::====>{}\n".format(pack))
        T.insert(tk.END,"DAC::====>{}\n".format(dac))
        T.insert(tk.END,"USB::====>{}\n".format(usb))
        T.insert(tk.END,"CAN::====>{}\n".format(can))
        T.insert(tk.END,"SDIO::====>{}\n".format(sdio))
        T.insert(tk.END,"COMP::====>{}\n".format(comp))
        T.insert(tk.END,"AES::====>{}\n".format(aes))
        T.insert(tk.END,"TRNG::====>{}\n".format(trng))
        T.insert(tk.END,"===========================================================================\n")

    def micro_controller_details():
        row_items = 5
        d = 1
        for i in range(0, 30):
            microcontroller = Label(master, text=mc_list[d]['id'], bg="#142E54", fg="white", font="Lato 8 bold",
                                    padx="5", pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=0,
                                                                                             sticky=N + S + E + W)
            processor = Label(master, text=mc_list[d]['processor'], bg="#142E54", fg="white", font="Lato 8 bold",
                              padx="5", pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=1,
                                                                                       sticky=N + S + E + W)
            frequency = Label(master, text=mc_list[d]['frequency'], bg="#142E54", fg="white", font="Lato 8 bold",
                              padx="5", pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=2,
                                                                                       sticky=N + S + E + W)
            flash = Label(master, text=mc_list[d]["flash"], bg="#142E54", fg="white", font="Lato 8 bold", padx="5",
                          pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=3, sticky=N + S + E + W)
            ram = Label(master, text=mc_list[d]["ram"], bg="#142E54", fg="white", font="Lato 8 bold", padx="5",
                        pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=4, sticky=N + S + E + W)
            gpio = Label(master, text=mc_list[d]["gpio"], bg="#142E54", fg="white", font="Lato 8 bold", padx="5",
                         pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=5, sticky=N + S + E + W)
            adv_tm = Label(master, text=mc_list[d]["adv_tm"], bg="#142E54", fg="white", font="Lato 8 bold", padx="5",
                           pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=6, sticky=N + S + E + W)
            gptm = Label(master, text=mc_list[d]["gptm"], bg="#142E54", fg="white", font="Lato 8 bold", padx="5",
                         pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=7, sticky=N + S + E + W)
            wdg = Label(master, text=mc_list[d]["wdg"], bg="#142E54", fg="white", font="Lato 8 bold", padx="5",
                        pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=8, sticky=N + S + E + W)
            rtc = Label(master, text=mc_list[d]["rtc"], bg="#142E54", fg="white", font="Lato 8 bold", padx="5",
                        pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=9, sticky=N + S + E + W)
            uart = Label(master, text=mc_list[d]["uart"], bg="#142E54", fg="white", font="Lato 8 bold", padx="5",
                         pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=10, sticky=N + S + E + W)
            i2c = Label(master, text=mc_list[d]["i2c"], bg="#142E54", fg="white", font="Lato 8 bold", padx="5",
                        pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=11, sticky=N + S + E + W)
            spi = Label(master, text=mc_list[d]["spi"], bg="#142E54", fg="white", font="Lato 8 bold", padx="5",
                        pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=12, sticky=N + S + E + W)
            adc = Label(master, text=mc_list[d]["adc"], bg="#142E54", fg="white", font="Lato 8 bold", padx="5",
                        pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=13, sticky=N + S + E + W)
            eeprom = Label(master, text=mc_list[d]["eeprom"], bg="#142E54", fg="white", font="Lato 8 bold", padx="5",
                           pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=14,
                                                                          sticky=N + S + E + W)
            pack = Label(master, text=mc_list[d]["pack"], bg="#142E54", fg="white", font="Lato 8 bold", padx="5",
                         pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=15, sticky=N + S + E + W)
            dac = Label(master, text=mc_list[d]["dac"], bg="#142E54", fg="white", font="Lato 8 bold", padx="5",
                        pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=16, sticky=N + S + E + W)
            usb = Label(master, text=mc_list[d]["usb"], bg="#142E54", fg="white", font="Lato 8 bold", padx="5",
                        pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=17, sticky=N + S + E + W)
            can = Label(master, text=mc_list[d]["can"], bg="#142E54", fg="white", font="Lato 8 bold", padx="5",
                        pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=18, sticky=N + S + E + W)
            sdio = Label(master, text=mc_list[d]["sdio"], bg="#142E54", fg="white", font="Lato 8 bold", padx="5",
                         pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=19, sticky=N + S + E + W)
            comp = Label(master, text=mc_list[d]["comp"], bg="#142E54", fg="white", font="Lato 8 bold", padx="5",
                         pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=20, sticky=N + S + E + W)
            aes = Label(master, text=mc_list[d]["aes"], bg="#142E54", fg="white", font="Lato 8 bold", padx="5",
                        pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=21, sticky=N + S + E + W)
            trng = Label(master, text=mc_list[d]["trng"], bg="#142E54", fg="white", font="Lato 8 bold", padx="5",
                         pady="5", borderwidth=2, relief="groove").grid(row=row_items, column=22, sticky=N + S + E + W)
            row_items = row_items + 1
            d = d + 1

    def selection_changed(self, event):
        #print("your selected::", self.combo.get())
        if self.combo.get() == "MM32F003NW":
            # print("mm32f submenu displayed here\n")
            #T.insert(tk.END, "MM32F Family is selected\n")
            self.combo = ttk.Combobox(self)
            self.combo.place(x=50, y=160)
            #self.combo["values"] = ["MM32F003", "MM32F031", "MM32F032", "MM32F103"]
            #self.combo.bind("<<ComboboxSelected>>", self.selection_changed)
            self.combo.bind("<<ComboboxSelected>>", self.details("ARM Cortex M0",48,16,2,16,1,5,2,1,1,1,8,"QFN20"))

        elif self.combo.get() == "MM32F003TW":
            # print("mm32f submenu displayed here\n")
            #T.insert(tk.END, "MM32F Family is selected\n")
            self.combo = ttk.Combobox(self)
            self.combo.place(x=50, y=160)
            #self.combo["values"] = ["MM32F003", "MM32F031", "MM32F032", "MM32F103"]
            #self.combo.bind("<<ComboboxSelected>>", self.selection_changed)
            self.combo.bind("<<ComboboxSelected>>", self.details("ARM Cortex M0",48,16,2,16,1,5,2,1,1,1,8,"QFN20"))

        elif self.combo.get() == "MM32F031F4P6":
            # print("mm32L submenu displayed here\n")
            #T.insert(tk.END, "MM32L Family is selected\n")
            #self.combo = ttk.Combobox(self)
            #self.combo.place(x=50, y=160)
            self.combo.bind("<<ComboboxSelected>>", self.details("ARM Cortex M0",48,16,2,16,1,5,2,1,1,1,8,"QFN20"))

        elif self.combo.get() == "MM32W":
            # print("mm32W submenu displayed here\n")
            T.insert(tk.END, "MM32W Family is selected\n")
            #self.combo = ttk.Combobox(self)
            #self.combo.place(x=50, y=160)
            #self.combo["values"] = ["MM32W051", "MM32W062", "MM32W073", "MM32W362"
                #  , "MM32W373", "MM32W384", "MM32W395"]
            #self.combo.bind("<<ComboboxSelected>>", self.micro_controller_details())


        elif self.combo.get() == "MM32SPIN":
            # print("mm32SPIN submenu displayed here\n")
            #T.insert(tk.END, "MM32SPIN Family is selected\n")
            #self.combo = ttk.Combobox(self)
            #self.combo.place(x=50, y=160)
            #self.combo["values"] = ["MM32F003", "MM32F031", "MM32F032", "MM32F103"]
            self.combo.bind("<<ComboboxSelected>>", self.selection_changed)

        else:
            # print("mm32P submenu displayed here\n")
            T.insert(tk.END, "MM32P Family is selected\n")
            self.combo.bind("<<ComboboxSelected>>", self.selection_changed)


# =========================main window start here================================
main_window = tk.Tk()
# lbl.pack()
# pprint(dict(lbl))
# root = tk.Tk()
# T.insert(tk.END, "MM32 main details\navailable here\n")
#main_window.add_command(label="Clear screen", command=clear)
app = Application(main_window)
#app.micro_controller_details(1)
# img2 = ImageTk.PhotoImage(Image.open(path))
# panel = tk.Label(main_window, image = img2)
# panel.pack(side = "bottom", fill = "both", expand = "yes")
# panel.place(x=0,y=0)
T = tk.Text(main_window, width=100, height=30)
T.pack()
app.mainloop()
# ===============================main window end here=====================================





