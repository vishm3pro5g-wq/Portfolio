from django.http import JsonResponse
from django.views.generic import View

# Create your views here.

class About(View):
    def get(self,request):
        data={
            "id":1,
            "full_name":"Vishnu",
            "title":"Python Developer",
            "bio":"I am a passionate software engineer",
            "email":"vishnu@gmail.com",
            "linkedinurl":"https://www.linkedin.com/Muralikrishnan/",
            "githuburl":"https://github.com/muralikrishnannair/"
        }
        return JsonResponse(data)

class Education(View):
    def get(self, request):
        data={
            "id":1,
            "institution":"SSET",
            "university":"KTU",
            "location": "Angamaly",
            "qualification":"B Tech",
            "start_year":"2016",
            "end_year":"2020 ",
            "grade_or_cgpa":" 6.5 "
            
        }
        return JsonResponse(data)

class Project(View):
    def get(self, request):
        data=[
            {
            "id":1,
            "title":"Smart Expense Tracke",
            "short_description":"A responsive web application for tracking personal expenses, managing budgets, and visualizing spending patterns.",
            "long_description":"Smart Expense Tracker is a full-stack web application designed to help users efficiently manage their personal finances. Users can add, edit, and delete transactions, categorize expenses, set budgets, and view spending summaries through an intuitive dashboard. The application provides a responsive interface that works across desktop and mobile devices and uses secure authentication and persistent data storage.",
            "techonologies_used":"React.js, Node.js, Express.js, MongoDB, JavaScript, HTML5, CSS3, REST API, Git & GitHub",
            "live_url":"https://your-project-live-url.com",
            "github_url":"https://github.com/yourusername/smart-expense-tracker",
            "image_url":"https://your-image-url.com/project-screenshot.png",
            "featured":"True"
            }
        ]
        return JsonResponse(data,safe=False)

class skill(View):
    def get(self,request):
        data=[
            {
                'id': 1,
                'title': 'Python',
                'description': 'Programming, application development, automation, and problem solving.',
                'technologies': ['Python', 'OOP', 'File Handling', 'Exception Handling'],
                'image_url': 'image/python.png',
                'featured': True

            }
        ]
        return JsonResponse(data,safe=False)

class certification(View):
    def get(self,request):
        data=[
            {
                "id":1,
                "name":"Python",
                "duration":"1 year",
                "issued_date":"2026-06-15",
                "description":"certification in python programming",
                "featured":"True"
            
            }
        ]
        return JsonResponse(data,safe=False)
