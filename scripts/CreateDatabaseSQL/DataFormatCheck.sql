SELECT InvoiceQuantity, 
	InvoiceUnitNetPriceNEW, 
	TaxRate 
FROM InvoiceLine 
WHERE TRY_CONVERT(DECIMAL(18,2), InvoiceQuantity) IS NULL
OR TRY_CONVERT(DECIMAL(18,2), InvoiceUnitNetPriceNEW) IS NULL 
OR TRY_CONVERT(DECIMAL(5,2), TaxRate) IS NULL;

------------------------------------------------------------------

SELECT InvoiceDate, 
InvoicePaymentDueDate, 
SalesDate 
FROM Invoice 
WHERE ISDATE(InvoiceDate) = 0 
OR ISDATE(SalesDate) = 0 
OR ISDATE(InvoicePaymentDueDate) = 0;

--------------------------------------------------------------------

DBCC USEROPTIONS;

