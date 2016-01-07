Algorithms
==========

Collected algorithm files for using/importing later. For most files, initial
version won't be fully refactored. Explanation of algorithm included here.


Quick Union
-----------

For simply connected graphs with no edge weighting, you can determine if two
are connected by building the graph from `self.unite()` calls. Then, you can
check if two point are connected with `self.find()`.

Should you need to reduce the map down more for easier processing, you can
use `self.reduce()` to simplify the graph down more.

You unite two nodes, checking to see if one tree (from that node) is larger
or smaller than the other, so that the tree don't become too tall while
still joining everything up. In addition, when searching for a root, the
tree is further compressed by setting each observed node to its parent's
value.

