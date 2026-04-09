from flask import Flask, render_template

app = Flask(__name__)

videos = [
    {
        "url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246414/vauq4o_xhtmy9.mp4",
        "caption": "Badger best"
    },
    {
        "url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246413/izjoty_tkg9xn.mp4",
        "caption": "Badger also"
    },
    {
        "url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246410/j6wxck_g9ps3t.mp4",
        "caption": "Another Badger"
    },
    {
        "url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246409/9uenlv_ntdjg5.mp4",
        "caption": "Again a Badger"
    }
]


@app.route('/')
def home():
    return render_template('index.html', media=media_items)


from flask import Flask, render_template

app = Flask(__name__)

media_items = [
    {
        "type": "video",
        "url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246414/vauq4o_xhtmy9.mp4",
        "caption": "Badger best"
    },
    {
        "type": "video",
        "url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246413/izjoty_tkg9xn.mp4",
        "caption": "Badger also"
    },
    {
        "type": "video",
        "url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246410/j6wxck_g9ps3t.mp4",
        "caption": "Another Badger"
    },
    {
        "type": "video",
        "url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246409/9uenlv_ntdjg5.mp4",
        "caption": "Again a Badger"
    }
]


@app.route('/')
def index():
    return render_template('index.html', media=media_items)
