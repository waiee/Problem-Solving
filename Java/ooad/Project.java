package ooad;

import java.util.ArrayList;

public class Project {
    private String projectName;
    private boolean status;
    private ArrayList<String> comment;
    
  
    public Project(String projectName, boolean status) {
      this.projectName = projectName;
      this.status = status;
    }
  
    public String getProjectName() {
      return projectName;
    }
  
    public boolean getStatus() {
      return status;
    }
  
    public void setProjectName(String projectName) {
      this.projectName = projectName;
    }
  
    public void setStatus(boolean status) {
      this.status = status;
    }
  }