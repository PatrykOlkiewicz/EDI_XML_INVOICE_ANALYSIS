BULK INSERT Buyer
FROM 'C:\Temp\SQLBackups\DaneComarch\Buyer.csv'
WITH (
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

BULK INSERT Invoice
FROM 'C:\Temp\SQLBackups\DaneComarch\Invoice.csv'
WITH (
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

BULK INSERT InvoiceLine
FROM 'C:\Temp\SQLBackups\DaneComarch\InvoiceLine.csv'
WITH (
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

BULK INSERT Seller
FROM 'C:\Temp\SQLBackups\DaneComarch\Seller.csv'
WITH (
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

