import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class ProjectTableFrame extends JFrame {
    private List<Project> projects;

    public ProjectTableFrame(List<Project> projects) {
        this.projects = projects;

        setTitle("Projects");
        setSize(600, 400);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        getContentPane().add(panel, BorderLayout.CENTER);
        panel.setLayout(new BorderLayout(0, 0));

        JButton btnShowTable = new JButton("Show Table");
        panel.add(btnShowTable, BorderLayout.NORTH);
        btnShowTable.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Create a table model based on the list of projects
                ProjectTableModel model = new ProjectTableModel(projects);

                // Create the table and add it to a scroll pane
                JTable table = new JTable(model);
                JScrollPane scrollPane = new JScrollPane(table);

                // Add the scroll pane to the frame
                panel.add(scrollPane, BorderLayout.CENTER);

                // Update the frame
                panel.revalidate();
                panel.repaint();
            }
        });
    }
}
