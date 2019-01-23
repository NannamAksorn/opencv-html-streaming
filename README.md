# opencv-html-streaming
Streaming live python OpenCV or Pillow frame to HTML locally and remotely using Redis, Flask, and NodeJs server. 
## Getting Started
  Download and Install [python3](https://www.python.org/downloads/) and [NodeJS](https://nodejs.org/en/), if you don't have them.
  ### Installing
    ```
    cd opencv-html-streaming/
    pip3 install -r requirements.txt
    cd server-nodejs/
    npm install
    ```
    
### Usage
  <b>Start redis server</b> by run following commands in terminal
  ```
  redis-server
  ```
  If you want to run remotely,
  ```
  redis-cli
  config set protected-mode no
  ```
  <b>Start web server</b>
  You can choose either Nodejs or python flask for the web server (for faster result, use Node)
  #### - Nodejs server
  ```
  cd server-nodejs/
  npm start
  ```
  #### - Flask server
  ```
  python3 server.py
  ```
  <b>Start webcam</b>
    If you want to run remotely, in [server.py](./server.py) change host and port for your redis server
  ```
  #redis server host:port
  HOST = "0.0.0.0"
  PORT = 6379
  ```
  Config your webcam paremeter in [server.py](./server.py)
  ```
  #webcam ID
  DEVICE = 0
  WIDTH = 1280
  HEIGHT = 720
  QUALITY = 70
  ```
   run the webcam
  ```
  cd ../
  python3 client.py
  ```
## Result
  For NodeJs Server go to (http://localhost:5000)
  For Flask Server go to (http://localhost:8081)
   
## License
This project is licensed under the [MIT](https://opensource.org/licenses/MIT) License
