import sys
import abc
from typing import TypeVar, Generic, Callable
import opres.result as res

T = TypeVar('T')
E = TypeVar('E')
S = TypeVar('S')


class Option(Generic[T], metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def unwrap(self) -> T:
        pass

    @abc.abstractmethod
    def unwrap_or(self, default: T) -> T:
        pass

    @abc.abstractmethod
    def unwrap_or_else(self, default_func: Callable[[], T]) -> T:
        pass

    @abc.abstractmethod
    def is_nothing(self) -> bool:
        pass

    @abc.abstractmethod
    def is_some(self) -> bool:
        pass

    @abc.abstractmethod
    def expect(self, message: str) -> T:
        pass

    @abc.abstractmethod
    def map(self, f: Callable[[T], S]) -> 'Option[S]':
        pass

    @abc.abstractmethod
    def map_or(self, f: Callable[[T], S], default: S) -> 'Option[S]':
        pass

    @abc.abstractmethod
    def map_or_else(self, f: Callable[[T], S], default_func: Callable[[], S]) -> 'Option[S]':
        pass

    @abc.abstractmethod
    def ok_or(self, err: E) -> res.Result[T, E]:
        pass

    @abc.abstractmethod
    def ok_or_else(self, err_func: Callable[[], E]) -> res.Result[T, E]:
        pass


class Some(Option[T]):
    def __init__(cls, x: T):
        super(Some, cls).__init__()
        cls._x: T = x

    @property
    def x(self):
        return self._x

    def __eq__(self, other: object):
        if isinstance(other, Some):
            if isinstance(self._x, Exception) and isinstance(other._x, Exception):
                return isinstance(self._x, other._x.__class__) and (self._x.args == other._x.args)
            else:
                return self._x == other._x
        else:
            return False

    def __str__(self):
        return f"{self.__class__.__name__}({self._x})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self._x})"

    def unwrap(self) -> T:
        return self.x

    def unwrap_or(self, default: T) -> T:
        return self.x

    def unwrap_or_else(self, default_func: Callable[[], T]) -> T:
        return self.x

    def is_nothing(self):
        return False

    def is_some(self):
        return True

    def expect(self, message: str) -> T:
        return self.x

    def map(self, f: Callable[[T], S]) -> 'Option[S]':
        return Some(f(self.x))

    def map_or(self, f: Callable[[T], S], default: S) -> 'Option[S]':
        return Some(f(self.x))

    def map_or_else(self, f: Callable[[T], S], default_func: Callable[[], S]) -> 'Option[S]':
        return Some(f(self.x))

    def ok_or(self, err: E) -> res.Result[T, E]:
        return res.Ok(self.x)

    def ok_or_else(self, err_func: Callable[[], E]) -> res.Result[T, E]:
        return res.Ok(self.x)


class Nothing(Option[T]):
    __instance = None

    def __init__(self):
        super(Nothing, self).__init__()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __str__(self):
        return f"{self.__class__.__name__}"

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def __eq__(self, other: object):
        return isinstance(other, Nothing)

    def unwrap(self):
        sys.exit(f"{self} is None")

    def unwrap_or(self, default: T) -> T:
        return default

    def unwrap_or_else(self, default_func: Callable[[], T]) -> T:
        return default_func()

    def is_nothing(self):
        return True

    def is_some(self):
        return False

    def expect(self, message: str):
        sys.exit(message)

    def map(self, f: Callable[[T], S]) -> 'Option[S]':
        return self

    def map_or(self, f: Callable[[T], S], default: S) -> 'Option[S]':
        return Some(default)

    def map_or_else(self, f: Callable[[T], S], default_func: Callable[[], S]) -> 'Option[S]':
        return Some(default_func())

    def ok_or(self, err: E) -> res.Result[T, E]:
        return res.Err(err)

    def ok_or_else(self, err_func: Callable[[], E]) -> res.Result[T, E]:
        return res.Err(err_func())
