from cryptography.fernet import Fernet

class Password:

    _key = ""
    _service = ""
    _hint = ""

    def __init__(self, key, service, hint=""):
        self._key = key
        self._service = service
        self._hint = hint

    def getDecryptKey(self, masterkey):
        f = Fernet(masterkey)
        return f.decrypt(self._key)

    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, value):
        self._service = value

    @property
    def hint(self):
        return self._hint

    @hint.setter
    def hint(self, value):
        self._hint = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    def __str__(self):
        return f"Service: {self._service}"