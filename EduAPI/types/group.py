from dataclasses import dataclass

@dataclass
class Group:
    '''Группа'''
    name: str
    id: int
    kurs: int
    facul: str
    yearName: str
    facultyID: int
