# auto_push_url
腾讯云函数：每天定时对CDN的所有URL进行预热

## 功能
* 根据网址，对`https://{}/sitemap.xml`的链接进行预热
* 根据`urls.txt`，对其中的所有链接进行预热
* 可以设置云函数的触发条件来实现定时触发

## 使用方法
* 修改`config.example.py`的各个变量为自己需要的值
* 修改`config.example.py`名称为`config.py`
* 按需修改`urls.txt`的链接
* 安装依赖：在仓库主目录执行`pip3 install -r requirements.txt -t .`
* 上传文件夹：腾讯云函数，提交方式，选择`本地上传文件夹`，选择该仓库的文件夹即可（保证该文件夹根目录应包含`index.main_handler`方法）
