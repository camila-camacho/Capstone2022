from app import app
from flask import render_template, request
 
from firebase_admin import firestore, credentials, initialize_app, auth
import pyrebase



 
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
    user = 'camila@yahoo.com'  # This would come from the logged-in user
    user_type = 'Autism'  # This would come from the logged-in user
    person_questions = db.collection(user_type).document(user).get().to_dict()
    answers = []
    for question in person_questions:
        try:
            answer = float(person_questions[question])
            answers.append(answer)
        except ValueError:
            pass

    user_score = sum(answers) / len(answers)

    matches = []
    for document in db.collection('companiestest').list_documents():
        questions = document.get().to_dict()
        answers = []
        for question in questions:
            try:
                answer = float(questions[question])
                answers.append(answer)
            except ValueError:
                pass
        score = sum(answers) / len(answers)
        if score - 5 < user_score < score + 5:
            job = db.collection('JobPostings').document(questions['jobPosting']).get().to_dict()
            matches.append({'title': job['title'], 'description': job['jobDescription']})

    return render_template("superio-html/candidate-dashboard-job-alerts.html", matches=matches)

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
    user = 'q3FeVRUvwHJkSVDI56Dp'  # This would come from the logged-in user
    employee_type = 'downsyndrome'

    answers = []
    questions = db.collection('companiestest').document(user).get().to_dict()
    for question in questions:
        try:
            answer = float(questions[question])
            answers.append(answer)
        except ValueError:
            pass

    company_score = sum(answers) / len(answers)
    job = db.collection('JobPostings').document(questions['jobPosting']).get().to_dict()
    title = job['title']
    description = job['jobDescription']

    matches = []
    for document in db.collection(employee_type).list_documents():
        questions = document.get().to_dict()
        answers = []
        for question in questions:
            try:
                answer = float(questions[question])
                answers.append(answer)
            except ValueError:
                pass
        score = sum(answers) / len(answers)
        if score - 5 < company_score < score + 5:
            matches.append({'employee': document.id, 'title': title, 'description': description})
    return render_template("superio-html/dashboard-resume-alerts.html", matches=matches)

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

@app.route("/reservation.html")
def reservation():
    return render_template("superio-html/reservation.html")



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





# @app.route("/", methods=[ "GET","POST"])
# def registerUser():
#     if request.method == "POST":
#         email=request.form["email"]
#         password= request.form["password"]
#         print(email)
#         print(password)
#
#         user = auth.create_user(
#             email = email,
#             password = password,
#             phone_number = "+49000000000000"
#         )
#
#         # if user.phone_number == "+49000000000":
#         #     return 'return template for user'
#         # else:
#         #     return "return template for employee"
#
#
#
#
#         return '<h1>Test</h1>'


@app.route("/", methods=["GET", "POST"])
def registerUser():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        print(email)
        print(password)

        user = auth.create_user(
            email=email,
            password=password,
            phone_number="+49000000000000"
        )

        if user.phone_number == "+49000000000":
            return 'return template for user'
        else:
            return "return template for employee"

        return '<h1>Test</h1>'


@app.route("/loginUser", methods=["GET", "POST"])
def loginUser():
    if request.method == "POST":
        email = request.form["username"]
        password = request.form["password"]

        user = auth.sign_in_with_email_and_password(email, password)

        print("signed in user")

    #    user = auth.sign_in_with_email_and_password(email,password)
    #    auth.sign_in_with_email_and_password(email, password)

    return '<h1>Hi</h1>'


firebaseConfig = {
  "apiKey": "AIzaSyAp6aUbBeN4jgqJ-nMP1E7L5i79oJg6MXc",
  "authDomain": "capstone-33322.firebaseapp.com",
  "databaseURL": "https://capstone-33322-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "capstone-33322",
  "storageBucket": "capstone-33322.appspot.com",
  "messagingSenderId": "180237052934",
  "appId": "1:180237052934:web:41673674175839f814e787",
  "databaseURL": " "
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


# @app.route("/loginUser", methods=[ "GET","POST"])
# def loginUser():
#     if request.method == "POST":
#         email=request.form["username"]
#         password=request.form["password"]
#
#         # user = pyrebase.auth().sign_in_with_email_and_password(email, password)
#
#     config = {
#     "apiKey": "AIzaSyAp6aUbBeN4jgqJ-nMP1E7L5i79oJg6MXc",
#     "authDomain": "capstone-33322.firebaseapp.com",
#     "databaseURL": "https://databaseName.firebaseio.com",
#     "storageBucket": "projectId.appspot.com",
#     "serviceAccount": "path/to/serviceAccountCredentials.json"
#     }
#
#     firebase = pyrebase.initialize_app(config)
#
#     firebase.auth().sign_in_with_email_and_password(email, password)
#
#
#
#     return '<h1>Hi</h1>'

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

