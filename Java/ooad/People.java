package ooad;

public abstract class People{
    
    private String username;
    private String password;

    public People(){
    };

    public People (String nm, String pass){
        this.username = nm;
        this.password = pass;
    }

    // Getter
    public String getName(){
        return username;
    }

    // Setter
    public void setName(String nm){
        this.username = nm;
    }

    public String getPass(){
        return password;
    }

    public void setPass(String pass){
        this.password = pass;
    }

    public abstract String toString();
}
