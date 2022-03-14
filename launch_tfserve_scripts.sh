docker run -p 8501:8501 -p 8500:8500 --mount type=bind,source=/home/vinay/Documents/My_Docs/Deploy/vgg16,target=/models/vgg16 -e MODEL_NAME=vgg16 -t tensorflow/serving:latest

docker run -p 8501:8501 -p 8500:8500 --mount type=bind,source=/home/vinay/Documents/My_Docs/Deploy/resnet50,target=/models/resnet50 -e MODEL_NAME=resnet50 -t tensorflow/serving:latest

docker run --rm -it -p 8501:8501 -v /home/vinay/Documents/My_Docs/Deploy/model:/models -e MODEL_NAME=resnet50 tensorflow/serving