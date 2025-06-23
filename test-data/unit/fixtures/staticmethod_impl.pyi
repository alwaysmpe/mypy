import typing

class object:
    def __init__(self) -> None: pass

class type:
    def __init__(self, x) -> None: pass

class function: pass

_C_co = typing.TypeVar("_C_co", covariant=True)
_P = typing.ParamSpec("_P")
_R_co = typing.TypeVar("_R_co", covariant=True)

class staticmethod(typing.Generic[_C_co]):
    def __init__(self, f: _C_co, /) -> None: ...
    def __get__(self, instance: object, owner: type | None = None, /) -> _C_co: ...
    def __call__(self: staticmethod[typing.Callable[_P, _R_co]], *args: _P.args, **kwargs: _P.kwargs) -> _R_co: ...

class int:
    @staticmethod
    def from_bytes(bytes: bytes, byteorder: str) -> int: pass

class str: pass
class bytes: pass
class ellipsis: pass
class dict: pass
class tuple: pass
