# Subway surfer AI
A script that Detects subway surfer objects, and the ability to replay the game.

Orginally the goal was to create and develope a reinforcement learning DQN, however the site changed Subway Surfers design making my previous Dataset useless.

## Testing.py 
Testing.py is used for generating a video with the yolov8 models predictions the model is based on my Roboflow dataset https://app.roboflow.com/jacob-hadih/subway-surfer-y8wri/1
The shorcomings in the dataset annotations are
- Only 349 total images
- Coins annotated poorly, somtimes missed
- missing image of certain sequences in the game
- Power ups not being annotated

## Main.py
Main.py uses the best weights of the YOlOV8 model to predict objects on the screen.


