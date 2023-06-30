import uuid
from datetime import datetime
from app.stuquiz.entities.answer import Answer
from app.stuquiz.entities.category import Category
from app.stuquiz.entities.course import Course
from app.stuquiz.entities.question import Question
from app.stuquiz.entities.university import University

# Test data for Answer
TEST_ANSWER = Answer(
    id=str(uuid.uuid4()),
    question_id=str(uuid.uuid4()),
    answer="Test answer",
    creation_date=datetime.now(),
    correct=True,
    points=10
)

# Test data for Category
TEST_CATEGORY = Category(
    id=str(uuid.uuid4()),
    name="Test category"
)

# Test data for Course
TEST_COURSE = Course(
    id=str(uuid.uuid4()),
    university_id=str(uuid.uuid4()),
    name="Test course",
    description="Test course description",
    professor="Test professor",
    categories=[TEST_CATEGORY],
    code="TEST123"
)

# Test data for Question
TEST_QUESTION = Question(
    id=str(uuid.uuid4()),
    course_id=str(uuid.uuid4()),
    question="Test question",
    creation_date=datetime.now(),
    rating=5
)

# Test data for University
TEST_UNIVERSITY = University(
    id=str(uuid.uuid4()),
    name="Test University"
)
