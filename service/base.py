from abc import ABC

from db.repository.unit_of_work import UnitOfWork


class BaseService(ABC):

    def __init__(self):
        self.uow = UnitOfWork()


    def clean(self):
        self.uow.clean()

