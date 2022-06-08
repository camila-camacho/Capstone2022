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

@app.route("/3")
def blog_list_v2():
    return render_template("superio-html/blog-list-v2.html")

@app.route("/4")
def blog_list_v3():
    return render_template("superio-html/blog-list-v3.html")

@app.route("/5")
def blog_single():
    return render_template("superio-html/blog_single.html")


@app.route("/6")
def candidate_dashboard_applied_job():
    return render_template("superio-html/candidate-dashboard-applied-job.html")

@app.route("/7")
def candidate_dashboard_cv_manager():
    return render_template("superio-html/candidate-dashboard-cv-manager.html")


@app.route("/8")
def candidate_dashboard_job_alerts():
    return render_template("superio-html/candidate-dashboard-job-alerts.html")

@app.route("/9")
def candidate_dashboard_profile():
    return render_template("superio-html/candidate-dashboard-profile.html")

@app.route("/10")
def candidate_dashboard_resume():
    return render_template("superio-html/candidate-dashboard-resume.html")

@app.route("/11")
def candidate_dashboard_shortlisted_resume():
    return render_template("superio-html/candidate-dashboard-shortlisted-resume.html")

@app.route("/12")
def candidate_dashboard():
    return render_template("superio-html/candidate-dashboard.html")

@app.route("/17")
def candidates_list_v5():
    return render_template("superio-html/candidates-list-v5.html")

@app.route("/20")
def candidates_single_v3():
    return render_template("superio-html/candidates-single-v3.html")

@app.route("/21")
def contact():
    return render_template("superio-html/contact.html")

@app.route("/22")
def dashboard_applicants():
    return render_template("superio-html/dashboard-applicants.html")

@app.route("/23")
def dashboard_change_password():
    return render_template("superio-html/dashboard-change-password.html")

@app.route("/24")
def dashboard_company_profile():
    return render_template("superio-html/dashboard-company-profile.html")

@app.route("/25")
def dashboard_manage_job():
    return render_template("superio-html/dashboard-manage-job.html")

@app.route("/26")
def dashboard_messages():
    return render_template("superio-html/dashboard-messages.html")

@app.route("/27")
def dashboard_packages():
    return render_template("superio-html/dashboard-packages.html")

@app.route("/28")
def dashboard_post_job():
    return render_template("superio-html/dashboard-post-job.html")

@app.route("/29")
def dashboard_resume_alets():
    return render_template("superio-html/dashboard-resume-alerts.html")

@app.route("/30")
def dashboard_resumes():
    return render_template("superio-html/dashboard-resumes.html")

@app.route("/31")
def dashboard():
    return render_template("superio-html/dashboard.html")

@app.route("/32")
def elements():
    return render_template("superio-html/elements.html")

@app.route("/35")
def employers_list_v3():
    return render_template("superio-html/employers-list-v3.html")

@app.route("/36")
def employers_list_v4():
    return render_template("superio-html/employers-list-v4.html")

@app.route("/37")
def employers_single_v1():
    return render_template("superio-html/employers-single-v1.html")


@app.route("/40")
def faqs():
    return render_template("superio-html/faqs.html")
    
@app.route("/41")
def register():
    return render_template("superio-html/register.html")

@app.route("/42")
def register_popup():
    return render_template("superio-html/register-popup.html")

@app.route("/43")
def pricing():
    return render_template("superio-html/pricing.html")

@app.route("/44")
def login():
    return render_template("/login.html")

@app.route("/45")
def login_popup():
    return render_template("/login-popup.html")

@app.route("/46")
def job_single():
    return render_template("/job-single.html")

@app.route("/47")
def job_single_2():
    return render_template("/job-single-2.html")

@app.route("/48")
def index_17():
    return render_template("/index-17.html")

@app.route("/49")
def index_10():
    return render_template("/index-10.html")

@app.route("/50")
def index_8():
    return render_template("/index-8.html")

@app.route("/51")
def index_7():
    return render_template("/index-7.html")

@app.route("/52")
def index_6():
    return render_template("/index-6.html")