import heapq
import time
from random import random, seed

from typing import List, Tuple
from sklearn.utils import shuffle
from functools import wraps
from copy import deepcopy

from models.vector import Vetor

def execute_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        tempo_ms = (fim - inicio) * 1000
        print(f"A função {func.__name__} levou {tempo_ms:.3f} milissegundos para executar.")
        return resultado, tempo_ms
    return wrapper

@execute_time
def create_vector(positions: int, vector_name, vector_description) -> Tuple[Vetor, float]:
    ordered_vector = [i for i in range(1, positions)]
    return Vetor(vector_name, vector_description, ordered_vector)

def random_index(max_index: int) -> int:
    return int(random() * max_index)

@execute_time
def randomize_vector(vetor: Vetor, random_state: int) -> Tuple[List[int], float]:
    seed(random_state)
    copy_vector = deepcopy(vetor.values) 
    
    for i in range(len(copy_vector)):
        index1 = i
        index2 = random_index(len(copy_vector))
        copy_vector[index1], copy_vector[index2] = copy_vector[index2], copy_vector[index1]
        
    return Vetor(vetor.name, vetor.description, copy_vector)

@execute_time
def heap_sort(vetor: List[int]) -> Tuple[List[int], float]:
    copy_vector = deepcopy(vetor)
    heapq.heapify(copy_vector)
    ordered_vector = []
    while copy_vector:
        ordered_vector.append(heapq.heappop(copy_vector))
    return ordered_vector

@execute_time
def sort_time_taking(vetor: List[int]) -> Tuple[List[float], float]:
    sort_time_taking_list = []
    for _ in range(3):
        _, tempo_ms = heap_sort(vetor)
        sort_time_taking_list.append(tempo_ms)
    return sort_time_taking_list

@execute_time
def randomize_time_taking(vetor: List[int]) -> Tuple[List[float], float]:
    randomize_time_taking_list = []
    for _ in range(3):
        _, tempo_ms = randomize_vector(vetor)
        randomize_time_taking_list.append(tempo_ms)
    return randomize_time_taking_list


def convert_vector_to_text(vector: Vetor) -> str:
    return ','.join(map(str, vector.values))

def convert_text_to_vector(vector: str) -> List[int]:
    return list(map(int, vector.split(',')))
