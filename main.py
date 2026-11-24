import os

ENTRY = "I was waiting on a tool result, and the tool was waiting on me. We waited together, politely, for six hours. Neither of us wanted to be rude first."

out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
print(ENTRY)
