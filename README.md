# docker_mini_project
Project to create simple webpage to check timetable use resources from docker

Guides

**1. Install Docker and Start PostgreSQL in Docker**

# Create a Docker container for the PostgreSQL database
docker compose up

# Verify the container is running
docker ps

```

### 2. **Set Up the PostgreSQL Database and Tables**

create table courses
(
    id             integer      not null
        primary key autoincrement,
    level          integer      not null,
    program        varchar(255) not null,
    session        varchar(255) not null,
    year           integer      not null,
    hour           integer      not null,
    title          varchar(255) not null,
    instructor     varchar(255) not null,
    campus         varchar(255) not null,
    room           varchar(255) not null,
    days           varchar(255) not null,
    start_time     time         not null,
    end_time       time         not null,
    start_semester date         not null,
    end_semester   date         not null,
    tm             varchar(50)  not null
);


```

### 3. **Install Python and Django Dependencies**

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

django-admin startproject myproject
cd myproject

python manage.py runserver


```

### 4. **Create Django Application**

```django view
from logging import Filter

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView

from apps.forms import CourseModelForm
from apps.models import Course


class HomeTemplateView(TemplateView):
    template_name = 'apps/filter.html'

class FilterView(ListView):
    queryset = Course.objects.order_by('level')
    template_name = 'apps/home.html'
    context_object_name = 'courses'

    def get_queryset(self):
        query = super().get_queryset()
        program = self.request.GET.get('program')
        session = self.request.GET.get('session')
        year = self.request.GET.get('year')
        return query.filter(program=program , session=session, year=year)






```

### 5. **HTML Templates for Django**

#### **`home.html` (Form for Level Input)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>University Timetable</title>
</head>
<body>
    <h1>Welcome, Sabi!</h1>
    <h2>University Timetable</h2>
    <form method="POST">
        <label for="level">Enter Level:</label>
        <input type="number" id="level" name="level" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

#### **`filter.html` (Displaying Timetable)**

```<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Employee Table</title>
  <link rel="stylesheet" href="styles.css">
</head>
<style>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f8f8f8;
  color: #333;
}

.container {
  margin: 50px auto;
  width: 100%;
  max-width: 1200px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
  background: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

thead {
  background-color: #f0f0f0;
}

th, td {
  padding: 12px 20px;
  text-align: left;
}

th {
  font-size: 11px;
  text-transform: capitalize;
  color: #555;
}

tbody tr:nth-child(even) {
  background-color: #f9f9f9;
}

tbody tr:hover {
  background-color: #f1f1f1;
}

td {
  font-size: 14px;
  color: #333;
}
button {
        background-color: #3c8c67;
        color: #000000;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
        font-size: 14px;
    }

    button:hover {
        background-color: #2e2e7b;
    }


</style>
<body>
  <div class="container">
  <button><a href="{% url 'home' %}">Home</a></button>
  <h4 style="text-align: center">Mini project of Sitora</h4>
  <h4 style="text-align: center">Timetable for level</h4>
    <table>
      <thead>
        <tr>
          <th>Crs Sec</th>
          <th>Hrs</th>
          <th>Title</th>
          <th>Instructor</th>
          <th>Campus</th>
          <th>Building</th>
          <th>Room</th>
          <th>Days</th>
          <th>Time</th>
          <th>Date</th>
          <th>Tm</th>
          <th>Type</th>
        </tr>
      </thead>
      <tbody>
      {% for course in courses %}
      	<tr>
          <th>{{ course.id }}</th>
          <th>{{ course.hour }}</th>
          <th>{{ course.title }}</th>
          <th>{{ course.instructor }}</th>
          <th>{{ course.campus }}</th>
          <th>{{ course.building }}</th>
          <th>{{ course.room }}</th>
          <th>{{ course.days }}</th>
          <th>{{ course.start_time }}, {{ course.end_time }}</th>
          <th>{{ course.start_semester }} , {{ course.end_semester }}</th>
          <th>{{ course.tm }}</th>
          <th>Lecture</th>
        </tr>
      {% endfor %}



      </tbody>
    </table>
  </div>

</body>
</html>


```

### 6. **Running the Django Application**

```bash
python manage.py runserver localhost:8000 # django
docker compose up # to run command for docker+django
docker compose down # to stop command for docker+django

```


These are the commands and steps you would use to deploy and run this project. You can adapt or extend the project as needed based on additional requirements.
