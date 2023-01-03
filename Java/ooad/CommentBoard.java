package ooad;

import java.util.ArrayList;
import java.util.Scanner;

public class CommentBoard {

    private static ArrayList<String> comments = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\nWelcome to the Comment Board!");
            System.out.println("1. View comments");
            System.out.println("2. Leave a comment");
            System.out.println("3. Delete a comment");
            System.out.println("4. Exit");
            System.out.print("Please choose an option: ");

            int choice = scanner.nextInt();

            if (choice == 1) {
                // view comments
                viewComments();
            } else if (choice == 2) {
                // leave a comment
                System.out.print("Enter your comment: ");
                String comment = scanner.nextLine();
                leaveComment(comment);
            } else if (choice == 3) {
                // delete a comment
                System.out.print("Enter the index of the comment to delete: ");
                int index = scanner.nextInt();
                deleteComment(index);
            } else if (choice == 4) {
                // exit
                break;
            } else {
                System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    private static void viewComments() {
        for (int i = 0; i < comments.size(); i++) {
            System.out.println(i + ". " + comments.get(i));
        }
    }

    private static void leaveComment(String comment) {
        comments.add(comment);
        System.out.println("\nComment added successfully.");
    }

    private static void deleteComment(int index) {
        if (index < 0 || index >= comments.size()) {
            System.out.println("]\nInvalid index. No comment was deleted.");
        } else {
            comments.remove(index);
            System.out.println("\nComment deleted successfully.");
        }
    }
}