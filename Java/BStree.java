import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;

 
public class BStree {

public static void main(String[] args) {

BSTree<Integer> tree = new BSTree<Integer>();

String command;

int data;

 
Scanner input = new Scanner(System.in);

System.out.println("Enter a command: i(insert), r(emove), s(earch), inorder, p(rint), h(eight), nc(node count), w(idth), k(th smallest node), c(count trees),or q(uit)");

 
while (true) {

System.out.print("> ");

command = input.next();

if (command.equals("i")) {

data = input.nextInt();

if (tree.insert(data))

System.out.println(data + " inserted.");

else

System.out.println(data + " is in the tree.");

} else if (command.equals("r")) {

data = input.nextInt();

if (tree.remove(data))

System.out.println(data + " removed.");

else

System.out.println("No such " + data + "!");

} else if (command.equals("s")) {

data = input.nextInt();

if (tree.search(data))

System.out.println(data + " is in the tree.");

else

System.out.println("No such " + data + "!");

} else if (command.equals("inorder"))

tree.inorderTraverse();

else if (command.equals("h"))

System.out.println("Tree height: " + tree.height());

 

else if (command.equals("nc"))

System.out.println("Node count: " + tree.countNodes());

else if (command.equals("w"))

System.out.println("Max number of nodes: " + tree.width());

else if (command.equals("k")) {

data = input.nextInt();

BSTNode<Integer> node = tree.kthSmallestNode(data);

if (node != null)

System.out.println(node.item);

else

System.out.println("Out of range!");

} else if (command.equals("c")) {

int numKeys = input.nextInt();

System.out.println("Number of trees: " + tree.countTrees(numKeys));

} else if (command.equals("p"))

tree.print();

else if (command.equals("q")) {

System.out.println("Commands terminated.");

break;

}

}

input.close();

}

}

 

class BSTNode<T> {

public T item;

public BSTNode<T> left;

public BSTNode<T> right;

 

public BSTNode(T item) {

this.item = item;

left = null;

right = null;

}

 

public BSTNode(T item, BSTNode<T> left, BSTNode<T> right) {

this.item = item;

this.left = left;

this.right = right;

}

}

 

