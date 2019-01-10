import java.util.Scanner;
import java.util.Arrays;

Quiz : addQuestion( , getQuestion(q , setOptionVotes(q , getText() , commonSelectedOption())
Participant: Participant(name, q-1, lines[1]);
public class Solution {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		Quiz quiz = new Quiz();
		int questions = Integer.parseInt(scan.nextLine());
		for (int i = 0; i < questions; i++) {
			String question = scan.nextLine();
			String[] options = new String[4];
			for (int j = 0; j < options.length; j++) {
				options[j] = scan.nextLine();
			}
			quiz.addQuestion(new Question(question, options));
		}

		int participants = Integer.parseInt(scan.nextLine());
		for (int k = 0; k < participants; k++) {
			String name = scan.nextLine();
			for (int l = 0; l < questions; l++) {
				String[] lines = scan.nextLine().split(" ");
				int q = Integer.parseInt(lines[0]);
				Participant p = new Participant(name, q-1, lines[1]);
				Question question = quiz.getQuestion(q-1);
				question.setOptionVotes(question.indexOf(lines[1]));
			}
		}

		for (int i = 0; i < questions; i++) {
			System.out.println("Highest number of votes for question : "+ quiz.getQuestion(i).getText()
			 + " : " + quiz.getQuestion(i).commonSelectedOption());
		}

	}
}



