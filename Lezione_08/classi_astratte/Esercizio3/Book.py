from typing import Self

class Book:
    def __init__(self, title:str, autor:str, isbn:str):
        self._title = title
        self._author = autor
        self._isbn = isbn

    def __str__(self):
        return f"Title = {self._title}; Autor = {self._author}; ISBN = {self._isbn}"
    
    @classmethod
    def from_string (cls, repr_str: str) -> Self:
        sub_strs = repr_str.split(',')
        return cls(sub_strs[0], sub_strs[1], sub_strs[2])