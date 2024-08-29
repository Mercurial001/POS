import logging


class ExcludeSpecificLogMessageFilter(logging.Filter):
    def filter(self, record):
        # Check if the log message is the specific one you want to exclude
        return 'GET /expired_products/' not in record.getMessage()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
