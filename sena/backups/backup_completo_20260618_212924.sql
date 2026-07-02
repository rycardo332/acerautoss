-- Respaldo de acerautos_proyecto
-- Fecha: 2026-06-18 21:29:25
-- Tipo: Completo (Estructura + Datos)

-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: acerautos_proyecto
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
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',2,'add_permission'),(2,'Can change permission',2,'change_permission'),(3,'Can delete permission',2,'delete_permission'),(4,'Can view permission',2,'view_permission'),(5,'Can add group',1,'add_group'),(6,'Can change group',1,'change_group'),(7,'Can delete group',1,'delete_group'),(8,'Can view group',1,'view_group'),(9,'Can add content type',3,'add_contenttype'),(10,'Can change content type',3,'change_contenttype'),(11,'Can delete content type',3,'delete_contenttype'),(12,'Can view content type',3,'view_contenttype'),(13,'Can add session',4,'add_session'),(14,'Can change session',4,'change_session'),(15,'Can delete session',4,'delete_session'),(16,'Can view session',4,'view_session'),(17,'Can add caja',5,'add_caja'),(18,'Can change caja',5,'change_caja'),(19,'Can delete caja',5,'delete_caja'),(20,'Can view caja',5,'view_caja'),(21,'Can add cliente',6,'add_cliente'),(22,'Can change cliente',6,'change_cliente'),(23,'Can delete cliente',6,'delete_cliente'),(24,'Can view cliente',6,'view_cliente'),(25,'Can add compra',8,'add_compra'),(26,'Can change compra',8,'change_compra'),(27,'Can delete compra',8,'delete_compra'),(28,'Can view compra',8,'view_compra'),(29,'Can add marca',11,'add_marca'),(30,'Can change marca',11,'change_marca'),(31,'Can delete marca',11,'delete_marca'),(32,'Can view marca',11,'view_marca'),(33,'Can add proveedor',16,'add_proveedor'),(34,'Can change proveedor',16,'change_proveedor'),(35,'Can delete proveedor',16,'delete_proveedor'),(36,'Can view proveedor',16,'view_proveedor'),(37,'Can add Tipo de Servicio',18,'add_tiposervicio'),(38,'Can change Tipo de Servicio',18,'change_tiposervicio'),(39,'Can delete Tipo de Servicio',18,'delete_tiposervicio'),(40,'Can view Tipo de Servicio',18,'view_tiposervicio'),(41,'Can add Usuario del Sistema',19,'add_usuariosistema'),(42,'Can change Usuario del Sistema',19,'change_usuariosistema'),(43,'Can delete Usuario del Sistema',19,'delete_usuariosistema'),(44,'Can view Usuario del Sistema',19,'view_usuariosistema'),(45,'Can add orden servicio',13,'add_ordenservicio'),(46,'Can change orden servicio',13,'change_ordenservicio'),(47,'Can delete orden servicio',13,'delete_ordenservicio'),(48,'Can view orden servicio',13,'view_ordenservicio'),(49,'Can add producto',15,'add_producto'),(50,'Can change producto',15,'change_producto'),(51,'Can delete producto',15,'delete_producto'),(52,'Can view producto',15,'view_producto'),(53,'Can add factura',10,'add_factura'),(54,'Can change factura',10,'change_factura'),(55,'Can delete factura',10,'delete_factura'),(56,'Can view factura',10,'view_factura'),(57,'Can add detalle orden producto',9,'add_detalleordenproducto'),(58,'Can change detalle orden producto',9,'change_detalleordenproducto'),(59,'Can delete detalle orden producto',9,'delete_detalleordenproducto'),(60,'Can view detalle orden producto',9,'view_detalleordenproducto'),(61,'Can add Detalle de Servicio en Orden',14,'add_ordenserviciodetalle'),(62,'Can change Detalle de Servicio en Orden',14,'change_ordenserviciodetalle'),(63,'Can delete Detalle de Servicio en Orden',14,'delete_ordenserviciodetalle'),(64,'Can view Detalle de Servicio en Orden',14,'view_ordenserviciodetalle'),(65,'Can add vehiculo',20,'add_vehiculo'),(66,'Can change vehiculo',20,'change_vehiculo'),(67,'Can delete vehiculo',20,'delete_vehiculo'),(68,'Can view vehiculo',20,'view_vehiculo'),(69,'Can add Seguimiento de Mantenimiento',17,'add_seguimientomantenimiento'),(70,'Can change Seguimiento de Mantenimiento',17,'change_seguimientomantenimiento'),(71,'Can delete Seguimiento de Mantenimiento',17,'delete_seguimientomantenimiento'),(72,'Can view Seguimiento de Mantenimiento',17,'view_seguimientomantenimiento'),(73,'Can add notificacion',12,'add_notificacion'),(74,'Can change notificacion',12,'change_notificacion'),(75,'Can delete notificacion',12,'delete_notificacion'),(76,'Can view notificacion',12,'view_notificacion'),(77,'Can add compatibilidad producto',7,'add_compatibilidadproducto'),(78,'Can change compatibilidad producto',7,'change_compatibilidadproducto'),(79,'Can delete compatibilidad producto',7,'delete_compatibilidadproducto'),(80,'Can view compatibilidad producto',7,'view_compatibilidadproducto'),(81,'Can add Perfil de Usuario',21,'add_perfilusuario'),(82,'Can change Perfil de Usuario',21,'change_perfilusuario'),(83,'Can delete Perfil de Usuario',21,'delete_perfilusuario'),(84,'Can view Perfil de Usuario',21,'view_perfilusuario'),(85,'Can add log entry',22,'add_logentry'),(86,'Can change log entry',22,'change_logentry'),(87,'Can delete log entry',22,'delete_logentry'),(88,'Can view log entry',22,'view_logentry');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caja`
--

