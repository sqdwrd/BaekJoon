
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {

    private static final Integer[] mem = new Integer[1001];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        mem[1] = 1;
        mem[2] = 2;

        int result = partition(N);

        System.out.println(result);
    }

    private static int partition(int n) {
        if (mem[n] != null) {
            return mem[n];
        }

        mem[n] = (partition(n - 1) + partition(n - 2)) % 10007;
        return mem[n];
    }
}
