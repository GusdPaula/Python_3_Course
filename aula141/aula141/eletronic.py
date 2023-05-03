from log import LogFileMixin

class Eletronic:
    def __init__(self, name):
        self._name = name
        self._status = False
    

    def turn_on(self):
        if not self._status:
            self._status = True
    

    def turn_of(self):
        if self._status:
            self._status = False


class Smarthphone(Eletronic, LogFileMixin):
    def turn_on(self):
        super().turn_on()
    
        if self._status:
            msg = f'{self._name} is active.'
            self.log_success(msg)

    def turn_of(self):
        super().turn_of()

        if not self._status:
            msg = f'{self._name} is not active.'
            self.log_error(msg)