LOCK TABLES `caja` WRITE;
/*!40000 ALTER TABLE `caja` DISABLE KEYS */;
INSERT INTO `caja` VALUES (1,'Compra Factura 123456789',28000.00,'EGRESO','2026-06-19 01:13:46.514403','Proveedores','Efectivo','',NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,'carlos','CC','1020456789','+573107928074','melomolinaricardo@gmail.com'),(2,'julian','CC','1019234567','+573107928075','danielmelomolinamolina@gmail.com');
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
INSERT INTO `compatibilidad_producto` VALUES (1,1,1,1),(2,2,2,1);
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
INSERT INTO `compra` VALUES (1,20,'2026-06-19 01:11:19.000000','123456789','Efectivo',28000.00,'Pagada','2026-06-19 01:13:46.503904','facturas_proveedores/facturas-y-recibos-para-talleres-screenshot_1.png',1,2),(2,20,'2026-06-19 01:17:20.000000','123456788',NULL,20000.00,'Pendiente',NULL,'',2,1);
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
INSERT INTO `detalle_orden_producto` VALUES (1,1,32000.00,1,2);
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
  KEY `django_admin_log_user_id_c564eba6_fk_usuario_sistema_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_usuario_sistema_id` FOREIGN KEY (`user_id`) REFERENCES `usuario_sistema` (`id`),
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
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (22,'admin','logentry'),(5,'app','caja'),(6,'app','cliente'),(7,'app','compatibilidadproducto'),(8,'app','compra'),(9,'app','detalleordenproducto'),(10,'app','factura'),(11,'app','marca'),(12,'app','notificacion'),(13,'app','ordenservicio'),(14,'app','ordenserviciodetalle'),(15,'app','producto'),(16,'app','proveedor'),(17,'app','seguimientomantenimiento'),(18,'app','tiposervicio'),(19,'app','usuariosistema'),(20,'app','vehiculo'),(1,'auth','group'),(2,'auth','permission'),(3,'contenttypes','contenttype'),(4,'sessions','session'),(21,'usuario','perfilusuario');
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2026-06-18 23:57:55.417889'),(2,'contenttypes','0002_remove_content_type_name','2026-06-18 23:57:55.575646'),(3,'auth','0001_initial','2026-06-18 23:57:56.209103'),(4,'auth','0002_alter_permission_name_max_length','2026-06-18 23:57:56.429335'),(5,'auth','0003_alter_user_email_max_length','2026-06-18 23:57:56.447240'),(6,'auth','0004_alter_user_username_opts','2026-06-18 23:57:56.463949'),(7,'auth','0005_alter_user_last_login_null','2026-06-18 23:57:56.477470'),(8,'auth','0006_require_contenttypes_0002','2026-06-18 23:57:56.488868'),(9,'auth','0007_alter_validators_add_error_messages','2026-06-18 23:57:56.499791'),(10,'auth','0008_alter_user_username_max_length','2026-06-18 23:57:56.514599'),(11,'auth','0009_alter_user_last_name_max_length','2026-06-18 23:57:56.529854'),(12,'auth','0010_alter_group_name_max_length','2026-06-18 23:57:56.569818'),(13,'auth','0011_update_proxy_permissions','2026-06-18 23:57:56.580439'),(14,'auth','0012_alter_user_first_name_max_length','2026-06-18 23:57:56.590712'),(15,'app','0001_initial','2026-06-18 23:58:02.968980'),(16,'admin','0001_initial','2026-06-18 23:58:03.335766'),(17,'admin','0002_logentry_remove_auto_add','2026-06-18 23:58:03.360496'),(18,'admin','0003_logentry_add_action_flag_choices','2026-06-18 23:58:03.388126'),(19,'sessions','0001_initial','2026-06-18 23:58:03.472354'),(20,'usuario','0001_initial','2026-06-18 23:58:03.692134');
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
INSERT INTO `django_session` VALUES ('5rs02ccuuwv3rurv4kp9eegj0u9dpabe','.eJxVjDFOxDAQAP-yLXfWeuP4bJf0dPTWer0hhpBIcUKD-Ds66QpoZ0bzDZnPY85n1z23CgksXP6ywvKh613Ud17fNiPbeuytmHtiHrabl63q8vxo_w1m7jMkkImCTpFGqexoIBetWCW--RBocL6oLezUx2ALBRF_U9E4TsKVJ_UIFziXo31y3vWr9batmRfdD-6QgJD8Ff3VxlekhDaNzkSLYcAnxIQIP7_AzUmd:1waOYM:008gjqLh-cQXvo9zv0HzdRNac27LO3HitgeIchTL6p8','2026-07-03 02:01:54.922893');
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero_factura` (`numero_factura`),
  UNIQUE KEY `compra_id` (`compra_id`),
  KEY `factura_orden_servicio_id_35d209fc_fk_orden_servicio_id` (`orden_servicio_id`),
  KEY `factura_producto_id_8e907400_fk_producto_id` (`producto_id`),
  CONSTRAINT `factura_compra_id_d41cea05_fk_compra_id` FOREIGN KEY (`compra_id`) REFERENCES `compra` (`id`),
  CONSTRAINT `factura_orden_servicio_id_35d209fc_fk_orden_servicio_id` FOREIGN KEY (`orden_servicio_id`) REFERENCES `orden_servicio` (`id`),
  CONSTRAINT `factura_producto_id_8e907400_fk_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`),
  CONSTRAINT `factura_chk_1` CHECK ((`cantidad` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factura`
