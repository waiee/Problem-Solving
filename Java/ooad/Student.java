package ooad;

import java.util.List;

public abstract class Student extends People {
    private String username;
    private String password;
    private String specialization;

    public Student() {}

    public Student(String username, String password, String specialization) {
        this.username = username;
        this.password = password;
        this.specialization = specialization;
    }

    //Setter
    public void setUsername(String username) {
        this.username = username;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public void setSpecialization(String specialization) {
        this.specialization = specialization;
    }
    
    //Getter
    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    public String getSpecialization() {
        return specialization;
    }

    //View projects offered by lecturer
    public void viewProjects(Lecturer lecturer) {
        List<String> projects = lecturer.getProjects();
        for (String project : projects) {
            System.out.println(project);
        }
    }
}
