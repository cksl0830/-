import java.util.*;

class Solution {
    
    public int solution(int cacheSize, String[] cities) {
        if(cacheSize == 0) return 5 * cities.length;
        
        int answer = 0;
        
        LinkedList<String> cache = new LinkedList<>();
        
        for(int i = 0 ; i < cities.length ; i++){
            String city = cities[i].toLowerCase();
            
            // cache hit
            if(cache.remove(city)){
                cache.addLast(city);
                answer += 1;
            
            // cache miss
            } else {
                if(cache.size() == cacheSize){
                    cache.removeFirst();
                }
                cache.addLast(city);
                answer += 5;
            }
        }
        return answer;
    }
} 
