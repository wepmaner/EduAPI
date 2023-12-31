from dataclasses import dataclass
from typing import Optional

@dataclass
class Day:
    '''День'''
    код: int
    дата: str
    датаНачала: str
    датаОкончания: str
    перерыв: str
    начало: str
    конец: str
    деньНедели: int
    день_недели: str
    почта: str
    день: str
    код_Семестра: int
    типНедели: int
    номерПодгруппы: int
    дисциплина: str
    преподаватель: str
    должность: str
    аудитория: str
    учебныйГод: str
    группа: str
    custom1: str
    часы: str
    неделяНачала: int
    неделяОкончания: int
    замена: bool
    кодПреподавателя: int
    кодГруппы: int
    фиоПреподавателя: str
    кодПользователя: int
    элементЦиклРасписания: bool
    тема: str
    номерЗанятия: int
    ссылка: Optional[None]
    созданиеВебинара: bool
    кодВебинара: Optional[None]
    вебинарЗапущен: bool
    показатьЖурнал: bool
    кодыСтрок: list