# LORD USERBOT
FROM koala21/kampangbot:buster

#
# LORD
#
RUN git clone -b Lord-Userbot https://github.com/rimuru07/Ids-Raphael /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Rimuru07/Ids-Raphael/Ids-Raphael/requirements.txt

CMD ["python3","-m","userbot"]
