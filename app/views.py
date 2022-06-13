from app import app
from flask import render_template


@app.route("/") 
def index():
    return render_template("superio-html/index.html")

@app.route("/about.html") 
def about():
    return render_template("superio-html/about.html")


@app.route("/blog-list-v1.html") 
def blog_list_v1():
    return render_template("superio-html/blog-list-v1.html")

@app.route("/blog-list-v2.html") 
def blog_list_v2():
    return render_template("superio-html/blog-list-v2.html")

@app.route("/blog-list-v3.html") 
def blog_list_v3():
    return render_template("superio-html/blog-list-v3.html")

@app.route("/blog_single.html") 
def blog_single():
    return render_template("superio-html/blog_single.html")


@app.route("/candidate-dashboard-applied-job.html") 
def candidate_dashboard_applied_job():
    return render_template("superio-html/candidate-dashboard-applied-job.html")

@app.route("/candidate-dashboard-cv-manager.html") 
def candidate_dashboard_cv_manager():
    return render_template("superio-html/candidate-dashboard-cv-manager.html")


@app.route("/candidate-dashboard-job-alerts.html") 
def candidate_dashboard_job_alerts():
    return render_template("superio-html/candidate-dashboard-job-alerts.html")

@app.route("/candidate-dashboard-profile.html") 
def candidate_dashboard_profile():
    return render_template("superio-html/candidate-dashboard-profile.html")

@app.route("/candidate-dashboard-resume.html") 
def candidate_dashboard_resume():
    return render_template("superio-html/candidate-dashboard-resume.html")

@app.route("/candidate-dashboard-shortlisted-resume.html") 
def candidate_dashboard_shortlisted_resume():
    return render_template("superio-html/candidate-dashboard-shortlisted-resume.html")

@app.route("/candidate-dashboard.html") 
def candidate_dashboard():
    return render_template("superio-html/candidate-dashboard.html")

@app.route("/candidates-list-v5.html") 
def candidates_list_v5():
    return render_template("superio-html/candidates-list-v5.html")

@app.route("/candidates-single-v3.html") 
def candidates_single_v3():
    return render_template("superio-html/candidates-single-v3.html")

@app.route("/contact.html") 
def contact():
    return render_template("superio-html/contact.html")

@app.route("/dashboard-applicants.html") 
def dashboard_applicants():
    return render_template("superio-html/dashboard-applicants.html")

@app.route("/dashboard-change-password.html") 
def dashboard_change_password():
    return render_template("superio-html/dashboard-change-password.html")

@app.route("/dashboard-company-profile.html") 
def dashboard_company_profile():
    return render_template("superio-html/dashboard-company-profile.html")

@app.route("/dashboard-manage-job.html")
def dashboard_manage_job():
    return render_template("superio-html/dashboard-manage-job.html")

@app.route("/dashboard-messages.html") 
def dashboard_messages():
    return render_template("superio-html/dashboard-messages.html")

@app.route("/dashboard-packages.html")
def dashboard_packages():
    return render_template("superio-html/dashboard-packages.html")

@app.route("/dashboard-post-job.html")
def dashboard_post_job():
    return render_template("superio-html/dashboard-post-job.html")

@app.route("/dashboard-resume-alerts.html")
def dashboard_resume_alets():
    return render_template("superio-html/dashboard-resume-alerts.html")

@app.route("/dashboard-resumes.html")
def dashboard_resumes():
    return render_template("superio-html/dashboard-resumes.html")

@app.route("/dashboard.html")
def dashboard():
    return render_template("superio-html/dashboard.html")

@app.route("/elements.html")
def elements():
    return render_template("superio-html/elements.html")

@app.route("/employers-list-v3.html")
def employers_list_v3():
    return render_template("superio-html/employers-list-v3.html")

@app.route("/employers-list-v4.html")
def employers_list_v4():
    return render_template("superio-html/employers-list-v4.html")

@app.route("/employers-single-v1.html")
def employers_single_v1():
    return render_template("superio-html/employers-single-v1.html")


@app.route("/faqs.html")
def faqs():
    return render_template("superio-html/faqs.html")
    
@app.route("/register.html")
def register():
    return render_template("superio-html/register.html")

@app.route("/register-popup.html")
def register_popup():
    return render_template("superio-html/register-popup.html")

@app.route("/pricing.html")
def pricing():
    return render_template("superio-html/pricing.html")

@app.route("/login.html")
def login():
    return render_template("superio-html/login.html")

@app.route("/login-popup.html")
def login_popup():
    return render_template("superio-html/login-popup.html")

@app.route("/job-single.html")
def job_single():
    return render_template("superio-html/job-single.html")

@app.route("/index-17.html")
def index_17():
    return render_template("superio-html/index-17.html")

@app.route("/index-10.html")
def index_10():
    return render_template("superio-html/index-10.html")

@app.route("/index-8.html")
def index_8():
    return render_template("superio-html/index-8.html")

@app.route("/index-7.html") 
def index_7():
    return render_template("superio-html/index-7.html")

@app.route("/index-6.html")
def index_6():
    return render_template("superio-html/index-6.html")