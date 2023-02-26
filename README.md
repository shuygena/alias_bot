# alias_bot
Alias is a party game, where teams play against each other to guess as many words as possible before time runs out.
![Запись_2023_02_27_00_07_05_469](https://user-images.githubusercontent.com/75737596/221437540-4d6696c2-62f0-42d4-a30d-df8ae725a0a3.gif)
## :gear: Game settings
| setting | possible value | default value |
| ------- |:--------------:| -------------:|
| language   | Russian, English,  Karachay-Balkar | Russian |
| level     | Easy, Normal, Hard | Normal |
| score to win | number between 1 and 200 | 100 |
| time (sec) | number between 10 and 300  | 60 |
| pass tax | deduct or not deduct| not deduct |

## :speech_balloon: Spam control
Bot generate "Lorem-ipsum" answer to spam with API from https://api-ninjas.com/  
![image](https://user-images.githubusercontent.com/75737596/221439533-fda172ca-1316-4f43-805e-4503d3fda708.png)

## :toolbox: Requirements:  
This project was done with python-3.8.10 and aiogram-2.24

## :link: Download & Run
Clone repository:
```
git clone https://github.com/shuygena/alias_bot alias_bot
```
Go to directory:
```
cd alias_bot
```
Create virtual environments:
```
python3 -m venv venv
```
Activate virtual environments:
```
source venv/bin/activate
```
Install requirements:  
```
python3 -m pip install -r requirements.txt
```
Run:   
```
python3 bot.py
``` 
>you need to have your own .env where the tokens are stored (like in .env.example)
>

## :clipboard: TODO
- [x] write bot
- [x] add MIT.LICENSE
- [x] add README
- [ ] set Redis
- [ ] add DB with SQLite
- [ ] add logging
- [ ] add tests
- [ ] change notification about settings

## :mortar_board: Tutorial
[Telegram-bots course ](https://stepik.org/course/120924/info) (ru)
