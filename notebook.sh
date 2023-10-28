#!/bin/bash
docker build -t timeline-notebook ./
docker run -p 8888:8888 -v $(pwd):/home/jovyan/work localhost/timeline-notebook
