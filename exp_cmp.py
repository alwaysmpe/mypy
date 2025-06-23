from typing import Self, reveal_type

class Exp:
    def a(self) -> None:
        pass
    def b(self: Self) -> None:
        pass
    def c(self, arg: Self) -> None:
        pass
class Exp2:
    def c(self) -> None:
        Exp.a(self)
        Exp.b(self)
        Exp.c(self, self)
        Exp.c(self, Exp())
        Exp.c(Exp(), self)
    def d(self: Self) -> None:
        Exp.a(self)
        Exp.b(self)
        Exp.c(self, self)
        Exp.c(self, Exp())
        Exp.c(Exp(), self)
reveal_type(Exp.a)
reveal_type(Exp.b)
reveal_type(Exp.c)
