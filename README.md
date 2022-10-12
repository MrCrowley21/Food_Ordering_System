## Kitchen
This repository, _Food Ordering Service_, represents a part of a bigger project of a food ordering simulation,
performed as laboratory work during the _Network Programming_ course. Other components of
this project are: 
[_Dinning Hall_](https://github.com/MrCrowley21/Dinning_Hall.git),
[_Kitchen_](https://github.com/MrCrowley21/Kitchen.git), and
[_Client_Service_]https://github.com/MrCrowley21/Client_Service.git) .\
!**Note** the fact that this version of README file is not final and will be modified  further.\
First, to run the project into a docker container, perform the following commands:
````
$ docker network create food_ordering_network  
$ docker build -t food_ordering_image .  
$ docker run --net restaurant_network -p 5004:5004 --name food_ordering_container food_ordering_image
````
The first line will create an image of our project, while the next one - run project inside 
the created container. \
**NOTE** that the correct order of running the elements into the Docker container is the following: run the
command to create network, run the _Food Ordering Service_, run the _Kitchen_ component, run the _Dinning Hall_
component, and, in the end, run the Docker for _Client Service_ project.

For this moment, for more explanation regarding the code itself, please take a look at the comments 
that appears there.