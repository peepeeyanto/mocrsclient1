import requests
import json
import cv2
import time

def main():
    api_url = "YOUR_RSLOGIN_ENDPOINT"

    hospitalID = "YOUR_HOSPITAL_ID"
    password = "YOUR_HOSPITAL_PASSWORD"
    todo = {"hospitalID": hospitalID, "password": password}
    headers =  {"Content-Type":"application/json"}
    response = requests.post(api_url, data=json.dumps(todo), headers=headers)
    if(response.status_code != 200):
        print("wrong credentials")
        return
    
    data = response.json()
    token = data['token']
    streamlink = "YOUR_RSTP_LINK"

    

    while True:
        cap = cv2.VideoCapture(streamlink)
        # Read a frame from the stream
        ret, frame = cap.read()

        # Save the frame as a screenshot
        cv2.imwrite('screenshot.jpg', frame)

        # Send request to REST API
        url = 'YOUR_ML_ENDPOINT'
        files = {'file': ("screenshot.jpg", open('screenshot.jpg', 'rb'), "image/jpg")}
        headers1 = {"authorization": token}
        response = requests.post(url, files=files, headers=headers1)

        # Print response
        print(response.text)

        # Wait for 10 minutes before capturing the next screenshot
        time.sleep(600)
        
main()