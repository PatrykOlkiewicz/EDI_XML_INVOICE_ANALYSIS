SET DATEFORMAT dmy;

-----------------------------------------------

UPDATE Invoice
SET InvoiceDate = LTRIM(RTRIM(InvoiceDate)),
    SalesDate = LTRIM(RTRIM(SalesDate)),
    InvoicePaymentDueDate = LTRIM(RTRIM(InvoicePaymentDueDate));

--------------------------------------------------------------------

UPDATE InvoiceLine
SET InvoiceUnitNetPriceNEW = REPLACE(InvoiceUnitNetPriceNEW, ',', '.')
WHERE InvoiceUnitNetPriceNEW LIKE '%,%';

