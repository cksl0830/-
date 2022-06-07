import java.util.*;

class Solution {
    public String[] solution(String[] record) {
        HashMap<String,String> map=new HashMap();
        ArrayList<String> arr = new ArrayList<>();
        
        for(int i=0; i<record.length; i++){
            String[] temp = record[i].split(" ");
            if (temp.length==3) {
                map.put(temp[1],temp[2]);
            }
        }
        
        for(int i=0; i<record.length; i++){
            String[] temp = record[i].split(" ");
            if(temp[0].equals("Enter")){
                arr.add(map.get(temp[1]) + "님이 들어왔습니다.");
            }
            else if(temp[0].equals("Leave")){
                arr.add(map.get(temp[1]) + "님이 나갔습니다.");
            }
        }
        String[] answer;
        answer = arr.toArray(new String[arr.size()]);
        return answer;
    }
}
