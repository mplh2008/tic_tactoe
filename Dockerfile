FROM python:3.9.4

RUN pip install coverage

CMD [ "python3", "./tictactoe_integration_test.py"]
CMD [ "python3", "./tictactoe_unit_test.py"]
