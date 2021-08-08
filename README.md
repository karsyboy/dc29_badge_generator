# DC29 Badge Generator

To generate unlimited badge responses you need to know your badge response number and have a valid response from one device. Once this is done you can change the 5,6,7 and 8th characters to whatever you want to generate valid responses as if they are from other devices. Charters 17,18,19,20,21 and 22 indicates your device valid response code as long as this code is there it will know that the code is a valid response for your device. Characters 25 and 26 indicate whether or not the device has the signal. If the device has the signal it will be 01 if it does not it will be 00.

362F {F92C} 505800CE {509113} 57 {01} 7C7FBC

## How to use the script

To use the script you will need to install the python module pyserial.

To do this run the command:

```
sudo pip3 install pyserial
```

Once done you will need to change two veriables in the script "badge_str_1" and "badge_str_2".

"badge_str_1" should be the first 4 charters of the response code that you have gotten from some else device.

"badge_str_2" should be the 9th through 32nd characters from the same respones code that you pulled the first 4 characters from.

Once these veriables are change plug in your device and verify the console port in the scrip is correct.

You are now good to run the script.


## Know Issues

The Defcon 29 badge only allows a maximum of 65536 to connect to it before it resets back to ZERO. For this reason the script will ask you to input your current badge connection count before running. If anyone has a better way to handel this in the script feel free to reach out to me through discord.
