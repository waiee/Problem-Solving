package ooad;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Student {
    private String username;
    private String password;
    private boolean loggedIn;

    public Student(String username, String password) {
        this.username = username;
        this.password = password;
        this.loggedIn = false;
    }

    public void login(String username, String password) {
        if (this.username.equals(username) && this.password.equals(password)) {
            this.loggedIn = true;
            System.out.println("Successfully logged in.");
        } else {
            System.out.println("Incorrect username or password.");
        }
    }

    public void logout() {
        this.loggedIn = false;
        System.out.println("Successfully logged out.");
    }

    public boolean isLoggedIn() {
        return this.loggedIn;
    }

    public static Student[] loadStudentsFromCSV(String filepath) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader(filepath));
        String line;
        int numStudents = 0;
        while ((line = br.readLine()) != null) {
            numStudents++;
        }
        br.close();

        Student[] students = new Student[numStudents];
        br = new BufferedReader(new FileReader(filepath));
        int i = 0;
        while ((line = br.readLine()) != null) {
            String[] parts = line.split(",");
            String username = parts[0];
            String password = parts[1];
            students[i] = new Student(username, password);
            i++;
        }
        br.close();
        return students;
    }
}

class testStudent{
    
    Student[] students = Student.loadStudentsFromCSV("students.csv");
    Student s = students[0];
    s.login("username","password");
    if (s.isLoggedIn()) {
        // do something
        s.logout();
    }
}
