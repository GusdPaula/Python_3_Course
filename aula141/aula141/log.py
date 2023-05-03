# Abstraction
# Log
from abc import ABC, abstractmethod
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log(ABC):
    @abstractmethod
    def _log(self, msg): ...

    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatted = f'{msg} ({self.__class__.__name__})'

        print(f'Saving in log: {msg}')

        with open(LOG_FILE, 'a') as f:
            f.write(msg_formatted)
            f.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == "__main__":
    lp = LogPrintMixin()
    lp.log_error('blabla')
    lp.log_success('blablabla')

    lf = LogFileMixin()
    lf._log('OK')
    lf.log_error('Eofdf')
    lf.log_success('fdfdfd')
