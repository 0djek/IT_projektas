-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 11, 2022 at 03:20 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `it_maistas`
--

-- --------------------------------------------------------

--
-- Table structure for table `ingredient`
--

CREATE TABLE `ingredient` (
  `ingredient_id` char(36) NOT NULL COMMENT 'Id of the ingredient (char 36)',
  `ingredient_title` varchar(40) NOT NULL COMMENT 'Title for the ingredient (varchar 40)',
  `ingredient_seo_title` varchar(40) NOT NULL COMMENT 'Title for the ingredient, which will be used in urls (varchar 40)',
  `ingredient_unit` varchar(15) NOT NULL COMMENT 'Default unit for the ingredient (varchar 15)',
  `ingredient_date_created` datetime NOT NULL COMMENT 'When was the ingredient last created (datetime)',
  `fk_ingredient_user_id` char(40) NOT NULL COMMENT 'What user created this ingredient (char 40)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Holds all the ingredients in the database. Can add only by admin, but recipe_creators have the ability to suggest new recipes';

--
-- Dumping data for table `ingredient`
--

INSERT INTO `ingredient` (`ingredient_id`, `ingredient_title`, `ingredient_seo_title`, `ingredient_unit`, `ingredient_date_created`, `fk_ingredient_user_id`) VALUES
('04b47093-1898-404e-9f7a-92f8d8cfa80a', 'Bananai', 'bananai', 'g.', '2021-11-30 22:29:35', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('08e5ff11-9a25-4072-84b5-7b3872228ac9', 'Špinatai', 'spinatai', 'g.', '2021-11-30 22:27:35', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('0ad5d648-1081-4897-b8c3-fdc019912529', 'Burokėliai', 'burokeliai', 'g.', '2021-11-30 22:28:43', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('0dd882d5-980f-4e48-9f71-b49d7ae6128c', 'Paprika', 'paprika', 'g.', '2022-01-11 00:11:43', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('15d1da06-1a42-424a-9a83-dffe643c399d', 'Rūkyta dešra', 'rukytadesra', 'g.', '2021-11-30 22:33:12', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('216470ed-dd2e-4989-aab9-de25dec950e6', 'Mandarinai', 'mandarinai', 'g.', '2021-11-30 22:29:28', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('28c4aab4-6c9f-468a-91bf-b28e3f8d148e', 'Avietės', 'avietes', 'g.', '2021-11-30 22:30:53', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('2a0a768d-f811-43db-b7e6-5ef61508a866', 'Citrinos', 'citrinos', 'g.', '2021-11-30 22:29:57', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('2a56dfe8-766d-4396-a342-e7e71a271c6f', 'Svogūnai', 'svogunai', 'g.', '2021-11-30 21:36:55', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('3d47d65a-e182-4cda-bff8-3b532b696641', 'Salotos', 'salotos', 'g.', '2021-11-30 22:29:18', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('3e4c1c57-7217-4ed5-b06d-1d4f65a6434d', 'Varškė', 'varske', 'g.', '2021-11-30 22:32:36', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('41dec2f6-20d1-465d-a974-c09ed04174ac', 'Imbiero šaknys', 'imbierosaknys', 'g.', '2021-11-30 22:31:11', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('48cb3e14-dc10-4556-8eee-86ada0217062', 'Slyviniai pomidorai', 'slyviniai-pomidorai', 'g.', '2021-11-30 22:28:34', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('4a37f948-5a6d-438a-aee6-42dbc5f18501', 'Česnakai', 'cesnakai', 'g.', '2021-11-30 21:45:07', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('51cddc9e-87f6-40d6-9010-003cd2802bd6', 'Dešrelės', 'desreles', 'g.', '2021-11-30 22:33:33', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('55216ad5-853f-42d9-b8ef-235cfd319da5', 'Avižiniai dribsniai', 'aviziniaidribsniai', 'g.', '2021-11-30 22:33:47', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('5810d9e4-f0e6-494b-9d6a-49a732ddd2f0', 'Manai', 'manai', 'g.', '2021-11-30 22:33:52', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('58da1554-9cd5-4e6d-9734-f4ac91ac9756', 'Kopūstas', 'kopustas', 'g.', '2021-11-30 21:36:35', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('5e025f5a-e32d-4880-8651-337e16b74baa', 'Grietinėlė', 'grietinele', 'g.', '2021-11-30 22:31:51', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('616bc025-94c4-48f3-b5fa-a2e27b6f6d39', 'Mocarela', 'mocarela', 'g.', '2021-11-30 22:32:28', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('692a4e78-7838-4343-9fa9-1559361ff6e7', 'Obuoliai', 'obuoliai', 'g.', '2021-11-30 22:30:03', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('697da7f3-44ae-4df4-a2f5-32b7ea7f891a', 'Žuvis', 'zuvis', 'g.', '2021-11-30 22:33:04', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('7fe61f00-38c0-491e-a132-07c4dadea43a', 'Grikiai', 'grikiai', 'g.', '2021-11-30 22:33:57', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('814c0386-440a-46a2-941d-288d6ec31889', 'Morkos', 'morkos', 'g.', '2021-11-30 22:29:00', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('85addccd-641f-46af-840e-d1a5413251d6', 'Šilauogės', 'silauoges', 'g.', '2021-11-30 22:30:45', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('860eb06b-e6a0-49fb-b3f2-283c0352f572', 'Kiaušiniai', 'kiausiniai', 'g.', '2021-11-30 22:31:21', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('8a126e63-d0a3-4381-8e3f-9585a009e64f', 'Apelsinai', 'apelsinai', 'g.', '2021-11-30 22:29:22', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('8d1c6321-5d5b-4ff2-a000-b26cfcfd7fa4', 'Jautiena', 'jautiena', 'g.', '2021-11-30 22:32:50', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('9196ddf0-ef79-450f-9974-db760ddb3e3a', 'Grietinė', 'grietine', 'g.', '2021-11-30 22:31:38', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('972d7436-1d4a-4b64-9a88-0e7ce518236a', 'Sūris', 'suris', 'g.', '2021-11-30 22:32:22', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('980d3cff-6c05-48e3-9d6e-540653cffa22', 'Greipfrutai', 'greipfrutai', 'g.', '2021-11-30 22:29:51', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('9990889b-2e05-4598-bfa0-bf0ebfab5c53', 'Trešnės', 'tresnes', 'g.', '2021-11-30 22:30:26', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('9af265ac-6f4b-4c5b-bf62-0266f2635e63', 'Ridikėliai', 'ridikeliai', 'g.', '2021-11-30 22:28:53', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('a432d6d4-be03-4c42-b8b3-9748d139ad22', 'Ryžiai', 'ryziai', 'g.', '2021-11-30 22:34:05', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('b842884a-a221-40e2-aa9c-169dbaf77857', 'Vyšnios', 'vysnios', 'g.', '2021-11-30 22:30:18', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('b8ea895e-3257-4bed-811f-4db9c6e6f716', 'Kiauliena', 'kiauliena', 'g.', '2021-11-30 22:32:44', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('ba4fa5cf-c6be-407e-8290-0341dd41b230', 'Pienas', 'pienas', 'g.', '2021-11-30 22:31:28', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('be2a04ea-1f53-4388-ba40-8fadeded249c', 'Kruopos', 'kruopos', 'g.', '2021-11-30 22:33:38', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('c475e073-7e45-44c2-b597-e465299f22b0', 'Mangai', 'mangai', 'g.', '2021-11-30 22:30:10', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('c7680892-e0ea-4311-af9e-a3419306c30d', 'Persimonai', 'persimonai', 'g.', '2021-11-30 22:29:43', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('c9f1daff-df86-4f8b-b665-47e4d78db91e', 'Vynuogės', 'vynuoges', 'g.', '2021-11-30 22:30:36', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('cc2df8e3-50ad-4af0-8f24-589965848315', 'Cukinijos', 'cukinijos', 'g.', '2021-11-30 22:29:06', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('e0c5698c-8821-4425-9327-6800907ec393', 'Faršas', 'farsas', 'g.', '2021-11-30 22:33:21', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('e17b5738-1830-49f5-86a5-d7a7b7610744', 'Krapai', 'krapai', 'g.', '2021-11-30 22:28:01', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('e46f9715-9e10-43c5-af92-3b0ace2fcd6e', 'Pomidorai', 'pomidorai', 'g.', '2021-11-30 22:28:20', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('e797507e-c1a6-4ef1-aac7-6c25aaea8bad', 'Krevetės', 'krevetes', 'g.', '2021-11-30 22:32:57', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('ee742a5a-eb22-4130-bef9-f1d08d46d208', 'Pievagrybiai', 'pievagrybiai', 'g.', '2021-11-30 22:27:44', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('f98e2851-326d-4f0c-bf37-20802398cfaf', 'Svogūnų laiškai', 'svogunulaiskai', 'g', '2021-11-30 22:27:18', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('fed36344-0a47-496e-b531-eea9bcb65698', 'Bulvės', 'bulves', 'g.', '2021-11-30 22:27:04', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523');

-- --------------------------------------------------------

--
-- Table structure for table `recipe`
--

CREATE TABLE `recipe` (
  `recipe_id` char(36) NOT NULL COMMENT 'The id of the recipe (GUID char 36)',
  `recipe_title` varchar(40) NOT NULL COMMENT 'Ttile for the specific recipe (varchar 40)',
  `recipe_seo_title` varchar(40) NOT NULL COMMENT 'Ttile for the specific recipe to use in urls (varchar 40)',
  `recipe_description` text NOT NULL COMMENT 'Description for the recipe (text)',
  `recipe_desciption_exerpt` text NOT NULL COMMENT 'Short description for the recipe to view in overviews (text)',
  `recipe_date_created` datetime NOT NULL DEFAULT curdate() COMMENT 'When was the recipe created (datetime)',
  `fk_recipe_user_id` char(36) NOT NULL COMMENT 'Shows what user created this recipe (GUID, char 36)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='One recipe can be created.';

--
-- Dumping data for table `recipe`
--

INSERT INTO `recipe` (`recipe_id`, `recipe_title`, `recipe_seo_title`, `recipe_description`, `recipe_desciption_exerpt`, `recipe_date_created`, `fk_recipe_user_id`) VALUES
('4216f45a-3d22-428d-b013-6e93a75f6a9f', 'Ryžiai su  kepsnių ', 'Ryziaisukepsniu', 'Ryžiai su kepsniu', 'Ryžiai su kepsniu', '2021-12-21 22:22:24', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('59d30edd-9ebc-4ef8-9646-020cf3b1479b', 'Salotos', 'Salotos', 'Paprastos daržovių salotos. ', 'Paprastos daržovių salotos be priedų ', '2021-12-21 22:08:40', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('90980da0-b845-4566-a590-14d8e5ebf59d', 'Vaisių salotos', 'Vaisiusalotos', 'Įvairių vaisių salotos. ', 'Įvairių vaisių salotos. ', '2021-12-21 22:14:40', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('bc66cb92-1025-4b81-8b71-cb069d41967b', 'Spagečiai su sūriu ir grietinėle', 'Spageciaisusuriuirgrietinele', 'Spagečiai su sūriu ir grietinėle', 'Spagečiai su sūriu ir grietinėle', '2021-12-21 22:29:27', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('c5e301ad-8bca-4602-bfdd-20aef981bc38', 'Sūrio lazdelės', 'Suriolazdeles', 'Keptos sūrio lazdelės ivoliotos  ​trupiniuose', 'Keptos sūrio lazdelės ivoliotos  trupiniuose', '2021-12-21 21:57:44', '0e5194c1-532b-42d5-9dfe-c093c51e4f05');

-- --------------------------------------------------------

--
-- Table structure for table `recipe_ingredient`
--

CREATE TABLE `recipe_ingredient` (
  `recipe_ingredient_id` char(36) NOT NULL COMMENT 'Id for the ingredient, which will be used in the recipe (char 36)',
  `recipe_ingredient_quantity` decimal(5,2) UNSIGNED NOT NULL COMMENT 'How many of these will we need (double 5.2)',
  `fk_recipe_ingredient_recipe_id` char(36) NOT NULL COMMENT 'In which recipe is this ingredient used (char 36)',
  `fk_recipe_ingredient_ingredient_id` char(36) NOT NULL COMMENT 'char 36'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `recipe_ingredient`
--

INSERT INTO `recipe_ingredient` (`recipe_ingredient_id`, `recipe_ingredient_quantity`, `fk_recipe_ingredient_recipe_id`, `fk_recipe_ingredient_ingredient_id`) VALUES
('15d099fb-e2ea-4c29-af51-865fe24987da', '100.00', 'c5e301ad-8bca-4602-bfdd-20aef981bc38', '55216ad5-853f-42d9-b8ef-235cfd319da5'),
('6fd7876a-3791-45f0-97d8-08300a6993bc', '100.00', 'bc66cb92-1025-4b81-8b71-cb069d41967b', '5e025f5a-e32d-4880-8651-337e16b74baa'),
('83adbe9e-ff1d-457a-b045-a01232528f38', '50.00', '4216f45a-3d22-428d-b013-6e93a75f6a9f', 'e17b5738-1830-49f5-86a5-d7a7b7610744'),
('b1896da3-a7cc-43f3-b498-43cb1331e874', '30.00', '90980da0-b845-4566-a590-14d8e5ebf59d', '85addccd-641f-46af-840e-d1a5413251d6'),
('b73c4d04-d8c4-453e-8bba-57ed0d61a638', '60.00', '59d30edd-9ebc-4ef8-9646-020cf3b1479b', '9196ddf0-ef79-450f-9974-db760ddb3e3a'),
('f3de6e75-e671-4a28-82a5-cc04e0671421', '100.00', 'bc66cb92-1025-4b81-8b71-cb069d41967b', '972d7436-1d4a-4b64-9a88-0e7ce518236a');

-- --------------------------------------------------------

--
-- Table structure for table `recipe_step`
--

CREATE TABLE `recipe_step` (
  `recipe_step_id` char(36) NOT NULL COMMENT 'Id for the recipe (GUID char 36)',
  `recipe_step_title` varchar(40) NOT NULL COMMENT 'Title for the recipe (varchar 40)',
  `recipe_step_seo_title` varchar(40) NOT NULL COMMENT 'Title, which will be used in the urls (varchar 40)',
  `recipe_step_description` text NOT NULL COMMENT 'Description about specific step (text)',
  `recipe_step_step_order` tinyint(3) UNSIGNED NOT NULL COMMENT 'In what order does this step goes. Starts from 1 (tinyint)',
  `fk_recipe_step_recipe_id` char(36) NOT NULL COMMENT 'To what recipe does this step belong (char 36)',
  `fk_recipe_step_user_id` char(36) NOT NULL COMMENT 'What user uploaded this step (char 36)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Step you have to follow to make specific recipe';

--
-- Dumping data for table `recipe_step`
--

INSERT INTO `recipe_step` (`recipe_step_id`, `recipe_step_title`, `recipe_step_seo_title`, `recipe_step_description`, `recipe_step_step_order`, `fk_recipe_step_recipe_id`, `fk_recipe_step_user_id`) VALUES
('1a7ba645-9476-4838-b0cd-5f214a827620', 'Priedai', 'Priedai', '', 6, '59d30edd-9ebc-4ef8-9646-020cf3b1479b', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('1c95deee-c907-48ce-afb3-19afd3dfb695', 'Išvirkite spagečius', 'Isvirkitespagecius', '', 1, 'bc66cb92-1025-4b81-8b71-cb069d41967b', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('276d9f14-d4b4-4d4c-923b-550916d0355d', 'Supjaustykite vaisius', 'Supjaustykitevaisius', '', 2, '90980da0-b845-4566-a590-14d8e5ebf59d', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('28295a11-5b40-48cf-9856-8e31524f3151', 'Nuplaukite visus vaisiu', 'Nuplaukitevisusvaisius', '', 1, '90980da0-b845-4566-a590-14d8e5ebf59d', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('2854304a-582c-49fd-b519-be6b9382e0d8', 'Iškepkite lazdeles', 'Iskepkitelazdeles', '', 4, 'c5e301ad-8bca-4602-bfdd-20aef981bc38', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('290030a7-b81b-4a05-ad2c-fdffae9bdcde', 'Svogūnų laiškai', 'Svogunulaiskai', '', 4, '59d30edd-9ebc-4ef8-9646-020cf3b1479b', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('2af13996-bb5f-410a-a001-3cf68336967e', 'Jogurtas', 'Jogurtas', '', 4, '90980da0-b845-4566-a590-14d8e5ebf59d', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('2f7a132c-2259-47f7-82b5-f8b18474ff40', 'Sumaišykite visus vaisius', 'Sumaisykitevisusvaisius', '', 3, '90980da0-b845-4566-a590-14d8e5ebf59d', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('52c5aa1a-b428-4500-917f-d0cdc4e9969a', 'Kopūstas', 'Kopustas', '', 1, '59d30edd-9ebc-4ef8-9646-020cf3b1479b', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('53c0035a-f178-43c4-8d19-c246cdf38ab5', 'Kepsnio paruošimas', 'Kepsnioparuosimas', '', 3, '4216f45a-3d22-428d-b013-6e93a75f6a9f', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('6533b088-12c0-4dc3-bc0c-0f10eaeb7808', 'Iviniokite į trupinius', 'Iviniokiteitrupinius', '', 3, 'c5e301ad-8bca-4602-bfdd-20aef981bc38', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('79b10ee6-49fe-499d-8cc5-b268ffc5c92f', 'Sūrio paruošimas', 'Surioparuosimas', '', 1, 'c5e301ad-8bca-4602-bfdd-20aef981bc38', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('7afdc712-1624-4026-9f3e-6f67d7429d9f', 'Skanaus', 'Skanaus', '', 5, '90980da0-b845-4566-a590-14d8e5ebf59d', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('818724df-4eaf-4822-91da-bae59f048105', 'Skanaus', 'Skanaus', '', 5, '4216f45a-3d22-428d-b013-6e93a75f6a9f', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('839b8a9b-93ab-4aa5-a696-50cfd9fc9aa1', 'Sūris ', 'Suris', '', 3, 'bc66cb92-1025-4b81-8b71-cb069d41967b', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('ac28f2eb-2d09-4681-986a-c624fe446c53', 'Išplakite kiaušinį ', 'Isplakitekiausini', '', 2, 'c5e301ad-8bca-4602-bfdd-20aef981bc38', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('b52f1145-8957-4930-b301-b933be2dc046', 'Pomidorai', 'Pomidorai', '', 2, '59d30edd-9ebc-4ef8-9646-020cf3b1479b', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('b7bd0303-8b52-4153-9c40-381767cc5698', 'Svogūnai ', 'Svogunai', '', 5, '59d30edd-9ebc-4ef8-9646-020cf3b1479b', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('c490e9ef-6d3d-43a5-a352-96c624a23d77', 'Nuplaukite ryžius', 'Nuplaukiteryzius', '', 1, '4216f45a-3d22-428d-b013-6e93a75f6a9f', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('ce683688-1c11-40f4-883d-bc0a6a77dd9e', 'Oadažas', 'Padazas', '', 4, 'bc66cb92-1025-4b81-8b71-cb069d41967b', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('d8647325-19e9-4315-8b2e-aeaa30e2ce36', 'Grietinėlė', 'Grietinele', '', 2, 'bc66cb92-1025-4b81-8b71-cb069d41967b', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('dddd56af-b292-40ef-ba90-5f8e5defa337', 'Iškepkite kepsnį ', 'Iskepkitekepsni', '', 4, '4216f45a-3d22-428d-b013-6e93a75f6a9f', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('eafc49f6-2a6f-4fca-be92-1b9036ce437f', 'Salotos', 'Salotos', '', 3, '59d30edd-9ebc-4ef8-9646-020cf3b1479b', '0e5194c1-532b-42d5-9dfe-c093c51e4f05'),
('f85fc793-cd1b-4e2b-9481-f3d3916e37cc', 'Virimas', 'Virimas', '', 2, '4216f45a-3d22-428d-b013-6e93a75f6a9f', '0e5194c1-532b-42d5-9dfe-c093c51e4f05');

-- --------------------------------------------------------

--
-- Table structure for table `suggested_ingredient`
--

CREATE TABLE `suggested_ingredient` (
  `suggested_ingredient_id` char(36) NOT NULL COMMENT 'Id for the suggested id (char 36)',
  `suggested_ingredient_title` varchar(40) NOT NULL COMMENT 'Suggested ingredient title (varchar 40)',
  `suggested_ingredient_seo_title` varchar(40) NOT NULL COMMENT 'Suggested ingredient title, which is used in urls (varchar 40)',
  `suggested_ingredient_unit` varchar(15) NOT NULL COMMENT 'What unit is used to calculate quantity of the ingredient',
  `suggested_ingredient_date_suggested` datetime NOT NULL COMMENT 'When was this ingredient suggested (datetime)',
  `fk_suggested_ingredient_user_id` char(36) NOT NULL COMMENT 'User that suggested this ingredient (char 36)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `suggested_ingredient`
--

INSERT INTO `suggested_ingredient` (`suggested_ingredient_id`, `suggested_ingredient_title`, `suggested_ingredient_seo_title`, `suggested_ingredient_unit`, `suggested_ingredient_date_suggested`, `fk_suggested_ingredient_user_id`) VALUES
('0205a8f9-28d3-495a-aa0d-0e60db52b0df', 'Cukraus pudra', 'Cukrauspudra', 'g.', '2021-11-30 22:38:48', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('022536ad-8434-4b8a-adbc-bd3dda3561fd', 'Aitrioji paprika', 'Aitriojipaprika', 'g.', '2021-11-30 22:37:57', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('13c77045-6e53-4db3-a996-dd766aa011f0', 'Cukrus', 'Cukrus', 'g.', '2021-11-30 22:38:34', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('2ff2a10c-b9c2-43f3-8890-c833d2a04d49', 'Pupelės', 'Pupeles', 'g.', '2021-11-30 22:37:42', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('3f957cfa-01cb-4f57-99cd-f26479bbe653', 'Kajeno pipirai', 'Kajenopipirai', 'g.', '2021-11-30 22:38:11', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('4630a54f-5f9a-47b2-bd14-c89abd2528a7', 'Saldžioji paprika', 'Saldziojipaprika', 'g.', '2021-11-30 22:37:50', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('483f15e3-49b4-4100-841e-c00616c35275', 'Batonas', 'batonas', 'riekės', '2022-01-09 21:35:49', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('548dc084-88c8-4de7-abb0-b74fe7eea323', 'Miltai', 'Miltai', 'g.', '2021-11-30 22:37:16', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('6fe8d87a-ef70-4635-adf4-c1d09163bfbd', 'Cinamonas', 'Cinamonas', 'g.', '2021-11-30 22:38:57', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('71334b74-f00a-4815-951c-45badd750231', 'Vanilinis cukrus', 'Vaniliniscukrus', 'g.', '2021-11-30 22:38:41', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('7bc48d3d-7f1d-4e41-9b25-b2ca508debc6', 'Bulijonas', 'Bulijonas', 'Vnt.', '2021-11-30 22:37:09', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('8b7713f6-d432-4753-9649-c277a1d7de2f', 'Druska', 'druska', 'g.', '2021-11-30 22:38:27', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('bae34802-42ac-4170-9360-1e434be710f0', 'Bazilikas', 'Bazilikas', 'g.', '2021-11-30 22:38:03', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('c9bc9358-c36b-45a0-99a1-6c9aec0c5f6c', 'Duona', 'Duona', 'g.', '2021-11-30 22:34:45', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('e8813a0b-a001-4db3-92e8-822ea29d18cf', 'Kepimo milteliai', 'Kepimomilteliai', 'g.', '2021-11-30 22:37:24', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('e9621584-1e78-49b5-95de-1ea38e7305f4', 'Makaronai', 'Makaronai', 'g.', '2021-11-30 22:36:54', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523'),
('f8018329-79bc-404c-8151-0459bd47d86f', 'Juodieji pipirai', 'Juodiejipipirai', 'g.', '2021-11-30 22:38:20', 'da70c1ec-905d-4c4d-94e9-ed3d3cae5523');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` char(36) NOT NULL COMMENT 'Id for the user (GUID char 36)',
  `user_username` varchar(20) NOT NULL COMMENT 'Username for user to login (varchar 20)',
  `user_password` char(102) NOT NULL COMMENT 'Password to use for user (varchar 102)',
  `user_email` varchar(30) NOT NULL COMMENT 'Email that user uses to reset his password',
  `user_date_registered` datetime NOT NULL COMMENT 'When did the user registered (datetime)',
  `user_role` enum('normal','recipe_creator','admin') DEFAULT 'normal' COMMENT 'What role user has (enum - normal, recipe_creator, admin)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `user_username`, `user_password`, `user_email`, `user_date_registered`, `user_role`) VALUES
('0e5194c1-532b-42d5-9dfe-c093c51e4f05', 'Neda Val', 'pbkdf2:sha256:260000$qCsHzA9W2kQDuUU3$a60d1f8d74fb0a6fc1e488c9c6c18203e16d71010dac748d9a4d21fed816bd10', 'xikiovy@gmail.com', '2021-12-21 21:39:52', 'recipe_creator'),
('4e587b40-db0a-4850-b420-cb0a09b2a9fa', 'gedas', 'pbkdf2:sha256:260000$xW33ywhau8tcSMyQ$d6ba8b5bbd62e7a6587fa7c7246a1783b96acc51d77d131d9e6055794744bf7f', 'gedas@gmail.com', '2021-11-30 21:46:11', 'normal'),
('63981134-4431-4177-aadf-8a01528cf9bb', 'kebbas', 'pbkdf2:sha256:260000$URoGCsYNp4pAILDA$92f0bdded4be13a2c6e67ae0d7bb63b3884aaf0487d360223e65ca98dfdedd62', 'kebas@gmail.com', '2021-12-21 21:39:08', 'normal'),
('69e0a5f4-147d-4262-8de3-9a0944cf04eb', 'matas', 'pbkdf2:sha256:260000$RNi2dK9W3fHEblLJ$bdad7303564520496436370768e284802a21e5d5c1533eb2c24c64cc0cce40fa', 'matas@gmail.com', '2022-01-10 22:20:40', 'normal'),
('aa37069a-b6e8-4ac0-8ad8-393b353e2aab', 'tests', 'pbkdf2:sha256:260000$YDC2LyGg2shHxdD3$8378efa6c105d7557a07319a39217332fc7430e513f501996bc8d345c37349af', 'vaiciukyynas1@gmail.com', '2021-11-30 11:46:59', 'normal'),
('da70c1ec-905d-4c4d-94e9-ed3d3cae5523', 'aidvai1', 'pbkdf2:sha256:260000$9Nxd8Kew4zivM2om$da536ca16266585e1fe9a24a29b4fd1bd9af67f9999c4d3756c14abe25c10088', 'aidas.vaiciukynas@ktu.edu', '2021-11-29 21:14:03', 'admin'),
('dbc83bf8-b811-478d-a4e9-e51aeca2d5f3', 'petras', 'pbkdf2:sha256:260000$Em9y0Fw2fl59aIvR$82764045deed98731d90f6a8950d12e63302a2757f6636bdcde2ce403b110312', 'petras@gmail.com', '2021-11-30 21:46:28', 'normal'),
('e5070c01-b3fb-4577-bc0d-58819fd26d5a', 'jonas', 'pbkdf2:sha256:260000$vEOhnPyRvvIMLBCJ$2d4ac007188533c916c499599e4f108aa6298f2e21f61b8b6d19376ea9e42f6a', 'jonas@gmail.com', '2021-11-30 21:45:36', 'normal'),
('fddbccbc-5e5f-40da-9d5f-d53ff570c559', 'kestas', 'pbkdf2:sha256:260000$RLA6XNNk1LehJhCM$43293ae903a05ba3c00f00fd42d85d310ebe4b7ac8c51db31b394fbab76b4d54', 'kestas@gmail.com', '2021-11-30 21:45:51', 'normal');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ingredient`
--
ALTER TABLE `ingredient`
  ADD PRIMARY KEY (`ingredient_id`),
  ADD KEY `fk_ingredient_user` (`fk_ingredient_user_id`);

--
-- Indexes for table `recipe`
--
ALTER TABLE `recipe`
  ADD PRIMARY KEY (`recipe_id`),
  ADD KEY `fk_recipe_user` (`fk_recipe_user_id`);

--
-- Indexes for table `recipe_ingredient`
--
ALTER TABLE `recipe_ingredient`
  ADD PRIMARY KEY (`recipe_ingredient_id`),
  ADD KEY `fk_recipe_ingredient_recipe` (`fk_recipe_ingredient_recipe_id`),
  ADD KEY `fk_recipe_ingredient` (`fk_recipe_ingredient_ingredient_id`);

--
-- Indexes for table `recipe_step`
--
ALTER TABLE `recipe_step`
  ADD PRIMARY KEY (`recipe_step_id`),
  ADD KEY `fk_recipe_step_recipe` (`fk_recipe_step_recipe_id`),
  ADD KEY `fk_recipe_step_user` (`fk_recipe_step_user_id`);

--
-- Indexes for table `suggested_ingredient`
--
ALTER TABLE `suggested_ingredient`
  ADD PRIMARY KEY (`suggested_ingredient_id`),
  ADD KEY `fk_suggested_ingredient_user` (`fk_suggested_ingredient_user_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `ingredient`
--
ALTER TABLE `ingredient`
  ADD CONSTRAINT `fk_ingredient_user` FOREIGN KEY (`fk_ingredient_user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `recipe`
--
ALTER TABLE `recipe`
  ADD CONSTRAINT `fk_recipe_user` FOREIGN KEY (`fk_recipe_user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `recipe_ingredient`
--
ALTER TABLE `recipe_ingredient`
  ADD CONSTRAINT `fk_recipe_ingredient` FOREIGN KEY (`fk_recipe_ingredient_ingredient_id`) REFERENCES `ingredient` (`ingredient_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_recipe_ingredient_recipe` FOREIGN KEY (`fk_recipe_ingredient_recipe_id`) REFERENCES `recipe` (`recipe_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `recipe_step`
--
ALTER TABLE `recipe_step`
  ADD CONSTRAINT `fk_recipe_step_recipe` FOREIGN KEY (`fk_recipe_step_recipe_id`) REFERENCES `recipe` (`recipe_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_recipe_step_user` FOREIGN KEY (`fk_recipe_step_user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `suggested_ingredient`
--
ALTER TABLE `suggested_ingredient`
  ADD CONSTRAINT `fk_suggested_ingredient_user` FOREIGN KEY (`fk_suggested_ingredient_user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
