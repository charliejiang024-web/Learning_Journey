import logging
'''
为什么我们需要logger，因为当我们在做大项目时，想更加个性化的打印日志到终端或日志，区分开来各种log文件
'''

# 创建logger
logger = logging.getLogger('myapp')
logger.setLevel(logging.INFO)

# 2. 输出到控制台
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

# 3. 输出到文件
file_handler = logging.FileHandler("app.log", encoding="utf-8")
logger.addHandler(file_handler)

# 4. 设置格式
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 使用
logger.info("程序启动")
logger.error("连接数据库失败")