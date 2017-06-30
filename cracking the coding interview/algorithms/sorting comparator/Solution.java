
class Checker implements Comparator<Player> {
    
    public int compare(Player p1, Player p2) {
        int score = p2.score - p1.score;
        
        if (score == 0) {
            return p1.name.compareTo(p2.name);
        }
        
        return score;
    }
    
}