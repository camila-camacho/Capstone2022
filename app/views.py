from app import app
from flask import render_template, request
 
from firebase_admin import firestore, credentials, initialize_app
 
db=firestore.client()


@app.route("/") 
def index():

    return render_template("superio-html/index.html")

@app.route("/about.html") 
def about():
    return render_template("superio-html/about.html")

@app.route("/personality-test.html")
def personality_test():
    return render_template("superio-html/personality-test.html")

@app.route("/down-test.html")
def down_test():
    return render_template("superio-html/down-test.html")

@app.route("/autism-test.html")
def autism_test():
    return render_template("superio-html/autism-test.html")

@app.route("/company-test.html")
def down_company():
    return render_template("superio-html/company-test.html")

@app.route("/blog-down.html")
def blog_down():
    return render_template("superio-html/blog-down.html")

@app.route("/blog-autism.html")
def blog_autism():
    return render_template("superio-html/blog-autism.html")

@app.route("/blog-list-company.html")
def blog_list_company():
    return render_template("superio-html/blog-list-company.html")

@app.route("/blog-list-v3.html") 
def blog_list_v3():
    return render_template("superio-html/blog-list-v3.html")

@app.route("/blog-single.html") 
def blog_single():
    return render_template("superio-html/blog-single.html")

@app.route("/blog-single-company.html") 
def blog_single_company():
    return render_template("superio-html/blog-single-company.html")

@app.route("/candidates-trainings.html") 
def candidates_trainings():
    return render_template("superio-html/candidates-trainings.html")

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

@app.route("/dashboard-profile.html") 
def candidate_dashboard_profile_view():
    return render_template("superio-html/dashboard-profile.html")

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

@app.route("/dashboard-company-profile-view.html") 
def dashboard_company_profile_view():
    return render_template("superio-html/dashboard-company-profile-view.html")

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

@app.route("/index-10.html")
def index_10():
    return render_template("superio-html/index-10.html")



@app.route("/dashboard-post-job.html", methods=[ "GET","POST"])
def test():
    if request.method == "POST":
        
        email=request.form["email"]
        title=request.form["title"]
        jobDescription=request.form["jd"]
        grade=request.form["grade"]
        completeAddress=request.form["completeAddress"]
        jobType=request.form["jobType"]
        careerExperience=request.form["careerExperience"]
        experience=request.form["experience"]
        gender=request.form["gender"]
        indrustry =request.form["industry"]
        qualifications=request.form["qualifications"]
        applicationDeadline=request.form["applicationDeadline"]
        autonomousCommunities=request.form["autonomousCommunities"]
        
        
        doc_ref = db.collection(u'JobPostings').document(u'1001'+ email)
        doc_ref.set({
                u'email': email,
                u'title': title,
                u'jobDescription': jobDescription,
                u'grade': grade,
                u'jobType': jobType,
                u'careerExperience':careerExperience,
                u'experience':experience,
                u'gender': gender,
                u'indrustry': indrustry,
                u'qualifications':qualifications ,
                u'applicationDeadline': applicationDeadline,
                u'autonomousCommunities':autonomousCommunities,
                u'completeAddress':completeAddress,
                   
        })
        return render_template("superio-html/dashboard-post-job.html")
    else:
        return render_template("superio-html/dashboard-post-job.html")


@app.route("/candidate-dashboard-profile.html", methods=[ "GET","POST"])
def test1():
    if request.method == "POST":
      
        fullName=request.form["fullName"]
        jobTitle=request.form["jobTitle"]
        phone=request.form["phone"]
        emailAddress=request.form["emailAddress"]
        website=request.form["website"]
        currentSalary=request.form["currentSalary"]
        experience=request.form["experience"]
        age=request.form["age"]
        educationLevels=request.form["educationLevels"]
        languages=request.form["languages"]
        interestExperienceField =request.form["interestExperienceField"]
        allowSearch=request.form["allowSearch"]
        description=request.form["description"]
        
        doc_ref = db.collection(u'CandidateProfile').document(u'1001'+emailAddress)
        doc_ref.set({
                u'fullName': fullName,
                u'jobTitle': jobTitle,
                u'phone': phone,
                u'emailAddress': emailAddress,
                u'website':website,
                u'currentSalary':currentSalary,
                u'experience': experience,
                u'age': age,
                u'educationLevels':educationLevels ,
                u'languages': languages,
                u'interestExperienceField':interestExperienceField,
                u'allowSearch':allowSearch,
                u'description':description,  
                   
        })
        return render_template("superio-html/candidate-dashboard-profile.html")
    else:
        return render_template("superio-html/candidate-dashboard-profile.html")


@app.route("/register-popup.html", methods=[ "GET","POST"])
def register_database():
    if request.method == "POST":
      
        candidateEmployer=request.form["candidateEmployer"]
        emailAddress=request.form["emailAddress"]
        password=request.form["password"]


        doc_ref = db.collection(u'registration').document(u''+emailAddress)
        doc_ref.set({
                u'candidateEmployer':candidateEmployer,
                u'emailAddress': emailAddress,
                u'password': password,

        })

        return render_template("superio-html/register-popup.html")
    else:
        return render_template("superio-html/cregister-popup.html")