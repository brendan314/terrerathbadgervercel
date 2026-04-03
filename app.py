import os
from flask import Flask, render_template
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.utils import cloudinary_url

app = Flask(__name__)

# Configure Cloudinary - REPLACE WITH YOUR OWN CREDENTIALS
cloudinary.config(
    cloud_name = os.environ.get('CLOUDINARY_CLOUD_NAME', 'your_cloud_name'),
    api_key = os.environ.get('CLOUDINARY_API_KEY', 'your_api_key'),
    api_secret = os.environ.get('CLOUDINARY_API_SECRET', 'your_api_secret')
)

# Dummy video data - using Cloudinary public IDs
videos_data = [
    {
        'id': 'video1',
        'title': 'Badger Foraging at Night (Cloudinary)',
        'description': 'A lone badger caught on camera foraging for food during the late hours, now on Cloudinary!',
        'cloudinary_public_id': 'badger_foraging_example_video' # Replace with your actual Cloudinary video public ID
    },
    {
        'id': 'video2',
        'title': 'Badger Family Playtime (Cloudinary)',
        'description': 'A heartwarming video of a badger sow and her cubs playing near the sett entrance, from Cloudinary.',
        'cloudinary_public_id': 'badger_family_example_video' # Replace with your actual Cloudinary video public ID
    }
]

@app.route('/')
def index():
    processed_videos = []
    for video in videos_data:
        if 'cloudinary_public_id' in video:
            # Generate a secure Cloudinary video URL
            video_url, options = cloudinary_url(
                video['cloudinary_public_id'],
                resource_type="video",
                format="mp4", # Or your preferred video format
                controls=True
            )
            video['embed_url'] = video_url
        processed_videos.append(video)
    return render_template('index.html', videos=processed_videos)

