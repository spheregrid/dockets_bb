

import os

os.system(f"git add .")
os.system(f"git commit -m new")
os.system(f"git checkout --orphan 'latest_branch'")
os.system(f"git add -A")
os.system(f"git commit -am new")
os.system(f"git branch -D main")
os.system(f"git branch -m main")
os.system(f"git branch --set-upstream-to=origin/main main")
os.system(f"git push -f origin main")
