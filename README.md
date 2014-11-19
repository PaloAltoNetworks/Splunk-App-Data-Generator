
Sample Data Generator for Palo Alto Networks Splunk App
=======================================================

## Description ##

This app installs on Splunk side-by-side with the SplunkforPaloAltoNetworks 
app. When this app is enabled, it will generate events for the 
SplunkforPaloAltoNetworks app to parse and display.

## Requirements ##

- Splunk 5.x or 6.x
- SplunkforPaloAltoNetworks app (http://apps.splunk.com/app/491)

## Installation ##

All steps must be performed in order.  The examples assume Splunk is 
installed in /opt/splunk, but you can install Splunk in another directory.

- Install this pan_datagen app on Splunk using the .zip file or git.
- Restart Splunk
- Create a new user called 'pan' with password 'pan' and role 'pan'  
  (this is required for the data generator)

  For example, on the command line:  
  (replace `changeme` with your Splunk admin password)

    /opt/splunk/bin/splunk add user pan -password pan -role pan -auth admin:changeme

- Restart Splunk again
- Verify you are getting events by going to the  
  Palo Alto Networks app Overview Dashboard

## Known issues ##

- This app can consume a lot of resources, so it's not advised to run it on   
  a production Splunk environment. It should only be used for testing or   
  demonstration.
- The sample data may not always be in the form of the latest PAN-OS syslogs.  
  It may use older PAN-OS syslog formats, or a mix of old and new.
