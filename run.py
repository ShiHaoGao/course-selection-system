from app import app, db, models

if __name__ == "__main__":
    # 创建数据库表
    with app.app_context():
        # 创建课程对象并添加到数据库
        # course1 = models.Course(name="Course 1", description="Description for Course 1")
        # course2 = models.Course(name="Course 2", description="Description for Course 2")

        # db.session.add(course1)
        # db.session.add(course2)

        # # 提交更改
        # db.session.commit()
        db.create_all()
    app.run(debug=True)
