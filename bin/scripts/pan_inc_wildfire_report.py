# #############
# modify these vars if necessary
##############
splunkserver = 'localhost'
splunkport = '8089'
index = 'pan_logs'
sourcetype = 'pan_wildfire_report'
panuser = 'pan'
panpass = 'pan'
## events per second
EPS = 1
##############
# you shouldn't have to modify anything below this line
#########################################

import time  # for sleep
import sys  # for exits and inputs
import os  # for environ variables and joins
import urllib2  # to make the https connection

try:
    # you can change this value to your splunk install value
    SPLUNK_HOME = os.environ['SPLUNK_HOME']
except:
    print "can't find splunk home"
    sys.exit(-1)

# the path of the app
paninc_libPath = os.path.join(SPLUNK_HOME, 'etc', 'apps', 'pan_datagen')
## sample log location
#log_in = open(os.path.join(paninc_libPath,'bin','data','pan_incident.txt'),
# 'r').readlines()
log_in = []
for filename in os.listdir(
        os.path.join(paninc_libPath, 'bin', 'data', 'reports')):
    with open(os.path.join(paninc_libPath, 'bin', 'data', 'reports',
                           filename)) as f:
        log_in.append(f.readlines())

#print log_in
# more or less wholesale from: http://docs.python.org/2/library/urllib2.html
# Create an OpenerDirector with support for Basic HTTP Authentication...
auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(realm='/splunk',
                          uri='https://' + splunkserver + ':' + splunkport,
                          user=panuser,
                          passwd=panpass)
opener = urllib2.build_opener(auth_handler)
# ...and install it globally so it can be used with urlopen.
urllib2.install_opener(opener)
try:
    urllib2.urlopen(
        'https://' + splunkserver + ':' + splunkport +
        '/services/receivers/simple?index=' + index + '&sourcetype=pan_log',
        'this is a test')
except:
    print "May be Splunk is not running or the server path is correct"
    sys.exit(-1)


def replay():
    while True:

        # wait 5 mins
        time.sleep(300)

        for l in log_in:
            time.sleep(5)

            evt = str.join("", l)

            urllib2.urlopen(
                'https://' + splunkserver + ':' + splunkport +
                '/services/receivers/simple?index=' + index +
                '&sourcetype=' + sourcetype,
                evt)


replay()
