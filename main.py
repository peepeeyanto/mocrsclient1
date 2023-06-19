import requests
import json
import cv2


def main():
    api_url = "http://127.0.0.1:5000/rslogin"

    hospitalID = input("enter your hospital ID: ")
    password = input("enter your password: ")
    todo = {"hospitalID": hospitalID, "password": password}
    headers =  {"Content-Type":"application/json"}
    response = requests.post(api_url, data=json.dumps(todo), headers=headers)
    if(response.status_code != 200):
        print("wrong credentials")
        return
    
    data = response.json()
    token = data['token']
    streamlink = input("enter your rtsp link: ")

    cap = cv2.VideoCapture(streamlink)

    while True:
        # Read a frame from the stream
        ret, frame = cap.read()

        # Save the frame as a screenshot
        cv2.imwrite('screenshot.png', frame)

        # Send request to REST API
        url = 'http://127.0.0.1:5000/ml'
        files = {'file': ("screenshot.jpg", open('screenshot.jpg', 'rb'), "image/jpg")}
        headers1 = {"authorization": token}
        response = requests.post(url, files=files, headers=headers1)

        # Print response
        print(response.text)

        # Wait for 10 minutes before capturing the next screenshot
        cv2.waitKey(60000)  # 600,000 milliseconds = 10 minutes
        
main()