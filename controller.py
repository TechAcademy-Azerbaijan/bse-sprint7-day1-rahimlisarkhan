from flask import Flask, render_template
from app import app


students_info = [
    {
        'Id': 1,
        'Name': 'John',
        'Surname': 'Smith',
        'Gender': 'Male',
        'Status': 'Activate',
        'Image': 'https://i.pinimg.com/originals/70/7e/45/707e45bfafba9333537b22ebc7b844cb.jpg',
        'Bio': """ 
                Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                Excepturi dolores, non mollitia, impedit harum deleniti repellat quasi
                atque voluptate provident sit exercitationem voluptas et beatae nobis.
                Doloribus illo quisquam deleniti?
               """
    },
    {
        'Id': 2,
        'Name': 'Mary',
        'Surname': 'Miller',
        'Gender': 'Female',
        'Status': 'Deactivate',
        'Image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRE1C9UAv0BLsR_16Y4Xk63d50rSA9EnMQr0g&usqp=CAU',
        'Bio': """ 
                Lorem ipsum dolor sit amet consectetur, harum deleniti repellat quasi
                atque voluptate provident sit exercitationem voluptas et beatae nobis.
                Doloribus illo quisquam deleniti?
               """
    },
    {
        'Id': 3,
        'Name': 'Gary',
        'Surname': 'Johnson',
        'Gender': 'Male',
        'Status': 'Activate',
        'Image': 'https://blog.internationalstudent.com/wp-content/uploads/2019/08/GettyImages-1089948916-1.jpg',
        'Bio': ''
    }
]


@app.route("/")
def home():
    return render_template('home.html')



@app.route('/students/<int:stu_index>')
def student_list(stu_index):
    student_Uni = list(
        filter(lambda student: student['Id'] == stu_index, students_info))[0]
    return render_template('studentlist.html', studentAPI=student_Uni)


@app.route("/students/")
def students():
    return render_template('students.html', student_list=students_info)
