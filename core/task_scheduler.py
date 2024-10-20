import logging

class TaskScheduler:
    def __init__(self, account_manager):
        self.account_manager = account_manager
        self.logger = logging.getLogger(__name__)

    def run(self):
        self.logger.info("Task scheduler started")
        # TODO: 實現任務調度邏輯