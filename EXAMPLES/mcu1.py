def details(processor,frequency,flash,ram,gpio,adv_tm,gptm,wdg,rtc,uart,i2c,spi,adc,eeprom=0,pack=0,dac=0,usb=0,can=0,sdio=0,comp=0,aes=0,trng=0,**para):
    print("=====================================================================================")
    print("Max speed in hz\t\tFLASH\t\tRAM\t\tGPIO")
    print("===================================================================================")
    print("PROCESSOR::======>{}".format(processor))
    print("Frequency Max speed ::====>{}Mhz".format(frequency))
    print("FLASH::====>{}KBytes".format(flash))
    print("RAM::====>{}KBytes".format(ram))
    print("GPIO::====>{}Pins".format(gpio))
    print("Advanced timer::====>{}".format(adv_tm))
    print("GPTM::====>{}".format(gptm))
    print("WDG::====>{}".format(wdg))
    print("RTC::====>{}".format(rtc))
    print("UART::====>{}".format(uart))
    print("I2C::====>{}".format(i2c))
    print("SPI::====>{}".format(spi)) 
    print("ADC::====>{}x12bit".format(adc))
    print("EEPROM::====>{}KBytes".format(eeprom))
    print("PACk::====>{}".format(pack))
    print("DAC::====>{}".format(dac))
    print("USB::====>{}".format(usb))
    print("CAN::====>{}".format(can))
    print("SDIO::====>{}".format(sdio))
    print("COMP::====>{}".format(comp))
    print("AES::====>{}".format(aes))
    print("TRNG::====>{}".format(trng))
    print("====================================================================================")
    
    
#while(1):
in1=input("enter mm32 microcontroller")
print(in1)
#=====================================================================
# MM32F003 General Purpose & High Performance
#1.====================================================================
if in1=="mm32f003nw":
        print("mm32f003nw is selected\n")
        details("ARM Cortex M0",48,16,2,16,1,5,2,1,1,1,8,"QFN20")   
#2.===================================================================
elif in1=="mm32f003tw":
   print("mm32f003tw selected\n")
   details("ARM Cortex M0",48,16,2,16,1,5,2,1,1,1,8,"TSSOP20")
#=====================================================================
# MM32F031 General Purpose & High Performance
#1.===================================================================          
elif in1=="mm32f031f4p6":
    print("mm32f031f4p6 is selected\n")
    details("ARM Cortex M0",72,16,4,16,1,5,2,1,1,1,9,"TSSOP20")  
#2.===================================================================
elif in1=="mm32f031f4u6":
    print("mm32f031f4u6 is selected\n")
    details("ARM Cortex M0",72,16,4,16,1,5,2,1,1,1,9,"QFN20")  
#3.===================================================================
elif in1=="mm32f031k4u6":
    print("mm32f031k4u6 is selected\n")
    details("ARM Cortex M0",72,16,4,27,1,5,2,1,1,1,10,"QFN32") 
#4.===================================================================
elif in1=="mm32f031k4t6":
    print("mm32f031k4t6 is selected\n")
    details("ARM Cortex M0",72,16,4,25,1,5,2,1,1,1,10,"QFN32")
#5.===================================================================
elif in1=="mm32f031c4t6":
    print("mm32f031c4t6 is selected\n")
    details("ARM Cortex M0",72,16,4,39,1,5,2,1,1,1,10,"LQFP48")
#6.===================================================================
elif in1=="mm32f031f6p6":
    print("mm32f031f6p6 is selected\n")
    details("ARM Cortex M0",72,32,4,16,1,5,2,1,1,1,9,"TSSOP20")
#7.===================================================================
elif in1=="mm32f031f6u6":
    print("mm32f031f6u6 is selected\n")
    details("ARM Cortex M0",72,32,4,16,1,5,2,1,1,1,9,"QFN20")
#8.===================================================================
elif in1=="mm32f031k6u6":
    print("mm32f031k6u6 is selected\n")
    details("ARM Cortex_M0",72,32,4,27,1,5,2,1,1,1,10,"QFN32")
#9.===================================================================
elif in1=="mm32f031k6t6":
    print("mm32f031k6t6 is selected\n")
    details("ARM Cortex M0",72,32,4,25,1,5,2,1,1,1,10,"LQFP32")
