0-iam_betty
Switches the current user to the user "betty".

1-who_am_i
Prints the effective username of the current user.

2-groups
Prints all the groups the current user is a part of.

3-new_owner
Changes the owner of the file "hello" to the user "betty".

4-empty
Creates an empty file called "hello".

5-execute
Adds execute permission to the owner of the file "hello".

6-multiple_permissions
Adds execute permission to the owner and the group owner, and read permission to other users, to the file "hello".

7-everybody
Adds execution permission to the owner, the group owner, and other users for the file "hello".

8-James_Bond
Sets the permission of the file "hello" so that the owner and group have no permission at all, while other users have all permissions.

9-John_Doe
Sets the mode of the file "hello" to -rwxr-x-wx, changing the permissions for the owner, group owner, and others.

10-mirror_permissions
Sets the mode of the file "hello" to match the mode of the file "olleh".

11-directories_permissions
Adds execute permission to all subdirectories of the current directory for the owner, group owner, and other users. Regular files are not changed.

12-directory_permissions
Creates a directory called "my_dir" with permissions 751 in the working directory.

13-change_group
Changes the group owner of the file "hello" to "school".

100-change_owner_and_group
Changes the owner to "vincent" and the group owner to "staff" for all files and directories in the working directory.

101-symbolic_link_permissions
Changes the owner to "vincent" and the group owner to "staff" for the symbolic link "_hello".

102-if_only
Changes the owner of the file "hello" to "betty" only if it is currently owned by the user "guillaume".

103-Star_Wars
Plays an ASCII art representation of Star Wars IV in the terminal.
