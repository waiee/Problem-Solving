package ooad;

import java.util.List;

public class Student {
    private String specialization;

    public Student() {
        this.specialization = "";
    }

    public Student(String specialization) {
        this.specialization = specialization;
    }

    //Getter
    public String getSpecialization() {
        return specialization;
    }

    //Setter
    public void setSpecialization(String specialization) {
        this.specialization = specialization;
    }

    //View projects offered by lecturer
    public void viewProjects(Lecturer lecturer) {
        List<String> projects = lecturer.getProjects();
        for (String project : projects) {
            System.out.println(project);
        }
    }
}
