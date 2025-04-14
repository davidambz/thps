import csv
import os

def read_usernames_from_file(filepath: str) -> list[str]:
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")

    _, ext = os.path.splitext(filepath)

    if ext.lower() == ".txt":
        return _read_from_txt(filepath)
    elif ext.lower() == ".csv":
        return _read_from_csv(filepath)
    else:
        raise ValueError("Formato de arquivo não suportado. Use .txt ou .csv.")

def _read_from_txt(filepath: str) -> list[str]:
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def _read_from_csv(filepath: str) -> list[str]:
    usernames = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                usernames.append(row[0].strip())
    return usernames
