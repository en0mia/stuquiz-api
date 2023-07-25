CREATE DATABASE IF NOT EXISTS stuquiz;

USE stuquiz;

-- Tables definitions

CREATE TABLE IF NOT EXISTS university (
  id UUID PRIMARY KEY DEFAULT UUID(),
  name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS category (
    id UUID PRIMARY KEY DEFAULT UUID(),
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS professor (
    id UUID PRIMARY KEY DEFAULT UUID(),
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS course (
  id UUID PRIMARY KEY DEFAULT UUID(),
  university_id UUID NOT NULL,
  name TEXT NOT NULL,
  description TEXT NOT NULL,
  professor_id UUID NOT NULL,
  code TEXT NOT NULL,
  CONSTRAINT `fk_course_university`
      FOREIGN KEY (university_id) REFERENCES university(id)
          ON DELETE CASCADE
          ON UPDATE CASCADE,
  CONSTRAINT `fk_course_professor`
      FOREIGN KEY (professor_id) REFERENCES professor(id)
          ON DELETE CASCADE
          ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS course_category (
    course_id UUID NOT NULL,
    category_id UUID NOT NULL,
    PRIMARY KEY (course_id, category_id),
    CONSTRAINT `fk_course_category_course`
      FOREIGN KEY (course_id) REFERENCES course(id)
          ON DELETE CASCADE
          ON UPDATE CASCADE,
    CONSTRAINT `fk_course_category_category`
      FOREIGN KEY (category_id) REFERENCES category(id)
          ON DELETE CASCADE
          ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS question (
  id UUID PRIMARY KEY DEFAULT UUID(),
  course_id UUID NOT NULL,
  question TEXT NOT NULL,
  creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  rating INT NOT NULL DEFAULT 0,
  CONSTRAINT `fk_question_course`
      FOREIGN KEY (course_id) REFERENCES course(id)
          ON DELETE CASCADE
          ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS answer (
  id UUID PRIMARY KEY DEFAULT UUID(),
  question_id UUID NOT NULL,
  answer TEXT NOT NULL,
  creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  correct INTEGER NOT NULL DEFAULT 0,
  points FLOAT NOT NULL DEFAULT 1.0,
  CONSTRAINT `fk_answer_question`
      FOREIGN KEY (question_id) REFERENCES question(id)
          ON DELETE CASCADE
          ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS admin (
    id UUID PRIMARY KEY DEFAULT UUID(),
    username VARCHAR(25) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password TEXT NOT NULL,
    salt VARCHAR(20) NOT NULL
);