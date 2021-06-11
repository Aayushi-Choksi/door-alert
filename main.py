from boltiot import Sms,  Bolt
import json, time
api_key="d09eb872-679d-469e-90c5-39124f0c2859"
device_id="BOLT7990977"
ssid='AC696bfeb845d1a82dc111d3e53737814a'
auth_token='2406258b29c3efd193058d07bdf1c0e1'
from_number='+12547813514'
to_number='+916353397282'
minimum_limit = 15
mybolt=Bolt(api_key,device_id)
sms=Sms(ssid,auth_token,to_number,from_number)
print(format("Auto LED Controller",'_^50'))
error='{"success": "0", "message": "A Connection error occurred"}'
offlne='{"value": "offline", "time": null, "success": 1}'
result=mybolt.isOnline()
if result==error:
	print("\n Check weather your computer or bolt device is connected to Internet.....")
elif result==offlne:
	print("\n Bolt Device is offline....")
else :
	while True:
		print ("\n Recognizing Value from Sensor.......")
		response = mybolt.analogRead('A0')
		data = json.loads(response)
		print(type(response))
		print (type(data))
		inten=int(data['value'])
		print("value from sensor is: " + str(inten))
		if inten>minimum_limit:
			result=mybolt.digitalWrite('0','HIGH')
			print("Someone opened the door")
			response_sms = sms.send_sms("Someone opened the door")
			time.sleep(10)
			mybolt.digitalWrite('0','LOW')
			time.sleep(10)
		else:
			result=mybolt.digitalWrite('0','LOW')
			print("Locker is closed")
			time.sleep(10)