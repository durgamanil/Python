# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:45:43 2020

@author: Onyx1
"""

import sys
import glob
import serial


def serial_ports():


    ports = ['COM%s' % (i + 1) for i in range(256)]

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


if __name__ == '__main__':
    print(serial_ports())