--

LOCK TABLES `factura` WRITE;
/*!40000 ALTER TABLE `factura` DISABLE KEYS */;
INSERT INTO `factura` VALUES (1,'COMPRA','123456789','2026-06-19 01:13:38.589748',1,28000.00,0.00,28000.00,'Pagada','Efectivo','2026-06-19 01:13:46.533363',1,NULL,NULL),(2,'COMPRA','123456788','2026-06-19 01:17:55.325435',1,20000.00,0.00,20000.00,'Pendiente',NULL,NULL,2,NULL,NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marca`
--

LOCK TABLES `marca` WRITE;
/*!40000 ALTER TABLE `marca` DISABLE KEYS */;
INSERT INTO `marca` VALUES (1,'Toyota corolla','AUTO','Japon','marcas_logos/logo.png','',1,'2026-06-19 00:26:02.570663'),(2,'renault clio','AUTO','Francia','marcas_logos/Renault_logo.jpg','',1,'2026-06-19 00:28:09.924298'),(3,'Mobil','REPUESTO','Estados Unidos','marcas_logos/images_2.jpg','aceite vehiculos',1,'2026-06-19 00:42:52.425248'),(4,'castrol','REPUESTO','Reino Unido','marcas_logos/castrol-logo-0.png','',1,'2026-06-19 01:02:31.044193');
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notificacion`
--

LOCK TABLES `notificacion` WRITE;
/*!40000 ALTER TABLE `notificacion` DISABLE KEYS */;
INSERT INTO `notificacion` VALUES (1,'Alerta','SISTEMA','Stock CRITICO â€” Aceite Castrol Edge 5W-40','El producto \'Aceite Castrol Edge 5W-40\' tiene 0 unidades. Minimo recomendado: 10.',1,'2026-06-18',NULL),(2,'Alerta','SISTEMA','Stock CRITICO â€” Aceite Castrol 5W-20','El producto \'Aceite Castrol 5W-20\' tiene 0 unidades. Minimo recomendado: 10.',1,'2026-06-18',NULL);
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
INSERT INTO `orden_servicio` VALUES (1,'2026-06-19 01:19:26.758011',2000,'Pendiente',NULL,2,2);
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orden_servicio_detalle`
--

LOCK TABLES `orden_servicio_detalle` WRITE;
/*!40000 ALTER TABLE `orden_servicio_detalle` DISABLE KEYS */;
INSERT INTO `orden_servicio_detalle` VALUES (1,45000.00,1,1);
/*!40000 ALTER TABLE `orden_servicio_detalle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `perfil_usuario`
--

DROP TABLE IF EXISTS `perfil_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `perfil_usuario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rol` varchar(20) NOT NULL,
  `cedula` varchar(20) NOT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cedula` (`cedula`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `perfil_usuario_user_id_a77a2a33_fk_usuario_sistema_id` FOREIGN KEY (`user_id`) REFERENCES `usuario_sistema` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `perfil_usuario`
--

LOCK TABLES `perfil_usuario` WRITE;
/*!40000 ALTER TABLE `perfil_usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `perfil_usuario` ENABLE KEYS */;
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
INSERT INTO `producto` VALUES (1,'Aceite Castrol Edge 5W-40','Aceite sintÃ©tico para motores modernos de alta exigencia.',38000.00,20,10,'001','LT','productos/images_3.jpg',1,4,NULL),(2,'Aceite Castrol 5W-20','',32000.00,19,10,'002','UND','productos/61wg3ZXgDpL.jpg',1,4,NULL);
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
INSERT INTO `proveedor` VALUES (1,'Distribuidora Automotriz del Llano','9001234561','+573144567890','Carrera 15 # 8-32, Yopal',0),(2,'Repuestos y Lubricantes El Turbo','8002345672','+573209876543','Calle 20 # 12-45, Yopal',0);
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seguimiento_mantenimiento`
--

LOCK TABLES `seguimiento_mantenimiento` WRITE;
/*!40000 ALTER TABLE `seguimiento_mantenimiento` DISABLE KEYS */;
INSERT INTO `seguimiento_mantenimiento` VALUES (1,2000,5000,'2026-08-17','Pendiente',1,'Creado automÃ¡ticamente desde Orden #1. Km al momento: 2,000. PrÃ³ximo cambio a los 5,000 km (3,000 km restantes). Uso del vehÃ­culo: Uso normal (estÃ¡ndar) (~50 km/dÃ­a, cambio cada 5,000 km). Estimado: 60 dÃ­as.','2026-06-19 01:19:26.874663','2026-06-19 01:19:26.874836',1,1,2);
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
  `requiere_productos` tinyint(1) NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `fecha_actualizacion` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_servicio`
--

LOCK TABLES `tipo_servicio` WRITE;
/*!40000 ALTER TABLE `tipo_servicio` DISABLE KEYS */;
INSERT INTO `tipo_servicio` VALUES (1,'Cambio de aceite y filtro','Cambio de aceite y filtro segÃºn especificaciones del fabricante.',45000.00,1,1,1,'2026-06-19 00:35:52.427348','2026-06-19 00:35:52.427418'),(2,'RevisiÃ³n de frenos','nspecciÃ³n completa del sistema de frenado para garantizar seguridad.',50000.00,1,0,1,'2026-06-19 00:37:19.400803','2026-06-19 00:37:19.400837');
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_sistema`
--

LOCK TABLES `usuario_sistema` WRITE;
/*!40000 ALTER TABLE `usuario_sistema` DISABLE KEYS */;
INSERT INTO `usuario_sistema` VALUES (1,'pbkdf2_sha256$1200000$oDiT83YhdXnEv2hA8umLCF$Am68P67+YC6cL1BLyO5mrLHcwxjGa7YZqwvEFSfoUMM=','2026-06-19 00:31:00.202740',1,'Daniel','','','daniel@gmail.com',1,1,'2026-06-18 23:59:25.044283','CC',NULL,NULL,'ADMIN',1,''),(2,'pbkdf2_sha256$1200000$KyQAb8W6W0lf045dOV7hm8$/JgZu35G7y3wRUClN5LiFadMuRIxwIZYaRsT+pYeLzE=','2026-06-19 00:10:08.369469',0,'Ricardo','Daniel','melo','ewwe@gmail.com',0,1,'2026-06-19 00:04:03.383949','CC','1054283661','3107928074','MECANICO',1,'usuarios/fotos/perfil.jpg');
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehiculo`
--

LOCK TABLES `vehiculo` WRITE;
/*!40000 ALTER TABLE `vehiculo` DISABLE KEYS */;
INSERT INTO `vehiculo` VALUES (1,'ABC123','2026','BAJO','2026-06-19 00:26:28.838160','2026-06-19 00:26:28.838338',1,1),(2,'QWE123','2020','NORMAL','2026-06-19 00:28:37.046817','2026-06-19 00:28:37.046863',2,2);
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

-- Dump completed on 2026-06-18 21:29:25
