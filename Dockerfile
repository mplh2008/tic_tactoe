FROM python:3.9.4

ADD src src
ADD tictactoe.py .

RUN pip install coverage

CMD [ "python3", "./tictactoe.py"]