#10.===================================================================
elif in1=="mm32f031c6t6":
    print("mm32f031c6t6 is selected\n")
    details("ARM Cortex M0",72,32,4,39,1,5,2,1,1,1,10,"LQFP48")
#11.===================================================================
elif in1=="mm32f031k8u6":
    print("mm32f031k8u6 is selected\n")
    details("ARM Cortex_M0",72,64,8,27,1,5,2,2,1,1,10,"QFN32")
#12.===================================================================
elif in1=="mm32f031k8t6":
    print("mm32f031k8t6 is selected\n")
    details("ARM Cortex_M0",72,64,8,25,1,5,2,2,1,1,10,"LQFP32")
#13.===================================================================
elif in1=="mm32f031c8t6":
    print("mm32f031c8t6 is selected\n")
    details("ARM Cortex M0",72,64,8,39,1,5,2,2,1,2,10,"LQFP48")
#14.===================================================================
elif in1=="mm32f031kbu6":
    print("mm32f031kbu6 is selected\n")
    details("ARM Cortex M0",72,128,8,27,1,5,2,2,1,1,10,"LQFP32")
#15.===================================================================
elif in1=="mm32f031kbt6":
    print("mm32f031kbt6 is selected\n")
    details("ARM Cortex_M0",72,128,8,25,1,5,2,2,1,1,10,"LQFP32")
#16.===================================================================
elif in1=="mm32f031cbt6":
    print("mm32f031cbt6 is selected\n")
    details("ARM Cortex M0",72,128,8,39,1,5,2,2,1,2,10,"LQFP48")
#=====================================================================
#MM32F032 General Purpose & High Performance
#1.===================================================================   
elif in1=="mm32f032k6u6":
    print("mm32f032k6u6 is selected\n")
    details("ARM Cortex M0",72,32,8,27,1,5,2,"yes",2,1,1,10,"QFN32")
#2.==================================================================
elif in1=="mm32f032k6t6":
    print("mm32f032k6t6 is selected\n")
    details("ARM Cortex M0",72,32,8,25,1,5,2,"yes",2,1,1,10,"LQFP32")
#3.===================================================================
elif in1=="mm32f032c6t6":
    print("mm32f032c6t6 is selected\n")
    details("ARM Cortex M0",72,32,8,39,1,5,2,"yes",2,1,2,10,"LQFP48")
#4.===================================================================
elif in1=="mm32f032r6t6":
    print("mm32f032r6t6 is selected\n")
    details("ARM Cortex M0",72,32,8,56,1,5,2,"yes",2,1,2,10,"LQFP64")
#5.===================================================================
elif in1=="mm32f032k8u6":
    print("mm32f032k8u6 is selected\n")
    details("ARM Cortex M0",72,64,16,27,1,5,2,"yes",2,1,1,10,"QFN32")
#6.===================================================================
elif in1=="mm32f032k8t6":
    print("mm32f032k8t6 is selected\n")
    details("ARM Cortex M0",72,64,16,25,1,5,2,"yes",2,1,1,10,"LQFP32")
#7.===================================================================
elif in1=="mm32f032c8t6":
    print("mm32f032c8t6 is selected\n")
    details("ARM Cortex M0",72,64,16,39,1,5,2,"yes",2,1,2,10,"LQFP48")
#8.===================================================================
elif in1=="mm32f032r8t6":
    print("mm32f032r8t6 is selected\n")
    details("ARM Cortex_M0",72,64,16,56,1,5,2,"yes",2,1,2,10,"LQFP64")
#======================================================================
#MM32F103 General Purpose & High Performance
#1.1.==================================================================
elif in1=="mm32f103k8u6":
   print("mm32f103k8u6 is selected\n")
   details("ARM Cortex M3",96,64,20,25,1,3,2,1,2,1,1,10,"QFN32",0,1,1)
#1.2.===================================================================
elif in1=="mm32f103k8t6":
   print("mm32f103k8t6 is selected\n")
   details("ARM Cortex M3",96,64,20,23,1,3,2,1,2,1,1,10,"LQFP32",0,1,1)
#1.3.======================================================================
elif in1=="mm32f103c8t6":
   print("mm32f103c8t6 is selected\n")
   details("ARM Cortex M3",96,64,20,37,1,3,2,1,3,2,2,10,"LQFP48",0,1,1)
