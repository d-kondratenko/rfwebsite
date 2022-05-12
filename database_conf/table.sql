CREATE TABLE `ws_coeficient` (
  `id` int NOT NULL AUTO_INCREMENT,
  `project_src` varchar(255) NOT NULL,
  `project_dst` varchar(255) NOT NULL,
  `cost` float NOT NULL,
  `is_available` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
CREATE TABLE `ws_donate_code` (
  `code_id` int NOT NULL AUTO_INCREMENT,
  `code` varchar(8) NOT NULL,
  `cost` int NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `is_active` varchar(1) NOT NULL,
  PRIMARY KEY (`code_id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb3;
CREATE TABLE `ws_game_account_assign` (
  `id` int NOT NULL AUTO_INCREMENT,
  `project_id` int NOT NULL,
  `user_id` int NOT NULL,
  `account_name` varchar(255) NOT NULL,
  `is_premium` varchar(1) NOT NULL,
  `premStart` datetime DEFAULT NULL,
  `premFinish` datetime DEFAULT NULL,
  `cash` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
CREATE TABLE `ws_game_balance` (
  `bal_id` int NOT NULL AUTO_INCREMENT,
  `project` varchar(255) NOT NULL,
  `user_id` int NOT NULL,
  `user_bill` varchar(255) NOT NULL,
  `balance` float NOT NULL,
  PRIMARY KEY (`bal_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
CREATE TABLE `ws_game_payments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `project` varchar(255) NOT NULL,
  `account_name` varchar(255) NOT NULL,
  `payment_type` varchar(255) NOT NULL,
  `value` varchar(255) NOT NULL,
  `Coin_cost` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
CREATE TABLE `ws_payment_history` (
  `payment_id` int NOT NULL AUTO_INCREMENT,
  `bank_pay_id` varchar(255) NOT NULL,
  `user_id` int NOT NULL,
  `user_bill` varchar(255) NOT NULL,
  `payment_sum` int NOT NULL,
  `c_date` varchar(255) NOT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
CREATE TABLE `ws_payments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` longtext NOT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb3;
CREATE TABLE `ws_projects` (
  `project_id` int NOT NULL AUTO_INCREMENT,
  `project_name` varchar(255) NOT NULL,
  `project_abbrev` varchar(5) NOT NULL,
  `status` varchar(2) NOT NULL,
  PRIMARY KEY (`project_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
CREATE TABLE `ws_transfer_coef` (
  `id` int NOT NULL AUTO_INCREMENT,
  `project_name` varchar(255) DEFAULT NULL,
  `main` float DEFAULT NULL,
  `rf` float DEFAULT NULL,
  `pw` float DEFAULT NULL,
  `is_available` int DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
CREATE TABLE `ws_transfer_history` (
  `transfer_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `project` varchar(255) NOT NULL,
  `transfer_sum` int NOT NULL,
  `transfer_date` varchar(255) NOT NULL,
  PRIMARY KEY (`transfer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb3;
CREATE TABLE `ws_users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password_hash` varchar(60) NOT NULL,
  `user_bill` varchar(255) NOT NULL,
  `budget` float NOT NULL,
  `is_activate` int NOT NULL DEFAULT '0',
  `token` varchar(255) NOT NULL,
  `is_admin` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
