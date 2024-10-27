import pandas as pd
import folium
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os

def load_bus_stops(file_path):
    df = pd.read_csv(file_path)
    return df
