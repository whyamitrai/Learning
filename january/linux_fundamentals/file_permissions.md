# Linux File Permissions

## How do you view Linux file permissions?

The `ls` command along with its `-l` (for long listing) option will show you metadata about your Linux files, including the permissions set on the file.

```bash
$ ls -l
drwxr-xr-x. 4 root root    68 Jun 13 20:25 tuned
-rw-r--r--. 1 root root  4017 Feb 24  2022 vimrc
```

In this example, you see two different listings. The first field of the `ls -l` output is a group of metadata that includes the permissions on each file. Here are the components of the vimrc listing:

- **File type:** `-`
- **Permission settings:** `rw-r--r--`
- **Extended attributes:** dot (`.`)
- **User owner:** `root`
- **Group owner:** `root`

The fields "File type" and "Extended attributes" are outside the scope of this article, but in the featured output above, the vimrc file is a normal file, which is file type `-` (that is, no special type).

The tuned listing is for a `d`, or directory, type file. There are other file types as well, but these two are the most common. Available attributes are dependent on the filesystem format that the files are stored on. For Red Hat Enterprise Linux 7, 8, and 9, the default filesystem format is XFS.

## How do you read file permissions?

This article is about the permission settings on a file. The interesting permissions from the vimrc listing are:

```
rw-r--r--
```

This string is actually an expression of three different sets of permissions:

- `rw-`
- `r--`
- `r--`

The first set of permissions applies to the owner of the file. The second set of permissions applies to the user group that owns the file. The third set of permissions is generally referred to as "others." All Linux files belong to an owner and a group.

When permissions and users are represented by letters, that is called **symbolic mode**. For users, `u` stands for user owner, `g` for group owner, and `o` for others. For permissions, `r` stands for read, `w` for write, and `x` for execute.

## What are octal values?

When Linux file permissions are represented by numbers, it's called **numeric mode**. In numeric mode, a three-digit value represents specific file permissions (for example, 744.) These are called octal values. The first digit is for owner permissions, the second digit is for group permissions, and the third is for other users. Each permission has a numeric value assigned to it:

- `r` (read): **4**
- `w` (write): **2**
- `x` (execute): **1**

In the permission value 744, the first digit corresponds to the user, the second digit to the group, and the third digit to others. By adding up the value of each user classification, you can find the file permissions.

For example, a file might have read, write, and execute permissions for its owner, and only read permission for all other users. That looks like this:

- **Owner:** `rwx` = 4+2+1 = **7**
- **Group:** `r--` = 4+0+0 = **4**
- **Others:** `r--` = 4+0+0 = **4**

The results produce the three-digit value **744**.

**To modify the permission of a file we use "chmod 744 test.txt(filename)"**