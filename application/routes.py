from application import app, db
from flask import render_template, send_file
from application.models import Experience, Post
import os

IMAGES = "../../static/images"
app.config['UPLOAD_FOLDER'] = IMAGES

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    # Experience(job_id=2, company="My Coding Place", period="Spring 2020", location="Austin, TX", summary="Starting off as a studio coordinator, I optimized the website, communicated with customers, and managed the schedule. After transitioning into an instructor, I taught private lessons, classes, and large workshops covering programming basics using Scratch, Python, and Java. I taught both in-person and virtually.", achievement="Led and taught Scratch and Python virtual workshops to 50 kids for a corporate ERG", role="Studio Coordinator & Coding Instructor").save()
    # Experience(job_id=3, company="PricewaterhouseCoopers", period="Summer 2019", location="Austin, TX", summary="I prepared partnership tax returns for the State and Local Tax department for compliance with IRS. I used Excel, Alteryx, and other tax programs to manage financial data of over 3000 funds.", achievement="Learning Excel, tax programs, and accounting principles quickly to work the busy season.", role="Tax Intern").save()
    experience = Experience.objects.all()
    return render_template("index.html", index=True, experience=experience)

@app.route("/about")
def about():
    return render_template("aboutme.html", about = True)

@app.route("/projects")
def projects():
    return render_template("projects.html", work = True)

@app.route("/blog")
def blog():
    # Post(post_id=1,title="Building This Website", teaser="I know firsthand how intimidating it is to try and build something new, so I want to share some of my experiences building this web app. Here are some lessons I picked up through this project", body=[["When I took my first programming class in the spring of 2019, I had finally found a profession right for me. Before that semester, I had thought I could be pre-med since I loved science, or pre-law since I loved logic. Most of all, I had thought I could be an accountant since I loved details, and I had secured a tax internship that summer.  But learning Python for the first time, I finally found something that combined science, logic, and details—programming.","Since then, it’s been a speedy journey to learn as much as I can. I felt insecure that I was a business major, and I had started programming so late</. How could I start a career that involved coding? To answer that question, I changed my major to MIS, started my certificate in computer science, and seeked jobs with technical roles.","Then came my internship at Dell Technologies. My role involved project management, and I was excited. It was a career path that fit my background really well. However, I had a gut feeling that software engineering was where I really wanted to be. I scheduled as many 1x1s as I could with engineers at Dell, and I’m so happy I did. Their collective advice and support were so encouraging, and it gave me motivation to do a technical side project for Dell as well as start this website.","I know firsthand how intimidating it is to try and build something new, so I want to share some of my experiences building this web app. Here are some lessons I picked up through this project."],[">On the first day of building the website, I knew nothing about front-end. I had very minimal knowledge about HTML and Bootstrap, and I knew close to nothing about CSS and JavaScript. The only thing I knew was what I wanted the website to look like, and I realized this was all I needed to get started. I imagined an animation for the top of my website, a landscape view of mountains, changing from night to day with a single click. I knew how to make this with Processing, and I realized that I’d seen people embed their Processing sketches onto websites such as openprocessing.org. From there, I googled how to embed sketches into a web app, and I began to understand how HTML and JavaScript work together.","From there, I didn’t like the navigation bar, so I learned how Bootstrap and my own external CSS files interact. I wanted to place an image and text next to each other, so I learned the Bootstrap grid system. With each design change, I earned a nugget of information about front-end programming. By the time my home page looked the way I wanted, I was no longer googling every single change I wanted to make.","I may not have made a lot of visual progress during the first few days of coding my site, but soon after, my pace grew exponentially since I retained my new knowledge in a way that classroom learning doesn’t allow. Googling one design change enabled me to make the next one on my own."],["Thanks to the internet, we can learn almost any programming language, anytime. However, we can also follow coding tutorials without actually understanding what’s going on. Your website will look great, you followed all the steps someone else listed out. However, none of the skills end up sticking. This trap is appealing, but I found a way that allows me to learn from code I find on the internet.","When I wanted an interactive timeline on my home page, I realized I needed JavaScript. I didn’t know JavaScript, but I did see an in-depth tutorial for the exact timeline I wanted on Google. Before I started with the tutorial, I watched a JavaScript crash course video on YouTube. I learned what it does, basic syntax, and how much the language had changed over the years. Then, I followed the tutorial in small chunks at a time, making sure to type the code in myself rather than copying and pasting. With every few lines, I ran the application to see the changes the code made, and I gained a vague understanding. From there, I knew which lines of code I had to change to let me customize the timeline. For example, in the JS function determining when to disable the arrow buttons at the bottom of my timeline, I changed the visibility requirements to be narrower, to allow the user to see more of the timeline before an arrow button becomes disabled. Lastly, I “rubber duckied” every line of code, explaining to myself in comments what everything did. I also commented the source to the tutorial for the next person trying to build the same thing.","In summary, when following coding tutorials, I believe watching a crash course on the language, coding in small sections, and explaining the code in comments allows me to effectively learn new things."],["I’m still insecure about my technical abilities and future as a software engineer. But I feel more confident knowing I’m building my skills one project at a time. I feel so grateful for everyone who encourages me to build the solutions I want to see in the world. I’m excited to see what I learn next.","If you have any feedback on this site, I would love to hear it. I’m especially working towards writing clean code, learning more JavaScript, and improving the design of the site. Please reach out through email or LinkedIn for any constructive criticism!"]], date="08/08/2020", heading=["One Thing Leads to Another","The Tutorial Trap", "I'm Not Done Learning"]).save()
    posts = Post.objects.all()
    return render_template("bloghome.html", blog = True, posts=posts)

@app.route("/post/<string:id>/")
@app.route("/post/")
def blog_post(id=None):
    if (id == None):
        posts = Post.objects.all()
        return render_template("bloghome.html", blog = True, posts=posts)
    else:
        filename = os.path.join(IMAGES, "blog"+str(id)+".jpg")
        post = Post.objects.get(post_id=id)
        return render_template("post.html", blog=True, post = post, user_image=filename)
