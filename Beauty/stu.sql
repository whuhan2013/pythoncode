/*
Navicat MySQL Data Transfer

Source Server         : xampp
Source Server Version : 100113
Source Host           : localhost:3306
Source Database       : beauty

Target Server Type    : MYSQL
Target Server Version : 100113
File Encoding         : 65001

Date: 2016-08-30 11:05:04
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for stu
-- ----------------------------
DROP TABLE IF EXISTS `stu`;
CREATE TABLE `stu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stu` varchar(255) DEFAULT NULL,
  `img` varchar(255) DEFAULT NULL,
  `score` int(20) NOT NULL DEFAULT '1400',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=78 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of stu
-- ----------------------------
INSERT INTO `stu` VALUES ('1', 'Mary', 'imgs/1.jpg', '1400');
INSERT INTO `stu` VALUES ('2', 'Nancy', 'imgs/2.jpg', '1400');
INSERT INTO `stu` VALUES ('3', 'Kacy', 'imgs/3.jpg', '1400');
INSERT INTO `stu` VALUES ('4', 'Judegli', 'imgs/4.jpg', '1400');
INSERT INTO `stu` VALUES ('5', 'Kacy1', 'imgs/7.jpg', '1400');
INSERT INTO `stu` VALUES ('6', 'Judegli1', 'imgs/6.jpg', '1400');
SET FOREIGN_KEY_CHECKS=1;
