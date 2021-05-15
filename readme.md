## Follows List 
Simple script to fetch user's follow list from mangadex's api

### TOC
- [Follows List](#follows-list)
  - [TOC](#toc)
  - [Background](#background)
  - [Update](#update)
  - [Run from source](#run-from-source)
  - [Download executable](#download-executable)
  - [Contributing](#contributing)
  - [License](#license)

### Background 
This was created in order to make searching for your favourite manga in thirdparty apps like Tachiyomi a bit easier.
>Note: Follow list is created as a csv file for your convenience

### Update
- Added the functionality to get the last read chapter 

### Run from source
Clone repo:
```
git clone https://github.com/StoicSun/MD-Follow-list.git
```

Cd into directory where you cloned the repo  
eg.`cd Downloads\MD-Follow-list`

Create a virtualenv first:
```
python -m venv venv
```

Activate it:
```
PS C:\Users\<user>\<PATH to venv>\Scripts\activate.ps1
```

Install the required dependencies:
```
pip install > requirements.txt
```

Run the program:
```
python main.py
```

### Download executable
If you don't want to run from source then [download](https://github.com/StoicSun/MD-Follow-list/releases/download/1.0.0/main.exe) the executable from releases but be sure to look into the source code to reassure yourself since you'll have to provide your username and password to the program afterall.

### Contributing
If you think this program can be improved in any way please open a PR or if you find a bug or issue open a new issue  
Thanks!

### License
[MIT](LICENSE) © Suraj Das
