WORKDIR /app

COPY requirements.txt

RUN pip install -no-cashe-dir -r requirements.txt
COPY . . 

CMD ['python', 'src/main.py']
