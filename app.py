from flask import Flask, abort, redirect, render_template, url_for

app = Flask(__name__)

PROFILE = {
    "name": "Joseph Casino",
    "role": "Safety Service Engineer",
    "headline": "Computer Engineering graduate from UIUC with a Business minor.",
    "summary": (
        "I work across embedded systems, hardware design, software development, "
        "automation, and machine safety. I like hands-on engineering problems "
        "that combine real equipment, practical constraints, and clear technical "
        "communication."
    ),
    "resume": "/static/JosephCasino_Resume_2026.pdf",
    "email": "josephcasino88@gmail.com",
    "phone": "773-844-1041",
}

NAV_LINKS = [
    ("Home", "index"),
    ("About", "about"),
    ("Experience", "experience"),
    ("Education", "education"),
    ("Projects", "projects"),
    ("Socials", "socials"),
    ("Contact", "contact"),
]

SKILL_GROUPS = [
    {
        "title": "Hardware",
        "items": ["FPGA", "PCB", "Ki-Cad", "STM32", "Xilinx Vivado/Vitis", "Quartus", "PWM", "AXI", "SPI", "I2C", "UART", "LiDAR"],
    },
    {
        "title": "Software",
        "items": ["Verilog", "SystemVerilog", "C", "C++", "Assembly (RISC-V)", "Python", "HTML/CSS", "JavaScript", "Git", "GDB", "VS Code", "cPanel"],
    },
    {
        "title": "Administrative",
        "items": ["Microsoft Office Suites", "Canva", "Slack", "Data Analytics", "Accounting", "Marketing", "Organizational Management"],
    },
]

EXPERIENCES = [
    {
        "slug": "safe-t-sense-safety-services-engineer",
        "logo_label": "Safe-T-Sense, LLC logo",
        "logo": "/static/Images/SafeTSenseLogo.png",
        "date": "Jun 2026 - Present",
        "duration": "2 mos",
        "title": "Safety Services Engineer",
        "organization": "Safe-T-Sense, LLC",
        "employment": "Full-time",
        "location": "Schaumburg, Illinois, United States",
        "workplace": "On-site",
        "summary": "Safety Services Engineer at Safe-T-Sense, LLC.",
        "bullets": [
            "Support machine safety projects across risk assessment, safety concept, engineering, verification, integration, and validation.",
            "Document hazards, applicable standards, safeguards, and non-compliance items to improve safety and regulatory alignment.",
            "Assist with engineering deliverables including I/O lists, BOMs, layouts, validation plans, and safety function documentation.",
        ],
        "skills": [],
        "images": [],
    },
    {
        "slug": "grainger-ece-learning-assistant",
        "logo_label": "The Grainger College of Engineering logo",
        "logo": "/static/Images/UIUC_Grainger_Logo.png",
        "date": "Aug 2024 - Dec 2025",
        "duration": "1 yr 5 mos",
        "title": "ECE Engineering Learning Assistant",
        "organization": "The Grainger College of Engineering",
        "employment": "Part-time",
        "location": "Champaign, Illinois, United States",
        "workplace": "On-site",
        "summary": "Mentored first-year computer engineering students through lessons, resources, and one-on-one support.",
        "bullets": [
            "Led bi-weekly lessons introducing engineering concepts and campus resources to first-year computer engineering students.",
            "Provided 1:1 mentoring sessions to support personal and academic development, and integration into the Grainger community.",
        ],
        "skills": ["Public Speaking", "Teaching", "+2 skills"],
        "images": [],
    },
    {
        "slug": "leanmail-scaleyou-software-developer",
        "logo_label": "LeanMail / ScaleYOU logo",
        "logo": "/static/Images/ScaleYOU_Leanmail_Logo.png",
        "date": "Jun 2025 - Jul 2025",
        "duration": "2 mos",
        "title": "Software Developer",
        "organization": "LeanMail / ScaleYOU",
        "employment": "Internship",
        "location": "Barcelona, Catalonia, Spain",
        "workplace": "On-site",
        "summary": "Built automations, supported website improvements, and helped document software projects.",
        "bullets": [
            "Developed and deployed automations with Python and CRM scripting, streamlining workflows and reducing manual effort.",
            "Partnered with the marketing team to enhance the company website, improving performance and overall user experience.",
            "Contributed to end-to-end project planning, drafting technical specifications and user documentation to support delivery.",
        ],
        "skills": ["Python", "Customer Relationship Management", "+1 skill"],
        "images": ["/static/Images/Barcelona.png"],
    },
    {
        "slug": "usps-engineering-intern",
        "logo_label": "United States Postal Service logo",
        "logo": "/static/Images/USPSLogo.jpg",
        "date": "May 2024 - Jul 2024",
        "duration": "3 mos",
        "title": "Solutions Engineering Intern",
        "organization": "United States Postal Service",
        "employment": "Internship",
        "location": "Merrifield, Virginia, United States",
        "workplace": "",
        "summary": "Supported AFCS 200 camera analysis, calibration research, and supplier-facing technical updates.",
        "bullets": [
            "Assisted the Advanced Facer Canceller Modernization (AFCS) 200 Program by performing spatial frequency response analysis on custom-made target test cards using Burns Digital Imaging ImCheck4 software to analyze the quality of the AFCS 200 camera modules.",
            "Presented a proposal for a change in the camera calibration period for sortation machines, supported with thorough data analysis that can be applied to thousands of machines across the country, saving USPS about 1700 hours or about $132,000 of labor costs annually.",
            "Attended frequent technical meetings with hardware and software suppliers for program status updates.",
        ],
        "skills": ["Problem Solving", "Communication", "+5 skills"],
        "images": ["/static/Images/USPS.png"],
    },
    {
        "slug": "indian-hill-club-designer",
        "logo_label": "INDIAN HILL CLUB logo",
        "logo": "/static/Images/IndianHillLogo.png",
        "date": "May 2023 - Sep 2023",
        "duration": "5 mos",
        "title": "Website Maintenance, Graphic Designer",
        "organization": "INDIAN HILL CLUB",
        "employment": "Part-time",
        "location": "Winnetka, Illinois, United States",
        "workplace": "",
        "summary": "Maintained website content, created member-facing graphics, and supported club communications.",
        "bullets": [
            "Regularly updated website content using the NorthStar Club Management Software.",
            "Created graphics for upcoming events and sent finished products periodically to over 1000 active members.",
            "Worked on the Facilities Planning Project by designing graphics and webpages, then communicating with Club administration about project details.",
            "Designed and released a seasonal newsletter featuring messages from the Club administration and Board.",
        ],
        "skills": [],
        "images": [],
    },
]

