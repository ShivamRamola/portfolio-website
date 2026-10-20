# Shivam Ramola - Portfolio

Personal portfolio built with Flask and Bootstrap, deployed on Vercel.

Live site: https://portfolio-website-tawny-phi-56.vercel.app/

## Features

- Responsive layout with light and dark themes (follows the system setting, remembers the choice)
- Pages: Home, About (experience, education, skills), Projects, Contact
- Downloadable resume PDF
- Accessible markup: skip link, visible focus states, reduced-motion support
- No database or admin page, so there is nothing to secure or maintain

## Tech stack

- Python, Flask, Jinja2 templates
- Bootstrap 5, Font Awesome, custom CSS in `static/css/style.css`

## Run locally

```bash
git clone https://github.com/ShivamRamola/portfolio-website.git
cd portfolio-website
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## Updating content

All text content (experience, education, skills, projects, contact links) lives at the top of `app.py`. Replace `static/Shivam_Ramola_Resume.pdf` to update the downloadable resume.

## Project structure

```
app.py                  routes and site content
templates/              base layout, pages and the project card partial
static/css/style.css    theme and components
static/images/          profile image
static/                 resume PDF
vercel.json             Vercel deployment config
```

## Author

**Shivam Ramola** - [LinkedIn](https://www.linkedin.com/in/shivamramola/) | [GitHub](https://github.com/ShivamRamola)