#1.4.======================================================================
elif in1=="mm32f103r8t6":
   print("mm32f103r8t6 is selected\n")
   details("ARM Cortex M3",96,64,20,51,1,3,2,1,3,2,2,16,"LQFP64",0,1,1)
#1.5.======================================================================
elif in1=="mm32f103kbu6":
   print("mm32f103kbu6 is selected\n")
   details("ARM Cortex M3",96,128,20,25,1,3,2,1,2,1,1,10,"QFN32",0,1,1)
#1.6.===================================================================
elif in1=="mm32f103kbt6":
   print("mm32f103kbt6 is selected\n")
   details("ARM Cortex M3",96,128,20,23,1,3,2,1,2,1,1,10,"LQFP32",0,1,1)
#1.7.===================================================================
elif in1=="mm32f103cbt6":
   print("mm32f103cbt6 is selected\n")
   details("ARM Cortex M3",96,128,20,37,1,3,2,1,3,2,2,10,"LQFP48",0,1,1)
#1.8.====================================================================
elif in1=="mm32f103rbt6":
   print("mm32f103rbt6 is selected\n")
   details("ARM Cortex M3",96,128,20,51,1,3,2,1,3,2,2,16,"LQFP64",0,1,1)
#2.1.=====================================================================
elif in1=="mm32f103kcu6":
   print("mm32f103kcu6 is selected\n")
   details("ARM Cortex M3",144,256,64,25,2,6,2,1,5,1,2,7,"QFN32",0,1,1,0,2)
#2.2.=====================================================================
elif in1=="mm32f103kct6":
   print("mm32f103kct6 is selected\n")
   details("ARM Cortex M3",144,256,64,23,2,2,2,1,5,1,2,7,"LQFP32",0,1,1,0,2)
#2.3.======================================================================
elif in1=="mm32f103cct6":
   print("mm32f103cct6 is selected\n")
   details("ARM Cortex M3",144,256,64,37,2,2,2,1,5,2,3,7,"LQFP48",0,1,1,0,2)
#2.4.======================================================================
elif in1=="mm32f103rct6":
   print("mm32f103rct6 is selected\n")
   details("ARM Cortex M3",144,256,64,51,2,2,2,1,8,2,3,7,"LQFP64",0,1,1,1,2)
#2.5.======================================================================
elif in1=="mm32f103vct6":
   print("mm32f103vct6 is selected\n")
   details("ARM Cortex M3",144,256,64,80,2,2,2,1,8,2,3,7,"LQFP100",0,1,1,1,2)
#2.6.=======================================================================
elif in1=="mm32f103keu6":
   print("mm32f103keu6 is selected\n")
   details("ARM Cortex M3",144,512,128,25,2,2,2,1,5,1,2,7,"QFN32",0,1,1,0,2)
#2.7.=======================================================================
elif in1=="mm32f103ket6":
   print("mm32f103ket6 is selected\n")
   details("ARM Cortex M3",144,512,128,23,2,2,2,1,5,1,2,7,"LQFP32",0,1,1,0,2)
#2.8.=======================================================================
elif in1=="mm32f103cet6":
   print("mm32f103cet6 is selected\n")
   details("ARM Cortex M3",144,512,128,37,2,2,2,1,5,2,3,7,"LQFP48",0,1,1,0,2)
#2.9.========================================================================
elif in1=="mm32f103ret6":
   print("mm32f103ret6 is selected\n")
   details("ARM Cortex M3",144,512,128,51,2,2,2,1,8,2,3,7,"LQFP64",0,1,1,1,2)
#2.10.=========================================================================
elif in1=="mm32f103vet6":
   print("mm32f103vet6 is selected\n")
   details("ARM Cortex M3",144,512,128,80,2,2,2,1,8,2,3,7,"LQFP100",0,1,1,1,2)
#============================================================================
#MM32L0 low Power & High Security
#============================================================================
#MM32L050
#1.1.============================================================================
elif in1=="mm32l050tw":
   print("mm32l050tw is selected\n")
   details("ARM Cortex M0",48,32,4,16,1,5,2,0,1,1,1,0,"TSSOP20",0,0,0,0,2,"yes")
