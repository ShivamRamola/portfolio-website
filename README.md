# Personal Portfolio Website

A modern, responsive personal portfolio website built with Flask, featuring a clean design and professional presentation.

## 🚀 Features

- **Responsive Design**: Fully responsive layout that works on desktop, tablet, and mobile devices
- **Modern UI**: Clean and professional interface with intuitive navigation
- **Dynamic Content**: Flask-powered backend for easy content management
- **Sections Include**:
  - Home page with personal introduction
  - About page with detailed background
  - Projects showcase
  - Contact form
  - Admin panel for content management

## 🛠️ Technologies Used

- **Backend**: Python Flask
- **Frontend**:
  - HTML5, CSS3
  - Bootstrap 5
  - Font Awesome icons
- **Database**: SQLite
- **Other Tools**:
  - Flask-SQLAlchemy
  - Flask-Login (for admin panel)

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 🔧 Installation & Setup

1. Clone the repository

```bash
git clone https://github.com/ShivamRamola/portfolio.git
cd portfolio
```

2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set up environment variables (create a .env file)

```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key_here
```

5. Initialize the database

```bash
flask db init
flask db migrate
flask db upgrade
```

6. Run the application

```bash
flask run
```

The application will be available at `http://localhost:5000`

## 📁 Project Structure

```
flask_portfolio/
│
├── static/
│   └── images/
│       └── profile.png
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── projects.html
│   ├── contact.html
│   └── admin.html
│
├── app.py
├── portfolio.db
└── README.md
```

## 🔐 Admin Panel

The admin panel allows you to:

- Manage project entries
- Update personal information
- View contact form submissions
- Modify site content

Access the admin panel at `/admin` with appropriate credentials.

## 🎨 Customization

1. Update personal information in the templates
2. Modify styles in the CSS files
3. Add new projects through the admin panel
4. Customize the contact form fields

## 📱 Responsive Design

The portfolio is optimized for:

- Desktop (1200px and above)
- Tablet (768px to 1199px)
- Mobile (below 768px)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Shivam Ramola**

- Portfolio: [shivamramola.com](https://shivamramola.com)
- GitHub: [@ShivamRamola](https://github.com/ShivamRamola)
- LinkedIn: [Shivam Ramola](https://www.linkedin.com/in/shivamchandramola/)

## 🙏 Acknowledgments

- Bootstrap for the responsive framework
- Font Awesome for the icons
- Flask community for the excellent documentation
