## The diff command
You use the diff command to find the differences between two files. On its own, it’s a bit hard to use; instead, use diff -u to find lines that differ in two files:

# but what if we want to show only the lines ?

Simple ! we use : 
`diff -u hello_world.txt hello_world_long.txt`

```
~$ cat menu1.txt 
Menu1:

Apples
Bananas
Oranges
Pears

~$ cat menu2.txt 
Menu:

Apples
Bananas
Grapes
Strawberries

~$ diff -u menu1.txt menu2.txt 
--- menu1.txt   2019-12-16 18:46:13.794879924 +0900
+++ menu2.txt   2019-12-16 18:46:42.090995670 +0900
@@ -1,6 +1,6 @@
-Menu1:
+Menu:
 
 Apples
 Bananas
-Oranges
-Pears
+Grapes
+Strawberries

```

## The patch command
The patch command is useful for applying file **differences**. See the example below, which compares two files. The comparison is saved as a .diff file, which is then patched to the original file!

`~$ diff -u hello_world.txt hello_world_long.txt > hello_world.diff`

and when you patch : 

`patch hello_world.txt < hello_world.diff`