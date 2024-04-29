CREATE TABLE Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT UNIQUE NOT NULL,
    Password TEXT NOT NULL,
    IsTeacher INTEGER DEFAULT 0 CHECK (IsTeacher IN (0, 1))
);


CREATE TABLE Courses (
    CourseID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER,
    CourseName TEXT NOT NULL,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);


CREATE TABLE Assignments (
    AssignmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    CourseID INTEGER,
    Name TEXT NOT NULL,
    Section TEXT,
    DueDate DATE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);


CREATE TABLE Questions (
    QuestionID INTEGER PRIMARY KEY AUTOINCREMENT,
    AssignmentID INTEGER,
    Question TEXT NOT NULL,
    Answer TEXT NOT NULL,
    FOREIGN KEY (AssignmentID) REFERENCES Assignments(AssignmentID)
);


CREATE TABLE Submissions (
    SubmissionID INTEGER PRIMARY KEY AUTOINCREMENT,
    QuestionID INTEGER,
    UserID INTEGER,
    SubmissionDate DATE DEFAULT CURRENT_DATE,
    ReportPath TEXT DEFAULT NULL,
    AnswerText TEXT,
    Score INTEGER DEFAULT 0,
    FOREIGN KEY (QuestionID) REFERENCES Questions(QuestionID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);



CREATE TABLE Enrollments (
    EnrollmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    StudentUserID INTEGER,
    CourseID INTEGER,
    FOREIGN KEY (StudentUserID) REFERENCES Users(UserID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);
