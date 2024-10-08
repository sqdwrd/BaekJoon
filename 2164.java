import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

import java.util.Queue;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

        Queue<Integer> cards = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            cards.add(i+1);
        }
        
        while (true) {
            if (cards.size() == 1) break;
            cards.poll();

            if (cards.size() == 1) break;
            cards.add(cards.poll());
        }

        System.out.println(cards.peek());

    }
}
