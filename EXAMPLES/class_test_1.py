# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 19:16:27 2020

@author: anil durgam
"""

from tkinter import *
import tkinter as tk
#ARM Cortex M0",48,16,2,16,1,5,2,1,1,1,8,0,0,"QFN20"
class micro_controller_details():
    def __init__(self,Microcontroller,Processor,Frequency,Flash,RAM,GPIO,AdvTM,GPTM,WDG,RTC,UART,I2C,
                 SPI,ADC,EEPROM,PACK,DAC,USB,CAN,SDIO,COMP,AES,TRNG):
        self.Microcontroller=Microcontroller#1
        self.Processor=Processor#2
        self.Frequency=Frequency#3
        self.Flash=Flash#4
        self.RAM=RAM#5
        self.GPIO=GPIO#6
        self.AdvTM=AdvTM#7
        self.GPTM=GPTM#8
        self.WDG=WDG#9
        self.RTC=RTC#10
        self.UART=UART#11
        self.I2C=I2C#12
        self.SPI=SPI#13
        self.ADC=ADC#14
        self.EEPROM=EEPROM#15
        self.PACK=PACK#16
        self.DAC=DAC#17
        self.USB=USB#18
        self.CAN=CAN#19
        self.SDIO=SDIO#20
        self.COMP=COMP#21
        self.AES=AES#22
        self.TRNG=TRNG#23
        
    def display(self,row_num):
        
            microcontroller=Label(master,text="Microcontroller",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=0,sticky=N+S+E+W)
            processor=Label(master,text="Processor",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=1,sticky=N+S+E+W)
            frequency=Label(master,text="Frequency",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=2,sticky=N+S+E+W)
            flash=Label(master,text="Flash",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=3,sticky=N+S+E+W)
            ram=Label(master,text="RAM",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=4,sticky=N+S+E+W)
            gpio=Label(master,text="GPIO",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=5,sticky=N+S+E+W)
            adv_tm=Label(master,text="AdvTM",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=6,sticky=N+S+E+W)
            gptm=Label(master,text="GPTM",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=7,sticky=N+S+E+W)
            wdg=Label(master,text="WDG",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=8,sticky=N+S+E+W)
            rtc=Label(master,text="RTC",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=9,sticky=N+S+E+W)
            uart=Label(master,text="UART",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=10,sticky=N+S+E+W)
            i2c=Label(master,text="I2C",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=11,sticky=N+S+E+W)
            spi=Label(master,text="SPI",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=12,sticky=N+S+E+W)
            adc=Label(master,text="ADC",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=13,sticky=N+S+E+W)
            eeprom=Label(master,text="EEPROM",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=14,sticky=N+S+E+W)
            pack=Label(master,text="PACK",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=15,sticky=N+S+E+W)
            dac=Label(master,text="DAC",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=16,sticky=N+S+E+W)
            usb=Label(master,text="USB",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=17,sticky=N+S+E+W)
            can=Label(master,text="CAN",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=18,sticky=N+S+E+W)
            sdio=Label(master,text="SDIO",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=19,sticky=N+S+E+W)
            comp=Label(master,text="COMP",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=20,sticky=N+S+E+W)
            aes=Label(master,text="AES",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=21,sticky=N+S+E+W)
            trng=Label(master,text="TRNG",bg="#142E54",fg="white",font="Lato 10 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=22,sticky=N+S+E+W)
        ##########################################
            row_num=1
            d=1
            for i in range(0,30):
                microcontroller=Label(master,text=mc_list[d]['id'],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=0,sticky=N+S+E+W)
                processor=Label(master,text=mc_list[d]['processor'],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=1,sticky=N+S+E+W)
                frequency=Label(master,text=mc_list[d]['frequency'],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=2,sticky=N+S+E+W)
                flash=Label(master,text=mc_list[d]["flash"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=3,sticky=N+S+E+W)
                ram=Label(master,text=mc_list[d]["ram"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=4,sticky=N+S+E+W)
                gpio=Label(master,text=mc_list[d]["gpio"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=5,sticky=N+S+E+W)
                adv_tm=Label(master,text=mc_list[d]["adv_tm"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=6,sticky=N+S+E+W)
                gptm=Label(master,text=mc_list[d]["gptm"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=7,sticky=N+S+E+W)
                wdg=Label(master,text=mc_list[d]["wdg"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=8,sticky=N+S+E+W)
                rtc=Label(master,text=mc_list[d]["rtc"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=9,sticky=N+S+E+W)
                uart=Label(master,text=mc_list[d]["uart"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=10,sticky=N+S+E+W)
                i2c=Label(master,text=mc_list[d]["i2c"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=11,sticky=N+S+E+W)
                spi=Label(master,text=mc_list[d]["spi"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=12,sticky=N+S+E+W)
                adc=Label(master,text=mc_list[d]["adc"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=13,sticky=N+S+E+W)
                eeprom=Label(master,text=mc_list[d]["eeprom"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=14,sticky=N+S+E+W)
                pack=Label(master,text=mc_list[d]["pack"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=15,sticky=N+S+E+W)
                dac=Label(master,text=mc_list[d]["dac"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=16,sticky=N+S+E+W)
                usb=Label(master,text=mc_list[d]["usb"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=17,sticky=N+S+E+W)
                can=Label(master,text=mc_list[d]["can"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=18,sticky=N+S+E+W)
                sdio=Label(master,text=mc_list[d]["sdio"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=19,sticky=N+S+E+W)
                comp=Label(master,text=mc_list[d]["comp"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=20,sticky=N+S+E+W)
                aes=Label(master,text=mc_list[d]["aes"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=21,sticky=N+S+E+W)
                trng=Label(master,text=mc_list[d]["trng"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_num,column=22,sticky=N+S+E+W)
                row_num=row_num+1
                d=d+1  

mc_list={
          1: {
                'id':'MM32f003NW',
                'processor':'ARM Cortex M0',
                'frequency':'48',
                'flash':'16',
                'ram':'2',
                "gpio":"16",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"8x12bit",
                "eeprom":"0",
                "pack":"QFN20",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                
            },
            2:{
                "id":"MM32f003TW",
                "processor":"ARM Cortex M0",
                "frequency":"48",
                "flash":"16",
                "ram":"2",
                "gpio":"16",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"-",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"8x12bit",
                "eeprom":"0",
                "pack":"TSSOP20",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
###############################################################
#MM32f031 controller starte
###################################################################
             3:{
                "id":"MM32F031F4P6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"16",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"-",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"9x12bit",
                "eeprom":"",
                "pack":"TSSOP20",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
            4:{
                "id":"MM32F031F4U6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"16",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"9x12bit",
                "eeprom":"",
                "pack":"QFN20",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                5:{
                "id":"MM32f031K4U6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                  6:{
                "id":"MM32f031K4T6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"25",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"-",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"-",
                "pack":"LQFP32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                  7:{
                "id":"MM32f031C4T6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"39",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                8:{
                "id":"MM32f031K4U6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                9:{
                "id":"MM32f031K4U6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                10:{
                "id":"MM32f031K4U6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                11:{
                "id":"MM32f031K4U6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                12:{
                "id":"MM32f031K4U6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                13:{
                "id":"MM32f031K4U6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                14:{
                "id":"MM32f031K4U6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                15:{
                "id":"MM32f031K4U6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                16:{
                "id":"MM32f031K4U6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },        
                17:{
                "id":"MM32f031K4U6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                18:{
                "id":"MM32f031K4U6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
############################################################################
##------------------MM32F032-----
##-------------total 8 controllers available------
#############################################################################
                19:{
                "id":"MM32f032K4U6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                20:{
                "id":"MM32f032K4U6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                21:{
                "id":"MM32f032K4U6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                22:{
                "id":"MM32f032K4U6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                        23:{
                "id":"MM32f032K4U6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                                24:{
                "id":"MM32f032K4U6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                                        25:{
                "id":"MM32f032K4U6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                                        26:{
                "id":"MM32f032K4U6",
                "processor":"ARM Cortex M0",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
#########################################################
##------------------------MM32F103---cortext-m3
##
########################################################
                27:{
                "id":"MM32f103K4U6",
                "processor":"ARM Cortex M3",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                 28:{
                "id":"MM32F103K4U6",
                "processor":"ARM Cortex M3",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                 29:{
                "id":"MM32F103K4U6",
                "processor":"ARM Cortex M3",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                },
                           30:{
                "id":"MM32F103K4U6",
                "processor":"ARM Cortex M3",
                "frequency":"72",
                "flash":"16",
                "ram":"4",
                "gpio":"27",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"10x12bit",
                "eeprom":"",
                "pack":"QFN32",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":""
                }
                     
            }

'''def micro_controller_details():
    row_items=5
    d=1
    for i in range(0,30):
        microcontroller=Label(master,text=mc_list[d]['id'],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=0,sticky=N+S+E+W)
        processor=Label(master,text=mc_list[d]['processor'],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=1,sticky=N+S+E+W)
        frequency=Label(master,text=mc_list[d]['frequency'],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=2,sticky=N+S+E+W)
        flash=Label(master,text=mc_list[d]["flash"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=3,sticky=N+S+E+W)
        ram=Label(master,text=mc_list[d]["ram"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=4,sticky=N+S+E+W)
        gpio=Label(master,text=mc_list[d]["gpio"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=5,sticky=N+S+E+W)
        adv_tm=Label(master,text=mc_list[d]["adv_tm"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=6,sticky=N+S+E+W)
        gptm=Label(master,text=mc_list[d]["gptm"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=7,sticky=N+S+E+W)
        wdg=Label(master,text=mc_list[d]["wdg"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=8,sticky=N+S+E+W)
        rtc=Label(master,text=mc_list[d]["rtc"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=9,sticky=N+S+E+W)
        uart=Label(master,text=mc_list[d]["uart"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=10,sticky=N+S+E+W)
        i2c=Label(master,text=mc_list[d]["i2c"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=11,sticky=N+S+E+W)
        spi=Label(master,text=mc_list[d]["spi"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=12,sticky=N+S+E+W)
        adc=Label(master,text=mc_list[d]["adc"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=13,sticky=N+S+E+W)
        eeprom=Label(master,text=mc_list[d]["eeprom"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=14,sticky=N+S+E+W)
        pack=Label(master,text=mc_list[d]["pack"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=15,sticky=N+S+E+W)
        dac=Label(master,text=mc_list[d]["dac"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=16,sticky=N+S+E+W)
        usb=Label(master,text=mc_list[d]["usb"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=17,sticky=N+S+E+W)
        can=Label(master,text=mc_list[d]["can"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=18,sticky=N+S+E+W)
        sdio=Label(master,text=mc_list[d]["sdio"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=19,sticky=N+S+E+W)
        comp=Label(master,text=mc_list[d]["comp"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=20,sticky=N+S+E+W)
        aes=Label(master,text=mc_list[d]["aes"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=21,sticky=N+S+E+W)
        trng=Label(master,text=mc_list[d]["trng"],bg="#142E54",fg="white",font="Lato 8 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=row_items,column=22,sticky=N+S+E+W)
        row_items=row_items+1
        d=d+1
    
'''
        
        

  

#####------------------main program start_here-----------------
master = tk.Tk()
#scrollbar = Scrollbar(master)
#scrollbar.grid( side = RIGHT, fill=Y )

#Microcontroller,Processor,Frequency,Flash,RAM,GPIO,AdvTM,GPTM,WDG,RTC,UART,I2C,SPI,ADC,EEPROM,PACK,DAC,USB,CAN,SDIO,COMP,AES,TRNG
m1=micro_controller_details("MM32f003TW","Cortex M0",48,16,2,16,1,5,2,1,1,1,"-","8x12bit","-","QFN20","-","-","-","-","-","-","-")   
m1.display(1 )
m2=micro_controller_details("MM32f003NW","Cortex M0",48,16,2,16,1,5,2,1,1,1,"-","8x12bit","-","QFN20","-","-","-","-","-","-","-")   
m2.display(2)
m1=micro_controller_details("MM32f031TW","Cortex M0",48,16,2,16,1,5,2,1,1,1,"-","8x12bit","-","QFN20","-","-","-","-","-","-","-")   
m1.display(3)
m2=micro_controller_details("MM32f031NW","Cortex M0",48,16,2,16,1,5,2,1,1,1,"-","8x12bit","-","QFN20","-","-","-","-","-","-","-")   
m2.display(4)


#mylist.pack( side = LEFT, fill = BOTH )
#scrollbar.config( command = mylist.yview )

#buttom_status=Label(master,text = "@2020-copyright from onyx components and systems",bd=1,relief=SUNKEN,anchor=W)
#buttom_status.grid(row=row_num,column=22,sticky=N+S+E+W)
tk.mainloop()
print(mc_list)
print("end of the program\n")