EDUCATION = [
    {
        "slug": "uiuc",
        "logo_label": "UIUC logo",
        "logo": "/static/Images/UIUC-Logo.png",
        "date": "Class of 2026",
        "title": "University of Illinois Urbana-Champaign",
        "short": "B.S. Computer Engineering",
        "minor": "Business Minor",
        "detail_page": True,
        "engineering_classes": [
            "Advanced Computer Graphics",
            "Advanced Digital Projects Lab",
            "Algorithms and Models of Computation",
            "Analog Signal Processing",
            "Calculus I, II, and III",
            "Computer Systems Programming",
            "Data Structures",
            "Differential Equations",
            "Digital Systems Laboratory",
            "Discrete Structures",
            "Electronic Circuits",
            "Linear Algebra",
            "Machine Learning",
            "Physics: Electricity and Magnetism",
            "Physics: Mechanics",
            "Physics: Quantum",
            "Physics: Thermal",
            "Power Circuits and Electromechanics",
            "Principles of Safe Autonomy",
            "Robotics",
            "Senior Design Project Lab",
            "Sensors and Instrumentation",
        ],
        "business_classes": [
            "Accounting",
            "Data Analytics Applications",
            "Information Technology for Networked Organizations",
            "Marketing",
            "Organizational and Behavioral Management",
            "Personal Financial Planning",
        ],
        "ap_classes": [],
        "extracurriculars": [
            "Dodgeball Club",
            "Engineering Council",
            "Grainger First-Year Experience (GFX)",
            "Illini Pride (Block I and Orange Krush)",
            "Lego Masters",
            "Philippines Student Association",
        ],
        "images": [],
    },
    {
        "slug": "grant-community-high-school",
        "logo_label": "Grant Community High School logo",
        "logo": "/static/Images/GCHSLogo.png",
        "date": "Class of 2022",
        "title": "Grant Community High School",
        "short": "High School",
        "minor": "",
        "detail_page": True,
        "engineering_classes": [],
        "business_classes": [],
        "ap_classes": [
            "Calculus BC",
            "English Language and Composition",
            "Physics I",
            "Psychology",
            "Statistics",
        ],
        "extracurriculars": [
            "Big Dawg Mentor",
            "Chamber Singers",
            "Choir",
            "Class Council (President)",
            "Future Business Leaders of America (President)",
            "Lighting Crew",
            "Math Tutor",
            "National Honors Society (Publicist)",
            "Student Council (Publicist)",
        ],
        "images": [],
    },
]