class BSTree<T extends Comparable<T>> {

public BSTNode<T> root;

private boolean insertSuccess;

private boolean removeSuccess;

 

public BSTree() {

root = null;

}

 

public boolean insert(T data) {

if (isEmpty()) {

root = new BSTNode<T>(data);

insertSuccess = true;

} else root = insert(root, data);

return insertSuccess;

}

 

public BSTNode<T> insert(BSTNode<T> tree, T data) {

if (data.compareTo(tree.item) > 0) {

if (tree.right == null) {

tree.right = new BSTNode<T>(data);

insertSuccess = true;

return root;

} else insert(tree.right, data);

} else if (data.compareTo(tree.item) < 0) {

if (tree.left == null) {

tree.left = new BSTNode<T>(data);

insertSuccess = true;

return root;

} else insert(tree.left, data);

} else {

insertSuccess = false;

return root;

}

return root;

}

 

public boolean search(T data) {

if (isEmpty()) return false;

else return search(root, data);

}

 

private boolean search(BSTNode<T> tree, T data) {

if (data.compareTo(tree.item) > 0) {

if (tree.right != null)

return search(tree.right, data);

else return false;

} else if (data.compareTo(tree.item) < 0) {

if (tree.left != null)

return search(tree.left, data);

else return false;

} else {

return true;

}

}

public boolean remove(T data) {

if (isEmpty()) return false;

else root = remove(root, data);

return removeSuccess;

}

 

public BSTNode<T> remove(BSTNode<T> tree, T data) {

if (data.compareTo(tree.item) > 0) {

if (tree.right != null)

return remove(tree.right, data);

else {

removeSuccess = false;

return root;

}

} else if (data.compareTo(tree.item) < 0) {

if (tree.left != null)

return remove(tree.left, data);

else {

removeSuccess = false;

return root;

}

} else {

BSTNode<T> parent = FindParent(root, tree);

if (parent != null) {

if (tree.right == null && tree.left == null) {

if (parent.left == tree) parent.left = null;

else if (parent.right == tree) parent.right = null;

} else if (tree.right == null) {

if (parent.left == tree) parent.left = tree.left;

else if (parent.right == tree) parent.right = tree.left;

} else if (tree.left == null) {

if (parent.left == tree) parent.left = tree.right;

else if (parent.right == tree) parent.right = tree.right;

} else {

BSTNode<T> temp = FindReplacement(tree.left, tree);

temp.left = tree.left;

temp.right = tree.right;

if (parent.left == tree) parent.left = temp;

else if (parent.right == tree) parent.right = temp;

}

removeSuccess = true;

} else {

if (tree.right == null && tree.left == null) {

root = null;

} else if (tree.right == null) {

root = tree.left;

} else if (tree.left == null) {

root = tree.right;

} else {

BSTNode<T> temp = FindReplacement(tree.left, tree);

temp.left = tree.left;

temp.right = tree.right;

root = temp;

}

removeSuccess = true;

}

return root;

}

}

private BSTNode<T> FindParent(BSTNode<T> tree, BSTNode<T> child) {

if (child.item.compareTo(tree.item) > 0) {

if (tree.right == child)

return tree;

else return FindParent(tree.right, child);

} else if (child.item.compareTo(tree.item) < 0) {

if (tree.left == child)

return tree;

else return FindParent(tree.left, child);

} else {

return null;

}

}

 

private BSTNode<T> FindReplacement(BSTNode<T> tree, BSTNode<T> parent) {

if (tree.right == null) {

if (tree.left == null) {

if(parent.right == tree) parent.right = null;

else if(parent.left == tree) parent.left = null;

return tree;

} else {

if(parent.right == tree) parent.right = tree.left;

else if(parent.left == tree) parent.left = tree.left;

tree.left = null;

return tree;

}

} else {

return FindReplacement(tree.right, tree);

}

}

 

public boolean isEmpty() {

return root == null;

}

 

public void print() {

print(root, 0);

}

 

public void print(BSTNode<T> tree, int skip) {

if (tree != null) {

print(tree.right, skip + 10);

for (int i = 0; i < skip; i++)

System.out.print(" ");

System.out.print(tree.item);

if (tree.left != null)

System.out.print(",L");

if (tree.right != null)

System.out.print(",R");

System.out.println();

print(tree.left, skip + 10);

}

}

 

public void inorderTraverse() {

inorderTraverse(root);

System.out.println();

}

 

private void inorderTraverse(BSTNode<T> tree) {

if (tree != null) {

inorderTraverse(tree.left);

System.out.print(tree.item + " ");

inorderTraverse(tree.right);

}

}

 

public int height() {

if (isEmpty()) return -1;

else return heightCount(root, 0);

}

 

private int heightCount(BSTNode<T> tree, int i) {

int left = -1, right = -1;

if (tree.left != null) left = heightCount(tree.left, i + 1);

if (tree.right != null) right = heightCount(tree.right, i + 1);

if (tree.left == null && tree.right == null) return i;

else if (left >= right) return left;

else return right;

}

 

public int countNodes() {

int cn[] = new int[1];

CountInorder(root, cn);

return cn[0];

}

 

private void CountInorder(BSTNode<T> tree, int[] cn) {

if (tree != null) {

CountInorder(tree.left, cn);

cn[0]++;

CountInorder(tree.right, cn);

}

}

 

public int width() {

if (isEmpty()) return 0;

else {

ArrayList<Integer> widthlist = new ArrayList<Integer>();

widthCount(root, 0, widthlist);

int max = 0;

Iterator<Integer> itr = widthlist.iterator();

while (itr.hasNext()) {

int tmp = itr.next();

if (tmp > max)

max = tmp;

}

return max;

}

}

 

private void widthCount(BSTNode<T> tree, int i, ArrayList<Integer> widthlist) {

if (widthlist.size() <= i) widthlist.add(1);

else widthlist.set(i, widthlist.get(i) + 1);

if (tree.left != null) widthCount(tree.left, i + 1, widthlist);

if (tree.right != null) widthCount(tree.right, i + 1, widthlist);

}

 

 

public BSTNode<T> kthSmallestNode(int kth) {

int count[] = new int[1];

count[0] = 0;

if (isEmpty()) return null;

else return inorder4kth(root, kth, count);

}

 

private BSTNode<T> inorder4kth(BSTNode<T> tree, int k, int[] count) {

if (tree != null) {

BSTNode<T> tempNode = inorder4kth(tree.left, k, count);

if (tempNode != null) return tempNode;

count[0]++;

if (count[0] == k) return tree;

tempNode = inorder4kth(tree.right, k, count);

if (tempNode != null) return tempNode;

}

return null;

}

}





#자바
#자바자료구조
#자바이진탐색트리
#자바탐색트리
블로그카페Keep메모보내기 인쇄
[출처] [자바] 이진탐색트리 코드 및 설명|작성자 뿌잉뿌우삥