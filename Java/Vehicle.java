public abstract class Vehicle {

    private String carName;
    private String carBrand;
    
    public Vehicle(){
    };

    public Vehicle(String cn, String cb){
        this.carName = cn;
        this.carBrand = cb;
    }

    public String getName(){
        return carName;
    }

    public String getBrand(){
        return carBrand;
    }
}

class testVehicle {
    public static void main(String args[]){

    }
}
