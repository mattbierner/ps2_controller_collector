Simple tools used to log PlayStation 2 controller state during gameplay on physical console.

## Wiring
Tested on Arduino Uno with original PlayStation 2 controller.

![http://store.curiousinventor.com/media/images/guides/ps2/wiring.jpg]

* Yellow / Attention to pin 10 
* Brown / Data to pin 11 
* Blue / clock to pin 13 

These should be connected in parallel with wiring running from the controller to the console. The rest of the wires from the console to the controller should be hooked normally.

## Collecting Data
1. Wire eveything up.
1. Deploy ps2_logger to your Arduino.
1. Turn on console and enable analog mode on the controller. By default, only analog data points are collected but you can modify the script to collect others.
1. Launch `collector.py` to dump the serial data from the Arduino to a file on your computer: `$ python collector.py out_file.data --log`. This will write the data to `out_file.data` and print the events to the screen.
   * You may have to update the target port in `collector.py`.

### Example
Collects ~60 samples per second of the form:

```
2016-05-22 13:09:51.785502, 255, 255, 128, 122, 150, 125
2016-05-22 13:09:51.937324, 255, 255, 128, 122, 150, 125
2016-05-22 13:09:52.003464, 255, 255, 128, 122, 150, 125
...
```

* Time - When the sample was taken.
* Button states 1
* Button states 2
* Right joystick x - 0 is far left, 255 is far right.
* Right joystick y - 0 is far up, 255 is far down.
* Left joystick x - 0 is far left, 255 is far right.
* Left joystick y - 0 is far up, 255 is far down.


## Button States
Bit map of button states. 1 == no depressed, 0 == depressed.

**Button states 1**
From lsb to msb

* Select
* L3
* R3
* Start
* Up
* Right
* Down
* Left

**Button states 2**
From lsb to msb 

* L2
* R2
* L1
* R1
* Triangle
* Circle
* X
* Square


[pyserial]: https://github.com/pyserial/pyserial