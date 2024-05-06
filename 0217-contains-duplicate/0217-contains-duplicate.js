/**
 * Given an array of integers, return true if any value appears at least twice.
 * @param {number[]} nums - The array of integers.
 * @returns {boolean} - True if any value appears at least twice, otherwise false.
 */
function containsDuplicate(nums) {
    const set = new Set();

    for (let i = 0; i < nums.length; i++) {
        if (set.has(nums[i])) {
            return true;
        }
        set.add(nums[i]);
    }

    return false;
}
