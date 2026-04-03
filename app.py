from flask import Flask, render_template
import os

app = Flask(__name__)

# List of direct video URLs (e.g., from Cloudinary CDN direct links, or any other hosting)
# In a real application, this would typically come from a database.
videos_urls = [
 "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246414/vauq4o_xhtmy9.mp4",
    "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246413/izjoty_tkg9xn.mp4",
    "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246410/j6wxck_g9ps3t.mp4",
    "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246409/9uenlv_ntdjg5.mp4"
]

@app.route('/')
def index():
    processed_videos = []
    for video_url in videos_urls:
        # Extract a "public ID" like string from the URL to generate title/description
        # This assumes a URL structure like .../public_id.mp4
        filename = os.path.basename(video_url)
        public_id = os.path.splitext(filename)[0]

        # Generate title and description from the extracted public ID
        # Example: "badger_foraging_example_video" -> "Badger Foraging Example Video"
        title = public_id.replace('_', ' ').title()
        description = f"A captivating moment from Terrerath Badger Watch: {title.lower()}."

        processed_videos.append({
            'id': public_id, # Use the extracted public_id as a unique ID
            'title': title,
            'description': description,
            'embed_url': video_url
        })
    return render_template('index.html', videos=processed_videos)

