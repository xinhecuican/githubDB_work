DROP DATABASE IF EXIST `test`
CREATE DATABASE `test`

-- ----------------------------
-- Table structure for t_user
-- ----------------------------
DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user` (
  `id` SMALLINT(5) UNSIGNED NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) DEFAULT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `password` VARCHAR(255) DEFAULT NULL,
  `phone` VARCHAR(20) DEFAULT NULL,
  `email` VARCHAR(40) DEFAULT NULL,
  `address` VARCHAR(255) DEFAULT NULL,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
) ENGINE=InnoDB AUTO_INCREMENT=613 DEFAULT CHARSET=UTF8;