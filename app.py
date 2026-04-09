from flask import Flask, render_template

app = Flask(__name__)

media_items = [
    {
        "type": "video",
        "poster": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246414/vauq4o_xhtmy9.jpg",
        "url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246414/vauq4o_xhtmy9.mp4",
        "caption": "Badger best"
    },
    {
        "type": "video",
        "poster": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246413/izjoty_tkg9xn.jpg",
        "url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246413/izjoty_tkg9xn.mp4",
        "caption": "Badger also"
    },
    {
        "type": "video",
        "poster": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246410/j6wxck_g9ps3t.jpg",
        "url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246410/j6wxck_g9ps3t.mp4",
        "caption": "Another Badger"
    },
    {
        "type": "video",
        "poster": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246409/9uenlv_ntdjg5.jpg",
        "url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246409/9uenlv_ntdjg5.mp4",
        "caption": "Again a Badger"
    },
    {
        "type": "video",
        "poster": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775768315/IMAG0036_ltgh93.jpg",
        "url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775768315/IMAG0036_ltgh93.mp4",
        "caption": "Rabbit hopping"
    },
    {
        "type": "video",
        "poster": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775768309/IMAG0039_jnpexy.jpg",
        "url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775768309/IMAG0039_jnpexy.mp4",
        "caption": "Rabbit speed"
    },
    {
        "type": "video",
        "poster": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775767260/IMAG0084_bld7wb.jpg",
        "url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775767260/IMAG0084_bld7wb.mp4",
        "caption": "Rabbit eating"
    },
    {
        "type": "video",
        "poster": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775772059/IMAG0024_xvrk0v.jpg",
        "url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775772059/IMAG0024_xvrk0v.mp4",
        "caption": "Badger walking"
    },
    {
        "type": "video",
        "poster": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775772440/IMAG0096_frcjjb.jpg",
        "url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775772440/IMAG0096_frcjjb.mp4",
        "caption": "Pheasant"
    },
    {
        "type": "image",
        "url": "https://res.cloudinary.com/dkheyxxzk/image/upload/v1775774624/IMAG0011_c2mpai.jpg",
        "caption": "Pheasant still"
    }
]

# {
#     "type": "embed",
#     "url": "https://player.cloudinary.com/embed/?cloud_name=dkheyxxzk&public_id=IMAG0084_bld7wb&profile=cld-default",
#     "caption": "Rabbit eating"
# }

@app.route('/')
def index():
    return render_template('index.html', media=media_items)
