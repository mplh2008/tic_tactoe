FROM python:3.9.4

RUN pip install coverage

CMD [ "python3", "./tictactoe.py"]
