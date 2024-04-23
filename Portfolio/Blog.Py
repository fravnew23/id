class BlogPost:
    def __init__(self, title, date, content):
        self.title = title
        self.date = date
        self.content = content

# Daftar posting blog
blog_posts = [
    BlogPost("Judul Posting Pertama", "22 Oktober 2023", "Isi posting pertama Anda di sini."),
    BlogPost("Judul Posting Kedua", "21 Oktober 2023", "Isi posting kedua Anda di sini."),
]

# Fungsi untuk menampilkan posting blog
def show_blog_posts():
    for post in blog_posts:
        print(f"Judul: {post.title}")
        print(f"Tanggal: {post.date}")
        print(post.content)
        print("")

# Panggil fungsi untuk menampilkan posting blog
show_blog_posts()