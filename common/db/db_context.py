from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

from configuration.config_manager import Configuration
from tools.singeltone import Singleton


class DbContext(metaclass=Singleton):

    def __init__(self):
        self._config: dict = Configuration().get("db")
        self._engine = None
        self._context_active = False
        self.stam = ""


    def _open_connection_if_not_exist(self):
        if not self._engine:
            db_url = f"{self._config['type']}://{self._config['username']}:{self._config['password']}@{self._config['host']}:" \
                     f"{self._config['port']}/{self._config['database']}"
            self._engine = create_engine(db_url, echo=True)
        self._context_active = True


    def get_or_create_connection(self):
        self._open_connection_if_not_exist()
        return self._engine


    class SessionContext:
        def __init__(self):
            self._session = None


        def _create_session(self):
            engine = DbContext().get_or_create_connection()
            Session = sessionmaker()
            self._session = Session(bind=engine)


        def __enter__(self):
            self._create_session()
            return self._session


        def __exit__(self, exc_type, exc_val, exc_tb):
            self._session.close()


        def get_session(self):
            if self._session:
                return self._session
            self._create_session()
            return self._session


        def close_session(self):
            if self._session:
                self._session.close()