#1.2.============================================================================
elif in1=="mm32l050nt":
   print("mm32l050nt is selected\n")
   details("ARM Cortex M0",48,32,4,27,1,5,2,0,2,1,1,0,"QFN32",0,0,0,0,2,"yes")
#1.3.============================================================================
elif in1=="mm32l050pt":
   print("mm32l050pt is selected\n")
   details("ARM Cortex M0",48,32,4,25,1,5,2,0,2,1,1,0,"LQFP32",0,0,0,0,2,"yes")
#1.4.============================================================================
elif in1=="mm32l050pf":
   print("mm32l050pf is selected\n")
   details("ARM Cortex M0",48,32,4,39,1,5,2,0,2,1,2,0,"LQFP48",0,0,0,0,2,"yes")
#============================================================================
#MM32L051
#1.5.================================================================================
elif in1=="mm32l051tw":
   print("mm32l051tw is selected\n")
   details("ARM Cortex M0",48,32,4,16,1,5,2,0,1,1,1,9,"TSSOP20",0,0,0,0,2,"yes")
#1.6.============================================================================
elif in1=="mm32l051nt":
   print("mm32l051nt is selected\n")
   details("ARM Cortex M0",48,32,4,27,1,5,2,0,2,1,1,10,"QFN32",0,0,0,0,2,"yes")
#1.7.============================================================================
elif in1=="mm32l051pt":
   print("mm32l051pt is selected\n")
   details("ARM Cortex M0",48,32,4,25,1,5,2,0,2,1,1,10,"LQFP32",0,0,0,0,2,"yes")
#1.8.============================================================================
elif in1=="mm32l051pf":
   print("mm32l051pf is selected\n")
   details("ARM Cortex M0",48,32,4,39,1,5,2,0,2,1,2,10,"LQFP48",0,0,0,0,2,"yes")
#============================================================================
#MM32L052
#1.9.============================================================================
elif in1=="mm32l052nt":
   print("mm32l052nt is selected\n")
   details("ARM Cortex M0",48,32,4,27,1,5,2,0,2,1,1,10,"QFN32",0,1,0,0,2,"yes")
#1.10.============================================================================
elif in1=="mm32l052pt":
   print("mm32l052pt is selected\n")
   details("ARM Cortex M0",48,32,4,25,1,5,2,0,2,1,1,10,"LQFP32",0,1,0,0,2,"yes")
#1.11.============================================================================
elif in1=="mm32l052pf":
   print("mm32l052pf is selected\n")
   details("ARM Cortex M0",48,32,4,39,1,5,2,0,2,1,2,10,"LQFP48",0,1,0,0,2,"yes")
#============================================================================
#MM32L061
#1.12.===========================================================================
elif in1=="mm32l061tw":
   print("mm32l061tw is selected\n")
   details("ARM Cortex M0",48,64,8,16,1,5,2,0,1,1,1,9,"TSSOP20",0,0,0,0,2,"yes")
#1.13.============================================================================
elif in1=="mm32l061nt":
   print("mm32l061nt is selected\n")
   details("ARM Cortex M0",48,64,8,27,1,5,2,0,2,1,1,10,"QFN32",0,0,0,0,2,"yes")
#1.14.============================================================================
elif in1=="mm32l061pt":
   print("mm32l061pt is selected\n")
   details("ARM Cortex M0",48,64,8,25,1,5,2,0,2,1,1,10,"LQFP32",0,0,0,0,2,"yes")
#1.15.============================================================================
elif in1=="mm32l061pf":
   print("mm32l061pf is selected\n")
   details("ARM Cortex M0",48,64,8,39,1,5,2,0,2,1,2,10,"LQFP48",0,0,0,0,2,"yes")
#================================================================================
#MM32L062
#2.1============================================================================
elif in1=="mm32l062tw":
   print("mm32l062tw is selected\n")
   details("ARM Cortex M0",48,64,8,16,1,5,2,0,1,1,1,9,"TSSOP20",0,1,0,0,2,"yes")
#2.2============================================================================
elif in1=="mm32l062nt":
   print("mm32l062nt is selected\n")
   details("ARM Cortex M0",48,64,8,27,1,5,2,0,2,1,1,10,"QFN32",0,1,0,0,2,"yes")
