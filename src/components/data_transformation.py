import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
import os

def process_skills(skill_str):
    skills=skill_str.split("|")
    weights={
        "python":2,"dsa":3,"ml":3,
        "dl":4,"sql":2,"java":2,"c++":2    }