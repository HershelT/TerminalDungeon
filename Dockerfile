FROM python:latest

# Install necessary packages for X11
# RUN apt-get update && apt-get install -y \
#     x11-apps \
#     && rm -rf /var/lib/apt/lists/*

WORKDIR C:\Users\hersh\Downloads\Conversational_Analysis_The_Game-main
COPY . .
ADD requirements.txt .
ADD adventureGame.py .
ADD animationDepartment.py . 
ADD biomeMaps.py .
ADD breakableItems.py .
ADD Data.py .
ADD gameNounsandWords.py .
ADD ideasAdventure.py .
ADD itemsList.py .
ADD monsterList.py .
ADD storyAdventure.py .

# Set the DISPLAY environment variable
# ENV DISPLAY host.docker.internal:0.0

RUN pip install -r requirements.txt
CMD [ "python", "./adventureGame.py" ]