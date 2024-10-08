
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

    private static int N;
    private static int K;
    private static Queue<Integer> seat;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] line = br.readLine().split(" ");
        N = Integer.parseInt(line[0]);
        K = Integer.parseInt(line[1]);

        seat = new LinkedList();
        for (int i = 0; i < N; i++) {
            seat.add(i + 1);
        }

        System.out.print("<");

        while (true) {
            for (int i = 0; i < K - 1; i++) {
                seat.add(seat.poll());
            }
            System.out.print(seat.poll());
            if (seat.isEmpty()) {
                break;
            } else {
                System.out.print(", ");
            }
        }

        System.out.print(">");
    }
}
