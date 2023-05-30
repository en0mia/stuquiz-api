CREATE DATABASE IF NOT EXISTS stuquiz;

USE stuquiz;

-- Tables definitions

CREATE TABLE IF NOT EXISTS university (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  uuid UUID UNIQUE NOT NULL DEFAULT UUID(),
  name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS category (
    id INTEGER PRIMARY KEY,
    uuid UUID UNIQUE NOT NULL DEFAULT UUID(),
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS course (
  id INTEGER PRIMARY KEY,
  uuid UUID UNIQUE NOT NULL DEFAULT UUID(),
  university_id UUID NOT NULL,
  name TEXT NOT NULL,
  description TEXT NOT NULL,
  professor TEXT NOT NULL,
  code TEXT NOT NULL,
  CONSTRAINT `fk_course_university`
      FOREIGN KEY (university_id) REFERENCES university(uuid)
          ON DELETE CASCADE
          ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS course_category (
    course_id UUID NOT NULL,
    category_id UUID NOT NULL,
    PRIMARY KEY (course_id, category_id),
    CONSTRAINT `fk_course_category_course`
      FOREIGN KEY (course_id) REFERENCES course(uuid)
          ON DELETE CASCADE
          ON UPDATE CASCADE,
    CONSTRAINT `fk_course_category_category`
      FOREIGN KEY (category_id) REFERENCES category(uuid)
          ON DELETE CASCADE
          ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS question (
  id INTEGER PRIMARY KEY,
  uuid UUID UNIQUE NOT NULL DEFAULT UUID(),
  course_id UUID NOT NULL,
  question TEXT NOT NULL,
  creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  rating INT NOT NULL DEFAULT 0,
  CONSTRAINT `fk_question_course`
      FOREIGN KEY (course_id) REFERENCES course(uuid)
          ON DELETE CASCADE
          ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS answer (
  id INTEGER PRIMARY KEY,
  uuid UUID UNIQUE NOT NULL DEFAULT UUID(),
  question_id UUID NOT NULL,
  answer TEXT NOT NULL,
  creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  correct INTEGER NOT NULL DEFAULT 0,
  points FLOAT NOT NULL DEFAULT 1.0,
  CONSTRAINT `fk_answer_question`
      FOREIGN KEY (question_id) REFERENCES question(uuid)
          ON DELETE CASCADE
          ON UPDATE CASCADE
);