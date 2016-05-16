import httplib, urllib, os, glob, time

base_url = 'https://api.thingspeak.com/channels/116042/fields/1/last'


print 'connecting ...'
conn = urllib.urlopen(base_url)
control = conn.read()
num = len(control)
control = control[1:num-1]



print float(control)
conn.close()

