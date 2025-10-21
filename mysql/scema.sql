use rossmann;
drop table sales;

CREATE TABLE rossmann.sales (
    Store INT,
    DayOfWeek INT,
    Date DATE,
    Sales INT,
    Customers INT,
    Open INT,
    Promo INT,
    StateHoliday VARCHAR(20),
    SchoolHoliday INT,
    StoreType VARCHAR(10),
    Assortment VARCHAR(10),
    CompetitionDistance FLOAT
);

describe sales;
SELECT count(*) FROM sales;
SELECT * FROM sales LIMIT 5;

ALTER TABLE sales
ADD COLUMN InsertedAt DATETIME DEFAULT CURRENT_TIMESTAMP;

ALTER TABLE sales
ADD CONSTRAINT unique_store_date UNIQUE (Store, Date);




