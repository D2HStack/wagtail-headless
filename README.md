# Wagtail Headless Template

This project provides a streamlined starting point for building headless [Wagtail](https://wagtail.org) applications. Inspired by the official [Wagtail News Template](https://github.com/wagtail/news-template), it includes a set of preconfigured pages, blocks, features, and fixtures to accelerate your development workflow.

A [headless CMS](https://wagtail.org/headless/) means that Wagtail is used solely to manage and serve content through its API — without rendering the frontend. This allows you to plug in any frontend technology to consume and display the content.

In a separate project, this backend is integrated with a [React](https://react.dev/) frontend, demonstrating how easily it can be paired with modern frontend frameworks.

🔗 **Live Demo:** You can see this headless setup in action on my website: [aporiamind.com](https://aporiamind.com)

## Getting Started

1. **Check that you have an appropriate version of Python 3** You want to make sure that you have a [compatible version](https://docs.wagtail.org/en/stable/releases/upgrading.html#compatible-django-python-versions) installed:

   ```sh
   python --version
   # Or:
   python3 --version
   # **On Windows** (cmd.exe, with the Python Launcher for Windows):
   py --version
   ```

2. **Create a Virtual Environment**: Set up a virtual environment to isolate your project dependencies. These instructions are for GNU/Linux or MacOS, but there are [other operating systems in the Wagtail docs](https://docs.wagtail.org/en/stable/getting_started/tutorial.html#create-and-activate-a-virtual-environment).

   ```bash
   python -m venv myproject/env
   source myproject/env/bin/activate
   ```

3. **Navigate to Project Directory**: Move into the newly created project directory.

   ```bash
   cd myproject
   ```

4. **Clone the repository**: Clone the repository in your folder.

   ```bash
   git clone https://github.com/D2HStack/wagtail-headless.git ./
   ```

5. **Install Project Dependencies**: Install the project's dependencies into a virtual environment.

   ```bash
   pip install -r requirements.txt
   ```

All commands from now on should be run from inside the virtual environment.

8. **Load Dummy Data**: Load in some dummy data to populate the site with some content.

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

9. **Start the Server**: Start the Django development server.

   ```bash
   python ./manage.py runserver
   ```

10. **Access the Site and Admin**: Once the server is running, you can view the site at `localhost:8000` and access the Wagtail admin interface at `localhost:8000/admin`. Log in with the default credentials provided by :

    - Username: admin
    - Password: password

