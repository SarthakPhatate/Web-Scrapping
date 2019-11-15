-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Sep 06, 2019 at 08:39 AM
-- Server version: 5.7.26
-- PHP Version: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flimapia`
--

-- --------------------------------------------------------

--
-- Table structure for table `flim_info`
--

DROP TABLE IF EXISTS `flim_info`;
CREATE TABLE IF NOT EXISTS `flim_info` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `time_stamp` varchar(100) NOT NULL,
  `film_name` varchar(255) NOT NULL,
  `cast` varchar(300) NOT NULL,
  `director` varchar(100) NOT NULL,
  `production` varchar(150) NOT NULL,
  `year` varchar(10) NOT NULL,
  `language` varchar(200) NOT NULL,
  `descpriton` varchar(15000) NOT NULL,
  `location` varchar(1000) NOT NULL,
  `location_link` varchar(1000) NOT NULL,
  `scenes` varchar(1000) NOT NULL,
  `scenes_descripton` varchar(10000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
