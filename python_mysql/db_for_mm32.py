# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:25:03 2020

@author: Onyx1
"""

import pymysql
  
conn=pymysql.connect(host="localhost",user="root",password="",db="my_python")
mycursor=conn.cursor()
"""processor,frequency,flash,ram,gpio,adv_tm,gptm,wdg,rtc,uart,
i2c,spi,adc,eeprom="-",pack="-",dac="-",usb="",can="",sdio=0,comp=0,aes=0,trng=0,"""
"""
mycursor.execute(CREATE TABLE mm32_microcontroller
           (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
           controller varchar(20) NOT NULL,
           processor varchar(20) NOT NULL,
           frequency varchar(20) NOT NULL,
           flash varchar(20) NOT NULL,
           ram varchar(20) NOT NULL,
           gpio varchar(20) NOT NULL,
           adv_tm varchar(20),
           gptm varchar(20),
            wdg varchar(20),
           rtc varchar(20),
            uart varchar(20) NOT NULL,
            i2c varchar(20),
           spi varchar(20),
            adc varchar(20),
            eeprom varchar(20),
           pack varchar(20),
            dac varchar(20),
          usb varchar(20),
           can varchar(20),
           sdio varchar(20),
            comp varchar(20),
          aes varchar(20),
           trng varchar(20)
            )               
           )
           """
print("\nPlease enter your choice\n")
#print
while True:
    choice=int(input("1.add\n2.show\n3.show all\n"))
    if choice==1:
        mycursor.execute("INSERT INTO mm32_microcontroller(id,controller,processor,frequency,flash,ram,gpio,adv_tm,gptm,wdg,rtc,uart,i2c,spi,adc,eeprom,pack,dac,usb,can,sdio,comp,aes,trng) VALUES(null,'MM32F003','ARM Cortex M0','48Mhz','16','2','16','1','5','2','-','1','1','1','8x12bit','-','QFN20','-','-','-','-','-','-','-');")
        print("->data inserted")
        conn.commit()
    elif choice ==2 :
        mycursor.execute("SELECT * FROM mm32_microcontroller")
        row = mycursor.fetchone()
        while row is not None:
            print(row)
            row = mycursor.fetchone()
    else:
        mycursor.execute("SELECT * FROM mm32_microcontroller")
        rows = mycursor.fetchall()
        print('Total Row(s):', mycursor.rowcount)
        for row in rows:
            print(row)

#conn.commit()
conn.close()