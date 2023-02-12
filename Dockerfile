FROM python:latest
WORKDIR C:\Users\hersh\OneDrive\Desktop\Python\game
COPY . .
ADD requirements.txt .
ADD adventureGame.py .
ADD animationDepartment.py . 
ADD biomeMaps.py .
ADD Data.py .
ADD gameNounsandWords.py .
ADD ideasAdventure.py .
ADD itemsList.py .
ADD monsterList.py .
ADD storyAdventure.py .


RUN pip install -r requirements.txt
CMD [ "python", "./adventureGame.py" ]