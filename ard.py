import tensorflow as tf
import numpy as np
from asyncore import loop
import serial


arduino_port = 'COM7'


serialFromArduino = serial.Serial(arduino_port, 4800, timeout=1)


while True:

    line = serialFromArduino.readline().decode("utf-8")

    print(val)

    if (val>=600)
    {
        for(long i=0; i<10; i++){

      digitalWrite(13, HIGH);

      delay(500);

      digitalWrite(13, LOW);

      delay(500);
    }
     }
    else if (400<val<600)
    {
        load_model('model.h5')
    }