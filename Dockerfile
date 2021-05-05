FROM python:3.9.2

ADD src src
ADD main.py .

RUN pip install coverage

CMD [ "python3", "./tictactoe.py"]
