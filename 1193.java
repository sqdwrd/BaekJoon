import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());
		int step = 0;
		while (true) {
			step++;
			// System.out.println("" + step + " " + n);

			if (n <= step) {
				if (step % 2 == 0) {
					System.out.println("" + n + "/" + (step - n + 1));
				} else {
					System.out.println("" + (step - n + 1) + "/" + n);
				}
				return;
			} else {
				n -= step;
			}
		}
	}
}
