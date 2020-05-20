import abc
import sys
from typing import TypeVar, Generic, Callable

import opres.option as opt

T = TypeVar('T')
E = TypeVar('E')
S = TypeVar('S')


class Result(Generic[T, E], metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def unwrap(self) -> T:
        pass

    @abc.abstractmethod
    def unwrap_err(self) -> E:
        pass

    @abc.abstractmethod
    def unwrap_or(self, default: T) -> T:
        pass

    @abc.abstractmethod
    def unwrap_or_else(self, default_func: Callable[[], T]) -> T:
        pass

    @abc.abstractmethod
    def is_ok(self) -> bool:
        pass

    @abc.abstractmethod
    def is_err(self) -> bool:
        pass

    @abc.abstractmethod
    def expect(self, message: str) -> T:
        pass

    @abc.abstractmethod
    def map(self, f: Callable[[T], S]) -> 'Result[S, E]':
        pass

    @abc.abstractmethod
    def map_or(self, f: Callable[[T], S], default: S) -> 'Result[S, E]':
        pass

    @abc.abstractmethod
    def map_or_else(self, f: Callable[[T], S], default_func: Callable[[], S]) -> 'Result[S, E]':
        pass

    @abc.abstractmethod
    def ok(self) -> 'opt.Option[T]':
        pass

    def err(self) -> 'opt.Option[E]':
        pass


class Ok(Result[T, E]):
    def __init__(self, x: T):
        self._x: T = x

    @property
    def x(self):
        return self._x

    def __eq__(self, other: object):
        if isinstance(other, Ok):
            return self._x == other._x
        else:
            return False

    def __str__(self):
        return f"{self.__class__.__name__}({self._x})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self._x})"

    def unwrap(self) -> T:
        return self.x

    def unwrap_err(self):
        sys.exit(self.x)

    def unwrap_or(self, default: T) -> T:
        return self.x

    def unwrap_or_else(self, default_func: Callable[[], T]) -> T:
        return self.x

    def is_ok(self):
        return True

    def is_err(self):
        return False

    def expect(self, message: str) -> T:
        return self.x

    def map(self, f: Callable[[T], S]) -> 'Result[S, E]':
        return Ok(f(self.x))

    def map_or(self, f: Callable[[T], S], default: S) -> 'Result[S, E]':
        return Ok(f(self.x))

    def map_or_else(self, f: Callable[[T], S], default_func: Callable[[], S]) -> 'Result[S, E]':
        return Ok(f(self.x))

    def ok(self):
        return opt.Some(self.x)

    def err(self):
        return opt.Nothing()


class Err(Result[T, E]):
    def __init__(self, err: E):
        self._error = err

    @property
    def error(self):
        return self._error

    def __eq__(self, other: object):
        if isinstance(other, Err):
            if isinstance(self._error, Exception) and isinstance(other._error, Exception):
                return isinstance(self._error, other._error.__class__) and (self._error.args == other._error.args)
            else:
                return self._error == other._error
        else:
            return False

    def __str__(self):
        return f"{self.__class__.__name__}"

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def unwrap(self):
        sys.exit(self.error)

    def unwrap_err(self) -> E:
        return self.error

    def unwrap_or(self, default: T) -> T:
        return default

    def unwrap_or_else(self, default_func: Callable[[], T]) -> T:
        return default_func()

    def is_ok(self):
        return False

    def is_err(self):
        return True

    def expect(self, message: str):
        sys.exit(str(message))  # 0を渡されると正常終了とみなされるため

    def map(self, f: Callable[[T], S]) -> 'Result[S, E]':
        return Err(self.error)

    def map_or(self, f: Callable[[T], S], default: S) -> 'Result[S, E]':
        return Ok(default)

    def map_or_else(self, f: Callable[[T], S], default_func: Callable[[], S]) -> 'Result[S, E]':
        return Ok(default_func())

    def ok(self):
        return opt.Nothing()

    def err(self):
        return opt.Some(self.error)
