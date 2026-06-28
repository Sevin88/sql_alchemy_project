from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.orm import (
    declarative_base,
    relationship,
    sessionmaker
)

# Base
Base = declarative_base()


# جدول دانشجو
class Student(Base):
    tablename = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    courses = relationship(
        "Course",
        back_populates="student",
        cascade="all, delete-orphan"
    )

    def repr(self):
        return f"<Student(id={self.id}, name='{self.name}')>"


# جدول درس
class Course(Base):
    tablename = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    unit = Column(Integer, nullable=False)

    student_id = Column(
        Integer,
        ForeignKey("students.id", ondelete="CASCADE"),
        nullable=False
    )

    student = relationship(
        "Student",
        back_populates="courses"
    )

    def repr(self):
        return (
            f"<Course(id={self.id}, "
            f"title='{self.title}', "
            f"unit={self.unit}, "
            f"student_id={self.student_id})>"
        )


# اتصال به دیتابیس
engine = create_engine("sqlite:///university.db", echo=True)

# ساخت جداول
Base.metadata.create_all(engine)

# ساخت Session
Session = sessionmaker(bind=engine)
session = Session()

# تست برنامه
student1 = Student(name="Ali Mohammadi")

course1 = Course(
    id=1,
    title="Database",
    unit=3,
    student=student1
)

course2 = Course(
    id=2,
    title="Advanced Programming",
    unit=4,
    student=student1
)

session.add(student1)
session.add_all([course1, course2])

session.commit()

# نمایش اطلاعات
for student in session.query(Student).all():
    print(student)

    for course in student.courses:
        print("   ", course)

session.close()