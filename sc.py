import os
import json

IMAGE_FOLDER = "image"

extensions = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".gif"
}

photos = []

for filename in sorted(os.listdir(IMAGE_FOLDER)):
    ext = os.path.splitext(filename)[1].lower()

    if ext in extensions:
        photos.append({
            "src": f"{IMAGE_FOLDER}/{filename}",
            "caption": "😂 Another legendary moment"
        })

with open("photos.js", "w", encoding="utf-8") as f:
    f.write("const PHOTOS = ")
    json.dump(photos, f, ensure_ascii=False, indent=2)
    f.write(";")

print(f"✅ Added {len(photos)} photos")
