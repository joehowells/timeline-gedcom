FROM jupyter/scipy-notebook

ADD ./requirements.txt /home
RUN pip3 install -r /home/requirements.txt
