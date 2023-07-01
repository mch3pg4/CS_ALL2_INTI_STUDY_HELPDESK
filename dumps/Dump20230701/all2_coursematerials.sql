-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: all2
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `coursematerials`
--

DROP TABLE IF EXISTS `coursematerials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coursematerials` (
  `idcoursematerials` int NOT NULL AUTO_INCREMENT,
  `week` int NOT NULL,
  `subj_name` varchar(100) NOT NULL,
  `material_name` longtext NOT NULL,
  `material_file` longtext NOT NULL,
  PRIMARY KEY (`idcoursematerials`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coursematerials`
--

LOCK TABLES `coursematerials` WRITE;
/*!40000 ALTER TABLE `coursematerials` DISABLE KEYS */;
INSERT INTO `coursematerials` VALUES (1,1,'Computer Architecture & Networks','Chapter 1-Machine Level Representation of Data\n','C:\\Users\\mch\\Desktop\\CS_ALL2_INTI_STUDY_HELPDESK\\course_materials\\Chapter 1 (Part A) Machine Level Representation of Data.pdf'),(2,2,'Computer Architecture & Networks','Chapter 2-Number Systems\n','C:\\Users\\mch\\Desktop\\CS_ALL2_INTI_STUDY_HELPDESK\\course_materials\\02_4004CEM_Number Systems_v2.pdf'),(3,2,'Computer Architecture & Networks','Lab 1\n','C:\\Users\\mch\\Desktop\\CS_ALL2_INTI_STUDY_HELPDESK\\course_materials\\Lab 1(A).pdf'),(4,3,'Computer Architecture & Networks','Chapter 3-Data Representation\n','C:\\Users\\mch\\Desktop\\CS_ALL2_INTI_STUDY_HELPDESK\\course_materials\\03_Data Representation.pdf'),(5,3,'Computer Architecture & Networks','Exercise 3-Data Representation\n','C:\\Users\\mch\\Desktop\\CS_ALL2_INTI_STUDY_HELPDESK\\course_materials\\Exercise 03_Data Representation.pdf'),(6,4,'Computer Architecture & Networks','Chapter 4-Digital Logic & Digital Systems (Part A)','C:\\Users\\mch\\Desktop\\CS_ALL2_INTI_STUDY_HELPDESK\\course_materials\\Chapter 2 - Digital Logic & Digital Systems (Part A).pdf');
/*!40000 ALTER TABLE `coursematerials` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-01 15:34:51
