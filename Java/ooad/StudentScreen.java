package ooad;
import javax.swing.*;
import java.awt.*;

public class StudentScreen {

    public StudentScreen(){
        //  // Create a new JFrame container
        //  JFrame frame = new JFrame("Student Screen");
        //  frame.setSize(400, 300);
 
        //  // Create a new JPanel
        //  JPanel panel = new JPanel();
        //  panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
 
        //  // Add a JLabel to the panel
        //  JLabel label = new JLabel("Welcome to the Student Screen!");
        //  panel.add(label);
 
        //  // Add a "View Subject" button to the panel
        //  JButton viewSubjectButton = new JButton("View Subject");
        //  panel.add(viewSubjectButton);
 
        //  // Add the panel to the frame
        //  frame.add(panel, BorderLayout.CENTER);
        //  frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        //  frame.pack();
        //  frame.setVisible(true);

        JFrame frame = new JFrame();
        
        JPanel panel = new JPanel();
        panel.setBorder(BorderFactory.createEmptyBorder(30, 30, 10, 30));
        
    }

    public static void main(String[] args) {
       new StudentScreen();
    }
}