-- Respaldo de proyectoo
-- Fecha: 2026-06-22 19:05:42
-- Tipo: Completo (Estructura + Datos)

-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: proyectoo
-- ------------------------------------------------------
-- Server version	8.0.45

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',2,'add_permission'),(2,'Can change permission',2,'change_permission'),(3,'Can delete permission',2,'delete_permission'),(4,'Can view permission',2,'view_permission'),(5,'Can add group',1,'add_group'),(6,'Can change group',1,'change_group'),(7,'Can delete group',1,'delete_group'),(8,'Can view group',1,'view_group'),(9,'Can add content type',3,'add_contenttype'),(10,'Can change content type',3,'change_contenttype'),(11,'Can delete content type',3,'delete_contenttype'),(12,'Can view content type',3,'view_contenttype'),(13,'Can add caja',4,'add_caja'),(14,'Can change caja',4,'change_caja'),(15,'Can delete caja',4,'delete_caja'),(16,'Can view caja',4,'view_caja'),(17,'Can add cliente',5,'add_cliente'),(18,'Can change cliente',5,'change_cliente'),(19,'Can delete cliente',5,'delete_cliente'),(20,'Can view cliente',5,'view_cliente'),(21,'Can add compra',7,'add_compra'),(22,'Can change compra',7,'change_compra'),(23,'Can delete compra',7,'delete_compra'),(24,'Can view compra',7,'view_compra'),(25,'Can add marca',10,'add_marca'),(26,'Can change marca',10,'change_marca'),(27,'Can delete marca',10,'delete_marca'),(28,'Can view marca',10,'view_marca'),(29,'Can add proveedor',15,'add_proveedor'),(30,'Can change proveedor',15,'change_proveedor'),(31,'Can delete proveedor',15,'delete_proveedor'),(32,'Can view proveedor',15,'view_proveedor'),(33,'Can add Tipo de Servicio',17,'add_tiposervicio'),(34,'Can change Tipo de Servicio',17,'change_tiposervicio'),(35,'Can delete Tipo de Servicio',17,'delete_tiposervicio'),(36,'Can view Tipo de Servicio',17,'view_tiposervicio'),(37,'Can add Usuario del Sistema',18,'add_usuariosistema'),(38,'Can change Usuario del Sistema',18,'change_usuariosistema'),(39,'Can delete Usuario del Sistema',18,'delete_usuariosistema'),(40,'Can view Usuario del Sistema',18,'view_usuariosistema'),(41,'Can add orden servicio',12,'add_ordenservicio'),(42,'Can change orden servicio',12,'change_ordenservicio'),(43,'Can delete orden servicio',12,'delete_ordenservicio'),(44,'Can view orden servicio',12,'view_ordenservicio'),(45,'Can add producto',14,'add_producto'),(46,'Can change producto',14,'change_producto'),(47,'Can delete producto',14,'delete_producto'),(48,'Can view producto',14,'view_producto'),(49,'Can add factura',9,'add_factura'),(50,'Can change factura',9,'change_factura'),(51,'Can delete factura',9,'delete_factura'),(52,'Can view factura',9,'view_factura'),(53,'Can add detalle orden producto',8,'add_detalleordenproducto'),(54,'Can change detalle orden producto',8,'change_detalleordenproducto'),(55,'Can delete detalle orden producto',8,'delete_detalleordenproducto'),(56,'Can view detalle orden producto',8,'view_detalleordenproducto'),(57,'Can add Detalle de Servicio en Orden',13,'add_ordenserviciodetalle'),(58,'Can change Detalle de Servicio en Orden',13,'change_ordenserviciodetalle'),(59,'Can delete Detalle de Servicio en Orden',13,'delete_ordenserviciodetalle'),(60,'Can view Detalle de Servicio en Orden',13,'view_ordenserviciodetalle'),(61,'Can add vehiculo',19,'add_vehiculo'),(62,'Can change vehiculo',19,'change_vehiculo'),(63,'Can delete vehiculo',19,'delete_vehiculo'),(64,'Can view vehiculo',19,'view_vehiculo'),(65,'Can add Seguimiento de Mantenimiento',16,'add_seguimientomantenimiento'),(66,'Can change Seguimiento de Mantenimiento',16,'change_seguimientomantenimiento'),(67,'Can delete Seguimiento de Mantenimiento',16,'delete_seguimientomantenimiento'),(68,'Can view Seguimiento de Mantenimiento',16,'view_seguimientomantenimiento'),(69,'Can add notificacion',11,'add_notificacion'),(70,'Can change notificacion',11,'change_notificacion'),(71,'Can delete notificacion',11,'delete_notificacion'),(72,'Can view notificacion',11,'view_notificacion'),(73,'Can add compatibilidad producto',6,'add_compatibilidadproducto'),(74,'Can change compatibilidad producto',6,'change_compatibilidadproducto'),(75,'Can delete compatibilidad producto',6,'delete_compatibilidadproducto'),(76,'Can view compatibilidad producto',6,'view_compatibilidadproducto'),(77,'Can add Perfil de Usuario',20,'add_perfilusuario'),(78,'Can change Perfil de Usuario',20,'change_perfilusuario'),(79,'Can delete Perfil de Usuario',20,'delete_perfilusuario'),(80,'Can view Perfil de Usuario',20,'view_perfilusuario'),(81,'Can add session',21,'add_session'),(82,'Can change session',21,'change_session'),(83,'Can delete session',21,'delete_session'),(84,'Can view session',21,'view_session'),(85,'Can add log entry',22,'add_logentry'),(86,'Can change log entry',22,'change_logentry'),(87,'Can delete log entry',22,'delete_logentry'),(88,'Can view log entry',22,'view_logentry'),(89,'Can add Producto del Proveedor',24,'add_proveedorproducto'),(90,'Can change Producto del Proveedor',24,'change_proveedorproducto'),(91,'Can delete Producto del Proveedor',24,'delete_proveedorproducto'),(92,'Can view Producto del Proveedor',24,'view_proveedorproducto'),(93,'Can add compra detalle',23,'add_compradetalle'),(94,'Can change compra detalle',23,'change_compradetalle'),(95,'Can delete compra detalle',23,'delete_compradetalle'),(96,'Can view compra detalle',23,'view_compradetalle');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `caja`
--

