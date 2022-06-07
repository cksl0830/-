class Solution {
    public int solution(String s) {
        int answer = s.length();
        if(answer==1 || answer==2){
            return answer;
        }
    
        //i개 단위로 자르며 반복
        for(int i = 1; i <= s.length() / 2; i++) {
            String temp = s.substring(0, i);
            String cur = ""; //현재 문자열
            int cnt = 1; 
            StringBuilder sb = new StringBuilder();
            
            for(int start = i; start <= s.length(); start += i) {
                if(start + i >= s.length()) {
                    cur = s.substring(start, s.length());
                }
                else {
                    cur = s.substring(start, start + i);
                }
            
                if(cur.equals(temp)) {
                    cnt++;
                }
                else if(cnt == 1){
                    sb.append(temp);
                    temp = cur;
                }
                else {
                    sb.append(cnt).append(temp);
                    temp = cur;
                    cnt = 1;
                }
            }
            
            if(cnt!=1) sb.append(cnt).append(temp);
            else sb.append(temp);
            
            answer = Math.min(answer, sb.toString().length());
        }
    
        return answer;
    }
}
