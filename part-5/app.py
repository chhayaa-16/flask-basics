"""
Part 5: Mini Project - Personal Website with Flask
===================================================
A complete personal website using everything learned in Parts 1-4.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template

app = Flask(__name__)

# =============================================================================
#YOUR DATA - Customize this section with your own information! 
# =============================================================================


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        # YOUR DATA - Customize this section with your own information!

        name = request.form.get('name')
        email = request.form.get('email')
        course = request.form.get('course')
        college = request.form.get('college')
        city = request.form.get('city')

        return render_template(
            'result.html',
            name=name,
            email=email,
            course=course,
            college=college,
            city=city
        )

PERSONAL_INFO = {
    'name': 'Chhaya Patil',
    'title': 'Web Developer',
    'bio': 'A passionate developer learning Flask and web development.',
    'email': 'chhayapatil2001@example.com',
    'github': 'https://github.com/chhayaa-16',
    'linkedin': 'https://www.linkedin.com/in/chhaya-patil-311390307?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app',
}

SKILLS = [
    {'name': 'Python', 'level': 80},
    {'name': 'HTML/CSS', 'level': 75},
    {'name': 'Flask', 'level': 60},
    {'name': 'JavaScript', 'level': 50},
    {'name': 'SQL', 'level': 75},
]

PROJECTS = [
    {'id': 1, 'name': 'Personal Website', 'description': 'A Flask-powered personal portfolio website.', 'tech': ['Python', 'Flask', 'HTML', 'CSS'], 'status': 'Completed'},
    {'id': 2, 'name': 'Todo App', 'description': 'A simple task management application.', 'tech': ['Python', 'Flask', 'SQLite'], 'status': 'In Progress'},
    {'id': 3, 'name': 'Weather Dashboard', 'description': 'Display weather data from an API.', 'tech': ['Python', 'Flask', 'API'], 'status': 'Planned'},
    {'id': 4, 'name': ' word venturegame', 'description':'this is gaming app to find word in maze it has a multiples levels .','tech':['html','css','javascript'],'status': 'completed'},
]


# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO)


@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS)


@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)


@app.route('/project/<int:project_id>')  # Dynamic route for individual project
def project_detail(project_id):
    project = None
    for p in PROJECTS:
        if p['id'] == project_id:
            project = p
            break
    return render_template('project_detail.html', info=PERSONAL_INFO, project=project, project_id=project_id)


@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)

BLOG_POSTS = [
    {'title': 'Learning Flask', 'content': 'Flask is a lightweight Python web framework.'},
    {'title': 'Why MCA?', 'content': 'MCA helps build strong foundations in software development.'},
]

@app.route('/blog')
def blog():
    return render_template('blog.html', info=PERSONAL_INFO, posts=BLOG_POSTS)

@app.route('/skill/<skill_name>')
def skill_detail(skill_name):
    related_projects = []

    for project in PROJECTS:
        if skill_name.capitalize() in project['tech']:
            related_projects.append(project)

    return render_template(
        'skill.html',
        skill=skill_name,
        projects=related_projects,
        info=PERSONAL_INFO
    )


if __name__ == '__main__':
    app.run(port=5001,debug=True)


# =============================================================================
# PROJECT STRUCTURE:
# =============================================================================
#
# part-5/
# ├── app.py              <- You are here
# ├── static/
# │   └── style.css       <- CSS styles
# └── templates/
#     ├── base.html       <- Base template (inherited by all pages)
#     ├── index.html      <- Home page
#     ├── about.html      <- About page
#     ├── projects.html   <- Projects list
#     ├── project_detail.html <- Single project view
#     └── contact.html    <- Contact page
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 5.1: Personalize your website
#   - Update PERSONAL_INFO with your real information
#   - Add your actual skills and projects
#
# Exercise 5.2: Add a new page
#   - Create a /blog route
#   - Add blog posts data structure
#   - Create blog.html template
#
# Exercise 5.3: Enhance the styling
#   - Modify static/style.css
#   - Add your own color scheme
#   - Make it responsive for mobile
#
# Exercise 5.4: Add more dynamic features
#   - Create a /skill/<skill_name> route
#   - Show projects that use that skill
#
# =============================================================================
