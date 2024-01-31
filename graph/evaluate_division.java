public class evaluate_division {
    
}

class Solution {
    public double[] calcEquation1(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Map<String, Map<String, Double>> edges = new HashMap<>();
        for(int i = 0; i < equations.size(); i++){
            String pt1 = equations.get(i).get(0);
            String pt2 = equations.get(i).get(1);
            double val = values[i];

            edges.putIfAbsent(pt1, new HashMap());
            edges.putIfAbsent(pt2, new HashMap());

            edges.get(pt1).put(pt2, val);
            edges.get(pt2).put(pt1, 1/val);
        }

        double[] result = new double[queries.size()];
        
        for(int i = 0; i < queries.size(); i++){
            String src = queries.get(i).get(0);
            String dest = queries.get(i).get(1);
            result[i] = dfs(src, dest, edges, new HashSet<>());
        }

        return result;
    }

    public double dfs(String cur, String dest, Map<String, Map<String, Double>> edges, Set<String> visited){
        if (!edges.containsKey(cur) || !edges.containsKey(dest))
            return -1.0;
        
        if (cur.equals(dest))
            return 1.0;
        
        visited.add(cur);
        
        Map<String, Double> neighbors = edges.get(cur);
        for (Map.Entry<String, Double> entry : neighbors.entrySet()) {
            String neighbor = entry.getKey();
            double val = entry.getValue();
            
            if (!visited.contains(neighbor)) {
                double result = dfs(neighbor, dest, edges, visited);
                if (result != -1.0)
                    return val * result;
            }
        }
        
        visited.remove(cur);
        
        return -1.0;
    }

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries){
        Map<String, Map<String, Double>> edges = new HashMap<>();
        for(int i = 0; i < equations.size(); i++){
            String pt1 = equations.get(i).get(0);
            String pt2 = equations.get(i).get(1);
            double val = values[i];

            edges.putIfAbsent(pt1, new HashMap());
            edges.putIfAbsent(pt2, new HashMap());

            edges.get(pt1).put(pt2, val);
            edges.get(pt2).put(pt1, 1/val);
        }

        double[] result = new double[queries.size()];
    
        for(int i = 0; i < queries.size(); i++){
            String src = queries.get(i).get(0);
            String dest = queries.get(i).get(1);
            Queue<Pair<String, Double>> queue = new LinkedList<>();
            Set<String> visited = new HashSet<>();
            double totalVal = -1.0;
            if(edges.containsKey(src)){
                queue.offer(new Pair<>(src, 1.0));
                visited.add(src);
            }
            while(!queue.isEmpty()){
                Pair<String, Double> pair = queue.poll();
                String cur = pair.getKey();
                Double val = pair.getValue();
                if(cur.equals(dest)){
                    totalVal = val;
                    break;
                }
                Map<String, Double> neighbors = edges.get(cur);
                for (Map.Entry<String, Double> entry : neighbors.entrySet()){
                    String neighbor = entry.getKey();
                    double neighborVal = entry.getValue();
                    if(!visited.contains(neighbor)){
                        visited.add(neighbor);
                        queue.offer(new Pair<>(neighbor, val * neighborVal));
                    }
                }
            }
            result[i] = totalVal;
        }

        return result;

    }

}