class AccountManager:
    def __init__(self, accounts_config):
        self.main_accounts = accounts_config['main_accounts']
        self.sub_accounts = accounts_config['sub_accounts']

    def get_main_accounts(self):
        return self.main_accounts

    def get_sub_accounts(self):
        return self.sub_accounts

    # TODO: 添加更多帳號管理方法