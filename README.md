# Site to find the nearest cafes
- This is a site with a bot that searches for the nearest cafes, marking them on the map.

<p align="center">
<img src="https://github.com/Elkarapuzik/--cafes/blob/main/img/map.PNG" style="width:55%"/>
</p>

## How to install
- Download the repository from the git hub:

```
https://github.com/Elkarapuzik/--cafes
```

- Python3 should already be installed. Then use pip(or pip3 if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
``` 
## Prepare to run
- Go to your email, log in to your YANDEX developer account and get the geocoder key
- Create `.env` file in the program folder
- The `.env` file should have the following form:
```
YANDEX_GEOCODER_KEY=your_geocoder_key 
```
- Then we need to create a file ``coffee.json`` with cafe data in the folder with the program (the sample file is already in the project file).

## How to run the program
- To run the program you need to enter in the command line:
```
python3 main.py
```
