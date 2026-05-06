from app.config.logger import setup_logging
from app.config.opus_loader import setup_opus

setup_logging()
# 在导入 opuslib 之前需要加载 opus.dll 动态链接库
setup_opus()

if __name__ == "__main__":
    # import run_proxy 需要在 setup_opus 初始化 opuslib 之后导入
    from app.process_handler import run_proxy

    run_proxy()
