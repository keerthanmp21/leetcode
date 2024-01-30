class Solution {
    public boolean canVisitAllRooms1(List<List<Integer>> rooms) {
        Set<Integer> visited = new HashSet<>();
        dfs(0, visited, rooms);
        if(visited.size() == rooms.size()){
            return true;
        }
        else{
            return false;
        }
    }

    private void dfs(int key, Set<Integer> visited, List<List<Integer>> rooms){
        if(visited.contains(key)){
            return;
        }
        visited.add(key);
        List<Integer> room = rooms.get(key);
        for(int i = 0; i < room.size(); i++){
            dfs(room.get(i), visited, rooms);
        }
    }

    public boolean canVisitAllRooms(List<List<Integer>> rooms){
        Set<Integer> visited = new HashSet<>();
        Deque<Integer> queue = new ArrayDeque<>();
        queue.add(0);

        while(!queue.isEmpty()){
            int key = queue.poll();
            if(visited.contains(key)){
                continue;
            }
            visited.add(key);
            List<Integer> room = rooms.get(key);
            for(int i = 0; i < room.size(); i++){
                queue.add(room.get(i));
            }
        }

        if(visited.size() == rooms.size()){
            return true;
        }
        else{
            return false;
        }
    }
}