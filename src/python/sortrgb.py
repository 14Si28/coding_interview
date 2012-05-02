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

def sort_rgb_bubble(rgb_values):
    """
    Bubble sort, one of the easiest to remember from university!
    Worst case amortized time complexity O(n**2). 
    The problem is for O(n) or better, so this is not the "right" answer. 
    """
    RGB_ORDER = {
        'r': 0,
        'g': 1,
        'b': 2
    }

    def compare_gt(left, right):
        return RGB_ORDER[left] > RGB_ORDER[right]

    rgb_values = list(rgb_values) # Remove this copy to fit the O(1) space constraint. Leaving this in allows us to use python strings instead of arrays, which is easier for testing.
    end = len(rgb_values)
    while end > 0:
        for x in xrange(0, end-1):
            if compare_gt(rgb_values[x], rgb_values[x+1]):
                tmp = rgb_values[x]
                rgb_values[x] = rgb_values[x+1]
                rgb_values[x+1] = tmp

        end -= 1

    return ''.join(rgb_values) # Convert from array back to string

# Other faster sorting algorithms have O(n log n) amortized worst case time complexity, 
# which also do not meet the O(n) or better requirement.
# Instead we turn to...

def sort_rgb_dutch(rgb_values):
    """
    Dijkstra's flag sorter.
    """
    rgb_values = list(rgb_values) # See note above re. O(1) 
    p = 0
    q = len(rgb_values) - 1
    i = 0
    while i <= q:
        if rgb_values[i] == 'r': # first value
            rgb_values[i], rgb_values[p] = rgb_values[p], rgb_values[i]
            p += 1
            i += 1
        elif rgb_values[i] == 'b': # middle value
            rgb_values[i], rgb_values[q] = rgb_values[q], rgb_values[i]
            q -= 1
        else:
            i += 1

    return ''.join(rgb_values) # Convert from array back to string


def test_sort(sort_func, expected, input):
    actual = sort_func(input)
    if not expected == actual:
        raise Exception('FAIL Expected: {}   Actual: {}'.format(expected, actual))
    print 'PASS sorted: {}'.format(actual)

def test_sort_funcs(expected, input):
    test_sort(sort_rgb_bubble, expected, input)
    test_sort(sort_rgb_dutch, expected, input)

if __name__ == '__main__':
    test_sort_funcs('rrrgggb', 'grbrrgg')
    test_sort_funcs('rrrrrgggbbb',  'bgrbgrbgrrr')





    

