-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: academic_performance
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('dc94f7460a48');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `curriculums`
--

DROP TABLE IF EXISTS `curriculums`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `curriculums` (
  `id` int NOT NULL AUTO_INCREMENT,
  `discipline_name` varchar(100) NOT NULL,
  `name_of_specialty` varchar(100) NOT NULL,
  `semester` int NOT NULL,
  `number_of_hours` int NOT NULL,
  `reporting_form_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_curriculums_reporting_form_id_reporting_forms` (`reporting_form_id`),
  CONSTRAINT `fk_curriculums_reporting_form_id_reporting_forms` FOREIGN KEY (`reporting_form_id`) REFERENCES `reporting_forms` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `curriculums`
--

LOCK TABLES `curriculums` WRITE;
/*!40000 ALTER TABLE `curriculums` DISABLE KEYS */;
INSERT INTO `curriculums` VALUES (1,'Автоматизация','Информационная безопасность',5,100,1),(2,'1234тест','тест',4,245,1);
/*!40000 ALTER TABLE `curriculums` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forms_of_education`
--

DROP TABLE IF EXISTS `forms_of_education`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `forms_of_education` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forms_of_education`
--

LOCK TABLES `forms_of_education` WRITE;
/*!40000 ALTER TABLE `forms_of_education` DISABLE KEYS */;
INSERT INTO `forms_of_education` VALUES (1,'дневная'),(2,'вечерняя'),(3,'заочная');
/*!40000 ALTER TABLE `forms_of_education` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `journals_of_performance`
--

DROP TABLE IF EXISTS `journals_of_performance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `journals_of_performance` (
  `id` int NOT NULL AUTO_INCREMENT,
  `semester` int NOT NULL,
  `student_id` int NOT NULL,
  `curriculum_id` int NOT NULL,
  `mark_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_journals_of_performance_curriculum_id_curriculums` (`curriculum_id`),
  KEY `fk_journals_of_performance_mark_id_marks` (`mark_id`),
  KEY `fk_journals_of_performance_student_id_users` (`student_id`),
  CONSTRAINT `fk_journals_of_performance_curriculum_id_curriculums` FOREIGN KEY (`curriculum_id`) REFERENCES `curriculums` (`id`),
  CONSTRAINT `fk_journals_of_performance_mark_id_marks` FOREIGN KEY (`mark_id`) REFERENCES `marks` (`id`),
  CONSTRAINT `fk_journals_of_performance_student_id_users` FOREIGN KEY (`student_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `journals_of_performance`
--

LOCK TABLES `journals_of_performance` WRITE;
/*!40000 ALTER TABLE `journals_of_performance` DISABLE KEYS */;
INSERT INTO `journals_of_performance` VALUES (1,5,1,1,3);
/*!40000 ALTER TABLE `journals_of_performance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marks`
--

DROP TABLE IF EXISTS `marks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `number_mark` int NOT NULL,
  `text_mark` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marks`
--

LOCK TABLES `marks` WRITE;
/*!40000 ALTER TABLE `marks` DISABLE KEYS */;
INSERT INTO `marks` VALUES (1,2,'неудовлетворительно'),(2,3,'удовлетворительно'),(3,4,'хорошо'),(4,5,'отлично');
/*!40000 ALTER TABLE `marks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reporting_forms`
--

DROP TABLE IF EXISTS `reporting_forms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reporting_forms` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reporting_forms`
--

LOCK TABLES `reporting_forms` WRITE;
/*!40000 ALTER TABLE `reporting_forms` DISABLE KEYS */;
INSERT INTO `reporting_forms` VALUES (1,'экзамен',NULL),(2,'зачет',NULL);
/*!40000 ALTER TABLE `reporting_forms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Администратор','Администратор'),(2,'Модератор','Модератор'),(3,'Студент','Студент');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `login` varchar(100) NOT NULL,
  `password_hash` varchar(200) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `role_id` int NOT NULL,
  `year_of_admission` year DEFAULT NULL,
  `form_of_education_id` int DEFAULT NULL,
  `group_number` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_users_login` (`login`),
  KEY `fk_users_form_of_education_id_forms_of_education` (`form_of_education_id`),
  KEY `fk_users_role_id_roles` (`role_id`),
  CONSTRAINT `fk_users_form_of_education_id_forms_of_education` FOREIGN KEY (`form_of_education_id`) REFERENCES `forms_of_education` (`id`),
  CONSTRAINT `fk_users_role_id_roles` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'user','pbkdf2:sha256:600000$dJqnf8XkY1vg87Bp$55327f95b22cd1232636d491ac8482bcf1ce2046853d8db1a8abf9a23f44757e','Иванов','Иван','Иванович',3,2023,1,'211-331'),(2,'admin','pbkdf2:sha256:600000$dJqnf8XkY1vg87Bp$55327f95b22cd1232636d491ac8482bcf1ce2046853d8db1a8abf9a23f44757e','Админов','Админ','Админович',1,NULL,NULL,NULL),(3,'student','pbkdf2:sha256:600000$1XCGMYVKGHFjey9j$fe472e69d44a7dac33800e3b06491e687510bad120466f8454c97f846ad39b08','student','student','student',3,2000,3,'123-456'),(4,'student1','pbkdf2:sha256:600000$cbgyMLKrD9hnMLZI$48d77f734af3f8b2ddf5d13afc54e7bb614a96046ed7686ef084a06526708061','student_edit','student_edit_too','student_not_student',3,1987,NULL,'123-450');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-27 20:34:08