PROJECTS = [
    {
        "slug": "impact-insoles",
        "title": "Impact Insoles",
        "category": "Senior Design",
        "image": "/static/Images/ImpactInsoles.jpg",
        "summary": "Pressure-sensing insoles for runners using force sensing resistors, custom circuitry, Bluetooth communication, and web-based data visualization.",
        "bullets": [
            "Designed and built pressure-sensing insoles using force sensing resistors embedded in foam insoles.",
            "Developed a wearable system with a custom PCB, Bluetooth communication, and web data visualization.",
            "Earned an honorable mention from the University of Illinois ECE Department.",
        ],
        "tags": ["PCB", "Bluetooth", "Web App"],
        "featured": True,
    },
    {
        "slug": "atat-walker",
        "title": "AT-AT Walker",
        "category": "Embedded Systems and Robotics",
        "image": "/static/Images/ATAT.png",
        "summary": "A custom robotic walker built around STM32 control, PWM-driven servos, Bluetooth communication, custom PCB design, and gait sequencing.",
        "bullets": [
            "Built a servo-controlled walking robot using an STM32 microcontroller, PWM motor control, and embedded C.",
            "Designed movement sequences and control logic for coordinated multi-leg motion.",
            "Integrated hardware, firmware, and mechanical design into a functional embedded system.",
        ],
        "tags": ["STM32", "PWM", "Robotics"],
        "featured": True,
    },
    {
        "slug": "risc-v-operating-system",
        "title": "RISC-V Operating System",
        "category": "Systems Software",
        "image": "/static/Images/391.png",
        "summary": "A low-level operating systems project involving paging, memory management, process control, device interfaces, and file systems.",
        "bullets": [
            "Implemented virtual memory, paging, process control, and file system operations.",
            "Worked with low-level C, assembly concepts, page tables, interrupts, traps, and device interfaces.",
            "Strengthened systems-level debugging and computer architecture understanding.",
        ],
        "tags": ["RISC-V", "C", "OS"],
        "featured": True,
    },
    {
        "slug": "systemverilog-tetris",
        "title": "SystemVerilog Tetris",
        "category": "Digital Design",
        "image": "/static/Images/Tetris.png",
        "summary": "A Tetris-style game on FPGA hardware using SystemVerilog, display output, keyboard input, and game-state logic.",
        "bullets": [
            "Created a Tetris-style game on FPGA hardware using SystemVerilog and digital design principles.",
            "Implemented display output, keyboard control, game logic, collision detection, and hardware-based state management.",
            "Gained experience with FPGA design, hardware debugging, and real-time digital systems.",
        ],
        "tags": ["SystemVerilog", "FPGA", "Game Logic"],
        "featured": False,
    },
    {
        "slug": "autonomous-vehicle",
        "title": "Autonomous LiDAR Mapping Car",
        "category": "Robotics & Autonomy",
        "image": "/static/Images/484.png",
        "summary": "Autonomous systems work involving ROS, Gazebo, LiDAR, localization, mapping, pure pursuit, lane detection, and particle filters.",
        "bullets": [
            "Worked with ROS, Gazebo, LiDAR, and vehicle control algorithms for autonomous vehicle development.",
            "Implemented and studied pure pursuit control, particle filter localization, mapping, and perception.",
            "Applied software, robotics, and control theory to autonomous driving simulations and robotic systems.",
        ],
        "tags": ["ROS", "LiDAR", "Autonomy"],
        "featured": False,
    },
    {
        "slug": "mtd-bus-led-tracker",
        "title": "MTD Bus LED Tracker",
        "category": "Embedded Systems",
        "image": "/static/Images/MTDTracker.png",
        "summary": "A STM32-based system that visualizes live UIUC bus locations using Wi-Fi networking, MTD API data, and an addressable LED display.",
        "bullets": [
            "Connected live transit data to a physical LED visualization.",
            "Combined microcontroller work, networking, APIs, and display logic.",
        ],
        "tags": ["STM32", "API", "LEDs"],
        "featured": False,
    },
    {
        "slug": "object-tracking-camera",
        "title": "Real-Time Object Tracking Camera",
        "category": "FPGA Vision",
        "image": "/static/Images/Camera.png",
        "summary": "An FPGA-based vision system using frame differencing and centroid extraction to drive closed-loop pan tracking.",
        "bullets": [
            "Processed camera frames for real-time object tracking.",
            "Connected visual processing to motor movement for closed-loop control.",
        ],
        "tags": ["FPGA", "Vision", "Motor Control"],
        "featured": False,
    },
    {
        "slug": "python-pokedex",
        "title": "Python Pokedex",
        "category": "Desktop Application",
        "image": "/static/Images/PyPokedex.png",
        "summary": "A tkinter-based Python app using a Pokemon API to search and display information for more than 1,000 characters.",
        "bullets": [
            "Built a searchable desktop interface using Python and API data.",
            "Focused on data display, interaction flow, and continued iteration.",
        ],
        "tags": ["Python", "API", "tkinter"],
        "featured": False,
        "external_url": "https://github.com/JCPandaz/Python-Pokedex",
    },
    {
        "slug": "personal-portfolio-website",
        "title": "Personal Portfolio Website",
        "category": "Web Development",
        "image": "/static/Images/JC_Work.png",
        "summary": "A personal website built to organize projects, experience, education, socials, and contact information in one place.",
        "bullets": [
            "Built a multi-page portfolio with dedicated routes for projects, education, experience, socials, and contact.",
            "Created a red and blue visual system with responsive layouts and image-focused pages.",
            "Structured the site so each project can grow into its own detailed page.",
        ],
        "tags": ["Flask", "HTML/CSS", "Portfolio"],
        "featured": False,
    },
]

