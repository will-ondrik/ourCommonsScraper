CREATE TABLE MembersOfParliament (
    id INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    constituency VARCHAR(75) NOT NULL,
    caucus VARCHAR(25) NOT NULL,
    salary FLOAT NOT NULL
);

CREATE TABLE Contact (
    id INT PRIMARY KEY AUTO_INCREMENT,
    memberId INT NOT NULL,
    email VARCHAR(128) NOT NULL,
    website VARCHAR(128),
    hillOfficeAddress VARCHAR(255),
    hillOfficePhone VARCHAR(15),
    hillOfficeFax VARCHAR(15),
    constituencyOfficeAddress VARCHAR(255),
    constituencyOfficePhone VARCHAR(15),
    constituencyOfficeFax VARCHAR(15),
    linkToSite VARCHAR(128),
    FOREIGN KEY (memberId) REFERENCES MembersOfParliament(id)
);


CREATE TABLE Committees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    memberId INT NOT NULL,
    name VARCHAR(512) NOT NULL,
    abbreviation VARCHAR(15) NOT NULL,
    FOREIGN KEY (memberId) REFERENCES MembersOfParliament(id)
);

CREATE TABLE ParliamentaryAssociationsAndInterparliamentaryGroups (
    id INT PRIMARY KEY AUTO_INCREMENT,
    memberId INT NOT NULL,
    name VARCHAR(512) NOT NULL,
    abbreviation VARCHAR(15) NOT NULL,
    executiveCommittee TINYINT NOT NULL,
    FOREIGN KEY (memberId) REFERENCES MembersOfParliament(id)
);


CREATE TABLE Expense (
    id INT PRIMARY KEY AUTO_INCREMENT,
    memberId INT NOT NULL,
    claimType VARCHAR(25) NOT NULL,
    cost FLOAT NOT NULL,
    reportingPeriodStart DATE NOT NULL,
    reportingPeriodEnd DATE NOT NULL,
    year INT NOT NULL,
    fiscalQuarter INT NOT NULL,
    FOREIGN KEY (memberId) REFERENCES MembersOfParliament(id)
);

CREATE TABLE TravelClaim (
    id INT PRIMARY KEY AUTO_INCREMENT,
    expenseId INT NOT NULL,
    memberId INT NOT NULL,
    startDate DATE,
    endDate DATE,
    transportationCosts FLOAT NOT NULL,
    accommodationCosts FLOAT NOT NULL,
    mealsAndIncidentalsCosts FLOAT NOT NULL,
    regularPoints FLOAT NOT NULL,
    specialPoints FLOAT NOT NULL,
    usaPoints FLOAT NOT NULL,
    totalCost FLOAT NOT NULL,
    FOREIGN KEY (expenseId) REFERENCES Expense(id),
    FOREIGN KEY (memberId) REFERENCES MembersOfParliament(id)
);

CREATE TABLE HospitalityClaim (
    id INT PRIMARY KEY AUTO_INCREMENT,
    expenseId INT NOT NULL,
    memberId INT NOT NULL,
    date DATE NOT NULL,
    location VARCHAR(50) NOT NULL,
    attendance INT NOT NULL,
    purpose TEXT NOT NULL,
    totalCost FLOAT NOT NULL,
    FOREIGN KEY (expenseId) REFERENCES Expense(id),
    FOREIGN KEY (memberId) REFERENCES MembersOfParliament(id)
);

CREATE TABLE ContractClaim (
    id INT PRIMARY KEY AUTO_INCREMENT,
    expenseId INT NOT NULL,
    memberId INT NOT NULL,
    supplier VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    purpose TEXT NOT NULL,
    totalCost FLOAT NOT NULL,
    FOREIGN KEY (expenseId) REFERENCES Expense(id),
    FOREIGN KEY (memberId) REFERENCES MembersOfParliament(id)
);

CREATE TABLE Traveller (
    id INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    type VARCHAR(50) NOT NULL
);

CREATE TABLE Travel (
    id INT PRIMARY KEY AUTO_INCREMENT,
    travellerId INT NOT NULL,
    claimId INT NOT NULL,
    date DATE,
    departure VARCHAR(50),
    destination VARCHAR(50),
    purpose TEXT NOT NULL,
    FOREIGN KEY (travellerId) REFERENCES Traveller(id),
    FOREIGN KEY (claimId) REFERENCES TravelClaim(id)
);

CREATE TABLE Event (
    id INT PRIMARY KEY AUTO_INCREMENT,
    claimId INT NOT NULL,
    claimNumber VARCHAR(25) NOT NULL,
    type TEXT NOT NULL,
    supplier FLOAT NOT NULL,
    totalCost FLOAT NOT NULL,
    FOREIGN KEY (claimId) REFERENCES HospitalityClaim(id)
);

