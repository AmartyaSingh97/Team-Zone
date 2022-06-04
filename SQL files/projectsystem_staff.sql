CREATE DATABASE  IF NOT EXISTS `projectsystem` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `projectsystem`;
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: projectsystem
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `staff` (
  `First` varchar(250) NOT NULL,
  `Middle` varchar(250) NOT NULL,
  `Last` varchar(250) NOT NULL,
  `Staff_ID` int NOT NULL,
  `DOB` date DEFAULT NULL,
  `Email` varchar(250) NOT NULL,
  `Contact` double DEFAULT NULL,
  `Gender` varchar(250) NOT NULL,
  PRIMARY KEY (`Staff_ID`),
  UNIQUE KEY `Email` (`Email`),
  UNIQUE KEY `Contact` (`Contact`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` VALUES ('bhargavi','akash','kamble',101,'2002-09-14','bhargavi@gmail.com',9145376257,'f'),('shruti','arun','patil',102,'2002-03-26','shruti@gmail.com',9232124557,'f'),('shreyas','amit','joshi',103,'2002-05-29','shreyas@gmail.com',9092124557,'m'),('dheeraj','piyush','zagade',104,'2003-11-21','dheeraj@gmail.com',9876512345,'m'),('priya','manish','shukla',105,'2000-01-01','priya@gmail.com',9129321213,'f'),(' ashish','kashish','nehra',106,'2001-03-23','ashish@gmail.com',8748398247,'m'),('manik','rajesh','verma',107,'2000-04-30','manik@gmail.com',9849384732,'m'),('atul ','ajay','wagh',108,'2001-07-07','atul@gmail.com',8347837242,'m');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed
