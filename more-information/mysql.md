Dump of mysql schema.

```SQL
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mis_club           |
+--------------------+
2 rows in set (0.01 sec)

mysql> use mis_club
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+------------------------------+
| Tables_in_mis_club           |
+------------------------------+
| attendance_meeting           |
| attendance_meeting_attendees |
| attendance_member            |
| auth_group                   |
| auth_group_permissions       |
| auth_permission              |
| auth_user                    |
| auth_user_groups             |
| auth_user_user_permissions   |
| django_admin_log             |
| django_content_type          |
| django_migrations            |
| django_session               |
+------------------------------+
13 rows in set (0.00 sec)

mysql> show columns from attendance_meeting;
+-----------------------+--------------+------+-----+---------+----------------+
| Field                 | Type         | Null | Key | Default | Extra          |
+-----------------------+--------------+------+-----+---------+----------------+
| id                    | int(11)      | NO   | PRI | NULL    | auto_increment |
| title                 | varchar(200) | NO   |     | NULL    |                |
| date_time             | datetime     | YES  |     | NULL    |                |
| description           | longtext     | NO   |     | NULL    |                |
| bonus                 | tinyint(1)   | NO   |     | NULL    |                |
| available_for_sign_in | tinyint(1)   | NO   |     | NULL    |                |
+-----------------------+--------------+------+-----+---------+----------------+
6 rows in set (0.01 sec)

mysql> show columns from attendance_meeting_attendees;
+------------+---------+------+-----+---------+----------------+
| Field      | Type    | Null | Key | Default | Extra          |
+------------+---------+------+-----+---------+----------------+
| id         | int(11) | NO   | PRI | NULL    | auto_increment |
| meeting_id | int(11) | NO   | MUL | NULL    |                |
| user_id    | int(11) | NO   | MUL | NULL    |                |
+------------+---------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

mysql> show columns from attendance_member;
+-------------------------+-------------+------+-----+---------+----------------+
| Field                   | Type        | Null | Key | Default | Extra          |
+-------------------------+-------------+------+-----+---------+----------------+
| id                      | int(11)     | NO   | PRI | NULL    | auto_increment |
| phone                   | varchar(12) | YES  |     | NULL    |                |
| year_in_school          | varchar(2)  | NO   |     | NULL    |                |
| major                   | varchar(40) | NO   |     | NULL    |                |
| user_id                 | int(11)     | NO   | UNI | NULL    |                |
| ksu_identification_code | bigint(20)  | NO   | UNI | NULL    |                |
+-------------------------+-------------+------+-----+---------+----------------+
6 rows in set (0.00 sec)

mysql> show columns from auth_user;
+--------------+--------------+------+-----+---------+----------------+
| Field        | Type         | Null | Key | Default | Extra          |
+--------------+--------------+------+-----+---------+----------------+
| id           | int(11)      | NO   | PRI | NULL    | auto_increment |
| password     | varchar(128) | NO   |     | NULL    |                |
| last_login   | datetime     | NO   |     | NULL    |                |
| is_superuser | tinyint(1)   | NO   |     | NULL    |                |
| username     | varchar(30)  | NO   | UNI | NULL    |                |
| first_name   | varchar(30)  | NO   |     | NULL    |                |
| last_name    | varchar(30)  | NO   |     | NULL    |                |
| email        | varchar(75)  | NO   |     | NULL    |                |
| is_staff     | tinyint(1)   | NO   |     | NULL    |                |
| is_active    | tinyint(1)   | NO   |     | NULL    |                |
| date_joined  | datetime     | NO   |     | NULL    |                |
+--------------+--------------+------+-----+---------+----------------+
11 rows in set (0.01 sec)
```
