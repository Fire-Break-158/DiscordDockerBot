FROM python

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

#ENTRYPOINT /bin/bash
ENTRYPOINT ["python", "status.py"]
