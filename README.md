# twitter-summarizer-rest-service-jinyu-tn
twitter-summarizer-rest-service-jinyu-tn created by GitHub Classroom

## If you need the website please send me an email at jinyutn@bu.edu then I will give you the website and open the server for you!

file folder **myVideo** contains the result video of this program

**application.py** is the flask file

file folder **templates** contains the html file

other files are same with hw4

# video-jinyu-tn
video-jinyu-tn created by GitHub Classroom

## Project target:
1. Get tweets from twitter by keyboard with twitter API.
2. Convert the tweets into images and convert the images into a video.
## File description:
`testcase` : the result of queue.py, contains results of 10 usernames.

`ComingSoon.ttf`: the font this homework used.

`test.json` : json file used when there is no API keys.

## Module description：

### Tweets Grub Module:
- Use twitter API to get tweets by keyboard which user typing in. Store the tweets to a python list and pass it to the next module and also write them to a text file. If there is no usable API key, the python code will open a json file and covert a list containing "No API key found" and convert it to the next module.
- Using **JSON** **Twitter API**
### Word to Image Module
- Convert each tweets to a image and store all the images to a same file folder, which named by the user's name.
- Using **PIL**
### Image to Video Module:
- Convert all of the images into a video.
- Using **cv2**
### Queue Module:
- Imitate 3 threads running 10 users task in turn.
- Using **queue** **threading**

## Project Demo:

### Queue: 
![case1](https://github.com/BUEC500C1/video-jinyu-tn/blob/master/queue_image.png)
### Input:
![case2result](https://github.com/BUEC500C1/video-jinyu-tn/blob/master/runtest_image.png)
### Output files:
![case2](https://github.com/BUEC500C1/video-jinyu-tn/blob/master/test_result_image.png)
### Pytest result:
![pytest](https://github.com/BUEC500C1/video-jinyu-tn/blob/master/pytest_image.png)