SOCIALS = [
    {
        "name": "Instagram",
        "handle": "@thejosephcasino",
        "href": "https://www.instagram.com/thejosephcasino",
        "icon": "/static/Social_Icons/1.png",
    },
    {
        "name": "LinkedIn",
        "handle": "joseph-casino",
        "href": "https://www.linkedin.com/in/joseph-casino/",
        "icon": "/static/Social_Icons/2.png",
    },
    {
        "name": "Discord",
        "handle": "@jcpandaz",
        "href": "https://discordapp.com/users/345012970402873345",
        "icon": "/static/Social_Icons/3.png",
    },
    {
        "name": "Spotify",
        "handle": "Joseph Casino",
        "href": "https://open.spotify.com/user/kwomt9ag8v0vnrzxzz1wbfc9v",
        "icon": "/static/Social_Icons/4.png",
    },
    {
        "name": "GitHub",
        "handle": "@JCPandaz",
        "href": "https://github.com/JCPandaz",
        "icon": "/static/Social_Icons/5.png",
    },
    {
        "name": "YouTube",
        "handle": "@JCPandaz",
        "href": "https://www.youtube.com/JCPandaz",
        "icon": "/static/Social_Icons/6.png",
    },
    {
        "name": "TikTok",
        "handle": "@jcpandaz",
        "href": "https://www.tiktok.com/@jcpandaz",
        "icon": "/static/Social_Icons/7.png",
    },
    {
        "name": "X",
        "handle": "@thejosephcasino",
        "href": "https://x.com/thejosephcasino",
        "icon": "/static/Social_Icons/8.png",
    },
    {
        "name": "Facebook",
        "handle": "Joseph Michael-Casino",
        "href": "https://www.facebook.com/profile.php?id=100011346090489",
        "icon": "/static/Social_Icons/9.png",
    },
]


def get_project(slug):
    return next((project for project in PROJECTS if project["slug"] == slug), None)


def get_experience(slug):
    return next((experience_item for experience_item in EXPERIENCES if experience_item["slug"] == slug), None)


def get_education(slug):
    return next((education_item for education_item in EDUCATION if education_item["slug"] == slug), None)


@app.context_processor
def inject_site_data():
    return {
        "nav_links": NAV_LINKS,
        "profile": PROFILE,
    }


@app.route("/")
def index():
    featured_projects = [project for project in PROJECTS if project.get("featured")]
    return render_template("index.html", projects=featured_projects, socials=SOCIALS)


@app.route("/about")
def about():
    return render_template("about.html", skills=SKILL_GROUPS)


@app.route("/experience")
def experience():
    return render_template("experience.html", experiences=EXPERIENCES)


@app.route("/experience/<slug>")
def experience_detail(slug):
    experience_item = get_experience(slug)
    if experience_item is None:
        abort(404)
    return render_template("experience_detail.html", experience=experience_item, experiences=EXPERIENCES)


@app.route("/education")
def education():
    return render_template("education.html", education=EDUCATION)


@app.route("/education/uiuc-computer-engineering")
def old_uiuc_education_detail():
    return redirect(url_for("education_detail", slug="uiuc"), code=301)


@app.route("/education/<slug>")
def education_detail(slug):
    education_item = get_education(slug)
    if education_item is None or not education_item.get("detail_page"):
        abort(404)
    return render_template("education_detail.html", education_item=education_item)


@app.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)


@app.route("/projects/<slug>")
def project_detail(slug):
    project = get_project(slug)
    if project is None:
        abort(404)
    return render_template("project_detail.html", project=project, projects=PROJECTS)


@app.route("/socials")
def socials():
    return render_template("socials.html", socials=SOCIALS)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=80)
