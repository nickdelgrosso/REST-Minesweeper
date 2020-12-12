from abc import ABC, abstractmethod

from src.data.inmemory import Session


class BaseUseCase(ABC):
    def __init__(self, session: Session):
        self.session = session

    @abstractmethod
    def __call__(self, *args, **kwargs):
        ...