DROP TABLE IF EXISTS `caja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caja` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(255) NOT NULL,
  `monto` decimal(12,2) NOT NULL,
  `tipo` varchar(10) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `categoria` varchar(20) NOT NULL,
  `metodo_pago` varchar(20) NOT NULL,
  `comprobante` varchar(100) DEFAULT NULL,
  `observaciones` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caja`
--

LOCK TABLES `caja` WRITE;
/*!40000 ALTER TABLE `caja` DISABLE KEYS */;
INSERT INTO `caja` VALUES (1,'Compra Factura 433324324',6700000.00,'EGRESO','2026-06-20 19:02:06.804547','Proveedores','TarjetaDebito','',NULL),(2,'Factura FAC-0003 â€” Orden de Servicio',390000.00,'INGRESO','2026-06-22 12:33:38.815695','Servicios','Nequi','',NULL),(3,'Factura FAC-0004 â€” Venta de Producto',8400000.00,'INGRESO','2026-06-23 00:03:20.086994','Ventas','Nequi','',NULL);
/*!40000 ALTER TABLE `caja` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) NOT NULL,
  `tipo_documento` varchar(3) NOT NULL,
  `numero_documento` varchar(20) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero_documento` (`numero_documento`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,'Sofia','CC','1054284348','+573434324324','pedrazayuliana198@gmail.com');
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compatibilidad_producto`
--

DROP TABLE IF EXISTS `compatibilidad_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compatibilidad_producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `marca_vehiculo_id` bigint NOT NULL,
  `producto_id` bigint NOT NULL,
  `tipo_servicio_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `compatibilidad_producto_producto_id_marca_vehicu_0b706a94_uniq` (`producto_id`,`marca_vehiculo_id`,`tipo_servicio_id`),
  KEY `compatibilidad_producto_marca_vehiculo_id_50d58ec7_fk_marca_id` (`marca_vehiculo_id`),
  KEY `compatibilidad_produ_tipo_servicio_id_905e4d0f_fk_tipo_serv` (`tipo_servicio_id`),
  CONSTRAINT `compatibilidad_produ_tipo_servicio_id_905e4d0f_fk_tipo_serv` FOREIGN KEY (`tipo_servicio_id`) REFERENCES `tipo_servicio` (`id`),
  CONSTRAINT `compatibilidad_producto_marca_vehiculo_id_50d58ec7_fk_marca_id` FOREIGN KEY (`marca_vehiculo_id`) REFERENCES `marca` (`id`),
  CONSTRAINT `compatibilidad_producto_producto_id_9bfe011d_fk_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compatibilidad_producto`
--

LOCK TABLES `compatibilidad_producto` WRITE;
/*!40000 ALTER TABLE `compatibilidad_producto` DISABLE KEYS */;
INSERT INTO `compatibilidad_producto` VALUES (1,1,1,1),(2,1,2,2);
/*!40000 ALTER TABLE `compatibilidad_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compra`
--

DROP TABLE IF EXISTS `compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compra` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad` int NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `num_factura_proveedor` varchar(50) NOT NULL,
  `metodo_pago` varchar(20) DEFAULT NULL,
  `total_pagado` decimal(12,2) NOT NULL,
  `estado_pago` varchar(10) NOT NULL,
  `fecha_pago` datetime(6) DEFAULT NULL,
  `archivo_factura` varchar(100) DEFAULT NULL,
  `producto_id` bigint NOT NULL,
  `proveedor_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `num_factura_proveedor` (`num_factura_proveedor`),
  KEY `compra_producto_id_ab4e0151_fk_producto_id` (`producto_id`),
  KEY `compra_proveedor_id_11336635_fk_proveedor_id` (`proveedor_id`),
  CONSTRAINT `compra_producto_id_ab4e0151_fk_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`),
  CONSTRAINT `compra_proveedor_id_11336635_fk_proveedor_id` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compra`
