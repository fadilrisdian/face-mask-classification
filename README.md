# face-mask-classification
## Nodeflux Internship Task 2

### Run app without docker

![image](https://user-images.githubusercontent.com/105907083/187399808-ae63dd4e-20d5-45f6-ae9b-cc35a6c1387a.png)

```
git clone https://github.com/fadilrisdian/face-mask-classification
cd face-mask-classification
pip install -r requirements.txt
streamlit run App.py
```

### Build application
```
git clone https://github.com/fadilrisdian/face-mask-classification
cd face-mask-classification
docker build -t fmask-classifier:latest .
docker run -p 8501:8501 fmask-classifier:latest
```
