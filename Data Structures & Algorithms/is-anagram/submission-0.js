class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length !== t.length) {
            return false;
        }

        let sSort = s.split("").sort().join();
        console.log(sSort);
        let tSort = t.split("").sort().join();
        console.log(tSort);
        return sSort == tSort;
    }
}
