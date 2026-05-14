import os
import re

folder = r"D:\Python-learning-and-codes\Python codes\Chapter-09-PS"

for filename in os.listdir(folder):
    if filename.endswith(".py"):
        match = re.match(r"(\d+)_problem(\d+)\.py$", filename)
        if match:
            num = match.group(1)
            new_name = f"{num}_problem.{num}.py"
            
            old_path = os.path.join(folder, filename)
            new_path = os.path.join(folder, new_name)
            
            os.rename(old_path, new_path)
            print(f"{filename}  →  {new_name}")

print("Done!")