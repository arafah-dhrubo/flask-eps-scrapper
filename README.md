# flask-eps-scrapper

## Intro

### Features:
- scrap data from official website of DSE https://www.dsebd.org/
- store the data in database
- see trades
- see eps data of every trades
- those data will come from database

### Techlnologies used in this project
- flask to get web interface
- beautifulsoup to scrap data from DSE
- sqlalchemy to use orm
- termcolor for color print in terminal

## File/Folder architecture

### The architecture:
- -app
- --static
- --- bootstrap.min.css
- -- templates
- --- eps.html
- --- import.html
- --- index.html
- --- main.html
- -- trade_app
- --- __init__.py
- --- helper.py (checking year, month and eps from scrap data)
- --- importer.py (importing the checked data in database)
- --- patterns.py (regex patterns for finding required lines, year, month and eps data from raw data)
- --- soup.py (configuration of beautiful soup)
- --- utils.py (abstraction for database methods)
- -- __init__.py
- -- models.py
- -- routes.pt
- -main.py
- -README.md
- -requirements.txt


### Run flask app:
- open project in any IDE
- create virtual environment using this command 
```bash 
python -m venv env
```
- activate virtual environment using this command 
```bash
env\Scripts\activate
```
- install required modules using this command
```bash
pip install -r requirements.txt
```
- run this command in terminal to run the app

```bash
python main.py
```


![image](https://user-images.githubusercontent.com/66543604/210126578-6bafec4e-bf4f-4ac9-886f-f178d5fa6628.png)


### Import scrapped data:
- goto import trade page
- click on import
- confirm and wait
- enjoy animation in terminal
![image](https://user-images.githubusercontent.com/66543604/209893749-4e4e06c5-fa2f-4998-856c-76ee265493b5.png)
![image](https://user-images.githubusercontent.com/66543604/209893812-6a57d06a-47c9-49fe-a629-1b6c69c1beb4.png)
![image](https://user-images.githubusercontent.com/66543604/210126598-96dacb43-678c-49f6-afb9-3ba863798737.png)


### See trades:
- after successful import you will be redirected to the index page
- you will see those trades like the below attchment
- you can also refresh this page using refresh button
- you can paginate over the result
- also you can search them
![image](https://user-images.githubusercontent.com/66543604/209893766-96f8c485-be9c-43e2-9e79-d73b18b031ac.png)


### See EPS data:
- if you want to see the eps data of those trades click on view
- you will see those EPS like the below attchment
- you can also refresh this page using refresh button
- you can paginate over the result
- also you can search them
![image](https://user-images.githubusercontent.com/66543604/209893780-02d51c0d-ce8f-4930-a125-ebaceeabdd52.png)
