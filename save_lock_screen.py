import os
import shutil

# Spotlight folder
src = os.path.join(
    os.getenv("LOCALAPPDATA"),
    r"Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
)

# Destination folder
dest = r"C:\LockScreenImages"
os.makedirs(dest, exist_ok=True)

for file in os.listdir(src):
    full_path = os.path.join(src, file)

    # Filter out tiny files (icons, metadata)
    if os.path.getsize(full_path) > 200_000:  # ~200 KB
        new_name = file + ".jpg"
        shutil.copy(full_path, os.path.join(dest, new_name))

print("Done. Images saved to:", dest)
