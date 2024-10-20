import logging
from core.account_manager import AccountManager
from core.task_scheduler import TaskScheduler
from utils.config import load_config
from utils.logger import setup_logger

def main():
    # 設置日誌
    setup_logger()
    logger = logging.getLogger(__name__)

    # 加載配置
    config = load_config()

    # 初始化帳號管理器
    account_manager = AccountManager(config['accounts'])

    # 初始化任務調度器
    task_scheduler = TaskScheduler(account_manager)

    # 開始運行任務
    logger.info("Starting Twitter automation system...")
    task_scheduler.run()

if __name__ == "__main__":
    main()