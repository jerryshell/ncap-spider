# 文本情感分类-新闻采集

## Docker

```bash
mkdir -p /docker-data/tf/notebooks
```

```bash
docker run -d \
  --rm \
  --name tf \
  -p 8888:8888 \
  -p 8000:8000 \
  -v /docker-data/tf/notebooks:/tf/notebooks \
  tensorflow/tensorflow:latest-py3-jupyter
```

## 依赖

```bash
pip3 install --upgrade requests bs4 fastapi uvicorn
```

## 报错解决：__NSPlaceholderDate initialize

https://stackoverflow.com/questions/50168647/multiprocessing-causes-python-to-crash-and-gives-an-error-may-have-been-in-progr

```bash
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
```
