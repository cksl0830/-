import java.util.*;

class Solution {
    public String[] solution(String[] record) {
        HashMap<String,String> map=new HashMap();
        ArrayList<String> list = new ArrayList<>();
        
        for(int i=0; i<record.length; i++){
            String[] temp = record[i].split(" ");
            if (temp.length==3) {
                map.put(temp[1],temp[2]);
            }
        }
        
        for(int i=0; i<record.length; i++){
            String[] temp = record[i].split(" ");
            if(temp[0].equals("Enter")){
                list.add(map.get(temp[1]) + "님이 들어왔습니다.");
            }
            else if(temp[0].equals("Leave")){
                list.add(map.get(temp[1]) + "님이 나갔습니다.");
            }
        }
        String[] answer;
        answer = list.toArray(new String[list.size()]);
        return answer;
    }
}



