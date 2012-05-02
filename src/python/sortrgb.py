"""
Sorting exercise as an interview question, as seen in the wild. 

This is a variant of the Dutch national flag problem (Dijkstra).


/*
* Suppose that we have three object types R, G, and B, and an array containing objects of
* those types:
*
* { g, r, b, r, r, g, g }
*
* The goal is to write a function that will, in place, rearrange the elements such
* that all R's appear at the beginning of the array, G's in the middle and B's at
* the end. For the input above, by the end of execution the input array should look like:
*
* { r, r, r, g, g, g, b }
*
* The goal is to solve this as efficiently as possible, optimizing O() runtime,
* O() space. The ideal solution uses O(1) space and only makes one pass through the array.
*
* Assume you have global functions:
*   bool isR(Object *o);
*   bool isG(Object *o);
*   bool isB(Object *o);
* to test each object type.
*
* Please do not use external resources like compilers and Google. We expect you to verify
* the code yourself without other help.
*/


"""


RGB_ORDER = {
    'r': 0,
    'g': 1,
    'b': 2
}

def compare_gt(left, right):
    return RGB_ORDER[left] > RGB_ORDER[right]

def sort_rgb_bubble(rgb_values):
    """
    Bubble sort, one of the easiest to remember from university!
    Worst case amortized time complexity O(n**2). 
    The problem is for O(n) or better, so this is not the "right" answer. 
    """
    #rgb_values = list(rgb_values)  # uncomment to avoid modifying the original list
    end = len(rgb_values)
    while end > 0:
        for x in xrange(0, end-1):
            if compare_gt(rgb_values[x], rgb_values[x+1]):
                tmp = rgb_values[x]
                rgb_values[x] = rgb_values[x+1]
                rgb_values[x+1] = tmp

        end -= 1

    return rgb_values

# Other sorting algorithms have O(n log n) amortized worst case time complexity, 
# which also do not meet the O(n) or better requirement.


def test_sort(sort_func, expected, input):
    actual = sort_func(input)
    if not expected == actual:
        raise Exception('FAIL Expected: {}   Actual: {}'.format(expected, actual))
    print 'PASS sorted: {}'.format(actual)

def test_sort_funcs(expected, input):
    test_sort(sort_rgb_bubble, expected, input)

if __name__ == '__main__':
    test_sort_funcs(
        ['r', 'r', 'r', 'g', 'g', 'g', 'b'], 
        ['g', 'r', 'b', 'r', 'r', 'g', 'g' ])
    

