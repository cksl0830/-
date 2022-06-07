import java.util.*;

class Solution {

    ArrayList<String> list = new ArrayList<>();
    HashMap<String, Integer> map = new HashMap<>();

    public String[] solution(String[] orders, int[] course) {

        // 1. 각 Order 정렬
        for (int i = 0; i < orders.length; i++) {
            char[] arr = orders[i].toCharArray();
            Arrays.sort(arr);
            orders[i] = String.valueOf(arr);
        }

        // 2. 각 order를 기준으로 조합 만들기
        for (int num : course) {
            for (String order : orders)
                combination("", order, num);

            // 3. 가장 많은 조합 answer에 저장
            if (!map.isEmpty()) {
                ArrayList<Integer> countList = new ArrayList<>(map.values());
                int max = Collections.max(countList);

                if (max > 1)
                    for (String key : map.keySet())
                        if (map.get(key) == max)
                            list.add(key);
                map.clear();
            }
        }

        Collections.sort(list);
        String[] answer;
        answer = list.toArray(new String[list.size()]);

        return answer;
    }

    public void combination(String order, String others, int count) {
        // 탈출 조건 : count == 0
        if (count == 0) {
            map.put(order, map.getOrDefault(order, 0) + 1);
            return;
        }

        for (int i = 0; i < others.length(); i++)
            combination(order + others.charAt(i), others.substring(i + 1), count - 1);
    }
}
