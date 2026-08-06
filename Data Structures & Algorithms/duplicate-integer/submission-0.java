class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> milo = new HashSet<>();
        for (int num : nums) {
            if (milo.contains(num)) {
                return true;
            }
            milo.add(num);
        }
        return false;
    }
}