#2.3.============================================================================
elif in1=="mm32l062pt":
   print("mm32l062pt is selected\n")
   details("ARM Cortex M0",48,64,8,25,1,5,2,0,2,1,1,10,"LQFP32",0,1,0,0,2,"yes")
#2.4.============================================================================
elif in1=="mm32l062pf":
   print("mm32l062pf is selected\n")
   details("ARM Cortex M0",48,64,8,39,1,5,2,0,2,1,2,10,"LQFP48",0,1,0,0,2,"yes")
#.==============================================================================
#MM32L072
#2.5.============================================================================
elif in1=="mm32l072tw":
   print("mm32l072tw is selected\n")
   details("ARM Cortex M0",48,128,8,16,1,5,2,0,1,1,1,9,"TSSOP20",0,1,0,0,2,"yes")
#2.6.============================================================================
elif in1=="mm32l072nt":
   print("mm32l072nt is selected\n")
   details("ARM Cortex M0",48,128,8,27,1,5,2,0,2,1,1,10,"QFN32",0,1,0,0,2,"yes")
#2.7.============================================================================
elif in1=="mm32l072pt":
   print("mm32l072pt is selected\n")
   details("ARM Cortex M0",48,128,8,25,1,5,2,0,2,1,1,10,"LQFP32",0,1,0,0,2,"yes")
#2.8.============================================================================
elif in1=="mm32l072pf":
   print("mm32l072pf is selected\n")
   details("ARM Cortex M0",48,128,8,39,1,5,2,0,2,1,2,10,"LQFP48",0,1,0,0,2,"yes")
#.==============================================================================
#MM32L073
#2.9.============================================================================
elif in1=="mm32l073tw":
   print("mm32l073tw is selected\n")
   details("ARM Cortex M0",48,128,8,16,1,5,2,0,1,1,1,9,"TSSOP20",0,1,1,0,2,"yes")
#2.10.============================================================================
elif in1=="mm32l073nt":
   print("mm32l073nt is selected\n")
   details("ARM Cortex M0",48,128,8,27,1,5,2,0,2,1,1,10,"QFN32",0,1,1,0,2,"yes")
#2.11.============================================================================
elif in1=="mm32l073pt":
   print("mm32l073pt is selected\n")
   details("ARM Cortex M0",48,128,8,25,1,5,2,0,2,1,1,10,"LQFP32",0,1,1,0,2,"yes")
#2.12.============================================================================
elif in1=="mm32l073pf":
   print("mm32l073pf is selected\n")
   details("ARM Cortex M0",48,128,8,39,1,5,2,0,2,1,2,10,"LQFP48",0,1,1,0,2,"yes")
#==============================================================================
#MM32L362
#3.1.==============================================================================
elif in1=="mm32l362nt":
   print("mm32l362nt is selected\n")
   details("ARM Cortex M3",96,64,20,25,1,3,2,"yes",2,1,1,10,0,"QFN32","2x12bit",1,0,0,0,"yes","no")
#3.2.============================================================================
elif in1=="mm32l362pt":
   print("mm32l362pt is selected\n")
   details("ARM Cortex M3",96,64,20,23,1,3,2,"yes",2,1,1,10,0,"LQFP32","2x12bit",1,0,0,0,"yes","no")
#3.3.============================================================================
elif in1=="mm32l362pf":
   print("mm32l073pf is selected\n")
   details("ARM Cortex M3",96,64,20,37,1,3,2,"yes",3,2,2,10,0,"LQFP48","2x12bit",1,0,0,0,"yes","no")
#3.4.============================================================================
elif in1=="mm32l362ps":
   print("mm32l073ps is selected\n")
   details("ARM Cortex M3",96,64,20,51,1,3,2,"yes",3,2,2,16,0,"LQFP64","2x12bit",1,0,0,0,"yes","no")
#============================================================================
#MM32L373
#3.5.==================================================================================
elif in1=="mm32l373nt":
   print("mm32l373nt is selected\n")
   details("ARM Cortex M3",96,128,20,25,1,3,2,"yes",2,1,1,10,0,"QFN32","2x12bit",1,1,0,0,"yes","no")
#3.6.============================================================================
elif in1=="mm32l373pt":
   print("mm32l373pt is selected\n")
   details("ARM Cortex M3",96,128,20,23,1,3,2,"yes",2,1,1,10,0,"LQFP32","2x12bit",1,1,0,0,"yes","no")
