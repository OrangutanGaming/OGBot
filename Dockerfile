FROM python:3.6.1
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y git
RUN git clone https://github.com/OrangutanGaming/OG_Bot.py.git
RUN pip install --upgrade -r requirements.txt # Install requirements.txt
RUN python3 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite # Install latest version of discord.py rewrite

WORKDIR /OG_Bot.py
ADD ./settings.json /settings.json
CMD ["python3", "OG_Bot.py"] # Run 'python3 "OG_Bot.py"'


