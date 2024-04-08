from abc import ABC, abstractmethod


class BaseRepo(ABC):
    def __init__(self, session):
        self.session = session


    @abstractmethod
    def get_all(self):
        raise NotImplementedError


    @abstractmethod
    def get_by_id(self, id):
        raise NotImplementedError
