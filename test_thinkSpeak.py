# Registrador de temperatura Nergiza.com
# python
import httplib, urllib, os, glob, time
import sys

os.system('modprobe w1-gpio')  
os.system('modprobe w1-therm')  
base_dir = '/sys/bus/w1/devices/'  
device_folder = glob.glob(base_dir + '28*')[0]  
device_file = device_folder + '/w1_slave'  

delay = 60*2 #about 2 minute 

def read_temp_raw():  
    f = open(device_file, 'r')  
    lines = f.readlines()  
    f.close()  
    return lines

def read_temp():  
    lines = read_temp_raw()  
    while lines[0].strip()[-3:] != 'YES':  
        time.sleep(0.2)  
        lines = read_temp_raw()  
    equals_pos = lines[1].find('t=')  
    if equals_pos != -1:  
        temp_string = lines[1][equals_pos+2:]  
        temp_c = float(temp_string) / 1000.0
	temp_f = temp_c * 9.0 / 5.0 + 32.0
	temp_k = temp_c + 273.15  
        return temp_c, temp_f, temp_k  


def main():
#	print 'starting ...'
	#base_url = 'https://api.thingspeak.com/update?api_key=JTOFAR65501GR127'
	try:
		base_url = 'https://api.thingspeak.com/update?api_key=JTOFAR65501GR127'		
		temp = read_temp()
		#print "temp = %f" % temp
#		print 'connecting ...'
		conn = urllib.urlopen(base_url + "&field1=%f&field2=%f&field3=%f" %(temp[0],temp[1],temp[2]))
		#print conn.read()
		conn.close()
		connected = 'T' 
	except:
		print '!!!_fail_!!!'
		connected = 'F'
	return connected


if __name__  == "__main__":
	print 'starting ...'
	while True:	
		#main()
		connect = main()
		if connect == 'F' :
			break
		time.sleep(delay)  
	print 'stop ...'	
		
 