#3.7.============================================================================
elif in1=="mm32l373pf":
   print("mm32l373pf is selected\n")
   details("ARM Cortex M3",96,128,20,37,1,3,2,"yes",3,2,2,10,0,"LQFP48","2x12bit",1,1,0,0,"yes","no")
#3.8.============================================================================
elif in1=="mm32l373ps":
   print("mm32l373ps is selected\n")
   details("ARM Cortex M3",96,128,20,51,1,3,2,"yes",3,2,2,16,0,"LQFP64","2x12bit",1,1,0,0,"yes","no")
#============================================================================
#MM32L384
#3.9.==================================================================================
elif in1=="mm32l384nt":
   print("mm32l384nt is selected\n")
   details("ARM Cortex M3",96,256,64,25,2,8,2,"yes",7,1,2,7,4,"QFN32","2x12bit","OTG",1,0,0,"yes","no")
#3.10.============================================================================
elif in1=="mm32l384pt":
   print("mm32l384pt is selected\n")
   details("ARM Cortex M3",96,256,64,23,2,8,2,"yes",7,1,2,10,4,"LQFP32","2x12bit",1,1,0,0,"yes","no")
#3.11.============================================================================
elif in1=="mm32l384pf":
   print("mm32l384pf is selected\n")
   details("ARM Cortex M3",96,256,64,37,2,8,2,"yes",8,2,3,10,4,"LQFP48","2x12bit",1,1,0,0,"yes","no")
#3.12.============================================================================
elif in1=="mm32l384ps":
   print("mm32l384ps is selected\n")
   details("ARM Cortex M3",96,256,64,51,2,8,2,"yes",8,2,3,16,4,"LQFP64","2x12bit",1,1,0,0,"yes","no")
#3.13.============================================================================
elif in1=="mm32l384ph":
   print("mm32l384ph is selected\n")
   details("ARM Cortex M3",96,256,64,80,2,8,2,"yes",8,2,3,16,4,"LQFP64","2x12bit",1,1,0,0,"yes","no")
#============================================================================
#MM32L395
#3.9.==================================================================================
elif in1=="mm32l395nt":
   print("mm32l395nt is selected\n")
   details("ARM Cortex M3",96,512,128,25,2,6,2,"yes",7,1,2,7,4,"QFN32","2x12bit","OTG",1,0,0,"yes","no")
#3.10.============================================================================
elif in1=="mm32l395pt":
   print("mm32l395pt is selected\n")
   details("ARM Cortex M3",96,512,128,23,2,6,2,"yes",7,1,2,10,4,"LQFP32","2x12bit",1,1,0,0,"yes","no")
#3.11.============================================================================
elif in1=="mm32l395pf":
   print("mm32l395pf is selected\n")
   details("ARM Cortex M3",96,512,128,37,2,6,2,"yes",8,2,3,10,4,"LQFP48","2x12bit",1,1,0,0,"yes","no")
#3.12.============================================================================
elif in1=="mm32l395ps":
   print("mm32l384ps is selected\n")
   details("ARM Cortex M3",96,512,128,51,2,6,2,"yes",8,2,3,16,4,"LQFP64","2x12bit",1,1,0,0,"yes","no")
#3.13.============================================================================
elif in1=="mm32l395ph":
   print("mm32l384ph is selected\n")
   details("ARM Cortex M3",96,512,128,80,2,6,2,"yes",8,2,3,16,4,"LQFP64","2x12bit",1,1,0,0,"yes","no")
#============================================================================
elif in1=="mm32w051":
    print("mm32w051 is selected\n")
elif in1=="mm32w062":
    print("mm32w062 is selected\n")
elif in1=="mm32w073":
    print("mm32w073 is selected\n")
elif in1=="mm32w362":
    print("mm32w362 is selected\n")
elif in1=="mm32w373":
    print("mm32w373 is selected\n")
elif in1=="mm32w384":
    print("mm32w384 is selected\n")
elif in1=="mm32w395":
    print("mm32w395 is selected\n")
elif in1=="mm32SPIN":
    print("mm32SPIN is selected\n")
else :
    print("microcontroller is not in the given list")