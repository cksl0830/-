class Solution {
    
    private static final String[] indicators = {"RT", "CF", "JM", "AN"};
    
    public String solution(String[] survey, int[] choices) {
        int[] cnt = new int['Z'-'A'+1];
        for (int i = 0; i < survey.length; i++) {
            char a = survey[i].charAt(0);
            char b = survey[i].charAt(1);
            int score = choices[i]-4;
            if (score == 0) continue;
            if (score<0) cnt[a-'A']-=score;
            else cnt[b-'A']+=score;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < indicators.length; i++) {
            char a = indicators[i].charAt(0);
            char b = indicators[i].charAt(1);
            int cntA = cnt[a-'A'];
            int cntB = cnt[b-'A'];
            if (cntA == cntB) sb.append(a);
            else sb.append(cntA>cntB ? a:b);
        }
        return sb.toString();
    }
}
