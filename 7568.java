
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[][] sizes = new int[N][2];
        int[] grade = new int[N];

        for (int i = 0; i < N; ++i) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            sizes[i][0] = Integer.parseInt(st.nextToken());
            sizes[i][1] = Integer.parseInt(st.nextToken());

            grade[i] = 1;
        }

        for (int target = 0; target < N; target++) {
            for (int comp = 0; comp < N; comp++) {
                if (target != comp && sizes[target][0] < sizes[comp][0] && sizes[target][1] < sizes[comp][1]) {
                    grade[target]++;
                }
            }
        }

        StringBuilder builder = new StringBuilder();

        for (int i = 0; i < N; ++i) {
            builder.append(grade[i] + " ");
            // System.out.print(grade[i] + " ");
        }
        System.out.println(builder.toString());
    }
}
