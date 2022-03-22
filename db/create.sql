CREATE TABLE IF NOT EXISTS employee (
    pk INT PRIMARY KEY AUTO_INCRIMENT,
    first_name varchar(20) NOT NULL,
    last_name varchar(20) NOT NULL,
    email varchar(20) NOT NULL,
    address varchar(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS job (
    pk INT PRIMARY KEY AUTO_INCREMENT,
    name varchar(15) NOT NULL,
    details varchar(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS employment (
    pk INT PRIMARY KEY AUTO_INCRMENT
    FOREIGN_KEY (employee_pk) REFERENCES employee(pk)
    FOREIGN_KEY (job_pk) REFERENCES job(pk)
);