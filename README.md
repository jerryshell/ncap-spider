# 新闻评论分析平台数据采集模块

## 相关项目

* [新闻评论分析平台 Web 端](https://github.com/jerryshell/ncap-admin)
* [新闻评论分析平台数据大屏](https://github.com/jerryshell/ncap-datav)
* [新闻评论分析平台服务端](https://github.com/jerryshell/ncap-server)
* [新闻评论分析平台情感分析模块](https://github.com/jerryshell/ncap-model)
* 新闻评论分析平台数据采集模块（当前项目）

## 依赖

```bash
pip3 install --upgrade requests bs4 fastapi uvicorn
```

## macOS __NSPlaceholderDate initialize 报错解决

https://stackoverflow.com/questions/50168647/multiprocessing-causes-python-to-crash-and-gives-an-error-may-have-been-in-progr

```bash
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
```
