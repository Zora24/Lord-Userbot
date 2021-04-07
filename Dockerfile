# LORD USERBOT
FROM koala21/kampangbot:buster

#
# LORD
#
RUN git clone -b Lord-Userbot https://github.com/rimuru07/Lord-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Rimuru07/Lord-Userbot/Lord-Userbot/requirements.txt

CMD ["python3","-m","userbot"]
