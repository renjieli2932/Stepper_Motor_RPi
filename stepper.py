import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#enable_pin = 18
coil_A_1_pin = 4 # red
coil_A_2_pin = 17 # black
coil_B_1_pin = 23 # blue
coil_B_2_pin = 24 # orange
 
'''# adjust if different
StepCount = 4
Seq = range(0, StepCount)
Seq[0] = [0,1,0,0]
Seq[1] = [0,1,0,1]
Seq[2] = [0,0,0,1]
Seq[3] = [1,0,0,1]
Seq[4] = [1,0,0,0]
Seq[5] = [1,0,1,0]
Seq[6] = [0,0,1,0]
Seq[7] = [0,1,1,0]
 '''
#GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
 
#GPIO.output(enable_pin, 1)
 
def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)
 
def forward(delay, steps):
    for i in range(steps):
	setStep(0,1,1,0)
	print('1')
	time.sleep(delay)
	setStep(1,0,1,0)
	print('2')
	time.sleep(delay)
	setStep(1,0,0,1)
	print('3')
	time.sleep(delay)
	setStep(0,1,0,1)
	print('4')
	time.sleep(delay)

''' 
def backwards(delay, steps):
    for i in range(steps):
        for j in reversed(range(StepCount)):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)
'''
 
if __name__ == '__main__':
    while True:
        delay = 5
        steps = 10000
        forward(int(delay) / 1000.0, int(steps)) 
