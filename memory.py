# ============================================
# memory.py
# Long-Term Memory Module
# ============================================

memory = {}

def save_memory(key, value):
    memory[key] = value

def load_memory(key):
    return memory.get(key, None)

def show_memory():
    return memory