--

LOCK TABLES `compra` WRITE;
/*!40000 ALTER TABLE `compra` DISABLE KEYS */;
INSERT INTO `compra` VALUES (1,23,'2026-06-20 19:01:24.000000','433324324','TarjetaDebito',6700000.00,'Pagada','2026-06-20 19:02:06.792831','',1,1),(2,35,'2026-06-20 20:05:56.000000','764544',NULL,7670000.00,'Pendiente',NULL,'',2,2);
/*!40000 ALTER TABLE `compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_orden_producto`
--

DROP TABLE IF EXISTS `detalle_orden_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_orden_producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad` int unsigned NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL,
  `orden_id` bigint NOT NULL,
  `producto_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `detalle_orden_producto_orden_id_c0323597_fk_orden_servicio_id` (`orden_id`),
  KEY `detalle_orden_producto_producto_id_4b1655ab_fk_producto_id` (`producto_id`),
  CONSTRAINT `detalle_orden_producto_orden_id_c0323597_fk_orden_servicio_id` FOREIGN KEY (`orden_id`) REFERENCES `orden_servicio` (`id`),
  CONSTRAINT `detalle_orden_producto_producto_id_4b1655ab_fk_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`),
  CONSTRAINT `detalle_orden_producto_chk_1` CHECK ((`cantidad` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_orden_producto`
--

LOCK TABLES `detalle_orden_producto` WRITE;
/*!40000 ALTER TABLE `detalle_orden_producto` DISABLE KEYS */;
INSERT INTO `detalle_orden_producto` VALUES (1,1,350000.00,1,2);
/*!40000 ALTER TABLE `detalle_orden_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (22,'admin','logentry'),(4,'app','caja'),(5,'app','cliente'),(6,'app','compatibilidadproducto'),(7,'app','compra'),(23,'app','compradetalle'),(8,'app','detalleordenproducto'),(9,'app','factura'),(10,'app','marca'),(11,'app','notificacion'),(12,'app','ordenservicio'),(13,'app','ordenserviciodetalle'),(14,'app','producto'),(15,'app','proveedor'),(24,'app','proveedorproducto'),(16,'app','seguimientomantenimiento'),(17,'app','tiposervicio'),(18,'app','usuariosistema'),(19,'app','vehiculo'),(1,'auth','group'),(2,'auth','permission'),(3,'contenttypes','contenttype'),(21,'sessions','session'),(20,'usuario','perfilusuario');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2026-06-13 18:37:09.121290'),(2,'contenttypes','0002_remove_content_type_name','2026-06-13 18:42:45.994548'),(3,'auth','0001_initial','2026-06-13 18:42:46.526520'),(4,'auth','0002_alter_permission_name_max_length','2026-06-13 18:42:46.666434'),(5,'auth','0003_alter_user_email_max_length','2026-06-13 18:42:46.678756'),(6,'auth','0004_alter_user_username_opts','2026-06-13 18:42:46.691901'),(7,'auth','0005_alter_user_last_login_null','2026-06-13 18:42:46.705346'),(8,'auth','0006_require_contenttypes_0002','2026-06-13 18:42:46.711245'),(9,'auth','0007_alter_validators_add_error_messages','2026-06-13 18:42:46.724586'),(10,'auth','0008_alter_user_username_max_length','2026-06-13 18:42:46.745968'),(11,'auth','0009_alter_user_last_name_max_length','2026-06-13 18:42:46.767986'),(12,'auth','0010_alter_group_name_max_length','2026-06-13 18:42:46.827269'),(13,'auth','0011_update_proxy_permissions','2026-06-13 18:42:46.846944'),(14,'auth','0012_alter_user_first_name_max_length','2026-06-13 18:42:46.878466'),(15,'app','0001_initial','2026-06-13 18:42:51.504894'),(16,'admin','0001_initial','2026-06-13 18:59:30.221052'),(17,'admin','0002_logentry_remove_auto_add','2026-06-13 18:59:46.926876'),(18,'admin','0003_logentry_add_action_flag_choices','2026-06-13 18:59:46.944230'),(19,'sessions','0001_initial','2026-06-13 18:59:47.034198');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1tsi3gorb5olyujmjlw0gb9ifxbamyib','.eJxVjztvwyAUhf8LaxsLLuQCHrt364543Ma0jokAt5Wq_vdiKUvW8_h0zi-rdMmt1-LoJ_fSCpt73emZuZtv7bvU5Co16q6XT9rYzJJHBbeTIEKjVeIxWkLU1p6lV6QADKZgz2wQ_N4XtzeqLqfRhEct-DiIh5E-_HYpUyxbrzlMR2S6u216LYnWl3v2AbD4toy2jNbLpIyxoJLxCtEEHUDFMciS5fysIElByQqLMliMQSC-gwSQpAwN6L72fPXj6FduuWzOr1S7b8dmDnjieAL-BmIGNQs9aW6F1k-cz5yzv3_Lj2V-:1wb3An:QgSRqtyiItZlf-tvCF9kB4EcJduN5rkS-qX52zcpcq4','2026-07-04 21:24:17.719805'),('x5m41exof7z5yt7zc6wpmq9oe9cnw6vz','.eJxVjLtuwzAMRf9FaxuBIiX6MWbPll2gbLpW69iAZWcp-u9xgAzpes-559dE2bcx7kXXmHvTmmA-37ck3Y_OT9B_y_y12G6ZtzUn-1TsixZ7WXqdzi_3X2CUMh5vrx1VHqs6sEBQ9o7VYWrqoOIGAJ-qgUBQa8dITgCVPCQODBQCDUd0n7Z8k7jqPZe8zFEmXTcpRxwB-QR8QrwitcG1xLaqG0fNB0ALYP4eCidHgA:1wboQS:OdC0G9IajQ7fZ8ldPKjUtEBIUcpg36DODVZCv51aj9U','2026-07-06 23:51:36.795554');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `factura`
--

DROP TABLE IF EXISTS `factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `factura` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tipo` varchar(10) NOT NULL,
  `numero_factura` varchar(20) NOT NULL,
  `fecha_emision` datetime(6) NOT NULL,
  `cantidad` int unsigned NOT NULL,
  `subtotal` decimal(12,2) NOT NULL,
  `iva` decimal(12,2) NOT NULL,
  `total` decimal(12,2) NOT NULL,
  `estado_pago` varchar(10) NOT NULL,
  `metodo_pago` varchar(20) DEFAULT NULL,
  `fecha_pago` datetime(6) DEFAULT NULL,
  `compra_id` bigint DEFAULT NULL,
  `orden_servicio_id` bigint DEFAULT NULL,
  `producto_id` bigint DEFAULT NULL,
  `comprobante_pago` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero_factura` (`numero_factura`),
  UNIQUE KEY `compra_id` (`compra_id`),
  KEY `factura_orden_servicio_id_35d209fc_fk_orden_servicio_id` (`orden_servicio_id`),
  KEY `factura_producto_id_8e907400_fk_producto_id` (`producto_id`),
  CONSTRAINT `factura_compra_id_d41cea05_fk_compra_id` FOREIGN KEY (`compra_id`) REFERENCES `compra` (`id`),
  CONSTRAINT `factura_orden_servicio_id_35d209fc_fk_orden_servicio_id` FOREIGN KEY (`orden_servicio_id`) REFERENCES `orden_servicio` (`id`),
  CONSTRAINT `factura_producto_id_8e907400_fk_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`),
  CONSTRAINT `factura_chk_1` CHECK ((`cantidad` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factura`
--

LOCK TABLES `factura` WRITE;
/*!40000 ALTER TABLE `factura` DISABLE KEYS */;
INSERT INTO `factura` VALUES (1,'COMPRA','433324324','2026-06-20 19:01:57.816571',1,6700000.00,0.00,6700000.00,'Pagada','TarjetaDebito','2026-06-20 19:02:06.823954',1,NULL,NULL,NULL),(2,'COMPRA','764544','2026-06-20 20:06:15.577383',1,7670000.00,0.00,7670000.00,'Pendiente',NULL,NULL,2,NULL,NULL,NULL),(3,'SERVICIO','FAC-0003','2026-06-22 12:33:04.559395',1,390000.00,0.00,390000.00,'Pagada','Nequi','2026-06-22 12:33:38.794902',NULL,1,NULL,'facturas_comprobantes/taller-2.jpeg'),(4,'PRODUCTO','FAC-0004','2026-06-23 00:02:45.172006',1,0.00,0.00,8400000.00,'Pagada','Nequi','2026-06-23 00:03:20.060059',NULL,1,NULL,'facturas_comprobantes/0eb1df56-44e7-4881-8d84-a02925551ac0.png');
/*!40000 ALTER TABLE `factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marca`
--

DROP TABLE IF EXISTS `marca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marca` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `categoria` varchar(10) NOT NULL,
  `pais_origen` varchar(50) DEFAULT NULL,
  `logo` varchar(100) DEFAULT NULL,
  `descripcion` longtext,
  `estado` tinyint(1) NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marca`
--

LOCK TABLES `marca` WRITE;
/*!40000 ALTER TABLE `marca` DISABLE KEYS */;
INSERT INTO `marca` VALUES (1,'chevrolet','AUTO','Arabia Saudita','','la mejor marca de la historita',1,'2026-06-20 18:12:58.416336'),(2,'MICHELLIN','REPUESTO','Argentina','','LLANTAS LAS MEJORICTAS',1,'2026-06-20 18:52:48.055756'),(3,'aceite 3 tiempos','REPUESTO','Australia','','aceite para carro',1,'2026-06-20 20:03:39.786519');
/*!40000 ALTER TABLE `marca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notificacion`
--

DROP TABLE IF EXISTS `notificacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notificacion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tipo` varchar(50) NOT NULL,
  `origen` varchar(10) NOT NULL,
  `titulo` varchar(150) NOT NULL,
  `mensaje` longtext NOT NULL,
  `leido` tinyint(1) NOT NULL,
  `fecha` date NOT NULL,
  `vehiculo_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `notificacion_vehiculo_id_eeb53247_fk_vehiculo_id` (`vehiculo_id`),
  CONSTRAINT `notificacion_vehiculo_id_eeb53247_fk_vehiculo_id` FOREIGN KEY (`vehiculo_id`) REFERENCES `vehiculo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notificacion`
--

LOCK TABLES `notificacion` WRITE;
/*!40000 ALTER TABLE `notificacion` DISABLE KEYS */;
INSERT INTO `notificacion` VALUES (1,'Alerta','SISTEMA','Stock CRITICO â€” LLANTAS','El producto \'LLANTAS\' tiene 0 unidades. Minimo recomendado: 1.',1,'2026-06-20',NULL),(2,'Alerta','SISTEMA','Stock CRITICO â€” uno carrin','El producto \'uno carrin\' tiene 0 unidades. Minimo recomendado: 34.',1,'2026-06-20',NULL),(3,'Alerta','SISTEMA','Stock BAJO â€” uno carrin','Stock BAJO: \'uno carrin\' tiene 34 unidades. Minimo: 34.',1,'2026-06-20',NULL);
/*!40000 ALTER TABLE `notificacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orden_servicio`
--

DROP TABLE IF EXISTS `orden_servicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orden_servicio` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha` datetime(6) NOT NULL,
  `km_actual` int NOT NULL,
  `estado` varchar(20) NOT NULL,
  `observaciones` longtext,
  `empleado_id` bigint DEFAULT NULL,
  `vehiculo_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orden_servicio_vehiculo_id_1f8a455d_fk_vehiculo_id` (`vehiculo_id`),
  KEY `orden_servicio_empleado_id_e6e8f574_fk_usuario_sistema_id` (`empleado_id`),
  CONSTRAINT `orden_servicio_empleado_id_e6e8f574_fk_usuario_sistema_id` FOREIGN KEY (`empleado_id`) REFERENCES `usuario_sistema` (`id`),
  CONSTRAINT `orden_servicio_vehiculo_id_1f8a455d_fk_vehiculo_id` FOREIGN KEY (`vehiculo_id`) REFERENCES `vehiculo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orden_servicio`
--

LOCK TABLES `orden_servicio` WRITE;
/*!40000 ALTER TABLE `orden_servicio` DISABLE KEYS */;
INSERT INTO `orden_servicio` VALUES (1,'2026-06-20 19:13:29.224707',56000,'Terminado',NULL,3,1);
/*!40000 ALTER TABLE `orden_servicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orden_servicio_detalle`
--

DROP TABLE IF EXISTS `orden_servicio_detalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orden_servicio_detalle` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `precio_mano_obra` decimal(12,2) NOT NULL,
  `orden_id` bigint NOT NULL,
  `tipo_servicio_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `orden_servicio_detalle_orden_id_tipo_servicio_id_5f1a29fc_uniq` (`orden_id`,`tipo_servicio_id`),
  KEY `orden_servicio_detal_tipo_servicio_id_43136163_fk_tipo_serv` (`tipo_servicio_id`),
  CONSTRAINT `orden_servicio_detal_tipo_servicio_id_43136163_fk_tipo_serv` FOREIGN KEY (`tipo_servicio_id`) REFERENCES `tipo_servicio` (`id`),
  CONSTRAINT `orden_servicio_detalle_orden_id_7cb4619f_fk_orden_servicio_id` FOREIGN KEY (`orden_id`) REFERENCES `orden_servicio` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orden_servicio_detalle`
--

LOCK TABLES `orden_servicio_detalle` WRITE;
/*!40000 ALTER TABLE `orden_servicio_detalle` DISABLE KEYS */;
INSERT INTO `orden_servicio_detalle` VALUES (2,40000.00,1,2);
/*!40000 ALTER TABLE `orden_servicio_detalle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` longtext,
  `precio` decimal(10,2) NOT NULL,
  `stock` int unsigned NOT NULL,
  `stock_minimo` int unsigned NOT NULL,
  `codigo` varchar(20) NOT NULL,
  `unidad_medida` varchar(5) NOT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `estado` tinyint(1) NOT NULL,
  `marca_id` bigint NOT NULL,
  `proveedor_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `codigo` (`codigo`),
  KEY `producto_marca_id_2793ee53_fk_marca_id` (`marca_id`),
  KEY `producto_proveedor_id_a09ce3bf_fk_proveedor_id` (`proveedor_id`),
  CONSTRAINT `producto_marca_id_2793ee53_fk_marca_id` FOREIGN KEY (`marca_id`) REFERENCES `marca` (`id`),
  CONSTRAINT `producto_proveedor_id_a09ce3bf_fk_proveedor_id` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor` (`id`),
  CONSTRAINT `producto_chk_1` CHECK ((`stock` >= 0)),
  CONSTRAINT `producto_chk_2` CHECK ((`stock_minimo` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (1,'LLANTAS','EFEWRER',700000.00,11,1,'344335','PAR','',1,2,NULL),(2,'uno carrin','ergregregregre',350000.00,34,34,'43254322','ML','',1,3,NULL);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `nit` varchar(20) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `direccion` varchar(150) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nit` (`nit`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
INSERT INTO `proveedor` VALUES (1,'LLANTITAS','434356565','+573466565','AQUITANIA',0),(2,'aceites sas','435435766','+573445456566','tunja',0);
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seguimiento_mantenimiento`
--

DROP TABLE IF EXISTS `seguimiento_mantenimiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seguimiento_mantenimiento` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `km_al_momento` int NOT NULL,
  `km_proximo_mantenimiento` int DEFAULT NULL,
  `fecha_proximo_mantenimiento` date DEFAULT NULL,
  `estado` varchar(15) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `observaciones` longtext,
  `fecha_creacion` datetime(6) NOT NULL,
  `fecha_actualizacion` datetime(6) NOT NULL,
  `orden_servicio_id` bigint DEFAULT NULL,
  `tipo_servicio_id` bigint DEFAULT NULL,
  `vehiculo_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `seguimiento_mantenim_orden_servicio_id_b19382b4_fk_orden_ser` (`orden_servicio_id`),
  KEY `seguimiento_mantenim_tipo_servicio_id_3a1d9c73_fk_tipo_serv` (`tipo_servicio_id`),
  KEY `seguimiento_mantenimiento_vehiculo_id_4de7b801_fk_vehiculo_id` (`vehiculo_id`),
  CONSTRAINT `seguimiento_mantenim_orden_servicio_id_b19382b4_fk_orden_ser` FOREIGN KEY (`orden_servicio_id`) REFERENCES `orden_servicio` (`id`),
  CONSTRAINT `seguimiento_mantenim_tipo_servicio_id_3a1d9c73_fk_tipo_serv` FOREIGN KEY (`tipo_servicio_id`) REFERENCES `tipo_servicio` (`id`),
  CONSTRAINT `seguimiento_mantenimiento_vehiculo_id_4de7b801_fk_vehiculo_id` FOREIGN KEY (`vehiculo_id`) REFERENCES `vehiculo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seguimiento_mantenimiento`
--

LOCK TABLES `seguimiento_mantenimiento` WRITE;
/*!40000 ALTER TABLE `seguimiento_mantenimiento` DISABLE KEYS */;
INSERT INTO `seguimiento_mantenimiento` VALUES (1,30000,35000,'2026-12-03','Pendiente',0,'Creado automÃ¡ticamente desde Orden #1. Km al momento: 30,000. PrÃ³ximo cambio a los 35,000 km (5,000 km restantes). Uso del vehÃ­culo: Uso bajo (ciudad, poco uso) (~30 km/dÃ­a, cambio cada 5,000 km). Estimado: 166 dÃ­as.','2026-06-20 19:13:29.301220','2026-06-20 19:13:29.301256',1,2,1),(2,56000,60000,'2026-10-31','Pendiente',1,'Creado automÃ¡ticamente desde Orden #1. Km al momento: 56,000. PrÃ³ximo cambio a los 60,000 km (4,000 km restantes). Uso del vehÃ­culo: Uso bajo (ciudad, poco uso) (~30 km/dÃ­a, cambio cada 5,000 km). Estimado: 133 dÃ­as.','2026-06-20 20:11:55.449328','2026-06-20 20:11:55.449364',1,2,1);
/*!40000 ALTER TABLE `seguimiento_mantenimiento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_servicio`
--

DROP TABLE IF EXISTS `tipo_servicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_servicio` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` longtext,
  `precio_mano_obra` decimal(12,2) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `requiere_seguimiento` tinyint(1) NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `fecha_actualizacion` datetime(6) NOT NULL,
  `requiere_productos` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_servicio`
--

LOCK TABLES `tipo_servicio` WRITE;
/*!40000 ALTER TABLE `tipo_servicio` DISABLE KEYS */;
INSERT INTO `tipo_servicio` VALUES (1,'CAMBIO DE LLANTAS','SE HIZO CMABIO DE LLANTAS',600000.00,1,0,'2026-06-20 18:51:41.702377','2026-06-20 18:51:41.702534',0),(2,'cambio de aceite','gregregerg',40000.00,1,1,'2026-06-20 19:12:22.352627','2026-06-20 19:12:22.352682',0),(3,'revision de radiador','se realizo revision para su posterior cambio',30000.00,1,0,'2026-06-20 19:40:40.561906','2026-06-20 19:40:40.561947',0);
/*!40000 ALTER TABLE `tipo_servicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_sistema`
--

DROP TABLE IF EXISTS `usuario_sistema`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario_sistema` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `tipo_documento` varchar(3) NOT NULL,
  `cedula` varchar(20) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `cargo` varchar(20) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `foto` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `cedula` (`cedula`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_sistema`
--

LOCK TABLES `usuario_sistema` WRITE;
/*!40000 ALTER TABLE `usuario_sistema` DISABLE KEYS */;
INSERT INTO `usuario_sistema` VALUES (1,'pbkdf2_sha256$1200000$vpdbidDHfU9i59CMI0MPYZ$mqCE+yIC7oeYUu2QoADdwblyepkJHQLyn/8Md6b9L2o=','2026-06-13 22:48:00.394831',1,'yuliana','','','pedraza123@gmail.com',1,1,'2026-06-13 19:03:11.392643','CC',NULL,NULL,'ADMIN',1,''),(2,'pbkdf2_sha256$1200000$kFINT7U0Dxs2pHacXRDoKI$uTuSudLy7uv9g6N2DVY2swr4K7saiRMmiIh7hPq88yI=','2026-06-14 19:56:26.736848',0,'yuyus123','Yuliana','Pedraza','pedrazayuliana198@gmail.com',0,1,'2026-06-14 19:19:10.943326','CC','1054284348','3044354414','ADMIN',1,''),(3,'pbkdf2_sha256$1200000$R3lUVHYKZXZcL2y5420Usx$VWAukTTKs+WGFeVPTCoYHFHt1J38L3Upx9JCX+wbdHw=',NULL,0,'manupe','Manuel','Sotaquira','manupe@gmail.com',0,1,'2026-06-20 18:50:50.614643','CC','7647598458','3084384834','MECANICO',1,''),(4,'pbkdf2_sha256$1200000$MyFmqmlMheDNdlsHybtFwM$29wcsK8yFnp4O+UlwxiKgYZa8LaCvcnRT9RkHeVKJ/E=',NULL,1,'angiangie','','','jshdshd@gmail.com',1,1,'2026-06-22 01:25:15.655861','CC',NULL,NULL,'ADMIN',1,''),(5,'pbkdf2_sha256$1200000$CM2tbibgMcj7evoS59E4DA$Dpa0BPthLuaFbmYEXVbGjPKgAxrrck52Eo5rXw7IyY8=','2026-06-22 12:11:16.426834',1,'pedraza','','','shdjsahd@gamil.com',1,1,'2026-06-22 12:10:51.741437','CC',NULL,NULL,'ADMIN',1,'');
/*!40000 ALTER TABLE `usuario_sistema` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_sistema_groups`
--

DROP TABLE IF EXISTS `usuario_sistema_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario_sistema_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuariosistema_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_sistema_groups_usuariosistema_id_group_id_22de142c_uniq` (`usuariosistema_id`,`group_id`),
  KEY `usuario_sistema_groups_group_id_3639004b_fk_auth_group_id` (`group_id`),
  CONSTRAINT `usuario_sistema_grou_usuariosistema_id_dcbe40e6_fk_usuario_s` FOREIGN KEY (`usuariosistema_id`) REFERENCES `usuario_sistema` (`id`),
  CONSTRAINT `usuario_sistema_groups_group_id_3639004b_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_sistema_groups`
--

LOCK TABLES `usuario_sistema_groups` WRITE;
/*!40000 ALTER TABLE `usuario_sistema_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario_sistema_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_sistema_user_permissions`
--

DROP TABLE IF EXISTS `usuario_sistema_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario_sistema_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuariosistema_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_sistema_user_per_usuariosistema_id_permis_4d7098b0_uniq` (`usuariosistema_id`,`permission_id`),
  KEY `usuario_sistema_user_permission_id_408f8403_fk_auth_perm` (`permission_id`),
  CONSTRAINT `usuario_sistema_user_permission_id_408f8403_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `usuario_sistema_user_usuariosistema_id_1619ab8b_fk_usuario_s` FOREIGN KEY (`usuariosistema_id`) REFERENCES `usuario_sistema` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_sistema_user_permissions`
--

LOCK TABLES `usuario_sistema_user_permissions` WRITE;
/*!40000 ALTER TABLE `usuario_sistema_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario_sistema_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehiculo`
--

DROP TABLE IF EXISTS `vehiculo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehiculo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `placa` varchar(10) NOT NULL,
  `modelo` varchar(50) NOT NULL,
  `km_ultimo_servicio` int DEFAULT NULL,
  `tipo_uso` varchar(10) NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `fecha_actualizacion` datetime(6) NOT NULL,
  `cliente_id` bigint NOT NULL,
  `marca_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `placa` (`placa`),
  KEY `vehiculo_cliente_id_967a1a09_fk_cliente_id` (`cliente_id`),
  KEY `vehiculo_marca_id_4c86da34_fk_marca_id` (`marca_id`),
  CONSTRAINT `vehiculo_cliente_id_967a1a09_fk_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `cliente` (`id`),
  CONSTRAINT `vehiculo_marca_id_4c86da34_fk_marca_id` FOREIGN KEY (`marca_id`) REFERENCES `marca` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehiculo`
--

LOCK TABLES `vehiculo` WRITE;
/*!40000 ALTER TABLE `vehiculo` DISABLE KEYS */;
INSERT INTO `vehiculo` VALUES (1,'DFR123','2025',NULL,'BAJO','2026-06-20 18:24:14.446013','2026-06-20 18:24:14.446057',1,1);
/*!40000 ALTER TABLE `vehiculo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-22 19:05:42
