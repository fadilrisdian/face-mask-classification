FROM pytorch/pytorch

RUN apt-get update

WORKDIR /app
COPY . /app

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 80

ENV NAME img_classifiers

CMD streamlit run app.py